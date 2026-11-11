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
5. **Queue each item** at `/workspace/tmec-team/approved/pending/seo/<id>.md`:
   ```
   ITEM: <id>
   BOT: seo
   KIND: gbp-post | gbp-qa | gbp-profile
   WHERE: Google Business Profile
   WHY: <the gap or search behind it, with source and date>
   HOW IT GOES OUT: Tommy publishes it from the profile. The bot can't, unless he grants a connection.
   PHOTO: <what to use, or none>
   TEXT:
   <the exact text>
   HASH: <sha256 of TEXT>
   ```
6. **Act on a decision.** `yes`: mark "approved, hand to Tommy to publish", give him the exact text, add the id to `state/sent-keys-seo.md`. `no`: mark declined. `change`: a new item. Record "published" only when Tommy says so or the public profile shows it (link it).

## Done means
Each profile gap has a draft waiting on Tommy or a reason; every draft uses only real material and facts.

## Never
- Publish, or log in to the profile.
- Invent a job, photo, customer, result or review.
- Offer anything in return for a review or a follow, or ask for a review in a post in a way that breaches Google's rules.
- Add a category or service TMEC doesn't provide.
