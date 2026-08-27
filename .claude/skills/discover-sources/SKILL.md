---
name: discover-sources
description: Use this skill whenever asked to find, discover, or search for new candidate documentation sources for one of gaussian-docs-scraper's research domains (e.g. Gaussian, bioinformatics, or any other domain with a configs/{domain}.toml file in this repo). Triggers on requests like "find new sources for gaussian", "discover more HPC documentation for bioinformatics", "look for sources to add to the scraper", "expand the source list", "/discover-sources gaussian", or similar -- even if the user doesn't say "discover" explicitly, use this skill whenever the intent is to grow the list of scraped sources for a domain. It searches the web for candidate HTML documentation pages, validates them with this repo's own check_sources.py tool, and writes a review-only proposal file. It does NOT edit configs/*.toml or presets.py directly -- do not use it if the user has already decided on specific URLs to add and just wants them added to a config; that's a direct edit, not a discovery task.
---

# Discovering New Sources

Finds new candidate HTML documentation sources for a gaussian-docs-scraper domain,
checks their quality with the repo's existing health-check tool, and writes a proposal
file for a human to review. It never edits `configs/*.toml` or `gaussian_scraper/presets.py`
directly -- every source currently in this repo was added by a human after review, and an
unreviewed source silently entering a dataset meant to be trustworthy would undermine the
whole point of curating sources in the first place. This skill automates the *search*
step only; deciding what actually gets added stays a deliberate human choice.

**Scope:** HTML documentation sources (`html_sources`) only. Stack Exchange tag sources
(`se_sources`) aren't covered -- there's no equivalent automated quality check for those
in this repo yet (just a live tag-discovery helper used inside the interactive wizard,
with no comparable GOOD/WEAK/FAIL bar), so don't attempt to discover or validate SE tags
here.

## Workflow

### 1. Load the domain's existing state

Run from the repo root:

```bash
py -c "from pathlib import Path; from gaussian_scraper.config import load_toml_config; c = load_toml_config(Path('configs/{domain}.toml')); print(c.keywords); print([s['url'] for s in c.html_sources])"
```

(or read `configs/{domain}.toml` directly). Collect the domain's `keywords` and every
existing `html_sources` URL -- this is the dedup baseline. Nothing already in the config
should be re-proposed; that would just waste a search and a health check on something
already decided.

### 2. Check for still-pending proposals from earlier runs

Look for `discovery_candidates/{domain}_*.md` files from previous runs (the directory may
not exist yet -- that's fine, it means this is the first run for any domain). Collect any
URLs already listed in those files too. Without this step, a candidate that was already
proposed but hasn't been reviewed yet would get proposed again every time this skill runs,
which just adds noise for the person reviewing it.

### 3. Search for candidates

Use WebSearch to find roughly 5-10 new candidate documentation pages for the domain's
topic, guided by its keywords. Look at the domain's *existing* sources first (from step 1)
to get a feel for the pattern worth matching -- this repo's sources are consistently
official university/HPC-center documentation pages (`.edu` domains, HPC center docs
sites), not forums, blogs, or vendor marketing. Aim for that same tier of source. Exclude
any URL already known from steps 1-2.

### 4. Validate every candidate

Don't write new validation logic -- this repo already has a health-check tool that's the
established quality bar for every source currently in it, and reusing it means a
discovered source is held to exactly the same standard as a manually-added one. Run it
once for the whole batch:

```bash
py check_sources.py --keywords "<comma-separated domain keywords>" \
  --url "<url1>" --label "<label1>" \
  --url "<url2>" --label "<label2>" \
  [... one --url/--label pair per candidate]
```

Read the printed report directly -- no need to parse it programmatically. It groups
results into `GOOD` (>=10 keyword-hit lines, safe to add), `WEAK` (1-9 hits, on-topic but
thin, worth a human look), and `EMPTY`/`FAIL` (unusable -- no content or the page
couldn't be fetched), each with the label/url/reason, ending in a `"{good}/{total} sources
are GOOD"` summary line.

### 5. Write the proposal file

Create (or append to, if run again same day) `discovery_candidates/{domain}_{YYYY-MM-DD}.md`
using today's actual date, in this format:

```markdown
# Discovered sources for {domain} -- {YYYY-MM-DD}

## GOOD ({n})

### {label}
- URL: {url}
- Keyword hits: {n}

\`\`\`toml
[[html_sources]]
label = "{label}"
url = "{url}"
\`\`\`

(repeat per GOOD candidate)

## WEAK -- needs a human look ({n})

- **{label}** -- {url}
  {reason}

(repeat per WEAK candidate)

## Not usable

{n} candidate(s) came back EMPTY or FAIL (no usable content, or the page couldn't be
fetched) and aren't listed individually here.

## Nothing was added automatically

This file is a proposal only. `configs/{domain}.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a GOOD candidate, copy its TOML block above into
`configs/{domain}.toml`. Note that `presets.py` (the wizard's built-in seed file) isn't
kept in sync with `configs/*.toml` automatically in this repo -- if you want an accepted
source to also show up for future fresh wizard runs, add it there too.
```

Give each GOOD candidate a ready-to-paste TOML block in the exact `[[html_sources]]`
format this repo's configs already use, so accepting one is a copy-paste, not a
re-transcription. WEAK candidates get listed with their reason but no TOML block, mirroring
`check_sources.py`'s own framing that a WEAK source needs a look before it's trusted.

### 6. Report back

Summarize in chat: how many candidates were found, the GOOD/WEAK/EMPTY/FAIL counts, and
the path to the proposal file. Don't claim anything was "added" -- it was proposed.
