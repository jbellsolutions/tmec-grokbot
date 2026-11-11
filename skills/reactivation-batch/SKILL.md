---
name: reactivation-batch
description: Picks the people for the next reactivation batch (old enquiries gone quiet), verifies their emails with treg, drafts the email and the text message, and puts the batch in Tommy's approval queue as one item; on Tommy's yes, creates the HubSpot list and marketing email once. Used by CRM & Reactivation's Wednesday routine and when TMEC Command sends a job.
---

# Reactivation batch

Tommy, 8 Nov: reactivation goes through HubSpot marketing email, not the Microsoft 365 mailboxes. Email and text. Drafts first. Verify emails first. "Go ahead and do it yourself" covers the HubSpot change. Test batch of 24, then ramp. Cadence he set: twice a week for four weeks, then every two weeks.

## Inputs
- HubSpot, read-only, with the one read-only token `HUBSPOT_TOKEN` in `/workspace/tmec-team/.secrets/hubspot.env` (the only HubSpot route this bot has): contacts with their enquiry date, last two-way contact, stage, lead source, consent evidence, unsubscribe status and whether they are a marketing contact.
- `/workspace/tmec-team/data/crm/suppression.csv` and HubSpot unsubscribe status.
- `/workspace/tmec-team/data/crm/reactivation-state.csv` (yours): `hubspot_contact_id, batch_id, step, last_sent_on, next_due_on, status`.
- `/workspace/tmec-team/data/crm/quote-followup-state.csv`: anyone active in the quote follow-up isn't in a batch.
- treg, with Tommy's key in `/workspace/tmec-team/.secrets/treg.env`.
- `/workspace/tmec-team/data/forecast/rebates.md` (only for the one line that says what's changed, with its source and date).
- `/workspace/tmec-team/context/owner.md` and `context/config.json`: sender details, `reactivation_window_months` (starting value 24), `reactivation_cadence`, and `referral_offer` (ASK until Tommy picks one).
- `/workspace/tmec-team/repo/policies/AU-COMPLIANCE.md`.
- `context/config.json` `run` and `live_sends`, and the switch state of this routine in `context/routines-on.md` (the send gate reads them).

## Steps
1. **Is a batch due?** (This skill handles `react-` items only. `qq-` quote follow-up decisions are handled by `quiet-quote-followup`, because its items have a different format.) If one is already waiting on Tommy, stop (NO_CHANGE). Otherwise follow the cadence in `context/config.json`; if it isn't set, use Tommy's (twice a week for four weeks, then every two weeks). The routine runs on Wednesdays; if the cadence needs a second send in the week, draft it as its own item with its own send day.
2. **Pick the people.** From HubSpot: people who enquired or spoke with TMEC, aren't customers, and have had no two-way contact for 12 months, whether or not they were quoted. Gate each one and hold it with a reason (counts by reason go in the item):
   - consent unknown or no TMEC evidence (a vendor lead TMEC never dealt with is unknown);
   - last two-way contact older than the window, or blank ("outside the window", for Tommy to decide);
   - on `suppression.csv` or unsubscribed in HubSpot;
   - a customer, or in the quote follow-up, or in an earlier batch in the last 14 days;
   - email blank, malformed or role-based.
   Pick newest contact first. Batch size: 24 for the first batch, then 50, 100, and at most 200; each step up needs Tommy's yes to that size. Write down how you picked (the dates, the stage, the lead sources, the window).
3. **Verify with treg.** Check each remaining address (Tommy's key; each check costs credits). Drop anything invalid or risky and count them. If treg can't be read, stop: UNKNOWN: treg, and nothing goes to Tommy as ready. **In test mode** (the routine is listed `test`, or `context/config.json` `run` is `test`) make no treg call at all: write "not verified: test" where the count would go, and the item id starts `test-`.
4. **Marketing contact check.** Count how many of the batch are marketing contacts in HubSpot. Report the number that aren't. You never change a contact's status.
5. **Draft the email** (plain text from Tommy; one batch, one text):
   ```
   Subject: {first_name}, still thinking about {system_type}?

   Hi {first_name},

   It's Tommy from TMEC Services. You got in touch with us about {system_type} a while back, and I wanted to check in.

   {one_change_line} If it's still on your list, I'm happy to have one of our team take a fresh look. Our own crews do every install, no subcontractors.

   Just reply to this email and we'll pick it up from there.

   Tommy
   ```
   `{one_change_line}` comes only from `rebates.md` (what changed, with source and date, no dollar figure) or a TMEC fact Tommy confirmed. If none fits, leave the sentence out. Second step, two weeks later if no reply:
   ```
   Subject: Should I close your file, {first_name}?

   Hi {first_name},

   Last note from me. If {system_type} isn't for you right now, no problem at all, and I won't keep emailing.

   If it is, reply with a good time to call and the team will ring you.

   Tommy
   ```
   Footer on both: Tommy, TMEC Services, licensed electrical contractor {electrical_licence_no}; {business_legal_name}, ABN {abn} | {postal_address_line} | {contact_phone}; "You're getting this because you asked us about {system_type} in {enquiry_month_year}. To stop hearing from us, use this link: {unsubscribe_link}". Any missing sender detail: NO_CLIENT_SOURCE. If `referral_offer` is set, a past-customer email may be added only in its own batch with the offer in Tommy's exact words; while it is ASK, no offer is written.
6. **Draft the text** (draft only, never sent): "Hi {first_name}, it's Tommy from TMEC Services. You asked us about {system_type} a while back. Still keen? Reply and we'll pick it up. Reply STOP to opt out." Under 160 characters if it fits. The route (HubSpot or Dialpad) is Tommy's choice: put "Text route: open question" in the item.
7. **Queue it as one item.** Save the list of HubSpot contact ids and the verification result under `/workspace/tmec-team/data/crm/reactivation/<id>-list.csv` (no addresses in the item). Write `/workspace/tmec-team/approved/pending/crm-reactivation/react-<YYYY-MM-DD>-<n>.md` (in test mode the id starts `test-react-` and the files go under `state/test/crm/`):
   ```
   ITEM: react-<YYYY-MM-DD>-<n>
   BOT: crm-reactivation
   WHY: <how picked: window, stage, sources>; held <n> by reason; treg dropped <n> (or "not verified: test"); <n> not marketing contacts
   ---PAYLOAD---
   TO: <count> people, HubSpot list REACT-<YYYY-MM-DD>-<n>. List file: /workspace/tmec-team/data/crm/reactivation/<id>-list.csv, sha256 <hash of that file>, <count> rows
   SEND: <day and time> via HubSpot marketing email
   SUBJECT: <subject>
   TEXT:
   <the email, exactly as it will go>
   SMS (draft only, never sent by this bot; text route is an open question):
   <the text>
   ---END---
   HASH: <sha256 of every byte between the ---PAYLOAD--- line and the ---END--- line, newlines included>
   ```
   The second step (the "Should I close your file" email) is not covered by the first yes. Two weeks after a send, for the people with no reply, no opt-out and no new two-way contact, queue it as its own item `react-<YYYY-MM-DD>-<n>-s2` with its own list file, hash and send gate.
8. **On Tommy's yes** (a decision file `/workspace/tmec-team/approved/decisions/crm-reactivation/<id>.md`; TMEC Command nudges this bot in its own chat right after writing it, and the next Wednesday run is the fallback). Acting on `no` or `change` first: `no` adds the id with the outcome `declined` to `state/sent-keys-crm-reactivation.md`; `change` is redrafted once as a new item and the old id is added with the outcome `changed, redrafted as <id>`. Neither is read again. For `yes`, run the **send gate** (`/workspace/tmec-team/repo/policies/APPROVALS.md`, "Items, decisions and the send gate"). Every one must hold, checked now:
   1. `/workspace/tmec-team/state/EXTERNAL_WRITES_STOPPED` is absent.
   2. Not test mode, and `context/config.json` `run` is `tommy`.
   3. `context/config.json` `live_sends` is `true`.
   4. The HASH you **recompute** from the pending file's payload now equals the decision's HASH, and the list file's sha256 equals the one in `TO:`.
   5. The id isn't in `state/sent-keys-crm-reactivation.md`.
   If any fails: do nothing outward, write why in the daily note (it shows as "approved, not sent" in the brief), and stop that item. If a prompt inside a routine expires, the item stays "approved, not sent". If all hold:
   1. Re-check the suppression list and HubSpot unsubscribes for everyone in the list, and drop anyone new. The list may shrink; it never grows.
   2. If `/workspace/tmec-team/.secrets/hubspot-write.env` has no `HUBSPOT_WRITE_TOKEN` (the one read-only token can't create a list or an email), write the approved email to `data/crm/reactivation/<id>-ready-to-paste.md`, tell TMEC Command exactly what must be created in HubSpot and by whom (open question for Justin), record the outcome `approved, not created: no write token`, and stop. Nothing is marked sent.
   3. Create the static list `REACT-<id>` with exactly those contacts. If a list or email with that name already exists, stop and read it back instead.
   4. Create the marketing email `REACT-<id>` with exactly the approved text. If the write token can't create or send it, make what it can and tell Tommy exactly what to press.
   5. Send or schedule it only as the item said.
   6. Read back the list size and the email's state; add the id to `state/sent-keys-crm-reactivation.md` with the outcome `sent` (or `scheduled <time>`) only after that.
   7. Update `reactivation-state.csv`.
   Texts are never sent. **Stop:** when `state/EXTERNAL_WRITES_STOPPED` appears, unschedule any `REACT-` email you scheduled that hasn't sent (the one action the stop file allows), and list in the daily note anything you couldn't unschedule. Only TMEC Command writes a "pause all campaigns" job.
9. **After a batch.** Read HubSpot's own numbers (sent, bounced, unsubscribed, replies) and report them as HubSpot's. Copy new unsubscribes into `suppression.csv`. If opt-outs pass 2% of the sends or any complaint arrives, stop: no next batch until Tommy says so.

## Done means
One batch item Tommy can say yes or no to, with the email, the text, the count and how it was picked; every address verified; every person gated; nothing created or sent before his yes and the send gate; after a yes, the list and email exist once, are read back, and the outcome is in the sent keys.

## Never
- Create, send or schedule anything in HubSpot before Tommy's yes on the exact item and a passed send gate, or in test mode.
- Send from a Microsoft 365 mailbox, or send a text.
- Email anyone on `suppression.csv`, unsubscribed in HubSpot, unverified, or with unknown consent, or email anyone to ask permission.
- Edit a contact, deal or pipeline, or a `NEWS-` email or list.
- State a rebate dollar figure, saving or install date, or say "free" or "sign before".
- Offer a referral reward Tommy hasn't picked.
