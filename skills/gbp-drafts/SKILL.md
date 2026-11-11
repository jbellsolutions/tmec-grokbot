---
name: gbp-drafts
description: Drafts TMEC's Google Business Profile posts, Q&A answers, and category, service and photo suggestions, each as an item for Tommy's yes. Used by SEO's weekly routine and when TMEC Command sends a Google profile job. Drafts only; Tommy publishes.
---

# Google Business Profile drafts

## Inputs
- `/workspace/tmec-team/data/seo/facts.md`: what the profile shows now, read this run by `seo-audit`.
- `/workspace/tmec-team/data/seo/searches.md` and `audit/<date>.md`.
- `/workspace/tmec-team/context/owner.md`: Tommy's voice notes, the services and areas he confirmed, what TMEC may offer.
- Real material TMEC has: job photos or notes Tommy or TMEC Command pointed to in `/workspace/tmec-team/requests/to-seo/`. Never invent a job, a customer or a result.
- `/workspace/tmec-team/repo/policies/AU-COMPLIANCE.md`.

## Steps
1. **Read the profile gaps** from the facts: stale posts (no post in 7 days), few photos, empty or wrong categories or services, unanswered public questions, missing service areas, a link that doesn't match the website.
2. **Draft up to 5 posts** for the week (a mix of: a helpful tip, a local job from real material, a seasonal note such as storm season or battery question, an offer only if `owner.md` lists one). Each 80 to 200 words, plain Australian English, one suburb or service in focus, a clear single action (call, visit the page), and TMEC named. No price, rebate amount, saving or install date unless a government source and date checked sit beside it. No customer's name or address without their written yes (Tommy confirms). No claim TMEC can't prove. No competitor named. Don't invent a photo: write `PHOTO: <what real photo to use>` or `PHOTO: none`.
3. **Q&A.** For each public question on the profile (if it shows), draft an answer from facts only. You may suggest up to 3 common questions with answers for Tommy to post himself as the owner, clearly his own; never post a question under a made-up customer's name.
4. **Categories, services, photos.** Suggest, with the reason from the audit: a primary category and up to 3 secondary categories that match what TMEC really does, services to list, and the photos worth adding (what, not an invented image). Never suggest a category TMEC doesn't provide (for example air conditioning, unless Tommy confirmed it).
5. **Queue each item.** Every item uses the payload format in `/workspace/tmec-team/repo/policies/APPROVALS.md`, section "Items, decisions and the send gate": `ITEM`, `BOT: seo`, `WHY`, then `---PAYLOAD---` (`TO`, `SEND`, `SUBJECT`, `TEXT`), `---END---`, and `HASH` = sha256 of every byte between those two lines, newlines included. The `ITEM:` id is the file name without `.md`. In test mode (the routine is listed `test`, or `context/config.json` `run` is `test`) ids start `test-`, data files go under `/workspace/tmec-team/state/test/seo/`, and nothing else changes: this bot never publishes, so there is no outward action and no paid call to switch off.
   Ids: `gbp-<YYYY-MM-DD>-<n>` (post), `gbpqa-<YYYY-MM-DD>-<n>` (Q&A), `gbpprofile-<YYYY-MM-DD>-<n>` (categories, services, photos). Write `/workspace/tmec-team/approved/pending/seo/<id>.md`:
   ```
   ITEM: <id>
   BOT: seo
   WHY: <the gap or search behind it, with source and date>
   ---PAYLOAD---
   TO: Google Business Profile (Tommy publishes it from the profile; the bot can't, unless he grants a connection)
   SEND: when Tommy publishes it
   SUBJECT: <gbp-post | gbp-qa | gbp-profile>
   TEXT:
   <the exact text>
   PHOTO: <what to use, or none>
   ---END---
   HASH: <sha256 of every byte between the ---PAYLOAD--- line and the ---END--- line, newlines included>
   ```
6. **Act on a decision.** For each file in `/workspace/tmec-team/approved/decisions/seo/` whose id isn't in `/workspace/tmec-team/state/sent-keys-seo.md`: **recompute** the sha256 of the pending file's payload now and compare it with the decision's `HASH:` (a mismatch means the item changed after Tommy saw it: ignore it and tell TMEC Command). This bot publishes nothing, so the rest of the send gate has nothing to hold back. `yes`: mark "approved, hand to Tommy to publish", give him the exact text through TMEC Command, and add the id to `state/sent-keys-seo.md` with the outcome `approved, handed to Tommy`. Record "published" only when Tommy says so or the public page shows it (link it). `no`: mark declined and add the id with the outcome `declined`. `change`: redraft once as a new item with a new id and add the old id with the outcome `changed, redrafted as <id>`. A decision is never read again once its id is in the sent keys.

## Done means
Each profile gap has a draft waiting on Tommy or a reason; every draft uses only real material and facts.

## Never
- Publish, or log in to the profile.
- Invent a job, photo, customer, result or review.
- Offer anything in return for a review or a follow, or ask for a review in a post in a way that breaches Google's rules.
- Add a category or service TMEC doesn't provide.
