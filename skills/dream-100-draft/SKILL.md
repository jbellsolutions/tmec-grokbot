---
name: dream-100-draft
description: Researches one Dream 100 business and writes a message for it alone, then puts it in Tommy's approval queue. Used by Dream 100's drafts routine and when TMEC Command sends a Dream 100 job.
---

# Dream 100 draft

## Inputs
- The business's row in `/workspace/tmec-team/data/partners/dream100.csv`.
- Its website, listing, reviews and recent public posts (Grok web and X search).
- `/workspace/tmec-team/repo/partners/kit/partner-one-pager.md`, `partner-terms.md`, `outreach-sequence.md` (the rules section).
- `/workspace/tmec-team/context/owner.md`: Tommy's sign-off, phone, and the names he gave.
- `/workspace/tmec-team/context/config.json`: `partner_fee` and `partner_fee_trigger`.

## Steps
1. **Research** (save to `data/partners/dream100/<id>/research.md` with links): what they do, who their customers are, where they work, one recent job or post, who decides (owner's name from their own site), and the specific way they meet TMEC's customer (before, during, after, alongside).
2. **Pick the angle.** One reason this business, and only this one, should talk to Tommy. Insurance builders: thermal imaging, electrical and solar reports after a storm, rectification quotes ready to approve. Trades: their customer gets TMEC's own crew. Programs (panel makers, Origin, EV dealers): TMEC as their in-house installer on the Coast. Wave 0 (people Tommy already works with): thank them first, then ask who else he should meet.
3. **Write the message** from Tommy, first person: a short lowercase subject; 80 to 140 words; one specific line that shows we know their business; the in-house edge; one plain ask (a 10-minute call); no link in the first touch; Tommy's name, TMEC's name, and his phone. If `partner_fee_trigger` isn't set, leave money out. Never "affiliate".
4. **Check it** against the rules: true and sourced; nothing it promises Tommy hasn't promised; no air-con claim; under the word cap; the opt-out line ("If this isn't for you, just say so and I won't write again.").
5. **Queue it.** Write `/workspace/tmec-team/approved/pending/dream-100/<id>-<n>.md`:
   ```
   ITEM: <id>-<n>
   BOT: dream-100
   TO: <name>, <business>, <email> (source: <link>)
   WHY: <score> · <one-line angle>
   SUBJECT: <subject>
   TEXT:
   <the message>
   HASH: <sha256 of SUBJECT + TEXT>
   ```
   Set the row's status to "waiting on Tommy".

## Done means
A message only this business could get, with its research linked, waiting in the queue.

## Never
- Send. Sending is `dream-100-send`, after Tommy's yes.
- Write to a generic address you guessed, or to anyone in `opt-outs.csv`.
- Reuse another business's message with the name swapped.
