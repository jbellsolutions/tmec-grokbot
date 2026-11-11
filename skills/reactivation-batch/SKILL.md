---
name: reactivation-batch
description: Picks the people for the next reactivation batch (old enquiries gone quiet), verifies their emails with treg, drafts the email and the text message, and puts the batch in Tommy's approval queue as one item; on Tommy's yes, creates the HubSpot list and marketing email once. Used by CRM & Reactivation's Wednesday routine and when TMEC Command sends a job.
---

# Reactivation batch

Tommy, 8 Nov: reactivation goes through HubSpot marketing email, not the Microsoft 365 mailboxes. Email and text. Drafts first. Verify emails first. "Go ahead and do it yourself" covers the HubSpot change. Test batch of 24, then ramp. Cadence he set: twice a week for four weeks, then every two weeks.

## Inputs
- HubSpot, read-only (`/workspace/tmec-team/.secrets/hubspot.env`): contacts with their enquiry date, last two-way contact, stage, lead source, consent evidence, unsubscribe status and whether they are a marketing contact.
- `/workspace/tmec-team/data/crm/suppression.csv` and HubSpot unsubscribe status.
- `/workspace/tmec-team/data/crm/reactivation-state.csv` (yours): `hubspot_contact_id, batch_id, step, last_sent_on, next_due_on, status`.
- `/workspace/tmec-team/data/crm/quote-followup-state.csv`: anyone active in the quote follow-up isn't in a batch.
- treg, with Tommy's key in `/workspace/tmec-team/.secrets/treg.env`.
- `/workspace/tmec-team/data/forecast/rebates.md` (only for the one line that says what's changed, with its source and date).
- `/workspace/tmec-team/context/owner.md` and `context/config.json`: sender details, `reactivation_window_months` (starting value 24), `reactivation_cadence`, and `referral_offer` (ASK until Tommy picks one).
- `/workspace/tmec-team/policies/AU-COMPLIANCE.md`.

## Steps
1. **Is a batch due?** If one is already waiting on Tommy, stop (NO_CHANGE). Otherwise follow the cadence in `context/config.json`; if it isn't set, use Tommy's (twice a week for four weeks, then every two weeks). The routine runs on Wednesdays; if the cadence needs a second send in the week, draft it as its own item with its own send day.
2. **Pick the people.** From HubSpot: people who enquired or spoke with TMEC, aren't customers, and have had no two-way contact for 12 months, whether or not they were quoted. Gate each one and hold it with a reason (counts by reason go in the item):
   - consent unknown or no TMEC evidence (a vendor lead TMEC never dealt with is unknown);
   - last two-way contact older than the window, or blank ("outside the window", for Tommy to decide);
   - on `suppression.csv` or unsubscribed in HubSpot;
   - a customer, or in the quote follow-up, or in an earlier batch in the last 14 days;
   - email blank, malformed or role-based.
   Pick newest contact first. Batch size: 24 for the first batch, then 50, 100, and at most 200; each step up needs Tommy's yes to that size. Write down how you picked (the dates, the stage, the lead sources, the window).
3. **Verify with treg.** Check each remaining address. Drop anything invalid or risky and count them. If treg can't be read, stop: UNKNOWN: treg, and nothing goes to Tommy as ready.
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
7. **Queue it as one item.** Write `/workspace/tmec-team/approved/pending/crm-reactivation/react-<YYYY-MM-DD>-<n>.md`:
   ```
   ITEM: react-<YYYY-MM-DD>-<n>
   BOT: crm-reactivation
   TO: <count> people, HubSpot list REACT-<YYYY-MM-DD>-<n> (members in data/crm/reactivation/<id>-list.csv)
   WHY: <how picked: window, stage, sources>; held <n> by reason; treg dropped <n>; <n> not marketing contacts
   SEND: <day and time> via HubSpot marketing email
   SUBJECT: <subject>
   TEXT:
   <the email>
   SMS (draft only):
   <the text>
   HASH: <sha256 of SUBJECT + TEXT>
   ```
   Save the list of HubSpot contact ids and the verification result under `data/crm/reactivation/`. Keep addresses out of the item.
8. **On Tommy's yes** (a decision file with the same id and HASH, not already in `state/sent-keys-crm-reactivation.md`; M4 and the marketing key only):
   1. Re-check the suppression list and HubSpot unsubscribes for everyone in the list, and drop anyone new.
   2. Create the static list `REACT-<id>` with exactly those contacts. If a list or email with that name already exists, stop and read it back instead.
   3. Create the marketing email `REACT-<id>` with exactly the approved text. If the key can't create or send it, make what it can and tell Tommy exactly what to press.
   4. Send or schedule it only as the item said.
   5. Read back the list size and the email's state; write the key to `state/sent-keys-crm-reactivation.md` only after that.
   6. Update `reactivation-state.csv`.
   Texts are never sent. A "no" marks the item declined; a change is a new item.
9. **After a batch.** Read HubSpot's own numbers (sent, bounced, unsubscribed, replies) and report them as HubSpot's. Copy new unsubscribes into `suppression.csv`. If opt-outs pass 2% of the sends or any complaint arrives, stop: no next batch until Tommy says so.

## Done means
One batch item Tommy can say yes or no to, with the email, the text, the count and how it was picked; every address verified; every person gated; nothing created or sent before his yes; after a yes, the list and email exist once and are read back.

## Never
- Create, send or schedule anything in HubSpot before Tommy's yes on the exact item, or in test mode.
- Send from a Microsoft 365 mailbox, or send a text.
- Email anyone on `suppression.csv`, unsubscribed in HubSpot, unverified, or with unknown consent, or email anyone to ask permission.
- Edit a contact, deal or pipeline, or a `NEWS-` email or list.
- State a rebate dollar figure, saving or install date, or say "free" or "sign before".
- Offer a referral reward Tommy hasn't picked.
