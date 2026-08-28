# Gaussian Docs Scraper

A domain-agnostic scraper that collects HPC documentation and Stack Exchange passages for a research topic (e.g. Gaussian, bioinformatics) and saves them to a per-domain SQLite database at `~/.inkly/{name}.db`, for [Inkly](https://github.com/Nathan-Todd-Rep/hpc-ink-setup) or any other consumer to read.

---

## What does it do?

It pulls content from two source types:

- **Curated HPC documentation pages**: a seed list of trusted sites, filtered by Gaussian-related keywords. Sources can be HTML pages, PDFs, Word docs, PowerPoint slides, or plain text (user manuals, workshop slides, HPC-specific guides) -- the fetcher detects which format a URL is automatically, no separate configuration needed.
- **Chemistry Stack Exchange**: top-voted questions and accepted answers tagged with `gaussian`

Passages are keyword-filtered and capped per source to keep the output focused. If a local [Ollama](https://ollama.com) instance is running, each source's passages are summarized before saving.

---

## Installation

Install dependencies:

```bash
pip install requests beautifulsoup4 pypdf python-docx python-pptx
```

---

## Usage

Run the scraper and follow the prompts -- no command-line experience needed:

```bash
py scrape.py
```

The wizard asks what to scrape (a built-in preset or a custom topic), lets you
add extra sources, and saves the result for Inkly to read. Output defaults to
`~/.inkly/{name}.db`, a SQLite database `search_docs.py` (and Inkly) can query.

Already have a config from a previous run? See what's saved with:

```bash
py scrape.py --list-configs
```

and re-run one without going through the wizard again with:

```bash
py scrape.py --config configs/gaussian.toml
```

Run `py scrape.py --help` for the full option list with examples.

---

## Continuous Re-scraping

`Daily Scrape.bat` re-scrapes a domain unattended with `--skip-summary` (raw
passages only, no Ollama needed) and appends output to
`~/.inkly/daily_scrape.log`. It's meant to be run by a scheduled task, not
double-clicked -- on this machine it's registered as a Windows Task Scheduler
entry (`GaussianScraperDailyScrape`, daily at 3:00 AM, runs only while logged
in) that keeps `gaussian.db` fresh without manual re-runs. Content-hashing
(see Output Format below) means a future full run *with* summarization would
only re-summarize sources whose content actually changed, so this is safe to
extend to summarized runs later without repeatedly re-paying for unchanged
sources. Currently scoped to the gaussian domain only; add more `--config`
lines to the batch file once other domains are ready for the same treatment.

---

## Ollama Summarization

If you have Ollama installed and running locally, the scraper will summarize each source's passages into 2-3 sentences before saving. This makes the content surfaced by Inkly cleaner and more concise.

The scraper expects Ollama to be running on `http://localhost:11434` with the `llama3` model available:

```bash
ollama pull llama3
ollama serve
```

If Ollama is not running, the scraper falls back to storing raw passages, no setup required to use the scraper without it.

Using a different model (e.g. one already pulled for another project)? Override it with `--model`:

```bash
py scrape.py --model llama3-cuttlefish
```

CPU-only Ollama (no GPU) can be slow -- real testing saw individual summaries
take anywhere from ~20s to over 90s. The scraper waits up to 120s per summary
by default; if summaries keep getting skipped even though Ollama is clearly
running, give it more room with `--summary-timeout`:

```bash
py scrape.py --summary-timeout 180
```

---

## Searching Scraped Passages by Relevance

Once a domain has been scraped, its passages can be ranked against a
question instead of read in full:

```bash
py search_docs.py --domain gaussian --query "how do I request memory for a job?"
```

This is the retrieval half of a RAG-style pipeline: it scores every scraped
passage for a domain against the query (TF-IDF + cosine similarity, no
external ML dependency) and returns only the top few, so a consumer never
needs to load the entire scraped dataset to answer one question. See
`gaussian_scraper/passage_index.py`.

---

## Discovering New Sources

Every source in `configs/*.toml` today was found by manually web-searching and
hand-adding it. The `/discover-sources <domain>` command (a Claude Code skill,
see `.claude/skills/discover-sources/`) automates the search step: it looks for
new candidate HTML documentation pages for a domain, validates them with
`check_sources.py`, and writes a proposal file to
`discovery_candidates/{domain}_{date}.md` -- it never edits `configs/*.toml` or
`presets.py` itself. Reviewing the proposal and copying accepted sources into a
config stays a manual step.

```bash
# from within a Claude Code session in this repo
/discover-sources gaussian
```

Currently covers HTML sources only, not Stack Exchange tags.

---

## Output Format

Each domain's data lives in its own SQLite database (`~/.inkly/{name}.db`), with
two tables:

- `sources`: one row per scraped source (`label`, `source_type` [`html`/`se`],
  `url` or `site`/`tag`, `content_hash`, `summary`, `last_scraped_at`).
  `content_hash` is a hash of the source's passages, used to skip
  re-summarizing a source whose content hasn't changed since the last scrape.
  `summary` is only populated when Ollama summarization ran successfully (or
  was reused from a prior run via the content hash).
- `passages`: one row per passage, linked to its source and ordered by
  position.

See `gaussian_scraper/storage.py` for the schema and `search_docs.py` /
`gaussian_scraper/passage_index.py` for how it's queried.

---

## Running Tests

```bash
py -m pytest -v
```

22 tests across the scraper, Stack Exchange fetcher, and summarizer modules.
