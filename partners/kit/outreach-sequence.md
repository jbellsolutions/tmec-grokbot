# Outreach sequence: opener and three follow-ups

The first email Dream 500 or Trades Outreach sends to a business, and the three follow-ups. Every send needs Tommy's yes on the exact draft (`policies/APPROVALS.md`). Signed as Tommy only on drafts he has approved.

## Rules

- Australian English. Plain words. Short sentences. Reads like a tradie who knows his stuff, not a call centre.
- Opener up to 110 words. Follow-ups up to 70. Subject up to 4 words, lower case, does not sell.
- No dashes used as punctuation, no exclamation marks, no emoji, no links except the unsubscribe link.
- No fee figure, no rebate figure, no results, no testimonials, no promised times.
- One true hook from a public page, with its source on the draft. If there is no true hook, use the fallback line.
- Every email carries the TMEC contact block and the unsubscribe line. Sent from the separate sending domain, but it says TMEC Services and gives TMEC's real details.
- Gaps between touches are in business days and are starting values: follow-up 1 after 3, follow-up 2 after 5 more, follow-up 3 after 7 more. Stop at four touches in total, or the moment they reply or unsubscribe.
- Follow-ups go in the same thread.

## Fields

| Field | Filled from |
|---|---|
| `{greeting}` | "Hi <first name>," if `owner_first_name` is recorded. Otherwise "Hi there," |
| `{hook_sentence}` | The row's `hook`, only if it has a source URL. Else the fallback below |
| `{trade_plural}` | The trade in the plural (air-con installers, roofers, pest controllers) |
| `{suburb}` | The row's suburb as published |
| `{tmec_contact_block}` | `policies/AU-COMPLIANCE.md` sender identification, from `context/owner.md`: legal or trading name, ABN, phone, reply-to, postal address line, and the line `Licensed electrical contractor <licence number>`. If any part is missing, the email is not drafted |
| `{unsubscribe_line}` | "If you'd rather not hear from me, reply UNSUBSCRIBE and I will take you off straight away." |

Fallback hook: "I came across {business} while looking at {trade_plural} around {suburb}."

Hook examples (use only if the page says it): "I saw {business} offers annual service plans for homes around {suburb}." / "I saw {business} has been looking after pools around {suburb}."

## Opener A: the partnership

Subject: `solar for your customers`

```
{greeting}

{hook_sentence}

I'm Tommy from TMEC Services on the Sunshine Coast. We install solar, batteries and EV chargers with our own installers, not subcontractors.

If your customers ever ask you about solar or batteries, they end up going elsewhere, because you don't do it. We'd like to be where you send them. You send one email to your customers recommending us. We write it for you. We pay you a fee for every sale that comes from it. Your customer list stays with you.

Open to a quick call to see if it suits you?

Tommy
{tmec_contact_block}

{unsubscribe_line}
```

## Opener B: the question (second angle, for the split)

Subject: `a partner idea`

```
{greeting}

{hook_sentence}

Quick question. Would you send one email to your customers if it paid you for every sale it led to? It would recommend TMEC Services for solar and batteries. We write it, you send it from your own account, and your list never leaves you.

Our installers are our own team, not subcontractors, so you wouldn't be putting your name next to a stranger. If it's not for you, just say so and I won't chase.

Tommy
{tmec_contact_block}

{unsubscribe_line}
```

## Follow-up 1 (3 business days after the opener)

Subject: same thread

```
{greeting}

Just checking my note reached you. The short version: you send one email to your customers recommending TMEC for solar and batteries, we write it, and we pay you a fee on each sale. Your list stays yours.

Worth a ten minute call?

Tommy
{tmec_contact_block}

{unsubscribe_line}
```

## Follow-up 2 (5 business days after follow-up 1)

Subject: same thread

```
{greeting}

In case it helps, here's what it asks of you. You read an email we've written, change it so it sounds like you, and send it once. We handle every enquiry that comes back, and we keep a record so every sale is tied to you.

Want me to send the draft email so you can see it? No commitment.

Tommy
{tmec_contact_block}

{unsubscribe_line}
```

## Follow-up 3: the last note (7 business days after follow-up 2)

Subject: same thread

```
{greeting}

Last note from me. If the timing's wrong or it's not for you, no problem, I'll leave it there. If you'd like a look at the idea later, just reply.

Tommy
{tmec_contact_block}

{unsubscribe_line}
```

After this, the business is set to `declined` (reason: no reply) and is not contacted again unless Tommy says so.

## QC before anything goes in a wave file

1. Word counts within the limits above.
2. No dashes as punctuation, no exclamation marks, no emoji, no link but the unsubscribe link.
3. None of: guaranteed, free solar, unlock, game-changer, passive income, easy money, synergy, leverage, transform, revolutionise.
4. One true hook with a source, or the fallback. Nothing about the business that was not read on a page.
5. No fee, rebate, price, result or review.
6. TMEC contact block and unsubscribe line present. Recipient not suppressed. Address has its source URL and date.
7. Reads aloud like a voicemail from Tommy, not a keynote.
