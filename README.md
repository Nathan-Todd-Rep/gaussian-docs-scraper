# Gaussian Docs Scraper

A scraper that collects Gaussian-related passages from HPC documentation sources and saves them to `~/.inkly/gaussian_docs.json`. This file is read at runtime by the `docs_gaussian` plugin in [Inkly](https://github.com/Nathan-Todd-Rep/hpc-ink-setup).

---

## What It Does

It pulls content from two source types:

- **Curated HPC documentation pages**: a seed list of trusted sites, filtered by Gaussian-related keywords
- **Chemistry Stack Exchange**: top-voted questions and accepted answers tagged with `gaussian`

Passages are keyword-filtered and capped per source to keep the output focused. If a local [Ollama](https://ollama.com) instance is running, each source's passages are summarized before saving.

---

## Installation

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

## Usage

Run the scraper to refresh the data:

```bash
py scrape.py
```

Output is saved to `~/.inkly/gaussian_docs.json`. The Inkly `docs_gaussian` plugin reads from this file automatically at runtime.

---

## Ollama Summarization

If you have Ollama installed and running locally, the scraper will summarize each source's passages into 2-3 sentences before saving. This makes the content surfaced by Inkly cleaner and more concise.

The scraper expects Ollama to be running on `http://localhost:11434` with the `llama3` model available:

```bash
ollama pull llama3
ollama serve
```

If Ollama is not running, the scraper falls back to storing raw passages — no setup required to use the scraper without it.

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
