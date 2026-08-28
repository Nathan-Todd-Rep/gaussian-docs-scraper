# Discovered blast sources for bioinformatics -- 2026-08-28

## GOOD (5, all confirmed by direct review)

### UWEC Blugold HPC - BLAST
- URL: https://docs.hpc.uwec.edu/software/guides/blast/
- Keyword hits: 13
- Verified: module availability, local database env vars, real SLURM blastp example, citation guidance.

```toml
[[html_sources]]
label = "UWEC Blugold HPC - BLAST"
url = "https://docs.hpc.uwec.edu/software/guides/blast/"
tool = "blast"
```

### MSU ICER - BLAST+
- URL: https://docs.icer.msu.edu/BLAST_BLAST+_with_Multiple_Processors/
- Keyword hits: 45
- Verified: multi-threading details, BLAST vs BLAST+ flag differences, BLASTDB config, data-prep workflow.

```toml
[[html_sources]]
label = "MSU ICER - BLAST+"
url = "https://docs.icer.msu.edu/BLAST_BLAST+_with_Multiple_Processors/"
tool = "blast"
```

### UGA GACRC - BLAST+ Teaching
- URL: https://wiki.gacrc.uga.edu/wiki/BLAST+-Teaching
- Keyword hits: 74
- Verified: full SLURM examples, multithreading CPU-allocation math, extensive blastn option reference.

```toml
[[html_sources]]
label = "UGA GACRC - BLAST+ Teaching"
url = "https://wiki.gacrc.uga.edu/wiki/BLAST+-Teaching"
tool = "blast"
```

### Iowa State Pronto - BLAST
- URL: https://research.it.iastate.edu/guides/pronto/bioinformatics/blast/
- Keyword hits: 38
- Verified: real performance benchmarking across thread counts, GNU Parallel multi-job SLURM script,
  practical tuning recommendations.

```toml
[[html_sources]]
label = "Iowa State Pronto - BLAST"
url = "https://research.it.iastate.edu/guides/pronto/bioinformatics/blast/"
tool = "blast"
```

### NC State HPC - BLAST
- URL: https://hpc.ncsu.edu/Software/Apps.php?app=BLAST
- Keyword hits: 79
- Verified: three execution modes (serial/shared-memory/MPI), a full worked tutorial, LSF batch
  templates. Best of this batch.

```toml
[[html_sources]]
label = "NC State HPC - BLAST"
url = "https://hpc.ncsu.edu/Software/Apps.php?app=BLAST"
tool = "blast"
```

## Not usable

0 candidates came back EMPTY, WEAK, or FAIL this run.

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a candidate, copy its TOML block above into
`configs/bioinformatics.toml`. Note that `presets.py` isn't kept in sync with `configs/*.toml`
automatically -- add accepted sources there too for consistency with future wizard runs.
