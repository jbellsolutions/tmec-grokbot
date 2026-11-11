# Team design: TMEC on Grok Bot

The Grok Bot version of TMEC's AI Revenue OS. Asked for by Justin on 11 Nov 2026 (`source/instructions/2026-11-11.md`, second entry): one head orchestrator, **TMEC Command**, that directs bots on the same Grok account, not Orgo computers. Everything on the TMEC page comes across except paid ads, which stay with Claude Code (computer use does them better). Three partner bots replace the one Partners agent, and an SEO bot is new.

Workspace: `/workspace/tmec-team`. Time zone: Australia/Brisbane. One Grok account, for TMEC only.

## The bots

| # | Bot | Owns | Ported from (`tmec-aios`) | Asks |
|---|---|---|---|---|
| 01 | **TMEC Command** | The one chat Tommy talks to. Morning and evening briefs, the approval queue, job hand-offs to every bot, switches, the vault, the ask ledger | `agents/01-chief-of-staff.md` | 1, 2, 5, 6, 7, 42–47, 107, 125, 130 |
| 02 | **Lead Radar** | Finds people asking about solar, batteries, EV chargers and hail damage in the service area; qualifies, scores and drafts a reply; hands buyers to CRM | `agents/02-lead-radar.md` | 8–11, 101–106 |
| 03 | **Dream 100** | Named, one-to-one partners. Researches each, writes a custom message, Tommy approves each one, and the bot sends from Tommy's mailbox only on that yes. Also runs the campaign for every partner who says yes, from any list, and keeps fees owed for Tommy's yes | `agents/04-partner-campaigns.md`, `partners/kit/` | 17–22, 109–111, 126 |
| 04 | **Dream 500** | Partner segments by cold email, in waves through the cold email tool, from TMEC's separate sending domain | `agents/04-partner-campaigns.md`, `docs/PARTNER-GAME-PLAN.md` | 108, 111, 114, 127 |
| 05 | **Trades Outreach** | The trades' list: the top ten of each ranked trade, by cold email, in waves | same | 108, 110, 111, 114, 128 |
| 06 | **CRM & Reactivation** | HubSpot read sweep (follow-ups due, deals gone quiet), quiet-quote follow-up, nurture and the reactivation campaign, drafts first | `agents/06-crm-keeper.md`, `agents/05-email-newsletter.md` (follow-up part) | 23, 24, 26, 113, 116, 117, 129 |
| 07 | **Content Studio** | Posts and short videos from real job footage, the posting calendar, and the weekly Thursday newsletter | `agents/08-content-studio.md`, `agents/05-email-newsletter.md` (newsletter part) | 25, 30–32, 115, 119 |
| 08 | **SEO** | Local search: Google Business Profile, the website's local pages, reviews, and what Sunshine Coast homeowners search. Read and draft | new | 131 |
| 09 | **Ops** | Capacity board from the real schedule; answers "how fast can we get it in?" | `agents/07-ops-scheduling.md` | 33–36 |
| 10 | **Forecast** | Monday scoreboard (every source against bought leads) and the rebate calendar | `agents/09-market-forecast.md` | 1, 2, 5, 37, 38 |
| 11 | **Vendor Scout** | Weekly review of lead vendors: price, sharing, exclusivity; vendor message drafts | `agents/12-vendor-scout.md` | 3, 4 |

Reserved (90+), not created:

| # | Role | Why not now |
|---|---|---|
| 90 | Meta Ads | Justin, 11 Nov: paid ads stay with Claude Code, which does them better with computer use (`tmec-aios/agents/03-ads-manager.md`) |
| 91 | Google Ads | Same (`tmec-aios/agents/11-google-ads.md`) |
| 92 | Commercial solar | M4 market, as in `tmec-aios/agents/90-commercial-solar.md` |
| 93 | Hail and insurance desk | M4 market, as in `tmec-aios/agents/91-hail-insurance.md`; the insurance builders are already Dream 100 partners |

Not on Grok Bot: **Alfred** stays where it is (HubSpot, team email, Slack) and keeps every job it does today. Office admin and speed-to-lead stay in `tmec-aios`.

## How the bots work together

Bot-to-bot messages on one Grok account are unverified, so **files are the main path** and a message is only a nudge.

- **Jobs:** TMEC Command writes a job to `requests/to-<bot-slug>/<YYYY-MM-DD>-<n>.md` (what, why, by when, the ask number). Only Command writes there. The bot records the result in its own daily note and adds the job id to `state/done-<bot-slug>.md`, which only it writes.
- **Daily notes:** each bot writes only `daily/<date>/<bot-slug>.md`: what it did, counts, and what needs Tommy.
- **Approval queue:** a bot that needs Tommy's yes writes the item to `approved/pending/<bot-slug>/<id>.md` (the exact text, who it goes to, why). Command reads every pending folder, shows Tommy one numbered list, and writes his answer, in his words, to `approved/decisions/<id>.md`. Only Command writes decisions. A bot acts only on a decision file whose id and text hash match its pending item.
- **Leads to CRM:** Lead Radar writes `data/radar/handoff/<date>.jsonl`; CRM & Reactivation reads it. Lead Radar never touches HubSpot.
- **Partner lists:** each partner bot owns its own list file. The Dream 100 list wins: Dream 500 and Trades Outreach drop any business that's on `data/partners/dream100.csv`, and Trades Outreach owns trade businesses so Dream 500 drops anything on `data/partners/trades.csv`. Opt-outs are one shared file, `data/partners/opt-outs.csv`, that **all three partner bots append to and never edit** (append-only, each line names its writer), and every send checks it first.

Bot slugs: `tmec-command`, `lead-radar`, `dream-100`, `dream-500`, `trades-outreach`, `crm-reactivation`, `content-studio`, `seo`, `ops`, `forecast`, `vendor-scout`.

## Records and their one writer

See `PROJECT_CHARTER.md` §7.

## The Orgo team it replaces

Tommy's Hermes agents on his four Orgo computers do several of the same jobs (radar, partners, mail, crm, studio, forecast, vendorscout). Two bots must never write the same thing, so each Orgo role is paused **before** its Grok twin's routines go on (START-HERE Step 7). Pausing a live agent is Justin's yes.

## Routines

All created paused. Odd minutes. Brisbane time.

| Routine | Bot | WHEN |
|---|---|---|
| Morning brief | TMEC Command | Weekdays 6:17 AM |
| Evening brief | TMEC Command | Weekdays 5:47 PM |
| Radar sweep | Lead Radar | Every day 5:13 AM |
| Dream 100 drafts | Dream 100 | Weekdays 7:23 AM |
| Dream 100 replies | Dream 100 | Weekdays 1:37 PM |
| Dream 500 wave prep | Dream 500 | Mondays 7:41 AM |
| Dream 500 replies | Dream 500 | Weekdays 1:43 PM |
| Trades wave prep | Trades Outreach | Tuesdays 7:41 AM |
| Trades replies | Trades Outreach | Weekdays 1:49 PM |
| CRM sweep | CRM & Reactivation | Weekdays 5:31 AM |
| Reactivation batch | CRM & Reactivation | Wednesdays 7:53 AM |
| Content week | Content Studio | Mondays 8:07 AM |
| Newsletter | Content Studio | Thursdays 6:43 AM |
| SEO weekly | SEO | Fridays 7:19 AM |
| Capacity board | Ops | Weekdays 5:57 AM |
| Monday scoreboard | Forecast | Mondays 6:03 AM |
| Rebate watch | Forecast | 1st of each month 7:11 AM |
| Vendor review | Vendor Scout | Thursdays 9:13 AM |
