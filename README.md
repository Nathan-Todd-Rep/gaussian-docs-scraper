# Gaussian Docs Scraper

A scraper that collects Gaussian-related passages from HPC documentation sources and saves them to `~/.inkly/gaussian_docs.json`. This file is read at runtime by the `docs_gaussian` plugin in [Inkly](https://github.com/Nathan-Todd-Rep/hpc-ink-setup).

---

## What does it do?

It pulls content from two source types:

- **Curated HPC documentation pages**: a seed list of trusted sites, filtered by Gaussian-related keywords
- **Chemistry Stack Exchange**: top-voted questions and accepted answers tagged with `gaussian`

Passages are keyword-filtered and capped per source to keep the output focused. If a local [Ollama](https://ollama.com) instance is running, each source's passages are summarized before saving.

---

## Installation

Install dependencies (BS4):

```bash
pip install requests beautifulsoup4
```

---

## Usage

Run the scraper and follow the prompts -- no command-line experience needed:

```bash
py scrape.py
```

The wizard asks what to scrape (a built-in preset or a custom topic), lets you
add extra sources, and saves the result for Inkly to read. Output defaults to
`~/.inkly/{name}_docs.json`; the Inkly `docs_gaussian` plugin reads the
Gaussian file automatically at runtime.

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

## Ollama Summarization

If you have Ollama installed and running locally, the scraper will summarize each source's passages into 2-3 sentences before saving. This makes the content surfaced by Inkly cleaner and more concise.

The scraper expects Ollama to be running on `http://localhost:11434` with the `llama3` model available:

```bash
ollama pull llama3
ollama serve
```

If Ollama is not running, the scraper falls back to storing raw passages, no setup required to use the scraper without it.

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

## Output Format

Each entry in `gaussian_docs.json` looks like this:

```json
{
  "label": "Chemistry Stack Exchange - Gaussian",
  "site": "chemistry",
  "tag": "gaussian",
  "passages": [
    "Set %mem=8GB and %nproc=4 in your Gaussian input file to match your Slurm resource request.",
    "..."
  ],
  "summary": "Gaussian 16 jobs on HPC clusters should set %mem and %nproc to match Slurm resource requests."
}
```

The `summary` key is only present when Ollama summarization ran successfully.

---

## Running Tests

```bash
py -m pytest -v
```

22 tests across the scraper, Stack Exchange fetcher, and summarizer modules.
