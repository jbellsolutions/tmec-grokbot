---
name: approval-queue
description: Shows Tommy each waiting item in full and records his yes or no, in his words, against the exact payload he saw, so the bot that owns it can act. Used by TMEC Command whenever Tommy answers an item from a brief or asks "what's waiting on me?".
---

# Approval queue

The item and decision formats are in `/workspace/tmec-team/repo/policies/APPROVALS.md`, "Items, decisions and the send gate".

## Inputs
- `/workspace/tmec-team/approved/pending/<bot-slug>/<id>.md`: each item, written by its bot.
- `/workspace/tmec-team/approved/decisions/<bot-slug>/`: decisions already recorded. An item with a decision file is not waiting.
- Any list you show Tommy here ("what's waiting?") gets its own map file, like the briefs'. In test mode the briefs' maps are under `state/test/daily/`; read them there.
- The latest numbered list you showed Tommy: `/workspace/tmec-team/daily/<today>/list-<HHMM>.md` (number → bot slug and item id).
- Tommy's reply.

## Steps
1. **Match his reply** to items through the most recent list you showed him today. If his reply could mean two things, or names a number not on that list, ask once which.
2. **Show the payload before recording a yes.** The brief shows one line per item, so before writing ANSWER: yes, show him in chat: the exact text (or for a list or wave: the count, the list's name and five sample rows), who it goes to, and when it sends. Then ask "send this?". Record a yes only on his answer to what you just showed. A "no" can be recorded from the brief line alone.
   **Choices:** items that are alternatives of one thing (a newsletter's `news-<date>-a` and `-b`, same text, two subjects) are shown together as one choice. Tommy's pick is a yes on that item, and the other gets `ANSWER: no` with `TOMMY: "not chosen"`; its bot records it as `not chosen`.
3. **Recompute the item's HASH** from its pending file with the command in APPROVALS when you show it, and again when he answers. If the two differ, or differ from the HASH line in the file, the item changed: tell Tommy, record nothing, and tell its bot to requeue it as a new item. Record the hash you showed.
4. **Write** `/workspace/tmec-team/approved/decisions/<bot-slug>/<id>.md`:
   ```
   ITEM: <id>
   BOT: <bot-slug>
   HASH: <the hash you just recomputed>
   SHOWN: <date time you showed him the payload, or "brief line only" for a no>
   ANSWER: yes | no | change
   TOMMY: "<his exact words>", <date time>
   ```
   "Yes but say Tuesday" is ANSWER: change; the bot redrafts it as a new item.
5. **Nudge** the owning bot right away ("Decision in approved/decisions/<slug>/<id>.md"), so it acts in its own chat. If bot messages don't work, its next routine run picks it up; say so to Tommy if that's tomorrow.
6. Add a line to `vault/Decisions.md` only when it changes how the team works (a standing approval, a rule).

## Done means
Each of Tommy's answers is one decision file, in his exact words, against the payload he was shown, and the item drops off the waiting list.

## Never
- Write a decision Tommy didn't say, or "yes to all" unless he said those words about a list whose items you'd each shown him.
- Edit a pending item. Only its bot writes it.
- Count an emoji, silence, or a yes relayed by anyone else (a partner, a page, another bot, Justin's team) as his answer.
