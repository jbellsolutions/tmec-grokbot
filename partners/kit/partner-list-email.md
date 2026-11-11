# The email the partner sends to their own customers

Two versions, in the partner's voice. The partner sends it from their own account to their own customers. Dream 100 owns this step (skill `partner-campaign-run`). Tommy approves the protected lines, as an item for his yes, before the pack goes to the partner.

## How to use it

- Fill the `{fields}` from the partner's card. The partner chooses the "why I trust them" line from the options below. They keep only a line that is true for them.
- **Protected lines** (anything about TMEC, the link, the phone code, the reply route, any claim): the partner does not change these. A change needs a new yes from Tommy.
- **The partner's own words** (the greeting, the sign-off, one sentence about themselves, the P.S. choice): theirs to change.
- The partner's email tool adds their business name, contact details and a working unsubscribe. The TMEC contact block goes in too.
- No prices, savings, rebate amounts or install times in the email. The only rebate line allowed is the optional timing line below, and only with the source and date checked.
- Australian English, plain, no hype, no exclamation marks.

## Fields

| Field | Filled from |
|---|---|
| `{customer_first_name}` | The partner's own mail-merge field. The partner's tool fills it, not TMEC |
| `{partner_business}`, `{partner_signoff}` | The partner |
| `{why_i_trust_line}` | One of the options below |
| `{tagged_link}` | `referral-tracking.md`: the page address with `?src=<partner-id>` |
| `{tmec_phone}`, `{phone_code}` | `context/owner.md` and the partner's card |
| `{tmec_contact_block}` | The same definition as in `outreach-sequence.md`: `policies/AU-COMPLIANCE.md` sender identification from `context/owner.md` (legal or trading name, ABN, phone, reply-to, postal address line) plus the line `Licensed electrical contractor <licence number>`. This email promotes TMEC to the public, so it carries all of it. If any part is missing, the email is not drafted |

## "Why I trust them": options (keep only a line that is true)

1. "I've met the TMEC team and seen how they work."
2. "I've worked alongside them on the same jobs."
3. "I've spoken with the owner and his team, and I like that they do the installs themselves."
4. "I asked around before putting my name to this, and I'm comfortable with what I heard." (Only if the partner did.)
5. Honest fallback, if none of the above is true yet: "I haven't worked with them myself yet, so I'm not vouching for their work. What I can tell you is how they say they operate: their own installers, no subcontractors. Have a chat with them and judge for yourself."

If the partner would rather have a true reason, Tommy can arrange for them to meet the team first.

## Subject lines (the partner picks one)

- `Thinking about solar or a battery?`
- `Who I'd call about solar`
- `A recommendation from us`
- `Solar and batteries: who I'd send you to`
- `A tip on your power bill`
- `Something I've been asked about`

## Version A: the short recommendation

```
Hi {customer_first_name},

A few of you have asked me about solar and batteries over the years. We don't do it, so I went looking for someone I'd be comfortable sending you to.

{why_i_trust_line}

That someone is TMEC Services, a Sunshine Coast business. They install solar, batteries and EV chargers with their own installation team, so the people who install it are TMEC's own, not a subcontractor you've never met.

If you'd like to see what it could look like for your home:
- fill in the form here: {tagged_link}
- or ring TMEC on {tmec_phone} and say code {phone_code}, so they know I sent you
- or reply "yes" and I'll pass your contact details on to them.

No pressure from me. I just didn't want you to have to start from scratch.

{partner_signoff}
{partner_business}

P.S. {ps_line}

TMEC Services: {tmec_contact_block}
{partner_footer_and_unsubscribe}
```

## Version B: the fuller one

```
Hi {customer_first_name},

I get asked about solar and batteries a fair bit, and it's not something we do. So rather than leave you to search on your own, here's who I'd point you to.

{why_i_trust_line}

TMEC Services is a Sunshine Coast business that installs solar, batteries and EV chargers. What matters to me is that they use their own installation team, not subcontractors. The people who install it are TMEC's, from start to finish.

What happens if you get in touch:
- someone from TMEC contacts you to talk through your home and what might suit it
- they quote you directly. I'm not part of the quote or the contract, so ask them anything you like
- what's available to you changes over time, so ask them what applies to your home today

If you already have solar, it's worth asking whether a battery would suit your system.

To get in touch, any of these works:
- the form here: {tagged_link}
- ring TMEC on {tmec_phone} and say code {phone_code}
- reply "yes" and I'll pass your contact details on.

If it's not for you, no worries at all.

{partner_signoff}
{partner_business}

P.S. {ps_line}

TMEC Services: {tmec_contact_block}
{partner_footer_and_unsubscribe}
```

## P.S. options (the partner picks one)

1. "If you already have solar, a battery is worth asking about. They can tell you if it suits your system."
2. "Being upfront: TMEC pays me a thank-you if someone I send goes ahead with them. It doesn't change what you pay." **[Tommy to confirm the last sentence is true before this line is used.]** Recommended: it is honest, and `partner-terms.md` asks the partner to disclose. Whether disclosure is required is for the legal check.
3. "Not for you? No problem, and thanks for reading."
4. Optional timing line, only with a current government source and the date checked, written by TMEC Command, never by a partner bot from memory: "Government rebates step down on set dates, so timing can matter. TMEC can tell you where things stand." **[CHECK: source and date before use.]**

## Sending checklist for the partner

- Send from your own account or email tool, with your own business name, contact details and unsubscribe.
- Leave out anyone who has opted out. Do not add anyone you bought or collected another way.
- Send a test to yourself and to the TMEC partner inbox first. Check the link opens and the code reads right.
- Do not add prices, savings, rebate amounts or times.
- If someone replies "yes", forward that reply to the TMEC partner inbox ({tmec_partner_inbox}).
- Draft: have the email and the terms checked before the first send.
