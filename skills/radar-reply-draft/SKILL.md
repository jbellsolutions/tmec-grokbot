---
name: radar-reply-draft
description: Writes a short, helpful reply in Tommy's voice to one hot or medium buyer Lead Radar found, queues it for Tommy's yes, records his decision, and drafts at most two follow-ups. Used by Lead Radar's Radar sweep routine and when TMEC Command sends a radar reply job. Tommy posts every reply himself.
---

# Radar reply draft

## Inputs
- The buyer's ledger row and hand-off line (`/workspace/tmec-team/data/radar/ledger.csv`, `/workspace/tmec-team/data/radar/handoff/<date>.jsonl`), and the post's public page.
- The community's public rules page, read today.
- `/workspace/tmec-team/context/owner.md`: Tommy's sign-off, and the only things TMEC may offer.
- `/workspace/tmec-team/repo/policies/AU-COMPLIANCE.md`.

## Steps
1. **Check the rules.** If the community bans business promotion or needs a flair or disclosure, say so under `RULES:`. If a reply naming TMEC isn't allowed there, set `TEXT:` to `DO NOT POST HERE` and still queue it so Tommy sees why. Never write a reply that hides TMEC.
2. **Write the reply** in Tommy's voice: Australian English, plain words, short sentences, like a tradie who knows his stuff. Helpful first, no hard sell. Up to 120 words on Reddit and forums; up to 80 on X and Facebook comments.
   - One sentence that shows you read their post (use one real detail).
   - One or two things that are genuinely useful (what to ask any installer: who does the install, what the warranty covers, whether the battery suits the existing system; for hail: take photos, read the policy before you sign anything).
   - One line saying it is from TMEC, a local team with its own install crews that doesn't subcontract the installs.
   - An open door: ask here and I'll answer.
3. **Rules for the words.** No price, rebate amount, saving or install date. If a rebate matters, say the current figures are on the government's site; a figure goes in only with its government source and the date checked. No offer (free quote, site visit) unless `owner.md` lists it. No link unless `owner.md` allows one. Never "guaranteed", "free solar", or a customer story. No competitor named. Never reveal anything about the person beyond what they wrote.
4. **Queue it.** Write `/workspace/tmec-team/approved/pending/lead-radar/<id>.md` (in test mode or a test run the id starts with `test-`, for example `test-<id>`):
   ```
   ITEM: <id>
   BOT: lead-radar
   WHY: <HOT|MEDIUM> · <area and evidence> · <one-line need> · THEIR WORDS: "<verbatim, at most 30 words>" · RULES: <community rules read on <date>; promotion allowed? disclosure needed?>
   ---PAYLOAD---
   TO: Tommy posts it himself, from TMEC's own account, at <post link> (<platform>, posted <date>). The bot cannot post.
   SEND: when Tommy posts it (the bot never posts)
   SUBJECT: none
   TEXT:
   <the reply, or DO NOT POST HERE>
   ---END---
   HASH: <sha256 of every byte between the ---PAYLOAD--- line and the ---END--- line, newlines included>
   ```
   Set the ledger status to `drafted`. The hand-off line (written by `radar-sweep`) carries this item's id and the reply text.
5. **Act on a decision.** For each file in `/workspace/tmec-team/approved/decisions/lead-radar/` whose id isn't already in `/workspace/tmec-team/state/sent-keys-lead-radar.md`:
   - **Recompute** the sha256 of the pending file's payload now (every byte between the `---PAYLOAD---` line and the `---END---` line) and compare it with the decision's `HASH:`. Never compare two copied lines. A mismatch means the item changed after Tommy saw it: ignore the decision, say so in the daily note and tell TMEC Command.
   - There is no outward action here (Tommy posts it himself), so the rest of the send gate has nothing to switch off, but in test mode write only to `state/test/` and leave the live sent keys alone.
   - `yes`: set ledger status `approved` ("approved, Tommy to post"). Add the item id to `sent-keys-lead-radar.md` with the outcome `approved, Tommy to post`. Posted is set later, only from Tommy's report (step 6).
   - `no`: set `skipped`; append a `skipped` update line to the hand-off; add the id to `sent-keys-lead-radar.md` with the outcome `declined`.
   - `change`: write a new item `<id>-2` with the changed text, once. Add the original id to `sent-keys-lead-radar.md` with the outcome `changed, redrafted as <id>-2`. Nothing goes out.
   The sent-keys line means the decision has been handled, so "no" and "change" are never read again.
6. **Record Tommy's report.** When a job says "posted <id>" or "skip <id>", set the ledger status `posted` (with the date) or `skipped`, append the update line to the hand-off file, and add the job id to `state/done-lead-radar.md`. Only Tommy's report sets `posted` or `won`.
7. **Follow-ups.** If a post is `posted` more than 1 business day, and the thread (read publicly) shows no answer, draft follow-up 1 as item `<id>-fu1`. After 2 more business days with no answer, draft follow-up 2 (`<id>-fu2`). If they answered, draft one reply to their answer and stop. Never a third follow-up. Each follow-up adds something useful and doesn't repeat the first reply. Each is queued in the item format above and needs Tommy's yes.

## Done means
Each hot and medium buyer has one reply waiting on Tommy with the rules check, or a recorded decision; nothing was posted by the bot.

## Never
- Post or send anything.
- Draft a second first reply for the same post.
- Hide that the reply is from TMEC.
- Set `posted` or `won` without Tommy's words.
- Write a sales reply to a safety post.
