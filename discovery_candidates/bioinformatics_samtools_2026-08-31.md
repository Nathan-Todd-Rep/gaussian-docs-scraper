# Discovered samtools sources for bioinformatics -- 2026-08-31

Rotation note: picked for this run because `bioinformatics_samtools_2026-08-27.md` and
`bioinformatics_bwa_2026-08-27.md`/`_run2.md` were the two oldest roster proposals (tied at
2026-08-27); bwa already got a same-day follow-up run (`_run2`) while samtools had only one
pass, so samtools was the more stale of the two.

Searched with samtools' own command vocabulary (`sort`, `index`, `flagstat`, `cram`,
`mpileup`) plus a direct search for its GitHub org/wiki, per the skill's tool-scoped mode.
Checked against `configs/bioinformatics.toml` (existing `tool = "samtools"` entries) and
`discovery_candidates/bioinformatics_samtools_2026-08-27.md` to exclude anything already
known.

Checked with:
`py check_sources.py --keywords "rna-seq,fastq,samtools,bwa,gatk,genome,variant-calling,ngs,vcf,alignment,bam,blast" ...`

## GOOD (3, all confirmed by direct review)

### Wayne State - How to Use SAMtools
- URL: https://tech.wayne.edu/kb/high-performance-computing/hpc-tutorials/500104
- Keyword hits: 30
- What it contains: A Wayne State grid-computing KB article (the URL 307-redirects to the
  live Team Dynamix article, which `check_sources.py`/`fetch_page_text` follow
  automatically) covering `samtools view`, `tview`, `sort`, and `index` with concrete
  command syntax (e.g. `samtools view sample.bam > sample.sam`) and module-load setup for
  their HPC environment. Brief in places (a couple of TODO-marked gaps) but genuinely
  instructional, not a stub.

```toml
[[html_sources]]
label = "Wayne State - How to Use SAMtools"
url = "https://tech.wayne.edu/kb/high-performance-computing/hpc-tutorials/500104"
tool = "samtools"
```

### Nebraska HCC - Running SAMtools Commands
- URL: https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/data_manipulation_tools/samtools/running_samtools_commands/
- Keyword hits: 42
- What it contains: A deeper sub-page of the HCC samtools docs (distinct from the
  already-configured top-level `.../samtools` page) walking through `view`, `sort`,
  `index`, `idxstats`, `merge`, `faidx`, `mpileup`, and `tview` with SLURM job-script
  examples and HCC-specific multithreading guidance (`-@` flag). Genuinely substantive,
  not a duplicate of the existing top-level page's content.

```toml
[[html_sources]]
label = "Nebraska HCC - Running SAMtools Commands"
url = "https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/data_manipulation_tools/samtools/running_samtools_commands/"
tool = "samtools"
```

### Idaho HPC - SAMtools
- URL: https://hpc.uidaho.edu/compute/Applications/SAMtools.html
- Keyword hits: 41
- What it contains: A full variant-calling walkthrough built around samtools -- BWA
  indexing/alignment, SAM-to-BAM conversion and sorting, mapping-quality assessment via
  samstat, coverage/variant calling (unfiltered and filtered VCF output), and downstream
  filtering with bcftools/vcfutils. Complete command-line examples throughout; genuine
  pipeline documentation, not a stub.

```toml
[[html_sources]]
label = "Idaho HPC - SAMtools"
url = "https://hpc.uidaho.edu/compute/Applications/SAMtools.html"
tool = "samtools"
```

## Rejected despite GOOD keyword count (2)

Both scored high enough on `check_sources.py` to land in GOOD, but reading the actual
extracted text showed they're thin -- exactly the failure mode the skill warns about,
where a passing hit count doesn't reliably mean substantive content:

- **Hull HPC - Samtools** -- https://hpc.mediawiki.hull.ac.uk/Applications/Samtools
  (22 hits) -- a bare quick-reference stub: version/license info, seven one-line usage
  examples, a link to htslib.org, no explanations or workflow context.
- **Sanger Institute - SAMtools/BCFtools/HTSlib** -- https://www.sanger.ac.uk/tool/samtools-bcftools-htslib/
  (21 hits) -- an institutional landing/attribution page, not documentation; it just
  points out to www.htslib.org and GitHub for the actual content.

## WEAK -- needs a human look (0)

None this run -- results split cleanly into substantive GOOD or thin/rejected.

## Not usable

3 candidate(s) came back EMPTY or FAIL (no usable content, or the page couldn't be
fetched) and aren't listed individually here. (UPenn HPC Wiki - Samtools,
https://hpcwiki.pmacs.upenn.edu/wiki/index.php/HPC:samtools, returned no extractable
content -- likely JS-rendered. UVA Research Computing - Samtools,
https://www.rc.virginia.edu/userinfo/hpc/software/samtools/, returned HTTP 403. UMD HPC -
Samtools, https://hpcc.umd.edu/software/packages/samtools/, returned a network error --
all three worth a manual look if desired.)

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and
`gaussian_scraper/presets.py` were not touched. To accept a GOOD candidate, copy its TOML
block above into `configs/bioinformatics.toml`. Note that `presets.py` (the wizard's
built-in seed file) isn't kept in sync with `configs/*.toml` automatically in this repo --
if you want an accepted source to also show up for future fresh wizard runs, add it there
too.
