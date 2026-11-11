# Build record

This record keeps what's specified, what's built and what's actually running separate, and honest. Justin's team updates this file; the bots never do. The lead bot keeps the live list in `/workspace/tmec-team/context/team-registry.md`.

**Where it stands (2026-11-11): a specification package.** Everything below exists as files in this repo. Nothing is set up, connected or switched on anywhere until a bot follows `START-HERE.md` and reads back what it created. The first run is Justin's test, on a Justin's-team Grok account with no Tommy apps.

## Status by piece

- **Specified:** the job is written down.
- **Built in repo:** the file the bot uses exists here.
- **Active:** it's running on Tommy's account and has been read back.

| Piece | Specified | Built in repo | Active |
|---|---|---|---|
| Project charter, team design, approvals, data and AU rules | Yes | `PROJECT_CHARTER.md`, `docs/TEAM-DESIGN.md`, `policies/` | Not yet |
| The install | Yes | `START-HERE.md` (a test run and Tommy's run) | Not yet |
| TMEC Command | Yes | `agents/01-tmec-command.md`; briefs, dispatch, approval queue | Not yet |
| Lead Radar | Yes | `agents/02-lead-radar.md`; Radar sweep | Not yet |
| Dream 100 | Yes | `agents/03-dream-100.md`; drafts, send, replies | Not yet |
| Dream 500 | Yes | `agents/04-dream-500.md`; segment lists, cold email waves, replies | Not yet |
| Trades Outreach | Yes | `agents/05-trades-outreach.md`; trades list, waves, replies | Not yet |
| CRM & Reactivation | Yes | `agents/06-crm-reactivation.md`; sweep, quiet quotes, reactivation | Not yet |
| Content Studio | Yes | `agents/07-content-studio.md`; content week, newsletter | Not yet |
| SEO | Yes | `agents/08-seo.md`; audit, profile drafts, review replies | Not yet |
| Ops | Yes | `agents/09-ops.md`; capacity board | Not yet |
| Forecast | Yes | `agents/10-forecast.md`; scoreboard, rebate watch | Not yet |
| Vendor Scout | Yes | `agents/11-vendor-scout.md`; vendor review | Not yet |
| Reserved: Meta Ads, Google Ads, Commercial solar, Hail and insurance | Role only | `agents/90-93-*.md` | No |
| Partner kit and seed list | Yes | `partners/` (copied from `tmec-aios`, paths changed for this team) | n/a |

## Sources

- Calls with Tommy: 28 Oct (sales), 2 Nov (Session 1), 5 Nov (install and build, two parts), 8 Nov (9 Nov in Brisbane). Digests in the build folder, `source/digests/`.
- Justin's instructions: 28 Oct, 29 Oct, 2 Nov, 3 Nov, 5 Nov, and 11 Nov (two entries; the second is this package's brief), in `source/instructions/`.
- The TMEC AIOS page of 29 Oct (`deliver/artifact/tmec-aios.html`): every agent on it except paid ads is on this team.
- The `tmec-aios` package (branch `partners/dream-plan`), which these charters, skills and the partner kit are ported from.

## Platform facts this build relies on

| Fact | Status |
|---|---|
| Every bot on one account shares one computer, its files and its logins | Verified in docs (client-build Grok Bot reference) |
| Routines run in the cloud in the bot's time zone; Test does real work | Verified |
| 50 routines per bot; schedules at least 5 minutes apart | Verified |
| A bot unpacks a zip attached to its first message | Unverified: Step 1 has the fallback |
| A bot can create other bots and message them on the same account | Unverified: files are the main path; Owner-step fallback in Step 6 |
| Approval prompts from a routine expire (about 10 minutes seen) | Unverified: routines never wait; items go to the queue |
| A routine can read keys from `.secrets/` (HubSpot, treg) | Unverified |
| Connect apps can read TMEC's mailbox on a schedule, and can send from it | Unverified: Step 5 records which; Dream 100 falls back to drafts Tommy sends |
| Connect apps can read the install schedule and HubSpot unattended | Unverified: Ops and Forecast say UNKNOWN if not |
| Grok web and X search run in a routine, reach Reddit and some public Facebook posts with dates | Unverified: Lead Radar reports per source, UNKNOWN when unreached |
| Grok can read a Google Business Profile, reviews and the public website as a visitor | Unverified |
| No connection to Google Business Profile, WordPress or social accounts yet | Known: those bots hand Tommy the text |
| HubSpot's API on TMEC's plan can create lists and marketing emails | Unverified: drafts and "what to press" if not |
| One HubSpot key for two bots, kept apart by `REACT-` and `NEWS-` name prefixes | A design choice, not a security boundary |
| The cold email tool's API (PlusVibe or Instantly) creates paused campaigns and reads replies | Unverified until the tool is chosen (M5) |
| Grok does the scoreboard arithmetic in-run, writing the inputs beside each figure | Unverified: checked at the first Monday run |
| Standing approvals fire from routines without an Auto-review prompt | Unverified: watched at M6 |
| How Grok Bot usage is metered | Unknown: counted in runs per week until M3 |

## Review findings

| Finding | What was done |
|---|---|
| Pending: the independent review runs before the first commit | |

## Open items and who owns them

| Item | Owner | Next action |
|---|---|---|
| The test run (Steps 0 to 9) | Justin's team | Pick the Grok account (OPEN_QUESTIONS J1), attach the zip, follow START-HERE |
| Pause each Orgo twin before its Grok routine goes on | Justin (his yes each time) | START-HERE Step 7 |
| Cold email tool, sending domain and mailboxes | Justin's team | OPEN_QUESTIONS J2 |
| Tommy's answers for M1 and M4 | Tommy | OPEN_QUESTIONS 1 to 18 |

## Change log

| Date | Change | Asks |
|---|---|---|
| 2026-11-11 | First build: TMEC Command plus ten bots on one Grok account; ported from `tmec-aios`; paid ads left with Claude Code; SEO added | 125 to 131, and the rows each charter names |
