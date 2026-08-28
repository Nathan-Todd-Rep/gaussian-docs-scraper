# Discovered bwa sources for bioinformatics -- 2026-08-27 (run 2)

Note: an earlier run today (`bioinformatics_bwa_2026-08-27.md`) already proposed the BWA
GitHub (lh3) and OSG Connect tutorial candidates. Those are excluded here as already
proposed/accepted; this run searched for additional, genuinely new candidates.

## GOOD (4)

### FSU RCC - BWA
- URL: https://docs.rcc.fsu.edu/software/bwa/
- Keyword hits: 14

```toml
[[html_sources]]
label = "FSU RCC - BWA"
url = "https://docs.rcc.fsu.edu/software/bwa/"
tool = "bwa"
```

### HPC @ QMUL - BWA
- URL: https://docs.hpc.qmul.ac.uk/apps/bio/bwa/
- Keyword hits: 23

```toml
[[html_sources]]
label = "HPC @ QMUL - BWA"
url = "https://docs.hpc.qmul.ac.uk/apps/bio/bwa/"
tool = "bwa"
```

### UNL HCC - BWA
- URL: https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/alignment_tools/bwa
- Keyword hits: 15

```toml
[[html_sources]]
label = "UNL HCC - BWA"
url = "https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/alignment_tools/bwa"
tool = "bwa"
```

### CSC Docs - BWA
- URL: https://docs.csc.fi/apps/bwa/
- Keyword hits: 57

```toml
[[html_sources]]
label = "CSC Docs - BWA"
url = "https://docs.csc.fi/apps/bwa/"
tool = "bwa"
```

## WEAK -- needs a human look (2)

- **UF Research Computing - BWA** -- https://docs.rc.ufl.edu/software/apps/bwa
  only 9 keyword hit(s) -- review before trusting
- **Clemson RCD - BWA** -- https://docs.rcd.clemson.edu/software/applications/bioinformatics/alignment/burrows_wheeler_aligner_bwa/
  only 9 keyword hit(s) -- review before trusting

## Not usable

4 candidate(s) came back EMPTY or FAIL (no usable content, or the page couldn't be
fetched) and aren't listed individually here: HPC@LSU - BWA (HTTP 404), USF Research
Computing - BWA (network error), UKY CCS Docs - BWA (network error), Uni Oldenburg HPC
Wiki - BWA (HTTP 403).

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and
`gaussian_scraper/presets.py` were not touched. To accept a GOOD candidate, copy its TOML
block above into `configs/bioinformatics.toml`. Note that `presets.py` (the wizard's
built-in seed file) isn't kept in sync with `configs/*.toml` automatically in this repo --
if you want an accepted source to also show up for future fresh wizard runs, add it there
too.
