---
name: getting-started
description: The intake interview. Use once at setup (the intake step in START-HERE), or whenever Tommy says their basic facts changed. It confirms what the build already knows, asks only what's missing, one question at a time, and writes Tommy's facts and the team config.
---

# Getting started: the intake

## Inputs
- `/workspace/tmec-team/repo/client-context/CLIENT-CONTEXT.template.md`: the headings.
- The private client context, if Justin's team attached it. Save it to `/workspace/tmec-team/context/owner.md` before you ask anything.
- `/workspace/tmec-team/repo/OPEN_QUESTIONS.md`: the questions that are waiting.

## Steps
1. If `context/owner.md` exists, read it back in one message: "Here's what I know. Is anything wrong?" Fix only what Tommy corrects.
2. Ask each line still marked `ASK`, then the OPEN_QUESTIONS rows that this milestone needs:
   - one question per message;
   - short enough to answer on a phone;
   - offer choices when there are only a few.
3. Write each answer in place of its `ASK`, with today's date. Write the team's settings to `context/config.json`. A required field nobody knows yet stays `REQUIRED`; never guess it.
4. When the apps are connected later, fill in any IDs you can now look up yourself (Slack member IDs, sheet column names), then confirm them with Tommy.
5. Done: no `ASK` is left that the current milestone needs. Tommy has said "right" to the readback.

## Never
- Ask for a password, key or token in chat.
- Invent a fact to fill a gap.
- Ask two questions in one message.
