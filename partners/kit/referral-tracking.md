# Referral tracking: how every enquiry and sale is tied to its partner

One rule: every enquiry that comes from a partner's email carries the partner's id, so Tommy can see who sent what and who is owed. This page sets the id, the link, the phone code, the routes an enquiry can take, and the rules for deciding who gets credit. Rules marked "Tommy's call" are starting values he changes.

## The partner id

`p001`, `p002` and so on, given by TMEC Command (no partner bot owns this step yet) when a trade first shows interest, never reused. The id contains no personal data, so it is safe in a web address.

## The tagged link

```
<TMEC page address>?src=<partner-id>
```

Example shape: `https://<tmec-site>/<solar-enquiry-page>?src=p012`

- `<TMEC page address>` is the TMEC website page the partner's customers land on. Starting choice: the solar enquiry page. A page that says "You're here because <partner> recommended us" would be better and is a small website job for later (Tommy's call).
- A repeat send by the same partner adds a campaign number: `?src=p012&c=2`.
- Optional tracking tags a web analytics tool understands can ride along: `&utm_source=partner&utm_medium=email&utm_campaign=p012`. Use them only if TMEC's site analytics reads them.
- Never put a customer's name, email or phone in a link.
- TMEC Command checks the link opens before it is handed over.

## The phone code

For customers who ring instead of clicking. A short word and the partner number, easy to say and spell out: `<WORD><NN>`, for example `COOL12` (an example shape only, not a real partner). The word is agreed with the partner (their trade or the first word of their business, up to six letters) and checked against all other codes. The code is on the partner's card and in their email. The sales team asks, on every first call: "Did someone send you our way?" and records the answer.

## The four routes an enquiry can take

| Route | How it is captured | Who records it | Status today |
|---|---|---|---|
| **form** | The customer opens the tagged link and fills in TMEC's form. The `src` value should be saved on the HubSpot contact in a property (suggested name: `partner_src`) | Alfred creates the property and the form mapping, on Tommy's yes | UNKNOWN until proved at install |
| **phone** | The customer rings TMEC and quotes the code | The sales team, in a HubSpot note or the same property; Alfred makes sure it is recorded | Works with no website change |
| **forward** | The customer replies "yes" to the partner, who forwards it to the TMEC partner inbox | TMEC Command reads the inbox and hands it off | Works with no website change |
| **named** | The customer says a partner sent them, with no link or code | The sales team records the partner's name; TMEC Command matches it | Works, but Tommy decides each case until a rule is set |

Every captured enquiry becomes one "for CRM & Reactivation" line in the partner bot's daily note (TMEC Command passes it on), then a tagged record in HubSpot written by Alfred on Tommy's yes.

## Proving the form route (once, at install)

1. Open the tagged link with the id `ptest`: `<TMEC page address>?src=ptest`.
2. Submit a test enquiry with the name "TEST Partner" and a number or address that belongs to the team.
3. CRM & Reactivation reads HubSpot and confirms that contact shows `ptest` in the partner property.
4. Record the result on CRM & Reactivation's and TMEC Command's run logs: **works**, or **does not carry the tag** (then phone, forward and named routes are the only ones, and the website fix goes on Tommy's list).
5. The TEST contact is left marked TEST. Deleting it is Tommy's yes.

## What can and cannot be seen

- Clicks and visits are only visible where they land on TMEC's own site, through whatever analytics the site has. What analytics Tommy has is UNKNOWN until install.
- Opens, clicks and replies inside the partner's own email tool are the partner's. The partner bots cannot see them.
- A customer who replies to the partner's email reaches the partner, not TMEC. That is why the email asks the customer to use the link or the phone, or reply "yes" and have the partner forward it.

## Who gets credit: starting rules (Tommy's call)

| Case | Rule |
|---|---|
| First tagged enquiry | The partner whose link, code or name came first gets the credit |
| Two partners for one customer | The first recorded enquiry stands unless Tommy decides otherwise |
| Already a TMEC contact before the partner's send | Recorded as `pre-existing`. Tommy decides whether it counts, with the reason told to the partner |
| Window | An enquiry counts if it comes within [attribution window, starting value 90 days] of the partner's send |
| Customer says "the tradie sent me" with no tag | Recorded as `named`. Counts only on Tommy's yes |
| Sale cancelled or refunded before the fee is paid | No fee. `disputed`, then Tommy decides |
| A disagreement with a partner | Tommy decides, in his words, after talking to them |

## Privacy

- A customer's name and contact details move from a partner to TMEC only when that customer asks to be contacted (by form, phone or a reply to the partner).
- The partner never sees a customer's details beyond what that customer has agreed.
- The ledger holds a HubSpot record id, never a name.

## Where it is recorded

| What | Where | Writer |
|---|---|---|
| Partner id, phone code, link | Set by TMEC Command (no partner bot owns it yet) | TMEC Command |
| Tagged enquiries awaiting CRM & Reactivation | A "for CRM & Reactivation" line in the writing bot's `daily/<date>/<bot>.md` | The bot that took the enquiry; TMEC Command passes it on |
| The tag on the HubSpot contact and deal | HubSpot | Alfred |
| Sales and fees | Home and writer set by TMEC Command; every payout waits for Tommy's yes | TMEC Command |
