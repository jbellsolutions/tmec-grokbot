---
name: dream-100-draft
description: Researches one Dream 100 business and writes a message for it alone, then puts it in Tommy's approval queue in the standard item format. Used by Dream 100's drafts routine and when TMEC Command sends a Dream 100 job.
---

# Dream 100 draft

The item format, the decision path and the send gate are in `/workspace/tmec-team/repo/policies/APPROVALS.md`, section "Items, decisions and the send gate". Follow it exactly. This skill only drafts and queues; it sends nothing.

## Inputs
- The business's row in `/workspace/tmec-team/data/partners/dream100.csv` (id `d100-<nnn>`).
- Its website, listing, reviews and recent public posts (Grok web and X search).
- `/workspace/tmec-team/repo/partners/kit/partner-one-pager.md`, `partner-terms.md`, `outreach-sequence.md` (the rules section).
- `/workspace/tmec-team/context/owner.md`: Tommy's sign-off, the TMEC contact block (`{business_legal_name}`, `{abn}`, `{contact_phone}`, `{reply_to}`, `{postal_address_line}`, `{electrical_licence_no}`), and the names he gave.
- `/workspace/tmec-team/context/config.json`: `partner_fee` and `partner_fee_trigger` (only to know whether they are set), `run`.
- `/workspace/tmec-team/repo/policies/AU-COMPLIANCE.md`.
- `/workspace/tmec-team/data/partners/opt-outs.csv`.

## Test mode
In test mode, or when `config.json` `run` is `test`: write research and drafts under `/workspace/tmec-team/state/test/partners/dream100/` instead of `data/partners/dream100/`, update the row status only in `state/test/partners/dream100.csv`, and start the ITEM id with `test-` (`test-d100-004-1`). The item still goes to `approved/pending/dream-100/`. Nothing is sent and nothing is paid for.

## Steps
1. **Gates before you spend time.**
   - The address must be on the business's own page (contact page or footer), with the page link and the date you read it. No published address, no draft: put "no published address, Tommy to say how he has it" in the daily note and stop on that business. Never guess, never use a pattern like info@.
   - **Does the site say no?** Read the site's terms, contact page and footer for any line that says no unsolicited commercial email or no marketing approaches (as `trades-list-build` does). If it does, set the row's status to `out` with the reason and the page link, and draft nothing.
   - Not on `opt-outs.csv` (by email, website, phone).
   - The TMEC contact block and the licence line are all in `owner.md`. A missing part is `NO_CLIENT_SOURCE`: don't draft.
2. **Research** (save to `data/partners/dream100/<id>/research.md` with links): what they do, who their customers are, where they work, one recent job or post, who decides (the owner's name from their own site), and the specific way they meet TMEC's customer (before, during, after, alongside).
3. **Pick the angle.** One reason this business, and only this one, should talk to Tommy. Insurance builders: thermal imaging, electrical and solar reports after a storm, rectification quotes ready to approve. Trades: their customer gets TMEC's own crew. Programs (panel makers, Origin, EV dealers): TMEC as their in-house installer on the Coast. Wave 0 (people Tommy already works with): thank them first, then ask who else he should meet.
4. **Write the message** from Tommy, first person: a short lowercase subject; 80 to 140 words counted from the greeting to the sign-off (not the contact block); one specific line that shows we know their business; the in-house edge; one plain ask (a 10-minute call); no link in the first touch. **No money at all**: no fee, no figure, no "paid" or "commission". A fee is only ever named once `config.json` has both `partner_fee` and `partner_fee_trigger` set by Tommy, and never in a first touch. Never "affiliate".
5. **Close with the contact block**, from `owner.md`:
   ```
   Tommy
   <business_legal_name>, ABN <abn>
   <contact_phone> | <reply_to>
   <postal_address_line>
   Licensed electrical contractor <electrical_licence_no>
   ```
   and the opt-out line: "If you'd rather not hear from me, just reply and say so and I will take you off straight away."
6. **Check it** against the rules: true and sourced; nothing it promises that Tommy hasn't promised; no air-con claim; within the word range; contact block, licence line and opt-out line present.
7. **Queue it.** Write `/workspace/tmec-team/approved/pending/dream-100/<id>-<n>.md` (`n` starts at 1; a redraft after "change" is the next number):
   ```
   ITEM: <id>-<n>
   BOT: dream-100
   WHY: <score> | <one-line angle>
   ---PAYLOAD---
   TO: <name>, <business>, <email>
   CONSENT: published_business_address: <page link>, read <date>; site checked, no refusal of unsolicited commercial email (inferred consent under the Spam Act, per policies/AU-COMPLIANCE.md)
   SEND: now on yes
   SUBJECT: <subject>
   TEXT:
   <the message, with the contact block and opt-out line>
   ---END---
   HASH: <sha256 of every byte between the ---PAYLOAD--- and ---END--- lines, newlines included>
   ```
   Save the item first, then compute the HASH from the saved bytes and add it. Set the row's status to `waiting on Tommy`.

## Done means
A message only this business could get, with its research and its consent evidence linked, waiting in the queue in the standard format.

## Never
- Send. Sending is `dream-100-send`, after Tommy's yes and the send gate.
- Write to a guessed or generic address, or to anyone in `opt-outs.csv`.
- Draft to a site that refuses unsolicited commercial email.
- Name a fee, or reuse another business's message with the name swapped.
