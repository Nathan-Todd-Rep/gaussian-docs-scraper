# Discovered DOCX sources for bioinformatics -- 2026-08-28

First DOCX-focused discovery pass for bioinformatics, following the DOCX support added this
session. Live, directly-linked .docx HPC/bioinformatics documentation turned out to be
genuinely rare on the open web (most institutions convert to PDF or publish as HTML) --
after extensive searching (site:edu filetype:docx across the domain's general keywords and
each of samtools/bwa/gatk/blast individually), the only real hits came from a single
source: the Babraham Institute Bioinformatics Group's training course exercises (UK
research institute behind FastQC/Trim Galore/SeqMonk -- widely used and cited bioinformatics
training material, same caliber as the university HPC-center docs already in this config,
even though it isn't a .edu domain). All 6 candidates found there were validated; all GOOD
candidates were fetched and read directly, not just keyword-counted.

## GOOD (3, all confirmed genuine and substantial by direct review)

### Babraham - Analysing RNA-Seq data Exercise (DOCX)
- URL: https://www.bioinformatics.babraham.ac.uk/training/RNASeq_Course/Analysing%20RNA-Seq%20data%20Exercise.docx
- Keyword hits: 52
- Verified: real workshop practical -- full RNA-Seq differential expression walkthrough
  (HiSat2 mapping, Samtools, FastQC, SeqMonk visualization/quantitation, DESeq2 differential
  expression), with real GEO accession datasets. Not a stub.

```toml
[[html_sources]]
label = "Babraham - Analysing RNA-Seq data Exercise (DOCX)"
url = "https://www.bioinformatics.babraham.ac.uk/training/RNASeq_Course/Analysing%20RNA-Seq%20data%20Exercise.docx"
```

### Babraham - Sequencing QC Exercise (DOCX)
- URL: https://www.bioinformatics.babraham.ac.uk/training/Sequence_QC_Course/Sequencing%20QC%20Exercise.docx
- Keyword hits: 38
- Verified: real QC practical using FastQC/FastQ Screen/MultiQC across several real public
  datasets (GEO/SRA accessions), with concrete exercises on interpreting per-base quality,
  per-tile quality, and adapter content sections. Not a stub.

```toml
[[html_sources]]
label = "Babraham - Sequencing QC Exercise (DOCX)"
url = "https://www.bioinformatics.babraham.ac.uk/training/Sequence_QC_Course/Sequencing%20QC%20Exercise.docx"
```

### Babraham - Linux Bootcamp Exercises (DOCX)
- URL: https://www.bioinformatics.babraham.ac.uk/training/Linux%20bootcamp/Linux%20Bootcamp%20Exercises.docx
- Keyword hits: 31
- Verified: substantial multi-exercise Unix/Linux skills course aimed at bioinformaticians --
  starts with generic shell basics but progresses into genome data file manipulation
  (chromosome .dat files, rRNA searches), fastq.gz handling with zcat/bzip2, sequence
  alignment via clustalw, and installing/building the NCBI BLAST+ toolkit from source. Not
  purely generic Linux material -- genuinely bioinformatics-flavored throughout. Left
  untagged (touches many tools, not specific to one).

```toml
[[html_sources]]
label = "Babraham - Linux Bootcamp Exercises (DOCX)"
url = "https://www.bioinformatics.babraham.ac.uk/training/Linux%20bootcamp/Linux%20Bootcamp%20Exercises.docx"
```

## WEAK -- needs a human look (3)

- **Babraham - Seurat Exercise (DOCX)** -- https://www.bioinformatics.babraham.ac.uk/training/10XRNASeq/Seurat%20Exercise.docx
  only 5 keyword hit(s) -- single-cell RNA-seq (Seurat/10X) practical, real content but
  vocabulary doesn't overlap much with this domain's keyword list -- review before trusting
- **Babraham - Loupe Browser Exercise (DOCX)** -- https://www.bioinformatics.babraham.ac.uk/training/10XRNASeq/Loupe%20Browser%20Exercise.docx
  only 1 keyword hit(s) -- 10X Genomics Loupe Browser GUI walkthrough, mostly click-through
  instructions with little of this domain's vocabulary -- review before trusting
- **Babraham - Gene Lists Exercise (DOCX)** -- https://www.bioinformatics.babraham.ac.uk/training/Gene_Set_Analysis/Gene_Lists_Exercise.docx
  only 1 keyword hit(s) -- gene set/pathway enrichment practical, a downstream-analysis topic
  adjacent to but distinct from this domain's alignment/variant-calling focus -- review
  before trusting

## Not usable

0 candidates came back EMPTY or FAIL this run -- all 6 Babraham URLs found were live and
fetched successfully; the split above is GOOD vs WEAK only.

Extensive additional searching for a gaussian-domain-equivalent .docx pass turned up nothing
usable at all (see `gaussian` summary in chat -- no proposal file was written for that domain
this run since there was nothing real to report).

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a GOOD candidate, copy its TOML block above into
`configs/bioinformatics.toml`. Note that `presets.py` isn't kept in sync with `configs/*.toml`
automatically -- add accepted sources there too for consistency with future wizard runs.
