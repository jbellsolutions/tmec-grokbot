---
name: seo-audit
description: Reads TMEC's website, Google Business Profile, directory listings and the local searches homeowners use, checks competitors' local results from public pages, and writes the weekly audit plus drafts of new suburb or service pages and fixes. Used by SEO's weekly routine and when TMEC Command sends an SEO job. Read and draft only.
---

# SEO audit

## Usage (read less)

Read TMEC's and competitors' pages with `python3 /workspace/tmec-team/repo/usage/scripts/clean_page.py <url> --max-chars 6000`. Save each page's text under `data/seo/pages/` and next week run `page_diff.py <url> data/seo/watch` first: unchanged pages need no re-read. Scripts: `usage/SKILL.md`.

## Inputs
- TMEC's website: the home page, each service page, the contact page and the footer, as a visitor sees them. Start from the address in `/workspace/tmec-team/context/owner.md`; if it isn't there, search for it and write what you found as UNKNOWN until Tommy confirms.
- TMEC's Google Business Profile and Maps listing, as a visitor sees them (Grok web search).
- Public search results for the searches below.
- `/workspace/tmec-team/data/seo/facts.md` (last week's facts), `citations.csv`, `competitors.md`.
- `/workspace/tmec-team/data/radar/ledger.csv`: the last 14 days of what locals asked (read only).
- `/workspace/tmec-team/context/owner.md`, `/workspace/tmec-team/context/config.json`.

## Steps
1. **Facts first.** Read the site and the profile. Write `/workspace/tmec-team/data/seo/facts.md`: for each fact, the value, the link it came from, and the date read. Facts: business name as shown, address or service area, phone, hours, categories, services listed, suburbs named, website link on the profile, number of reviews and average shown, date of the latest post, number of photos shown, whether Q&A shows. A fact you can't read is `UNKNOWN: <what>, <why>`. Never copy a fact from memory or an old note without re-reading it.
2. **Name, address, phone (NAP) and directories.** From the facts, build the one correct NAP as it appears on the website. Check up to 10 directories this run, rotating through `citations.csv` (start with Google, Bing Places, Apple Maps, Facebook page, Yellow Pages, True Local, Hotfrog, SolarQuotes, ProductReview, the industry body listings TMEC says it belongs to). For each: found or not found, the NAP shown, matches yes or no, link, date. Mismatches are fixes to draft; "not found" is UNKNOWN until read, never "not listed". Only list a directory TMEC is already on or Tommy asks for.
3. **What homeowners search.** For each topic (solar, solar battery, EV charger, hail-damaged solar panels, blackouts and backup power, high power bills) with each of the main suburbs (Beerwah, Caloundra, Maroochydore, Buderim, Nambour, Noosa, Caboolture, Gympie and the suburbs in `owner.md`): note the autocomplete and "people also ask" suggestions the search shows, and the questions locals asked in the radar ledger. Write `/workspace/tmec-team/data/seo/searches.md`. Say plainly: volumes are UNKNOWN without a paid tool.
4. **Local results and competitors.** For up to 8 searches (for example "solar installer Sunshine Coast", "solar battery Buderim", "EV charger installation Caloundra"), note who shows in the map results and the first organic results, and whether TMEC does ("seen on <date> in this search"). For up to 5 competitors seen most, note their profile categories, review count and rating, recent posts, and the local pages they have that TMEC doesn't. Facts only, with links. Never name a competitor in anything for the public. Write `competitors.md`.
5. **Website local pages.** List which suburb and service pages TMEC's site has, from reading it. For each gap with a real search behind it, draft a page (up to 3 a run) at `/workspace/tmec-team/data/seo/drafts/pages/<slug>.md`: a title (under 60 characters), a meta description (under 155), one H1, 300 to 500 words of plain English about what TMEC does in that suburb or for that service, a short FAQ using real questions locals asked, and the in-house edge. Use only facts from `owner.md` or read from the site. No prices, rebate amounts, savings or install dates; no claim TMEC can't prove; no text copied from a competitor. Also list fixes to existing pages (a missing title, a thin page, a wrong phone number), each with the page link and the exact change.
6. **Write the audit** `/workspace/tmec-team/data/seo/audit/<YYYY-MM-DD>.md`, in this order: what changed since last week; the 3 things to do first (each one item Tommy can say yes to); the profile (what's there, what's missing); reviews (count, rating, new, unanswered); website pages; directories (matches and mismatches); searches and competitors; UNKNOWN list and what would close each one (for example "profile insights: Tommy can share view-only access").
7. **Queue what needs Tommy.** Every item uses the payload format in `/workspace/tmec-team/repo/policies/APPROVALS.md`, section "Items, decisions and the send gate": `ITEM`, `BOT: seo`, `WHY`, then `---PAYLOAD---` (`TO`, `SEND`, `SUBJECT`, `TEXT`), `---END---`, and `HASH` = sha256 of every byte between those two lines, newlines included. The `ITEM:` id is the file name without `.md`. In test mode (the routine is listed `test`, or `context/config.json` `run` is `test`) ids start `test-`, data files go under `/workspace/tmec-team/state/test/seo/`, and nothing else changes: this bot never publishes, so there is no outward action and no paid call to switch off.
   For each page draft, page fix or directory correction (ids `page-<slug>`, `fix-<YYYY-MM-DD>-<n>`, `dir-<directory>-<YYYY-MM-DD>`), write `/workspace/tmec-team/approved/pending/seo/<id>.md`:
   ```
   ITEM: <id>
   BOT: seo
   WHY: <the search or fact behind it, with source and date>
   ---PAYLOAD---
   TO: <the page or directory, with link; who puts it live: UNKNOWN until Tommy says who edits the website, until then Tommy gets the text>
   SEND: when Tommy (or whoever he names) publishes it; the bot cannot
   SUBJECT: <page | page-fix | directory>
   TEXT:
   <the exact text or change>
   ---END---
   HASH: <sha256 of every byte between the ---PAYLOAD--- line and the ---END--- line, newlines included>
   ```
8. **Act on a decision.** For each file in `/workspace/tmec-team/approved/decisions/seo/` whose id isn't in `/workspace/tmec-team/state/sent-keys-seo.md`: **recompute** the sha256 of the pending file's payload now and compare it with the decision's `HASH:` (a mismatch means the item changed after Tommy saw it: ignore it and tell TMEC Command). This bot publishes nothing, so the rest of the send gate has nothing to hold back. `yes`: mark "approved, hand to Tommy to publish", give him the exact text through TMEC Command, and add the id to `state/sent-keys-seo.md` with the outcome `approved, handed to Tommy`. Record "published" only when Tommy says so or the public page shows it (link it). `no`: mark declined and add the id with the outcome `declined`. `change`: redraft once as a new item with a new id and add the old id with the outcome `changed, redrafted as <id>`. A decision is never read again once its id is in the sent keys.

## Output
`data/seo/facts.md`, `audit/<date>.md`, `searches.md`, `competitors.md`, `citations.csv`, page drafts, and items in `approved/pending/seo/`.

## Done means
Every fact has a source and a date or is UNKNOWN; every gap has a draft or a reason; the audit says what it can't see; nothing was published.

## Never
- Publish, edit, submit or log in anywhere, including the website.
- Assume a fact about TMEC's site or profile.
- Report a search rank as a measurement, or a volume it can't see.
- Use a paid tool, or a competitor's text.
- Put a price, rebate amount or saving in a draft without its government source and the date checked.
