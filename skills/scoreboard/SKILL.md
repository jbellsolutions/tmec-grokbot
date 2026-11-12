---
name: scoreboard
description: Builds the Monday scoreboard: every lead source against Tommy's bought-lead numbers, with UNKNOWN where a source has no data, and answers "what would it generate?" with break-even figures, never a promise. Used by Forecast's Monday scoreboard routine, and whenever Tommy asks how the lead sources are doing.
---

# Scoreboard

The answer to "what would it generate?" is a scoreboard, not a promise. Tommy's own numbers are the yardstick: bought leads at about 60 a lead, closing in the mid-20s percent, so roughly 240 to 250 a sale (his figures from the 28 Oct call; AUD is inferred; not yet measured).

## Usage (read less)

Answer each number with `python3 /workspace/tmec-team/repo/usage/scripts/sheet_q.py <file> "select ..."` and keep the source file closed. Scripts: `usage/SKILL.md`.

## Inputs
- `/workspace/tmec-team/context/owner.md`: Tommy's bought-lead figures (cost per lead, close rate). Missing: the line is UNKNOWN and says so.
- Counts for the week (Saturday to Friday, Brisbane), by source, from files and HubSpot, read only, with the one read-only token `HUBSPOT_TOKEN` in `/workspace/tmec-team/.secrets/hubspot.env` (the only HubSpot route this bot has: not Connect apps; counts and dates only, no personal details):
  - bought leads: HubSpot, where a source tag exists; spend is UNKNOWN unless Tommy has given it
  - radar: `/workspace/tmec-team/data/radar/handoff/` and HubSpot
  - partners, by list (Dream 100, Dream 500, Trades): `/workspace/tmec-team/data/partners/` and the partner code in HubSpot
  - reactivation and follow-up: `/workspace/tmec-team/data/crm/`
  - newsletter: `/workspace/tmec-team/data/content/`
  - SEO: `/workspace/tmec-team/data/seo/`
  - paid ads (Meta, Google): only figures Tommy's Claude Code reports, in a job in `/workspace/tmec-team/requests/to-forecast/`. Nothing reported: UNKNOWN.
- The last scoreboard in `/workspace/tmec-team/data/forecast/`, for the cumulative table.

## Test mode
If the routine is listed `test` in `context/routines-on.md`, or `context/config.json` `run` is `test`: write the scoreboard, `rebates.md` and notes under `/workspace/tmec-team/state/test/forecast/` instead of `data/forecast/` (Content Studio and Ops read the live files, so a test run must not replace them), start item ids with `test-`, and leave the live sent keys alone. Reading public pages and HubSpot counts is free, so it still happens. This bot makes no paid call and sends nothing.

## Definitions
- **Lead:** a person with contact details who asked for, or accepted, a conversation about a quote, created in HubSpot in the window. A radar post is not a lead until it is in HubSpot.
- **Quote:** sent in the window. **Sale:** a deal signed in the window. **Revenue:** the signed value as HubSpot records it (GST status UNKNOWN until Tommy says).
- **Spend:** direct cash cost of the source in the window. Shared costs go on a separate `overhead` line and are never spread across sources.
- **One source per lead:** the first source wins. A lead with no tag goes under `untagged` so totals reconcile.
- Weekly counts are events in that week, so a week's close rate understates until its leads have had time to close. Judge a source on the cumulative table.

## Steps
1. Work out the window. If `scoreboard-<date>.md` for it exists, this is a re-run: change nothing without noting old and new values.
2. For each source, collect leads, quotes, sales, revenue and spend. A number you couldn't read stays **UNKNOWN**, with the reason. Zero is written only when the source says zero.
3. Work out cost per lead, lead to quote, close rate, cost per sale, only where every input is known. Show the sample size (n) beside each. Under 30 leads: LOW.
4. Set each source against Tommy's line (about 60 a lead; mid-20s percent). Label it "Tommy's estimate". Add two break-even figures per source: the cost per lead it needs to match his cost per sale at its own close rate, and the close rate it needs at its own cost per lead. These are thresholds, not predictions.
5. Labels, only these: `TOMMY'S ESTIMATE` (his number, with the call), `ASSUMPTION` (needs Tommy's say-so or a cited public benchmark, else UNKNOWN), `MEASURED (n=<leads>, weeks <a> to <b>)`, `UNKNOWN`. An assumption is used only beside a break-even figure, never in a sentence about what TMEC will get. A source flips to MEASURED at 30 leads and 3 weeks of known spend; keep the old value beside it.
6. Write `/workspace/tmec-team/data/forecast/scoreboard-<YYYY-MM-DD>.md`: the line to beat; one table (source, leads, quotes, sales, cost per lead, close rate, cost per sale, n, label); the cumulative table; "UNKNOWN this week" with each reason; the break-even table.
7. If the measured bought-lead line has 30 or more leads, file a pending item `/workspace/tmec-team/approved/pending/forecast/fc-<YYYY-MM-DD>-measured-line.md` (the `ITEM:` id is the file name without `.md`), in the shared item format (`/workspace/tmec-team/repo/policies/APPROVALS.md`, "Items, decisions and the send gate"):
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
   The question in `TEXT` is "replace your stated numbers with the measured ones?". Only TMEC Command changes `owner.md`, in Tommy's words.
8. Put an 8-line summary in `/workspace/tmec-team/daily/<today>/forecast.md`. If the Rebate watch routine already wrote that note today (it can, when the 1st is a Monday), **append** your section and never overwrite it.
9. **Decisions.** For each file in `/workspace/tmec-team/approved/decisions/forecast/` whose id isn't in `/workspace/tmec-team/state/sent-keys-forecast.md`: recompute the sha256 of the pending item's payload now and compare it with the decision's HASH (a mismatch means the item changed after Tommy saw it: ignore it and tell TMEC Command). `yes`: note it and tell TMEC Command to carry it out (this bot changes nothing outside its own files, so no send gate applies); `no`: note it declined; `change`: refile once as a new item. Add the id and the outcome to the sent keys so it is never read twice.

## Answering "what would it generate?"
1. "I can't give you a number I'd stand behind. Nobody can, before a source has run."
2. "Your line to beat is about 60 a lead and mid-20s percent closing. That's your number, from your own business."
3. "For each source I can tell you the cost per lead it needs, at the close rate it actually gets, to match that. Here they are."
4. "As each source runs, its real figures replace my assumptions, with the sample size beside them."

## Done means
Every figure traces to a source named in the file; every UNKNOWN is listed with its reason; no assumption is shown as measured.

## Never
- Promise or forecast leads, sales or revenue.
- Treat an unknown as zero, or show a small sample without LOW.
- Read paid-ads accounts, or add paid-ads numbers nobody reported.
- Change Tommy's line itself.
