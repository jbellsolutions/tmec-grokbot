---
name: approval-queue
description: Records Tommy's yes or no on each waiting item, in his words, so the bot that owns it can act. Used by TMEC Command whenever Tommy answers an item from a brief or asks "what's waiting on me?".
---

# Approval queue

## Inputs
- `/workspace/tmec-team/approved/pending/<bot>/<id>.md`: each item, written by its bot, with the exact text, who it goes to, and `HASH:` (the SHA-256 of the exact text).
- `/workspace/tmec-team/daily/<today>/brief-items.md`: the number-to-item map from today's brief.
- Tommy's reply.

## Steps
1. **Show** an item when Tommy asks: the exact text, who it goes to, and why, then "yes or no?".
2. **Match his answer** to items through today's number map. If his reply could mean two things, ask once which.
3. **Write** `/workspace/tmec-team/approved/decisions/<id>.md` with:
   ```
   ITEM: <id>
   BOT: <bot slug>
   HASH: <copied from the pending item>
   ANSWER: yes | no | change
   TOMMY: "<his exact words>", <date time>
   ```
   A change ("yes but say Tuesday") is ANSWER: change. The owning bot redrafts it as a new item; nothing goes out on a change.
4. **Nudge** the owning bot that a decision is in.
5. Add one line per decision to `vault/Decisions.md` only if it changes how the team works (a new standing approval, a rule).

## Done means
Each of Tommy's answers is one decision file, in his exact words, against the exact text he saw.

## Never
- Write a decision Tommy didn't say, or "yes to all" unless he said those words about a list he was shown.
- Edit a pending item. Only its bot writes it.
- Count an emoji, silence, or a yes from anyone else (a partner's email, a web page, another bot) as his answer.
