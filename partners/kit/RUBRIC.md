# Partner rubric: who is worth Tommy's time, and in what order

The partner bots (Dream 100, Dream 500 and Trades Outreach) score every prospect with this rubric before it goes on any list. The score decides the order, never the yes: Tommy approves every list and every first message.

The question behind it (Justin, 9 Nov call): **who deals with our same customer before, during, after, or alongside a solar, battery or EV charger job, and benefits when TMEC helps them?**

## 1. Hard gates: fail one and the prospect is out

| Gate | Out if | Why |
|---|---|---|
| Not a competitor | They install solar, batteries or EV chargers, or are an electrical contractor | Electrical is TMEC's own trade. They have nothing to recommend |
| Not a lead seller | They sell shared leads or quotes (SolarQuotes, Solar Choice, The Quote Company and the like) | They are vendors, not partners. The vendor scout handles them |
| Not new-construction builders | Volume home builders and developers | Tommy: "I'd prefer not to do builder work… all your eggs in their basket" (9 Nov). Renovators and insurance builders are fine |
| Owner can say yes | A franchise run from head office | The local owner usually can't send to the list |
| No opt-out on record | Their site says no unsolicited commercial email, or they are on the suppression list | Spam Act; record the reason |
| In the area, or area-free | Their customers are outside Gympie (plus 10 km) to the Brisbane River's north side, and they aren't a statewide or national program | TMEC can't serve them |

## 2. Score: 100 points

| # | Criterion | Points | 0 | Half | Full |
|---|---|---|---|---|---|
| 1 | **Same customer.** Homeowners aged about 35 to 60, or owners of businesses with big roofs | 15 | Renters, one-off walk-ins | Mixed | Homeowners or roof owners, almost all |
| 2 | **Where they sit in the job.** Before (they see the decision coming), during (on the same roof or job), after (they serve a solar owner), alongside (same bill, same worry) | 15 | No link to energy, the roof or the home | One link, weak | On the roof, in the switchboard or in the bill conversation (roofers, insurance builders, HVAC, pool, EV dealers) |
| 3 | **Volume they can send.** A repeat customer list, or a steady stream of jobs | 15 | No list, a handful of jobs | A few hundred, or a few jobs a month | 1,000+ on a list, or several jobs a month (one insurance builder can be "multiple jobs per month") |
| 4 | **Trust in the home.** Their customer lets them in and takes their advice | 10 | Arm's length | Some | In the home regularly, on a service plan |
| 5 | **Hail and insurance fit.** They can send report or rectification work | 10 | None | Sometimes see storm damage | Insurance builder, loss assessor or storm roofer on an insurer's panel |
| 6 | **Deal size.** One yes can bring more than one sale | 10 | One-off referral | A list email | Ongoing work orders, a program, or a whole customer base (Origin, a panel maker's installer program, a panel builder) |
| 7 | **Warm path.** Tommy or his team already know them, or share a supplier, a supervisor or a job | 10 | Cold | Shared contact or community | Tommy knows them by name (Wave 0) |
| 8 | **Easy yes.** Owner-run, small enough to decide on a call, no conflict | 5 | Committee, legal review | Manager decides | Owner decides on one call |
| 9 | **Gets something back.** TMEC can return value: a fee, reports, referrals the other way, a better bill for their customer | 5 | Nothing obvious | A fee only | Two-way: referrals back, or a better offer for their customer |
| 10 | **Proof we can show them.** A job, a review or a story they'd recognise | 5 | None yet | Generic | A job in their suburb, or for their kind of customer |

Unknown scores 0, never half. On criterion 5, the 8 Nov call recorded that insurers' panel lists are on their websites; the 11 Nov check of RACQ, Suncorp, AAMI, QBE, Allianz, Youi and NRMA found only motor repairer schemes published. Score a panel claim only from the business's own pages, with the link. A prospect with three or more unknowns goes to the research pile, not a list.

## 3. Tiers

| Score | Tier | What happens |
|---|---|---|
| 75 to 100 | **Dream 100** | One to one. The Dream 100 bot writes a custom message for each; Tommy approves each one; the bot sends it from his mailbox on his yes (Tommy doesn't write or send them himself) |
| 50 to 74 | **Dream 500** | Segment cold email through the separate TMEC sending domain (send path B), in waves of 25 to 50, with a written first line for each |
| 30 to 49 | **Nurture** | Newsletter-style updates only, after a yes, or a later wave |
| Under 30 | **Out** | Not contacted. The reason is recorded |

The trades list is the top ten of each ranked trade (`partner-types.md`): the ten best roofers, the ten best HVAC firms, and so on, scored here. A trade business that scores 75 or more is Dream 100's, not the trades list's.

## 4. How the score is kept

- One row per prospect on the owning bot's list file (Dream 100: `data/partners/dream100.csv`; Dream 500: `data/partners/dream500/<segment>.csv`; Trades Outreach: `data/partners/trades.csv`), with the score, each criterion's evidence and its source link. Not a HubSpot record.
- The bots score from public sources only (the business's site, its listing, its reviews). No paid enrichment.
- After each wave, the scoreboard shows replies, yeses, sends and signed sales per trade and per tier. When the measured numbers disagree with the weights, the bots propose new weights to Tommy through TMEC Command. Tommy decides.
- Nothing here promises a number of partners or sales.
