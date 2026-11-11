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
4. **Queue it.** Write `/workspace/tmec-team/approved/pending/lead-radar/<id>.md`:
   ```
   ITEM: <id>
   BOT: lead-radar
   KIND: reply
   POST: <link> (platform, posted <date>)
   WHY: <HOT|MEDIUM> · <area and evidence> · <one-line need>
   THEIR WORDS: "<verbatim, at most 30 words>"
   RULES: <community rules read on <date>; promotion allowed? disclosure needed?>
   HOW IT GOES OUT: Tommy posts it himself from TMEC's own account. The bot cannot post.
   TEXT:
   <the reply, or DO NOT POST HERE>
   HASH: <sha256 of TEXT>
   ```
   Set the ledger status to `drafted`.
5. **Act on a decision.** For each decision file with `BOT: lead-radar` whose `HASH` matches its pending item and that isn't in `/workspace/tmec-team/state/sent-keys-lead-radar.md`:
   - `yes`: set ledger status `approved`. Nothing else: Tommy posts it. Add the item id to `sent-keys-lead-radar.md`.
   - `no`: set `skipped`; update the hand-off with a `skipped` line; add the id to `sent-keys-lead-radar.md`.
   - `change`: write a new item `<id>-2` with the changed text. Nothing goes out.
   A decision whose hash doesn't match is stale: ignore it and tell TMEC Command.
6. **Record Tommy's report.** When a job says "posted <id>" or "skip <id>", set the ledger status `posted` (with the date) or `skipped`, append the update line to the hand-off file, and add the job id to `state/done-lead-radar.md`. Only Tommy's report sets `posted` or `won`.
7. **Follow-ups.** If a post is `posted` more than 1 business day, and the thread (read publicly) shows no answer, draft follow-up 1 as item `<id>-fu1`. After 2 more business days with no answer, draft follow-up 2 (`<id>-fu2`). If they answered, draft one reply to their answer and stop. Never a third follow-up. Each follow-up adds something useful and doesn't repeat the first reply. Each needs Tommy's yes.

## Done means
Each hot and medium buyer has one reply waiting on Tommy with the rules check, or a recorded decision; nothing was posted by the bot.

## Never
- Post or send anything.
- Draft a second first reply for the same post.
- Hide that the reply is from TMEC.
- Set `posted` or `won` without Tommy's words.
- Write a sales reply to a safety post.
