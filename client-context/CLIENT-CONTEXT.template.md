# Client context (template)

The real file (`CLIENT-CONTEXT.md`) is private: Justin's team attaches it at install, and it is never committed. These are the headings the install expects. The lead bot copies the filled-in file to `/workspace/tmec-team/context/owner.md` and asks Tommy for anything still marked ASK.

## Who

- Name: ASK
- Time zone: Australia/Brisbane
- How Tommy likes messages: ASK

## The business

- Legal name and ABN: ASK
- Electrical contractor licence number: ASK
- Published business (postal) address for email footers: ASK
- Reply-to address: ASK
- TMEC contact block (phone, website) for emails: ASK
- What a reply or post may offer (free quote review, site visit, a link): ASK
- Referral reward for past customers, if any: ASK

- What it sells, and to whom: ASK
- Team (name, role; IDs are filled in after the apps connect): ASK

## Accounts

| System | Account / ID | Access |
|---|---|---|
| Mailbox (Outlook or Gmail) and Tommy's sending address | ASK | read; send only per approved Dream 100 message (M4) |
| HubSpot portal ID and BCC logging address | ASK | read-only (M1); marketing email for reactivation batches (M4) |
| Install schedule (calendar or sheet) | ASK | read-only |
| Website and who edits it | ASK | none |
| Google Business Profile | ASK | none until Tommy grants it |
| Social accounts (Facebook, Instagram, others) | ASK | none until Tommy grants it |
| Cold email tool (PlusVibe or Instantly) and the separate sending domain | ASK | none until M5 |
| treg (email verification) | ASK | key in `.secrets/treg.env` |

## Partners

- Service area: Gympie plus 10 km, south to the north side of the Brisbane River
- Partner fee and its trigger (deposit, install or final invoice): ASK (proposed $500 + GST per referred sale, unconfirmed; never quoted until Tommy sets both)
- Attribution window for a partner referral (starting value 90 days): ASK
- The three insurance panel builders and the supervisor: ASK
- Trades and businesses Tommy already knows: ASK
- Reply inbox for partner replies: ASK

## Lead vendors

- Current vendors, price per lead, how many installers each lead goes to (`lead_vendors`): ASK
- Bought-lead baseline: cost per lead (`baseline_cost_per_lead_aud`, about 60 on the 28 Oct call) and close rate (`baseline_close_rate_pct`, mid-20s): confirm
- Vendor Scout on or off (`vendor_scout`): ASK
- Vendor Scout drafts messages to vendors for Tommy's yes, or research only (`vendor_messages`, saved in config.json): ASK

## Schedule

- Where the install schedule lives and how Ops reads it (`schedule`): ASK

## Limits

- Never: ASK
- Away dates and quiet hours: ASK
