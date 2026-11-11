---
name: dream-100-send
description: Sends one Dream 100 message Tommy said yes to, exactly as he saw it, from his mailbox, once. Used by Dream 100 when a decision arrives.
---

# Dream 100 send

## Inputs
- `/workspace/tmec-team/approved/decisions/<id>.md` (written by TMEC Command, in Tommy's words).
- `/workspace/tmec-team/approved/pending/dream-100/<id>.md` (yours).
- `/workspace/tmec-team/state/sent-keys-dream-100.md`.
- `/workspace/tmec-team/data/partners/opt-outs.csv`.

## Steps
1. **Match.** The decision's ITEM and HASH must equal the pending item's, and ANSWER must be "yes". A mismatch means the text changed after Tommy saw it: don't send; redraft and queue it again.
2. **Check, every time:** the stop file `/workspace/tmec-team/state/EXTERNAL_WRITES_STOPPED` is absent; the address isn't in `opt-outs.csv`; the sent key `<date>|email|dream100|<id>-<n>|<address>` isn't in your sent-keys file; today's sends are under the limit. In test mode, write what you'd send to `state/test/` and stop.
3. **Verify the address** with treg if it hasn't been verified. Invalid: don't send; note it for Tommy.
4. **Send** from Tommy's mailbox: the exact subject and text, to the one recipient, BCC the HubSpot logging address if `context/config.json` has one.
5. **Confirm** it's in the sent folder. Then write the sent key, set the row's status to "sent <date>", and save a copy to `data/partners/dream100/<id>/sent-<n>.md`.
6. **If the send can't be confirmed,** look in the sent folder before anything else. Never send a second time on a guess.
7. **If the mailbox can't send** (Connect apps doesn't allow it): save it as a draft in Tommy's mailbox if that works, or give TMEC Command the text for Tommy to send, and mark the row "Tommy to send". Mark it sent only when it shows in his sent folder.
8. **"no":** status "declined by Tommy", nothing sent. **"change":** a new draft with his change, queued again.

## Done means
The exact approved text went to one person once, and the row and sent key say so.

## Never
- Send without a matching yes, or change a word after the yes.
- Send to anyone on `opt-outs.csv`.
- Send a follow-up Tommy didn't approve as its own item.
