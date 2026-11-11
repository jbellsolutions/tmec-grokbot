---
name: partner-score
description: Scores a prospective TMEC partner with the rubric's hard gates and 100 points, from public sources, and files it on the right list. Used by Dream 100, Dream 500 and Trades Outreach whenever a business is added or re-checked.
---

# Partner score

## Inputs
- `/workspace/tmec-team/repo/partners/kit/RUBRIC.md`: the gates, the ten criteria and the tiers.
- `/workspace/tmec-team/repo/partners/kit/partner-types.md`: the ranked trades and the "beyond trades" partners.
- `/workspace/tmec-team/repo/partners/lists/dream-seed.csv`: 219 named businesses with their source pages (11 Nov).
- The business's own website, Google listing and reviews.
- `/workspace/tmec-team/data/partners/opt-outs.csv`.

## Steps
1. **Gates first.** Check each hard gate from the business's own pages. Fail one and it's out, with the reason and the page that shows it. Unknown on "sells solar" means read the site's services page before going on.
2. **Score the ten criteria.** Full, half or 0, each with one line of evidence and its link. Unknown scores 0. Three or more unknowns: status "research", not a list.
3. **Tier:** 75+ Dream 100, 50 to 74 Dream 500, 30 to 49 nurture, under 30 out. A trade business (a ranked trade in partner-types.md) in the top ten of its trade goes to the trades list whatever its tier, unless it scored 75+, when the Dream 100 keeps it.
4. **Write the row** only to your own list file: Dream 100 writes `data/partners/dream100.csv`, Trades Outreach `data/partners/trades.csv`, Dream 500 `data/partners/dream500/<segment>.csv`. A business that belongs on another bot's list goes in your daily note as "for <bot>", and TMEC Command passes it on.
5. **No duplicates.** Before adding, check all three list files and `opt-outs.csv` by business name, website and phone. The Dream 100 list wins, then trades, then Dream 500.

Row columns: `id, business, website, phone, suburb, segment, trade_rank, gates, score, tier, evidence (criterion: points: link; ...), contact_name, contact_email, contact_source, status, updated`.

## Done means
Every row has gates, a score and evidence with links, and sits on exactly one list.

## Never
- Use a paid enrichment service, a bought list, or a guessed email (like info@ copied from a pattern). An email comes from the business's own page, or it stays blank.
- Score from memory.
- Add a business that's in `opt-outs.csv`.
