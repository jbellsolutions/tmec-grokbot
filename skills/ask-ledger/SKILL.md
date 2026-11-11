---
name: ask-ledger
description: Keep the list of everything Tommy has asked for. Use whenever Tommy sends a new idea, request or "it would be cool if", and in the weekly wrap. Every ask becomes a numbered row, with where it's solved, so nothing gets lost.
---

# Ask ledger

## Inputs
- `/workspace/tmec-team/context/asks.md`: the ledger. At setup, copy it from the build's `ASKS.md` if Justin's team attached one, and keep its numbering: the next number is the one its header names, or the last row + 1. The copy may hold only this account's rows, so numbers can skip.
- If there's no copy yet, start the file with the heading `# New asks (numbered N-1, N-2, ...)` and number new rows `N-1`, `N-2`. Never start at 1: the master ledger already uses those numbers. Justin's team gives them master numbers when they merge.

## When Tommy asks for something new
1. Check whether it's already a row. If it is, add today's date to that row's **When** and tell Tommy where it stands.
2. If it's new, append a row:
   - number: the last number + 1;
   - their words, quoted;
   - today's date and where it came from;
   - a status from the key at the top of the file;
   - where it's solved: a bot, routine or skill that already does it, or "new: needs Justin's team".
3. Reply in one line, for example: "Added as #43. The Sales Manager can do it with a new routine. Want me to draft it for Justin's team?"
4. New builds are tier 3. Write a request in `/workspace/tmec-team/requests/`. Never build or turn on something new without Tommy's yes.

## Weekly
Report in the weekly wrap:
- how many asks are open;
- the three oldest that wait on Tommy;
- anything that moved this week.

## Never
- Renumber rows.
- Drop an ask.
- Mark something done without evidence that it ran.
