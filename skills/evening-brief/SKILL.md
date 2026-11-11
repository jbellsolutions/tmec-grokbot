---
name: evening-brief
description: Writes Tommy's short evening wrap: what got done, what he decided, what waits for tomorrow. Used by TMEC Command's Evening brief routine.
---

# Evening brief

## Inputs
- `/workspace/tmec-team/daily/<today>/<bot>.md` for every bot.
- `/workspace/tmec-team/approved/decisions/*/` written today.
- `/workspace/tmec-team/approved/pending/*/` still open.
- Today's lines in `/workspace/tmec-team/log/runs-<YYYY-MM>.md`.

## Steps
1. If no bot did anything today, nothing was decided and nothing is waiting: NO_CHANGE, stop.
2. Done today: one line per bot that did something, with its number and file.
3. Decided today: each of Tommy's decisions in a few words.
4. Waiting tomorrow: the open items (no decision file yet), numbered, oldest first, with the number map written to `daily/<today>/list-<HHMM>.md`.
5. Save to `daily/<today>/evening.md`, add it to `vault/Daily/<today>.md`, send it to Tommy.

## Output
Under 120 words.

## Done means
Every line traces to a note, a decision file or a run-log line.

## Never
- Report work a bot didn't log.
- Send it when there's nothing to say.
