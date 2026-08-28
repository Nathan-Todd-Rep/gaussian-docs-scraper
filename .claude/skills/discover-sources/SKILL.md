---
name: discover-sources
description: Use this skill whenever asked to find, discover, or search for new candidate documentation sources for one of gaussian-docs-scraper's research domains (e.g. Gaussian, bioinformatics, or any other domain with a configs/{domain}.toml file in this repo) -- including sources for a specific tool within a domain, e.g. "find new samtools sources" or "discover sources for the bwa tool". Triggers on requests like "find new sources for gaussian", "discover more HPC documentation for bioinformatics", "look for sources to add to the scraper", "expand the source list", "find sources for the gatk tool", "/discover-sources gaussian", "/discover-sources bioinformatics samtools", or similar -- even if the user doesn't say "discover" explicitly, use this skill whenever the intent is to grow the list of scraped sources for a domain or a tool within one. It searches the web (and, when a tool is named, GitHub specifically) for candidate documentation pages, validates them with this repo's own check_sources.py tool, and writes a review-only proposal file. It does NOT edit configs/*.toml or presets.py directly -- do not use it if the user has already decided on specific URLs to add and just wants them added to a config; that's a direct edit, not a discovery task.
---

# Discovering New Sources

Finds new candidate HTML documentation sources for a gaussian-docs-scraper domain,
checks their quality with the repo's existing health-check tool, and writes a proposal
file for a human to review. It never edits `configs/*.toml` or `gaussian_scraper/presets.py`
directly -- every source currently in this repo was added by a human after review, and an
unreviewed source silently entering a dataset meant to be trustworthy would undermine the
whole point of curating sources in the first place. This skill automates the *search*
step only; deciding what actually gets added stays a deliberate human choice.

**Scope:** `html_sources` entries only -- this covers both HTML pages and PDF documents
(`fetch_page_text` auto-detects which one a URL is and extracts accordingly, no special
handling needed either way). Stack Exchange tag sources (`se_sources`) aren't covered --
there's no equivalent automated quality check for those in this repo yet (just a live
tag-discovery helper used inside the interactive wizard, with no comparable GOOD/WEAK/FAIL
bar), so don't attempt to discover or validate SE tags here.

**Optional tool scoping:** some domains -- bioinformatics especially -- aren't one
cohesive topic, they're a collection of mostly-independent tools (samtools, bwa, gatk,
...), often maintained by small academic projects whose only real documentation is a
GitHub README rather than a polished HPC-center doc page. Rather than a separate domain
per tool, this repo tags individual sources with an optional `tool` field and keeps them
in one domain (see `configs/bioinformatics.toml` for examples). If the request names a
specific tool (`/discover-sources bioinformatics samtools`, or "find new bwa sources"),
run this skill in **tool-scoped mode** (steps marked accordingly below); otherwise run it
domain-wide exactly as before, with no tool tag applied.

## Workflow

### 1. Load the domain's existing state

Run from the repo root:

```bash
py -c "from pathlib import Path; from gaussian_scraper.config import load_toml_config; c = load_toml_config(Path('configs/{domain}.toml')); print(c.keywords); print([s['url'] for s in c.html_sources])"
```

(or read `configs/{domain}.toml` directly). Collect the domain's `keywords` and every
existing `html_sources` URL -- this is the dedup baseline. Nothing already in the config
should be re-proposed; that would just waste a search and a health check on something
already decided. In tool-scoped mode, also note which existing sources already carry
`tool = "{tool}"`, since those are the ones worth looking at for a feel for what's already
covered for that specific tool.

### 2. Check for still-pending proposals from earlier runs

Look for `discovery_candidates/{domain}_*.md` files from previous runs (the directory may
not exist yet -- that's fine, it means this is the first run for any domain). Collect any
URLs already listed in those files too. Without this step, a candidate that was already
proposed but hasn't been reviewed yet would get proposed again every time this skill runs,
which just adds noise for the person reviewing it.

### 3. Search for candidates

**Domain-wide (no tool given):** Use WebSearch to find roughly 5-10 new candidate
documentation pages for the domain's topic, guided by its keywords. Look at the domain's
*existing* sources first (from step 1) to get a feel for the pattern worth matching --
this repo's sources are consistently official university/HPC-center documentation pages
(`.edu` domains, HPC center docs sites), not forums, blogs, or vendor marketing. Aim for
that same tier of source. PDF documents count too -- user manuals, workshop/tutorial
slides, and HPC-center-specific PDF guides are valid candidates alongside HTML pages, no
different treatment needed (a search like `"{topic} filetype:pdf site:edu"` can surface
these). Exclude any URL already known from steps 1-2.

**Tool-scoped (a tool was named):** Narrow the search to that specific tool's own name
and real technical vocabulary rather than the domain's generic keywords -- e.g. for
samtools that's terms like `sort`/`index`/`flagstat`/`cram`, not just "bioinformatics".
**Also explicitly search for the tool's GitHub repository and wiki** (e.g. `"{tool}
github"` or `"{tool} bioinformatics repository"`) as its own candidate, not only doc
sites -- this is the main point of tool-scoping, since many small academic tools have no
doc site at all, only a README. GitHub repo/wiki pages need no special handling: GitHub
server-renders README content into plain `h1`-`h4`/`li`/`pre`/`p` tags, the same tags
`fetch_page_text` already extracts from any HTML page, so they validate through
`check_sources.py` exactly like any other URL (verified for real against
`github.com/samtools/samtools`). Exclude any URL already known from step 1.

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
(domain-wide) or `discovery_candidates/{domain}_{tool}_{YYYY-MM-DD}.md` (tool-scoped),
using today's actual date, in this format:

```markdown
# Discovered sources for {domain} -- {YYYY-MM-DD}
<!-- tool-scoped runs: "# Discovered {tool} sources for {domain} -- {YYYY-MM-DD}" -->

## GOOD ({n})

### {label}
- URL: {url}
- Keyword hits: {n}

\`\`\`toml
[[html_sources]]
label = "{label}"
url = "{url}"
tool = "{tool}"
\`\`\`
<!-- omit the tool line entirely for domain-wide (non-tool-scoped) runs -->

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
