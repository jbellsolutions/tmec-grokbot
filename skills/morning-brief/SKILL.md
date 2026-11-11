---
name: morning-brief
description: Writes Tommy's morning brief from every bot's notes and the approval queue. Used by TMEC Command's Morning brief routine and whenever Tommy asks "what's going on?".
---

# Morning brief

## Inputs
- `/workspace/tmec-team/daily/<yesterday>/` and `/workspace/tmec-team/daily/<today>/`: each bot's note (`<bot>.md`).
- `/workspace/tmec-team/approved/pending/*/`: every item waiting on Tommy.
- `/workspace/tmec-team/log/runs-<YYYY-MM>.md`: yesterday's and today's lines.
- `/workspace/tmec-team/data/ops/capacity.md` (Ops) and, on Mondays, `/workspace/tmec-team/data/forecast/scoreboard-<date>.md` (Forecast).

## Steps
1. **Waiting on Tommy.** List every pending item, oldest first, at most 7 (starting value). Each is one line: number, bot, what, who it goes to, "yes or no?". Number them 1 to 7 and record the number-to-item map in `daily/<today>/brief-items.md` so his reply ("yes to 1 and 3") maps to the right items. Items past the first 7 are counted ("+4 more").
2. **One line per bot,** in this order: Lead Radar, Dream 100, Dream 500, Trades Outreach, CRM & Reactivation, Content Studio, SEO, Ops, Forecast, Vendor Scout. Each line says what happened, with the number and its file. A bot with no run-log line since the last brief is "no run". A run that failed is FAILED with its reason. A source a bot couldn't read is UNKNOWN.
3. **Capacity:** the next free install slot from Ops, if Ops wrote today.
4. **Mondays:** two lines from Forecast's scoreboard.
5. Save to `daily/<today>/brief.md`; put it at the top of `vault/Daily/<today>.md`; send it to Tommy.

## Output
Under 200 words. Decisions first, then bots, then capacity.

## Done means
Every line has a source, every waiting item is listed once, and the number map is saved.

## Never
- Fill a gap with a guess. "No run" and UNKNOWN are honest answers.
- Put a customer's phone number or email in the brief.
- Mark an item approved. Only Tommy's reply does that (`approval-queue`).
