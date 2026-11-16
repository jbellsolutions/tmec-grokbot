# Engines: which bot thinks with what

**Status: in the pack, switched off.** No routine or skill calls `engines/route.py` yet. Every bot thinks in its own Grok run, as before. This page says what turning it on takes.

## Why

A bot's own run spends the Grok plan's weekly usage. Sorting, scoring and long drafting can run on a subscription Tommy already pays for instead: Claude Code on his Claude plan, and Codex on a ChatGPT plan if he has one.

## The map

`engines/agents.json`, one entry per bot:

| Bot | Engine | Falls back to |
|---|---|---|
| TMEC Command, Dream 100, Dream 500, Trades Outreach, Ops, Forecast, Vendor Scout | The bot's own run | - |
| Lead Radar, CRM & Reactivation, SEO | Codex | Claude Code |
| Content Studio | Claude Code | Codex |
| Reply sorting (the three reply routines) | Codex sorts, Claude Code drafts | Claude Code |

Whether Tommy has a ChatGPT plan isn't known (`OPEN_QUESTIONS.md` 26). Until it is, every Codex bot runs on Claude Code: `route.py` moves to the fallback by itself when the Codex CLI isn't installed. If neither CLI answers, it exits 3 and the bot does the work in its own run, so nothing is lost.

## What the router does and doesn't do

- `python3 /workspace/tmec-team/repo/engines/route.py --list` shows the map and which CLIs are installed. `--check` exits 0 only if they all are.
- It runs each CLI headless with no tools, in an empty folder, with the items passed as data. It reads and answers; it can't send, post or write anywhere.
- It never calls a metered API. Each call is one line in `log/engine-<YYYY-MM>.jsonl` (set `BOT_HOME=/workspace/tmec-team`), which the weekly usage audit can read.
- It doesn't change the send gate. Anything an engine drafts is still an item waiting on Tommy.

## Turning it on (not done)

1. Tommy's yes, and his answer on ChatGPT (`OPEN_QUESTIONS.md` 26, J20).
2. The Claude Code CLI installed on the bot's computer and signed in with Tommy's own plan, by hidden prompt. The same for Codex if he has a plan. Never Justin's team's subscriptions.
3. `route.py --check` passes on that computer.
4. One routine at a time gets a line that sends its sorting through `route.py`, on `test` first. Lead Radar's scoring is the first candidate.
