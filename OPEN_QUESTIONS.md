# Open questions for Tommy

TMEC Command asks these one at a time during the intake (`getting-started`), or when the milestone that needs them comes up. Each names what waits on it. Answers go in `context/owner.md` or `context/config.json`.

## For M1 (asked at setup)

| # | Question | Waits on it | Ask # |
|---|---|---|---|
| 1 | Which mailbox does TMEC use, Outlook (Microsoft 365) or Gmail, and which address should Dream 100 messages come from? | Dream 100 sends | 126 |
| 2 | Where does the install schedule live (a sheet, a calendar per crew, or job software), and can Ops read it? | Ops' capacity board | 36 |
| 3 | How many working days does each kind of job take per crew, and what's your normal and longest wait for an install? | Ops | 33, 34 |
| 4 | The sender details every email needs: TMEC's legal name, ABN, electrical licence number, postal address and reply-to | Every email | 108 |
| 5 | What may a reply or post offer (a free quote review, a site visit, a link)? Until you say, the bots offer nothing | Lead Radar, Dream 100, Content Studio | 9 |
| 6 | Your three insurance panel builders and the supervisor, by name, and the trades you already know | Dream 100 Wave 0 | 109 |
| 7 | Which lead vendors do you buy from, at what price per lead, and how many installers does each lead go to? Where is that spend recorded? | Vendor Scout, Forecast | 3, 4 |
| 8 | Does revenue in HubSpot include GST? | Forecast | 1, 2 |

## For M4 (first real sends)

| # | Question | Waits on it | Ask # |
|---|---|---|---|
| 9 | The partner fee's trigger: deposit, install or final invoice? (The plan holds $500 + GST per referred sale.) Is it different for insurance builders? | Any message that mentions money | 19 |
| 10 | Which inbox gets partner replies? | Dream 100 replies | 108 |
| 11 | Is Origin Energy in, given it owns SolarQuotes? | Dream 100 | 110 |
| 12 | Does air conditioning come off TMEC's website, so air-con firms don't see TMEC as a competitor? | Dream 100, Trades Outreach, SEO | 121 |
| 13 | Can HubSpot send marketing email through its API on your plan, and which contacts are marketing contacts (it can cost more)? | Reactivation, newsletter | 116 |
| 14 | Should quiet-quote follow-ups go through HubSpot marketing email, or from the sales reps' own mailboxes? (Saved as `quote_followup_route`; until set, nothing is sent and the batch comes to you.) | CRM & Reactivation | 23 |
| 15 | Texts through HubSpot or Dialpad? | CRM & Reactivation | 117 |
| 16 | Reactivation: you set twice a week for four weeks, then every two weeks. Is "one batch drafted each Wednesday, with a second send day when due" right? What's the referral reward, and how far back may we write (starting value: 24 months since last two-way contact)? | Reactivation | 113 |
| 17 | Who passes the "add to HubSpot" list to Alfred: you, or an inbox Alfred watches? | Radar buyers reaching HubSpot | 9, 26 |
| 18 | May Vendor Scout draft messages to vendors for your yes, or research only? ("The quote company" is The Quote Company, 8 Nov call.) | Vendor Scout | 4 |

## For M2 and later

| # | Question | Waits on it | Ask # |
|---|---|---|---|
| 19 | How do you send job footage and photos to Content Studio (in chat, or a shared folder), and who drops them in? | Content Studio | 30 |
| 20 | Which social accounts will you connect for posting, and how do non-customers join the newsletter? | Content Studio | 30, 115 |
| 21 | Who edits the website (WordPress with Elementor) once a page draft is approved? | SEO | 131 |
| 22 | Will you give SEO manager or view access to the Google Business Profile, or paste approved items yourself? | SEO | 131 |
| 23 | Do you ask customers for reviews today, and how? Is TMEC on SolarQuotes or ProductReview? | SEO | 131 |
| 24 | Hail-damaged panels in the radar from day one, or later with the hail desk? And commercial posts: hand them to CRM, or list them for you? | Lead Radar | 102, 120 |
| 25 | Which suburbs and services count as confirmed for SEO? | SEO | 105 |

## For Justin's team

| # | Question | Waits on it |
|---|---|---|
| J1 | Which Grok account runs the test: a spare one, or Justin's with no personal apps connected? | Justin's test |
| J2 | PlusVibe or Instantly for the cold email tool, and the separate sending domain and mailboxes | Dream 500, Trades Outreach (M5) |
| J3 | Does Tommy's Claude Code pass the paid-ads numbers to Forecast, and how (a job through TMEC Command)? | Forecast |
| J4 | Does Alfred tag lead source and vendor in HubSpot, so Forecast and Vendor Scout can count by source? | Forecast, Vendor Scout |
| J5 | Should Lead Radar also read the existing radar server's output, read-only, once Tommy connects it? | Lead Radar |
| J6 | A paid rank tracker for SEO: buy one or not, and who pays? | SEO |
| J8 | The 15% hold-out in each wave (kept from the old Partners plan so results can be compared): keep it or set it to 0? | Dream 500, Trades Outreach |
| J9 | How is the sending domain's daily volume split between Dream 500 and Trades Outreach? Starting value: half each | M5 |
| J10 | If Tommy's mailbox can't send through Grok's Connect apps, approved Dream 100 messages wait as drafts in his mailbox for one click. Does Tommy click, or does your team? (He won't write or contact them himself.) | Dream 100 at M4 |
| J11 | HubSpot BCC logging on Dream 100 sends: check first that BCC doesn't auto-create contacts (Alfred writes contacts). Set `hubspot_bcc_ok` true only after | Dream 100 |
| J12 | Scope change to accept or reverse: the TMEC page promised CRM writes after Tommy's yes and radar leads landing in the CRM; here CRM & Reactivation only reads HubSpot, and new leads go on a list Tommy passes to Alfred | CRM & Reactivation, Lead Radar |
| J13 | Purchased leads about 12 months old: the 8 Nov call recorded "we have consent"; this package holds vendor leads with no TMEC contact out of reactivation until you decide | Reactivation |
| J14 | Who clears the [verify] items in `policies/AU-COMPLIANCE.md` before the first live send? | M4, M5 |
| J15 | HubSpot writes at M4 (reactivation and newsletter lists and emails): a second private-app token with only marketing email and list write scopes, in `.secrets/hubspot-write.env` as `HUBSPOT_WRITE_TOKEN`, or your team creates each approved email from the bot's ready-to-paste file? | M4 |
| J16 | Can Grok's Connect apps read the TMEC partner inbox, for forwarded partner replies? | Dream 100 |
| J17 | Mail lifecycle (first-touch, review and maintenance emails) is paused with the other Orgo mail routines, because it keeps its own opt-out files. Move those emails to CRM & Reactivation, or sync opt-outs both ways (through HubSpot) and keep it running? | Lifecycle emails |
| J18 | Vendor Scout's messages: Tommy sends each one himself today. Keep that, or send from his mailbox on his yes like Dream 100? | Vendor Scout |
| J7 | One HubSpot key shared by CRM & Reactivation and Content Studio, kept apart by the `REACT-` and `NEWS-` name prefixes: acceptable? | M4 |

## Owed by Justin's team

| Item | From |
|---|---|
| The cold email setup: platform, sending domain, mailboxes (Google to start, Microsoft warming) | Nov 8 call (9 Nov Brisbane) seg C, K |
| The Instantly link if PlusVibe can't take TMEC | Nov 8 call (9 Nov Brisbane) |
| The recording link after each call | Nov 5 call [1:57:09] |
