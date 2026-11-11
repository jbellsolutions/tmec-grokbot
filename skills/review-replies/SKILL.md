---
name: review-replies
description: Finds TMEC's new public reviews (Google first, then any other public review page TMEC has) and drafts a reply to each in Tommy's voice for his yes. Used by SEO's weekly routine and when TMEC Command sends a review job. Drafts only; Tommy posts the reply.
---

# Review replies

## Inputs
- TMEC's public reviews (Grok web search; the profile's reviews as a visitor sees them; any other review page TMEC has, such as SolarQuotes or ProductReview, if `facts.md` lists one).
- `/workspace/tmec-team/data/seo/reviews.csv`: reviews already seen. Columns: `id,platform,reviewer,stars,date,link,status,note`. `id` is the first 12 characters of the SHA-256 of the platform, reviewer and date.
- `/workspace/tmec-team/context/owner.md`: Tommy's sign-off and voice notes.
- `/workspace/tmec-team/repo/policies/AU-COMPLIANCE.md`.

## Steps
1. **Read** the reviews, newest first. Anything not in `reviews.csv` is new; add it with status `new`. A review page you can't read is `UNKNOWN: <page>`, never "no new reviews".
2. **Draft a reply to each new review** (at most 10 a run; the rest wait, listed). In Tommy's voice, first person, 25 to 70 words, plain Australian English:
   - 4 to 5 stars: thank them by first name as shown, name one real thing they said, and say it matters to the crew.
   - 3 stars or less: thank them, apologise for the part that went wrong without arguing or admitting fault for something unproven, say Tommy will look into it, and give the office contact from `owner.md` so it moves off the public page. Don't explain the job in public.
   - Never: a price, rebate amount, saving or install date; a customer's address, job details or private information; a promise (refund, redo, call-back) Tommy hasn't made; a link; an offer in exchange for changing or removing a review; blaming the customer; an ask for a review or a "5 stars".
   - A review that names a staff member, reports a safety problem, threatens legal action, or looks fake or from a competitor: don't draft a public reply. Write a pending item `KIND: review-flag` with the link and one plain line, and stop. Tommy decides (including flagging it to Google himself).
3. **Queue each reply** at `/workspace/tmec-team/approved/pending/seo/<id>.md`:
   ```
   ITEM: <id>
   BOT: seo
   KIND: review-reply
   WHERE: <platform> review by <reviewer>, <stars> stars, <date> (<link>)
   REVIEW SAYS: "<verbatim, at most 40 words>"
   HOW IT GOES OUT: Tommy posts it from the profile owner's account. The bot can't, unless he grants a connection.
   TEXT:
   <the reply>
   HASH: <sha256 of TEXT>
   ```
   Set the review's status to `drafted` in `reviews.csv`.
4. **Act on a decision.** `yes`: status `approved`; give Tommy the exact text; add the id to `state/sent-keys-seo.md`. `no`: `skipped`. `change`: a new item. Mark `posted` only when Tommy says so or the public reply shows (link it).
5. **Summary for the audit.** Count: new, drafted, waiting, unanswered older than 7 days, average stars as shown. No numbers that can't be read.

## Review rules (Google and ACCC)
TMEC never asks only happy customers for a review (gating), never pays or rewards anyone for a review, never writes or buys a review, and never asks for a review to be removed in return for anything. Asking all customers neutrally for honest feedback, through a link TMEC owns, is Tommy's decision and is not drafted here. If Tommy wants a review-request message, this bot says it can't write one that breaks these rules and gives him the compliant version for his yes.

## Done means
Every new review has a reply waiting on Tommy, a flag, or a reason it is waiting; nothing was posted.

## Never
- Post or log in.
- Invent a review, a reviewer or a response from a customer.
- Reveal anything a customer didn't already say publicly.
- Argue with a reviewer in public.
