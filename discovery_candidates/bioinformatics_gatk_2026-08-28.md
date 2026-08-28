# Discovered gatk sources for bioinformatics -- 2026-08-28

## GOOD (2, 1 confirmed by direct review, 1 flagged as a stub despite passing)

### USC CARC - GATK
- URL: https://www.carc.usc.edu/user-guides/life-sciences-computing/software-packages/gatk
- Keyword hits: 33
- Verified by direct fetch: genuine, substantial -- module loading, full SLURM script, HaplotypeCaller example with real parameters, best-practices section.

```toml
[[html_sources]]
label = "USC CARC - GATK"
url = "https://www.carc.usc.edu/user-guides/life-sciences-computing/software-packages/gatk"
tool = "gatk"
```

### Tufts Research Technology - GATK4 -- NOT RECOMMENDED despite GOOD verdict
- URL: https://rtguides.it.tufts.edu/bio/apps/gatk4.html
- Keyword hits: 18
- Verified by direct fetch: this is a stub/landing page -- version list, one generic HaplotypeCaller
  template, mostly external links. Passed the keyword threshold but isn't substantive. Listed here
  for completeness rather than omitted; recommend skipping.

## WEAK -- needs a human look (1)

- **MSU ICER - GATK** -- https://docs.icer.msu.edu/available_software/detail/GATK/
  only 7 keyword hit(s) -- review before trusting

## Not usable

4 candidate(s) came back FAIL: USF Research Computing (network error), Purdue RCAC (HTTP 404),
UVA HPC (HTTP 403), Kentucky CCS Docs (network error).

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a candidate, copy its TOML block above into
`configs/bioinformatics.toml`. Note that `presets.py` isn't kept in sync with `configs/*.toml`
automatically -- add accepted sources there too for consistency with future wizard runs.
