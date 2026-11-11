---
name: capacity-board
description: Rebuilds the install capacity board from the schedule read today, answers "how fast can we get a job in?", and warns TMEC Command when the two teams are running out of room. Used by Ops' Capacity board routine, and whenever Tommy or TMEC Command asks about install dates or whether the teams can take more work.
---

# Capacity board

TMEC has two in-house install teams and no subcontractors, so every date promised to a customer is a promise about those two teams. This skill never guesses a date: it reads the schedule and says what it read.

## Inputs
- The install schedule, read **today** (Brisbane date), from the source named under `schedule` in `/workspace/tmec-team/context/config.json`: `sheet` (a Google Sheet, one row per job: date, team, job type, suburb, days), `calendar` (one Google Calendar per team, one event per job), or `jobsoftware` (the job-management software, if it can be read). Access is read only, through Connect apps or a shared sheet. If `schedule` is missing, the source is unknown: the board says UNKNOWN.
- `/workspace/tmec-team/data/ops/capacity.md`: the board and the **Rules** at its top. Tommy confirms every rule; until he does it is UNKNOWN. Rules: usual days per job type per team; leave and public holidays; the normal and maximum wait Tommy is comfortable promising; any approval or parts lead time he wants added.
- HubSpot, read only through Connect apps: jobs sold but not yet scheduled (the backlog). Counts and job references only.
- This week's scoreboard in `/workspace/tmec-team/data/forecast/` (leads and quotes this week against last, for incoming load).

## Steps: the board (every run)
1. **Read the source now.** Note the time. If the read fails, write the board with status `UNKNOWN: cannot read the schedule`, the reason, and "not a promise". Never fall back to an older board.
2. **Rebuild** `/workspace/tmec-team/data/ops/capacity.md`: per team, per working day for the next 8 weeks (starting value), the job reference, job type and suburb. No customer names, phone numbers or street addresses. Mark leave and public holidays.
3. **Write the Status line** at the top: `GREEN`, `AMBER`, `RED` or `UNKNOWN`, with the read time and the date.
   - Measures: the earliest slot for a standard job; the share of working days booked in the next 4 weeks (starting value); the backlog count.
   - AMBER when the earliest slot passes Tommy's normal wait; RED when it passes his maximum. If Tommy hasn't given both, the status is `UNKNOWN: thresholds not set` and the raw numbers show. Never GREEN by default.
4. **On AMBER or RED**, add **Throttle options** under the status for TMEC Command. Use only outreach that brings in leads: Dream 100 sends, Dream 500 waves, Trades Outreach waves, reactivation batches, newsletter sends, radar replies. Never the lead vendors (Tommy keeps them as the baseline). For each option say what it would slow and what it wouldn't. Ops recommends; TMEC Command offers it to Tommy; nothing is slowed without his yes.
5. **File one item** in `/workspace/tmec-team/approved/pending/ops/<date>-capacity.md` when the status changes to AMBER or RED, not on every run (format below). On a Monday add `NOT_BEFORE: Tuesday 07:00`.
6. **Add incoming-load facts** (not a forecast): sold-not-scheduled count, quotes out in the last 30 days, leads this week against last week.
7. If the schedule is UNKNOWN two runs in a row, put it in the daily note for TMEC Command.

## Steps: answering "how fast can we get a job in?"
1. Read the source now (step 1 above). Never answer from yesterday's board.
2. Pin down the job type (solar, battery, EV charger, electrical, a combination) and size if it changes the days. If Tommy hasn't confirmed days for that type, say `UNKNOWN: days for <type>` and ask him one question. Don't assume.
3. Find the earliest start for each team: the first run of free working days long enough, skipping booked days, leave and public holidays.
4. Subtract the backlog honestly: jobs already sold and not yet on the schedule come first. Count them and say so. If the count is UNKNOWN, say the date may be later.
5. Answer in this shape: "Earliest slot: Team A, <weekday d Mon>; Team B, <weekday d Mon>. Read from <source> at <time>. Includes: <what>. Not included: <approvals, parts, finance, the customer's own availability>. Backlog ahead of this job: <n or UNKNOWN>."
6. If asked for words to send a customer, write a draft saying "the earliest we could be on site is <date>, subject to <not included>". Tommy or the sales lead sends it, never Ops.

## Steps: checking a planned surge
When TMEC Command gives a job in `/workspace/tmec-team/requests/to-ops/` (a wave size and date, before Tommy agrees to it): report the position as facts (status, earliest slot per team, backlog, weeks around the date that are already full). Add a line about expected sales only if the scoreboard shows a measured close rate for that source (30 leads or more); otherwise write `UNKNOWN: no measured close rate for <source> yet`. Recommend go, stagger or hold. Ops doesn't approve or schedule the surge.

## Output
- The answer, in the chat or in the daily note.
- `/workspace/tmec-team/data/ops/capacity.md`, rebuilt each weekday.
- A pending item on a change of status:
  ```
  ITEM: ops-<date>
  BOT: ops
  WHY: status changed to <AMBER|RED> · <the numbers, with source and read time>
  TEXT:
  <the throttle options, one per line, and the question "slow any of these?">
  HASH: <sha256 of TEXT>
  ```

## Done means
Every date in an answer came from a read made today and names its source; the board has no personal details; the status is never GREEN without Tommy's thresholds.

## Never
- Give a date from memory, from yesterday's board, or from a rule Tommy hasn't confirmed.
- Book, move or cancel an install, or message a customer.
- Present an optimistic slot without naming the backlog and what the schedule leaves out.
- Pause or change a lead vendor, or slow any outreach itself.
