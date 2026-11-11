# TMEC's AI team on Grok Bot

One bot to talk to, ten bots doing the work. Built for Tommy at TMEC Services (solar, batteries, EV chargers and electrical, Sunshine Coast) by Justin's team.

Tommy talks to **TMEC Command**. It hands each job to the bot that owns it and brings back one short, numbered list of yes or no, morning and evening. Nothing goes out without Tommy's yes on the exact message.

| Bot | What it does |
|---|---|
| **TMEC Command** | The one chat. Morning and evening briefs, the approval list, hands out every job |
| **Lead Radar** | Finds people on the Coast asking about solar, batteries, EV chargers and storm damage; drafts a helpful reply |
| **Dream 100** | Writes one custom message to each of TMEC's best-fit partners; sends it only on Tommy's yes |
| **Dream 500** | Partner segments (pool, pest, roofing, gas and the rest) by cold email, in waves |
| **Trades Outreach** | The top ten of each trade by cold email, in waves |
| **CRM & Reactivation** | Follows up every quote that went quiet; drafts the reactivation batches |
| **Content Studio** | Posts and short videos from real job footage; the Thursday newsletter |
| **SEO** | Google Business Profile, local pages, reviews |
| **Ops** | The capacity board: how fast can we get a job in? |
| **Forecast** | Monday scoreboard against bought leads; the rebate calendar |
| **Vendor Scout** | Keeps the lead vendors honest |

Paid ads (Meta, Google) stay with Claude Code on Tommy's Mac. Alfred keeps its jobs in HubSpot, email and Slack.

## Install

1. Open the **Grok** desktop app → **New chat (+)** → **Create new Bot**.
2. Attach `tmec-grokbot.zip` (from Justin's team, or **Code → Download ZIP** on this repo).
3. Send:

   ```
   Build my team from the attached zip. Follow START-HERE.md. This is Tommy's install for TMEC Services, my business account.
   ```

4. Answer its questions. It walks you through every click, one at a time. For Justin's team's test run, send `This is Justin's test run. Follow START-HERE.md.` instead.

Everything is created **paused**. Routines switch on only when Tommy says yes, one at a time.

## How it stays safe

- **One send gate.** Before anything goes out, a bot checks: the stop switch is off, this isn't a test, live sends are on, Tommy said yes to the exact text and recipients (hash-checked), and it hasn't already been sent. See [`policies/APPROVALS.md`](policies/APPROVALS.md).
- **Stop everything.** Say "stop everything" to any bot. Every bot stops sending; live cold email campaigns are paused.
- **Australian rules.** Spam Act 2003 and the Privacy Principles: [`policies/AU-COMPLIANCE.md`](policies/AU-COMPLIANCE.md).
- **No paid data.** Bots research from public sources only.

## What's inside

| Path | What |
|---|---|
| [`START-HERE.md`](START-HERE.md) | The install the bot follows, step by step |
| [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) | Why, objectives, the team, rules, who writes what, milestones |
| [`docs/TEAM-DESIGN.md`](docs/TEAM-DESIGN.md) | The eleven bots, how they hand off, and the routines |
| `agents/` | One charter per bot (90–93 are reserved for later) |
| `routines/` | 18 scheduled jobs, all created paused |
| `skills/` | 28 skills: how each job is done |
| `partners/` | The partner rubric, kit and a 219-business seed list |
| [`policies/`](policies/) | Approvals, data rules, Australian compliance |
| [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) | What only Tommy or Justin can answer |
| [`docs/BUILD-RECORD.md`](docs/BUILD-RECORD.md) | What's specified, built and actually running, and the review findings |

## Status

Built and reviewed twice; not yet installed on a Grok account. Live milestones: M0 setup → M1 apps read-only → M2 every bot and routine created, paused → M3 preview (messages to Tommy only) → M4 first real sends → M5 cold email waves → M6 standing approvals.

Built by Justin's team (Everyone Needs an AI Guy) with the client-build system, November 2026. Private.
