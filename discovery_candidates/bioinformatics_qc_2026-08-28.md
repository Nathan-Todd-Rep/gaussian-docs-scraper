# Discovered QC/trimming tool sources for bioinformatics -- 2026-08-28

Checked with:
`py check_sources.py --keywords "rna-seq,fastq,samtools,bwa,gatk,genome,variant-calling,ngs,vcf,alignment,bam,blast" ...`

## FastQC

### GOOD (5)

#### Babraham Bioinformatics - FastQC
- URL: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
- Keyword hits: 27
- What it contains: The tool's official project page. Explains that FastQC runs a modular set of QC analyses on raw FASTQ/BAM/SAM sequencing data (per-base quality, adapter content, GC content, duplication, etc.) and gives a quick pass/warn/fail impression before further analysis.

```toml
[[html_sources]]
label = "Babraham Bioinformatics - FastQC"
url = "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/"
tool = "fastqc"
```

#### GitHub - s-andrews/FastQC
- URL: https://github.com/s-andrews/FastQC
- Keyword hits: 13
- What it contains: The official source repository (maintained by Simon Andrews at Babraham). README describes FastQC as a QC application for FastQ files that spots potential problems in high-throughput sequencing datasets and produces a summary report.

```toml
[[html_sources]]
label = "GitHub - s-andrews/FastQC"
url = "https://github.com/s-andrews/FastQC"
tool = "fastqc"
```

#### Bucknell BisonNet - FastQC Guide (PDF)
- URL: https://bisonnet.bucknell.edu/files/2021/02/FASTQC-Help-Page-Final.pdf
- Keyword hits: 35
- What it contains: A beginner's guide to running FastQC on Bucknell's HPC cluster (BisonNet). Explains what FastQC does, why QC matters for raw sequencing data, and walks through interpreting the HTML report's graphs/tables.

```toml
[[html_sources]]
label = "Bucknell BisonNet - FastQC Guide (PDF)"
url = "https://bisonnet.bucknell.edu/files/2021/02/FASTQC-Help-Page-Final.pdf"
tool = "fastqc"
```

#### Missouri Genomics Core - FastQC Manual (PDF)
- URL: https://mugenomicscore.missouri.edu/PDF/FastQC_Manual.pdf
- Keyword hits: 33
- What it contains: A manual covering what FastQC is and why QC checks matter for high-throughput sequencer output, then walks through each analysis module and how to read pass/warn/fail results.

```toml
[[html_sources]]
label = "Missouri Genomics Core - FastQC Manual (PDF)"
url = "https://mugenomicscore.missouri.edu/PDF/FastQC_Manual.pdf"
tool = "fastqc"
```

#### MSU RTSF - FastQC Tutorial and FAQ (PDF)
- URL: https://rtsf.natsci.msu.edu/sites/_rtsf/assets/File/FastQC_TutorialAndFAQ_080717.pdf
- Keyword hits: 28
- What it contains: MSU's Research Technology Support Facility (Genomics Core) tutorial/FAQ on FastQC, explaining which of FastQC's modules the core relies on and why, aimed at end users interpreting their own reports.

```toml
[[html_sources]]
label = "MSU RTSF - FastQC Tutorial and FAQ (PDF)"
url = "https://rtsf.natsci.msu.edu/sites/_rtsf/assets/File/FastQC_TutorialAndFAQ_080717.pdf"
tool = "fastqc"
```

### WEAK -- needs a human look (0)
None.

### Not usable
8 candidate(s) came back EMPTY or FAIL and aren't listed individually (mostly university HPC wiki/software pages that returned network errors, HTTP 302 redirects, or JS-rendered pages with no extractable text -- e.g. UMD HPC, PMACS HPC wiki x2, MSI x2, University of Kentucky CCS Docs, and the non-PDF MSU RTSF page superseded above by its PDF).

## Trimmomatic

### GOOD (5)

#### USADELLAB - Trimmomatic Manual V0.32 (PDF)
- URL: http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf
- Keyword hits: 29
- What it contains: The tool's own official manual, from the maintainer's site (usadellab.org). Documents every trimming step (ILLUMINACLIP, SLIDINGWINDOW, LEADING/TRAILING, MINLEN, etc.) with syntax and usage examples for Illumina paired-end and single-end data.

```toml
[[html_sources]]
label = "USADELLAB - Trimmomatic Manual V0.32 (PDF)"
url = "http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf"
tool = "trimmomatic"
```

#### Ohio Supercomputer Center - Trimmomatic
- URL: https://www.osc.edu/resources/available_software/software_list/trimmomatic
- Keyword hits: 13
- What it contains: OSC's software page for Trimmomatic covering availability on their HPC systems, versioning, and how it fits into a typical NGS read-trimming workflow.

```toml
[[html_sources]]
label = "Ohio Supercomputer Center - Trimmomatic"
url = "https://www.osc.edu/resources/available_software/software_list/trimmomatic"
tool = "trimmomatic"
```

#### CyVerse - Trimmomatic Quick Start
- URL: https://cyverse-trimmomatic-quickstart.readthedocs-hosted.com/en/latest/
- Keyword hits: 18
- What it contains: A quickstart guide for running Trimmomatic through CyVerse's Discovery Environment: configuring sliding-window quality filtering and adapter removal, then validating results downstream with FastQC.

```toml
[[html_sources]]
label = "CyVerse - Trimmomatic Quick Start"
url = "https://cyverse-trimmomatic-quickstart.readthedocs-hosted.com/en/latest/"
tool = "trimmomatic"
```

#### Data Carpentry - Trimming and Filtering
- URL: https://datacarpentry.github.io/wrangling-genomics/03-trimming.html
- Keyword hits: 77
- What it contains: A full Data Carpentry genomics lesson on using Trimmomatic to filter poor-quality reads and trim poor-quality bases, with a detailed walkthrough of SLIDINGWINDOW, ILLUMINACLIP, MINLEN options and a complete paired-end command example.

```toml
[[html_sources]]
label = "Data Carpentry - Trimming and Filtering"
url = "https://datacarpentry.github.io/wrangling-genomics/03-trimming.html"
tool = "trimmomatic"
```

#### NIH HPC (Biowulf) - Trimmomatic
- URL: https://hpc.nih.gov/apps/trimmomatic.html
- Keyword hits: 33
- What it contains: NIH's Biowulf cluster documentation for Trimmomatic, covering the nine trimming operations it supports and how to run it interactively, as a batch job, or as a job swarm on their HPC system.

```toml
[[html_sources]]
label = "NIH HPC (Biowulf) - Trimmomatic"
url = "https://hpc.nih.gov/apps/trimmomatic.html"
tool = "trimmomatic"
```

### WEAK -- needs a human look (4)
- **USADELLAB - Trimmomatic** -- http://www.usadellab.org/cms/?page=trimmomatic
  Only 9 keyword hits. Official landing page for the tool but thinner than the PDF manual already proposed above; mostly links out rather than explaining usage in depth.
- **GitHub - usadellab/Trimmomatic** -- https://github.com/usadellab/Trimmomatic
  Only 8 keyword hits. Official repo, but the README is brief (build/install instructions) compared to the PDF manual.
- **UF RC - Trimmomatic** -- https://docs.rc.ufl.edu/software/apps/trimmomatic
  Only 2 keyword hits -- looked like a short module-load stub page.
- **Tufts HPC Bioinformatics - Trimmomatic** -- https://bioinformaticstuftshpc.readthedocs.io/en/latest/source/trimmomatic/trimmomatic.html
  Only 1 keyword hit -- appears to be mostly a SLURM job-script example with little surrounding explanation.

### Not usable
5 candidate(s) came back EMPTY or FAIL and aren't listed individually (PMACS HPC wiki, MSU ICER, Georgetown HPC, IBERS Aberystwyth wiki, and MSI -- all network errors, redirects, or JS-rendered pages with no extractable text).

## Cutadapt

### GOOD (4)

#### UT Austin Core NGS Tools - Pre-processing Raw Sequences
- URL: https://cloud.wikis.utexas.edu/wiki/spaces/CoreNGSTools/pages/54068284/2021+Pre-processing+raw+sequences
- Keyword hits: 112
- What it contains: A full course wiki page with a dedicated "Adapter trimming with cutadapt" section -- real cutadapt commands for R1/R2 GSAF RNA libraries, adapter-sequence selection by library type, batch-job setup, and reading cutadapt's log output. Also briefly covers FastQC and MultiQC as earlier steps in the same pipeline.

```toml
[[html_sources]]
label = "UT Austin Core NGS Tools - Pre-processing Raw Sequences"
url = "https://cloud.wikis.utexas.edu/wiki/spaces/CoreNGSTools/pages/54068284/2021+Pre-processing+raw+sequences"
tool = "cutadapt"
```

#### UNL HCC - cutadapt
- URL: https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/pre_processing_tools/cutadapt
- Keyword hits: 10
- What it contains: University of Nebraska-Lincoln's HPC docs for cutadapt: basic usage for 3'/5'/both-end adapter trimming, a SLURM batch script example, and notes on single-end vs paired-end support and cutadapt's summary statistics output.

```toml
[[html_sources]]
label = "UNL HCC - cutadapt"
url = "https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/pre_processing_tools/cutadapt"
tool = "cutadapt"
```

#### Emory Cores - MicroRNAseq Processing Pipeline (PDF)
- URL: https://www.cores.emory.edu/eicc/_includes/documents/sections/resources/miRNAseq_HRJ.pdf
- Keyword hits: 16
- What it contains: A short methods document describing a real miRNA-seq pipeline where Trimmomatic and cutadapt are used in tandem -- cutadapt specifically to strip a known miRNA adapter sequence before Trimmomatic removes remaining Illumina adapters. Cites the cutadapt paper directly.

```toml
[[html_sources]]
label = "Emory Cores - MicroRNAseq Processing Pipeline (PDF)"
url = "https://www.cores.emory.edu/eicc/_includes/documents/sections/resources/miRNAseq_HRJ.pdf"
tool = "cutadapt"
```

#### Augusta University HPC - cutadapt
- URL: https://auhpcs.augusta.edu/user-kb/applications/cutadapt.html
- Keyword hits: 9
- What it contains: Augusta University's HPC knowledge-base page describing cutadapt as a tool for finding/removing adapter, primer, and poly-A sequences from high-throughput reads, with module-load and run instructions for their cluster.

```toml
[[html_sources]]
label = "Augusta University HPC - cutadapt"
url = "https://auhpcs.augusta.edu/user-kb/applications/cutadapt.html"
tool = "cutadapt"
```

### WEAK -- needs a human look (3)
- **UT Austin BioITeam - FASTQ Manipulation Tools** -- https://cloud.wikis.utexas.edu/wiki/spaces/bioiteam/pages/47718686/FASTQ+Manipulation+Tools
  18 keyword hits, but the page is primarily about the FASTX-Toolkit; cutadapt only appears as one alternative-tool mention with a single example command near the end.
- **Cornell BioHPC - RNA-Seq Data Analysis Lecture 1 (PDF)** -- https://biohpc.cornell.edu/doc/RNA-Seq-2018-Lecture1.pdf
  74 keyword hits, but on inspection "Cutadapt" appears exactly once, in a bullet list alongside BBDuk and Trimmomatic as alternative trimming tools -- no substantive discussion of cutadapt itself. This is a broad RNA-seq lecture, not a cutadapt source.
- **GitHub - marcelm/cutadapt** -- https://github.com/marcelm/cutadapt/
  Only 1 keyword hit -- the README is real but uses cutadapt/genomics-specific vocabulary that doesn't overlap much with this domain's current keyword list (samtools/bwa/gatk/etc.), so it scores low despite being the tool's official repo. Worth a human look regardless of the low keyword score, since it's the canonical source.

### Not usable
5 candidate(s) came back EMPTY or FAIL and aren't listed individually: the Cutadapt readthedocs stable-docs homepage (JS-rendered, no extractable text), Georgetown HPC and MSU ICER cutadapt pages (JS-rendered), MSI (HTTP 302), and UF RC (only 1 hit / stub page, folded in here rather than WEAK since it had almost no content).

## MultiQC

### GOOD (2)

#### HBC Training (Harvard Chan Bioinformatics Core) - MultiQC Lesson
- URL: https://hbctraining.github.io/Intro-to-rnaseq-fasrc-salmon-flipped/lessons/11_multiQC.html
- Keyword hits: 17
- What it contains: A lesson from Harvard Chan Bioinformatics Core's RNA-seq training walking through running MultiQC on FastQC/STAR/Qualimap/Salmon outputs and interpreting the aggregated report's alignment rate, duplication, and contamination indicators.

```toml
[[html_sources]]
label = "HBC Training (Harvard Chan Bioinformatics Core) - MultiQC Lesson"
url = "https://hbctraining.github.io/Intro-to-rnaseq-fasrc-salmon-flipped/lessons/11_multiQC.html"
tool = "multiqc"
```

#### UT Austin BioITeam - Using MultiQC
- URL: https://cloud.wikis.utexas.edu/wiki/display/bioiteam/Using+MultiQC
- Keyword hits: 58
- What it contains: A workshop-style walkthrough of MultiQC: aggregating NGS QC reports from tools like FastQC, bowtie2, samtools flagstat/idxstats, and Picard into one consolidated interactive HTML report, including config-file customization.

```toml
[[html_sources]]
label = "UT Austin BioITeam - Using MultiQC"
url = "https://cloud.wikis.utexas.edu/wiki/display/bioiteam/Using+MultiQC"
tool = "multiqc"
```

### WEAK -- needs a human look (4)
- **GitHub - MultiQC/MultiQC** -- https://github.com/MultiQC/MultiQC
  Only 1 keyword hit -- the official repo, but its README emphasizes tool names (FastQC, Picard, DRAGEN, etc.) and general phrasing that barely overlaps this domain's current keyword list. Worth adding on merit despite the low score.
- **MultiQC Docs - Quick Start** -- https://multiqc.info/docs/getting_started/quick_start/
  Only 7 keyword hits. Official docs site, genuinely about MultiQC, just terse (install + first run) relative to the keyword list.
- **UIUC NCSA - MultiQC** -- https://docs.ncsa.illinois.edu/en/latest/software/bio/MultiQC.html
  Only 6 keyword hits -- a short module-load/version stub page.
- **Cornell BioHPC - MultiQC User Guide** -- https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=323
  Only 6 keyword hits -- brief software-catalog entry rather than a usage walkthrough.

### Not usable
3 candidate(s) came back EMPTY, FAIL, or were thin catalog pages and aren't listed individually: UF RC's MultiQC page (JS-rendered, no extractable text), TAMU HPRC (network error), and UT Austin's "2022 Core NGS Resources" page, which despite a high raw keyword count turned out on inspection to be a broad link-index page ("a healthy taste of resources ... not a comprehensive catalog") with only a one-line pointer to MultiQC -- exactly the thin-catalog trap called out in the task instructions, so it was excluded rather than proposed.

## Nothing was added automatically
This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py` were not touched.
