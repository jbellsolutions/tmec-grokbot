---
name: rebate-watch
description: Re-checks the Clean Energy Regulator's rebate pages each month and keeps the rebate calendar, every fact with its source and the date checked. Used by Forecast's Rebate watch routine, and whenever Tommy or TMEC Command asks what steps down and when.
---

# Rebate watch

Tommy's own words (28 Oct call [13:25]): the next drop is "the end of this year. So 1st of January"; the battery rebate "drops every six months, solar every 12 months". Those are his statements. This skill turns them into a dated calendar that says where each fact comes from, and never states a figure it hasn't checked.

## Usage (read less)

Run `python3 /workspace/tmec-team/repo/usage/scripts/page_diff.py <page url> /workspace/tmec-team/data/forecast/watch` on each page first. No output means the page hasn't changed: keep the facts and re-date them. Read only the changed lines. Scripts: `usage/SKILL.md`.

## Inputs
- `/workspace/tmec-team/data/forecast/rebates.md`: the calendar, Forecast's own file. First run: create it with the columns `Scheme | What steps down | Next step | Cadence | Source URL | Date checked | Status`.
- `/workspace/tmec-team/context/owner.md`: Tommy's rebate statements.
- Public pages, found at run time on cer.gov.au (the Solar batteries page and the Deeming period decline page) and other `.gov.au` sites. Record each page's URL and the date read. Don't rely on a remembered URL, amount or date.
- This week's scoreboard in `/workspace/tmec-team/data/forecast/` and `/workspace/tmec-team/data/ops/capacity.md`, for the plan around a step.

## Test mode
If the routine is listed `test` in `context/routines-on.md`, or `context/config.json` `run` is `test`: write the scoreboard, `rebates.md` and notes under `/workspace/tmec-team/state/test/forecast/` instead of `data/forecast/` (Content Studio and Ops read the live files, so a test run must not replace them), start item ids with `test-`, and leave the live sent keys alone. Reading public pages and HubSpot counts is free, so it still happens. This bot makes no paid call and sends nothing.

## Steps
1. Open `rebates.md`. If a row is new, seed it from the facts checked on 28 Oct 2026 against the Clean Energy Regulator: the battery factor, in certificates per kWh of usable capacity, is 6.8 for installs May to December 2026, **5.7 from 1 January 2027**, 5.2 from 1 July 2027 (the CER's table runs further; copy it with its source); rooftop solar's deeming period is 5 years for 2026 and 4 for 2027. The installation date decides the rebate, not the signing date. Mark each `FROM TOMMY` or `VERIFIED` as it stands.
2. For each row, find the governing government page and read it now. If it confirms, set `VERIFIED` with the URL and today's date. If it differs from the row or from Tommy's words, show both and file a pending item `/workspace/tmec-team/approved/pending/forecast/fc-<YYYY-MM-DD>-rebate-<n>.md` (the `ITEM:` id is the file name without `.md`) in the shared item format (`/workspace/tmec-team/repo/policies/APPROVALS.md`, "Items, decisions and the send gate"):
   ```
   ITEM: <id>
   BOT: forecast
   WHY: <one line, with the source and date behind it>
   ---PAYLOAD---
   TO: TMEC Command, for Tommy to decide (nothing goes out from this bot)
   SEND: <show Tommy now | Tuesday if filed on a Monday>
   SUBJECT: none
   TEXT:
   <the question, and the facts behind it>
   ---END---
   HASH: <sha256 of every byte between the ---PAYLOAD--- line and the ---END--- line, newlines included>
   ```
   with both versions and their sources in `TEXT`. If no page can be read, keep the row as it was and write "tried <date>, couldn't read: <reason>". Never delete a row.
3. Never write an amount, factor, percentage or date that isn't in a row with a source and a date checked. Never state the dollar value of a certificate.
4. Count the days from today to each verified next step. Inside 120 days, write a short plan as notes for TMEC Command (not actions): Content Studio an honest "what's changing on <date>" with only verified figures, partner bots timing, Ops whether the teams can take the extra demand (check capacity first; if AMBER or RED, bringing demand forward waits for Tommy).
5. After a step has passed, re-point the "next step" lines (for example, after 1 January 2027 the battery next step is 1 July 2027). Never write about a step that has happened as if it were coming.
6. Commercial solar's "new rebate" (Tommy [10:43]): if a CER page confirms it, record it as `VERIFIED` with URL and date; otherwise `FROM TOMMY`, details UNKNOWN.
7. Add a "What to watch" note, at most 3 lines, each from a public source cited with URL and date read, labelled `candidate, unvalidated`. No market sizes unless a cited source gives them.
8. Write `rebates.md` with a "Checked" line at the top (today's date) and a "What changed since last month" section. Content Studio reads this file for the newsletter, so keep each fact on its own line with its source.
9. Write the daily note `daily/<today>/forecast.md`; if the Monday scoreboard already wrote it today (it can, when the 1st is a Monday), **append** your section and never overwrite it.
10. **Decisions.** For each file in `/workspace/tmec-team/approved/decisions/forecast/` whose id isn't in `/workspace/tmec-team/state/sent-keys-forecast.md`: recompute the sha256 of the pending item's payload now and compare it with the decision's HASH (a mismatch means the item changed after Tommy saw it: ignore it and tell TMEC Command). `yes`: note it and tell TMEC Command to carry it out (this bot changes nothing outside its own files, so no send gate applies); `no`: note it declined; `change`: refile once as a new item. Add the id and the outcome to the sent keys so it is never read twice.

## Done means
Every rebate fact has a source URL and a date checked, or is marked FROM TOMMY or UNKNOWN; nothing is filled from memory.

## Never
- State a rebate amount, factor, percentage or scheme rule from memory.
- Tell Tommy the boom will last or end on a date; his 12 to 18 months is his estimate and is shown as his.
- Present a candidate as a plan.
- Use a paid data service.
