---
name: partner-score
description: Scores a prospective TMEC partner with the rubric's hard gates and 100 points, from public sources, and files it on the right list. Also fills the Dream 100 list when fewer than 5 rows are scored. Used by Dream 100, Dream 500 and Trades Outreach whenever a business is added or re-checked.
---

# Partner score

## Usage (read less)

Read each business's site or listing with `python3 /workspace/tmec-team/repo/usage/scripts/clean_page.py <url> --max-chars 4000`, never the full page; pick rows from the list files with `sheet_q.py`. Scripts: `usage/SKILL.md`.

## Inputs
- `/workspace/tmec-team/repo/partners/kit/RUBRIC.md`: the gates, the ten criteria and the tiers.
- `/workspace/tmec-team/repo/partners/kit/partner-types.md`: the ranked trades and the "beyond trades" partners.
- `/workspace/tmec-team/repo/partners/lists/dream-seed.csv`: 219 named businesses with their source pages (11 Nov).
- `/workspace/tmec-team/context/owner.md`: Tommy's own names (Wave 0).
- The business's own website, Google listing and reviews.
- `/workspace/tmec-team/data/partners/opt-outs.csv`.

## Test mode
In test mode, or when `config.json` `run` is `test`, write list rows under `/workspace/tmec-team/state/test/partners/` (same file names) instead of `data/partners/`. Scoring makes no paid call.

## Row ids
`<list>-<nnn>`: `d100-` on `dream100.csv`, `d500-` on a Dream 500 segment list, `trd-` on `trades.csv`. `<nnn>` is the next free number in that list file (three digits, more when needed). An id is never reused or renumbered. The row keeps its id when it changes status.

## Status values
Every row has exactly one. `updated` is the date it last changed.

| Status | Means | Set by |
|---|---|---|
| `research` | Three or more unknowns, so not on a list yet | the scorer |
| `scored` | Passed the gates, scored, in this list's tier, no message yet (Dream 100) | the scorer |
| `waiting on Tommy` | A message or wave is in `approved/pending/` | the drafter |
| `sent` | The approved message went out (Dream 100), once | the sender |
| `replied` | They answered; a draft or an opt-out is being handled | `partner-replies` |
| `yes` | They said yes to a campaign; Dream 100 now owns them (`partner-campaign-run`) | `partner-replies` |
| `no` | They said no | `partner-replies` |
| `declined` | We stopped: Tommy said no, or no reply after the last touch (the reason is in `notes`) | the sender, or the wave |
| `opted out` | They asked to stop; they're in `opt-outs.csv` | `partner-replies` |
| `out` | Failed a gate or scored under 30 (the reason and page are in `evidence`) | the scorer |

The two cold-email lists (Dream 500 and trades) also use `listed` (their form of `scored`: has a published email), `no email`, `nurture` (30 to 49, never emailed), `in wave <wave-id>`, `held out <wave-id>`, `contacted <date>` (the wave launched) and `bad address`. Only `partner-replies` moves a row to `replied`, `yes`, `no` or `opted out`.

## Steps
1. **Gates first.** Check each hard gate from the business's own pages. Fail one and it's `out`, with the reason and the page that shows it. Unknown on "sells solar" means read the site's services page before going on.
2. **Score the ten criteria.** Full, half or 0, each with one line of evidence and its link. Unknown scores 0. Three or more unknowns: status `research`, not a list. On criterion 5 (insurance fit), score only what the business's own pages say about panels: the 8 Nov call recorded that panel lists are on insurers' websites, but the 11 Nov check of RACQ, Suncorp, AAMI, QBE, Allianz, Youi and NRMA found only motor repairer schemes published.
3. **Tier:** 75+ Dream 100, 50 to 74 Dream 500, 30 to 49 nurture, under 30 out. A trade business (a ranked trade in partner-types.md) in the top ten of its trade goes to the trades list whatever its tier, unless it scored 75+, when the Dream 100 keeps it.
4. **Write the row** only to your own list file: Dream 100 writes `data/partners/dream100.csv`, Trades Outreach `data/partners/trades.csv`, Dream 500 `data/partners/dream500/<segment>.csv`. A business that belongs on another bot's list goes in your daily note as a line `for dream-500: <business>, <score>, <page>` or `for trades-outreach: ...`, and TMEC Command passes it on. Never write another bot's file.
5. **No duplicates.** Before adding, check all three list files and `opt-outs.csv` by business name, website and phone. The Dream 100 list wins, then trades, then Dream 500.

Row columns: `id, business, website, phone, suburb, segment, trade_rank, gates, score, tier, evidence (criterion: points: link; ...), contact_name, contact_email, contact_source, status, updated`.

## Filling the Dream 100 list (Dream 100 only)
Run this first in every Dream 100 drafts run, and whenever TMEC Command asks. Count the rows in `data/partners/dream100.csv` with status `scored`. **If fewer than 5**, score up to 10 more, in this order:
1. Tommy's own names in `context/owner.md` (Wave 0), in the order he gave them.
2. Then the rows of `/workspace/tmec-team/repo/partners/lists/dream-seed.csv`, starting with bucket A, skipping any already on a list or in `opt-outs.csv`.

Score each with steps 1 to 5 above. Only a row that lands in the Dream 100 tier (75 or more, gates passed) is written to `dream100.csv`, with status `scored`. Every other business you scored becomes a line in your daily note: `for dream-500: <business>, <score>, <page>` (50 to 74, not a ranked-trade top ten) or `for trades-outreach: <business>, <score>, <page>` (a ranked trade). Under 50 is recorded in the daily note as `not listed: <business>, <score>, <reason>` and nowhere else. Stop at 10 scored in a run, or when the seed and Tommy's names run out; if there are still fewer than 5 `scored` rows, say so in the daily note ("Dream 100 list short: <n> scored") so Tommy can add names.

## Done means
Every row has gates, a score and evidence with links, a status from the table, and sits on exactly one list.

## Never
- Use a paid enrichment service, a bought list, or a guessed email (like info@ copied from a pattern). An email comes from the business's own page, or it stays blank.
- Score from memory.
- Add a business that's in `opt-outs.csv`.
- Write to another bot's list or to `data/crm/`.
