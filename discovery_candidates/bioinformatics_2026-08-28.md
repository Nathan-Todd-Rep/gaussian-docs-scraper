# Discovered sources for bioinformatics (domain-wide) -- 2026-08-28

## GOOD (2, both confirmed by direct review)

### Purdue RCAC - HPC Orientation for Biologists
- URL: https://docs.rcac.purdue.edu/lifesciences/guides/hpc-orientation/
- Keyword hits: 17
- Verified: comprehensive onboarding -- access methods, BioContainers/module system, SLURM job
  submission, storage tiers, data transfer. General bioinformatics HPC orientation, not tied to
  one tool.

```toml
[[html_sources]]
label = "Purdue RCAC - HPC Orientation for Biologists"
url = "https://docs.rcac.purdue.edu/lifesciences/guides/hpc-orientation/"
```

### Harvard FAS - Snakemake Workshop
- URL: https://informatics.fas.harvard.edu/workshops/snakemake/run/
- Keyword hits: 19
- Verified: substantial workflow-manager tutorial -- rules/wildcards, dryruns, DAG visualization,
  debugging, SLURM executor integration, worked examples. Workflow orchestration applies across
  tools, not one specific one.

```toml
[[html_sources]]
label = "Harvard FAS - Snakemake Workshop"
url = "https://informatics.fas.harvard.edu/workshops/snakemake/run/"
```

## WEAK -- needs a human look (3)

- **Bioinformatics Workbook - HPC Cluster Basics** -- https://bioinformaticsworkbook.org/Appendix/Unix/unix-basics-6HPC.html
  only 1 keyword hit(s) -- review before trusting
- **IU HPC Onboarding for Biologists** -- https://ittraining.iu.edu/explore-topics/titles/bionboard/index.html
  only 2 keyword hit(s) -- review before trusting
- **Oregon State HPC - Nextflow** -- https://docs.hpc.oregonstate.edu/cqls/software/nextflow/
  only 2 keyword hit(s) -- review before trusting

## Not usable

2 candidate(s) came back FAIL: Purdue RCAC - Nextflow (HTTP 404), Brown CCV - Nextflow (HTTP 404).

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a candidate, copy its TOML block above into
`configs/bioinformatics.toml`. Note that `presets.py` isn't kept in sync with `configs/*.toml`
automatically -- add accepted sources there too for consistency with future wizard runs.
