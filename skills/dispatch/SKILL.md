---
name: dispatch
description: Turns what Tommy asks for into a job for the one bot that owns it, and follows it to done. Used by TMEC Command whenever Tommy asks for work, and when Ops says capacity is full.
---

# Dispatch

## Inputs
- What Tommy said, in his words.
- `/workspace/tmec-team/repo/docs/TEAM-DESIGN.md`: which bot owns which job.
- `/workspace/tmec-team/repo/agents/<NN>-<bot>.md`: the owner's charter.
- `/workspace/tmec-team/state/done-<bot>.md`: jobs that bot finished.

## Steps
1. **Find the one owner.** Match the request to the "Owns" column of TEAM-DESIGN. If two bots could own it, the charter's "Only writer of" row decides. If nobody owns it, it's a new ask: add it with `ask-ledger` and tell Tommy which bot you'd give it to.
2. **Paid ads** (Meta, Google) aren't on this team. Tell Tommy they're with his Claude Code on the Mac and stop.
3. **Write the job** to `/workspace/tmec-team/requests/to-<bot-slug>/<YYYY-MM-DD>-<n>.md`:
   ```
   JOB: <date>-<n>
   FOR: <bot name>
   FROM: Tommy, <date time>, "<his words>"
   WHAT: <one job, in plain words>
   DONE MEANS: <checkable>
   BY: <the next brief | a date Tommy gave>
   ASK: <ledger number, if any>
   ```
   One topic per job.
4. **Nudge** the bot with one line ("New job in requests/to-<bot>/<file>"). If bot-to-bot messages don't work on this account, skip it: each bot reads its folder at its next run, and Tommy hears when that is.
5. **Follow up.** In each brief, a job not in that bot's `state/done-<bot>.md` by its BY time is listed as late, with the bot's last run-log line.
6. **Capacity full.** When Ops' board says the next free slot is past `capacity_full_after_days` in `context/config.json`, write a job to Lead Radar, Dream 500 and Trades Outreach to hold new outreach, and tell Tommy. Lift it the same way when Ops says there's room.

7. **Hand-off lines between bots.** At every brief, read each bot's daily notes since the last brief for lines that start `for <bot name>:` (for example `for Dream 100: <business>, <their words>, <link>`). Write each as a job in `requests/to-<that bot's slug>/`, and log the source file and line in `state/handled-lines.md` (yours) so no line becomes two jobs.
8. **Stop.** When Tommy or Justin's team says "stop everything", or another bot tells you it created the stop file: make sure `/workspace/tmec-team/state/EXTERNAL_WRITES_STOPPED` exists with the reason, write "pause all campaigns" jobs to `requests/to-dream-500/` and `requests/to-trades-outreach/` and nudge both, nudge CRM & Reactivation and Content Studio to unschedule any scheduled HubSpot email, and tell Tommy once what's paused and what isn't. Only you write those jobs. Remove the stop file only on Tommy's words.

## Done means
Every request from Tommy is a job with one owner, and every job ends in that bot's done file or in the brief as late.

## Never
- Do the job itself, or give one job to two bots.
- Write anything in another bot's files besides its `requests/to-<bot>/` folder.
