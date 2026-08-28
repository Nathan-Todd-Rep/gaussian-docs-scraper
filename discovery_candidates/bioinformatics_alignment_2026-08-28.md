# Discovered alignment tool sources for bioinformatics -- 2026-08-28

Covers three read aligners with no existing `tool` tag in `configs/bioinformatics.toml`:
Bowtie2, STAR, and HISAT2 (alongside the existing `bwa` tag). Checked against
`configs/bioinformatics.toml` and all existing `discovery_candidates/bioinformatics_*.md`
files -- no URL below duplicates anything already present in either place.

For each GOOD candidate, the extracted text was actually fetched and read (not just the
keyword-hit count) to rule out thin catalog stubs and off-topic pages. Two candidates that
scored a GOOD hit count were downgraded after reading their real content: OSC's software-list
pages (Bowtie2, STAR, and HISAT2 versions) are all one-line descriptions plus a `module load`
command with no substantive usage guidance, and the CCB JHU "HISAT" manual turned out to
document the HISAT1 predecessor tool, not HISAT2.

## Bowtie2

### GOOD (4)

#### Bowtie2 GitHub (BenLangmead)
- URL: https://github.com/BenLangmead/bowtie2
- Keyword hits: 16
- What it contains: The official Bowtie2 README -- describes the tool, memory footprint
  (~3.2GB for the human genome), install paths (Bioconda, Biocontainers, source), and
  worked command examples for indexing and aligning reads.

```toml
[[html_sources]]
label = "Bowtie2 GitHub (BenLangmead)"
url = "https://github.com/BenLangmead/bowtie2"
tool = "bowtie2"
```

#### Bowtie2 MANUAL (raw GitHub)
- URL: https://raw.githubusercontent.com/BenLangmead/bowtie2/master/MANUAL
- Keyword hits: 325
- What it contains: The full official Bowtie2 manual text -- end-to-end vs. local alignment
  modes, scoring, paired-end handling, `bowtie2-build` index construction, SAM output, and
  worked Lambda-phage examples including a SAMtools downstream step.

```toml
[[html_sources]]
label = "Bowtie2 MANUAL (raw GitHub)"
url = "https://raw.githubusercontent.com/BenLangmead/bowtie2/master/MANUAL"
tool = "bowtie2"
```

#### UGA GACRC - Bowtie2 Teaching
- URL: https://wiki.gacrc.uga.edu/wiki/Bowtie2-Teaching
- Keyword hits: 25
- What it contains: A university HPC cluster guide with installation notes, module-load
  instructions, a batch job submission template, and a complete reference of Bowtie2
  command-line options.

```toml
[[html_sources]]
label = "UGA GACRC - Bowtie2 Teaching"
url = "https://wiki.gacrc.uga.edu/wiki/Bowtie2-Teaching"
tool = "bowtie2"
```

#### UMN Biostat - Intro to Linux and Bowtie (PDF)
- URL: http://www.biostat.umn.edu/~cavanr/NGSlecture3pubh74452016.pdf
- Keyword hits: 48
- What it contains: A University of Minnesota biostatistics lecture PDF covering Linux
  basics plus a dedicated section walking through Bowtie/Bowtie2 and SAMtools usage for
  NGS read alignment.

```toml
[[html_sources]]
label = "UMN Biostat - Intro to Linux and Bowtie (PDF)"
url = "http://www.biostat.umn.edu/~cavanr/NGSlecture3pubh74452016.pdf"
tool = "bowtie2"
```

### WEAK -- needs a human look (6)

- **FSU RCC - Bowtie2** -- https://docs.rcc.fsu.edu/software/bowtie2/
  only 3 keyword hit(s) -- review before trusting
- **UF RC - Bowtie2** -- https://docs.rc.ufl.edu/software/apps/bowtie2/
  only 2 keyword hit(s) -- review before trusting
- **MSU ICER - Bowtie2** -- https://docs.icer.msu.edu/available_software/detail/Bowtie2/
  only 1 keyword hit(s) -- review before trusting
- **WVU HPC - Bowtie2** -- https://docs.hpc.wvu.edu/text/705.bowtie2.html
  only 6 keyword hit(s) -- review before trusting
- **Stony Brook RCI - Bowtie2** -- https://rci.stonybrook.edu/HPC/software/bowtie2
  only 4 keyword hit(s) -- review before trusting
- **OSC - Bowtie2** -- https://www.osc.edu/resources/available_software/software_list/bowtie2
  scored 14 keyword hits (would auto-qualify as GOOD) but reading the actual page shows it
  is a thin stub: a one-line description, a version list, and a single `module load`
  command -- no real usage content, so it is flagged here rather than recommended.

### Not usable

3 candidate(s) came back EMPTY or FAIL and aren't listed individually: Bowtie2 Official
Manual / sourceforge.net (HTTP 403), Kennesaw State HPC - Bowtie2 (HTTP 404), HPC@LSU -
Bowtie2 (HTTP 404).

## STAR

### GOOD (6)

#### STAR Manual source (raw GitHub .tex)
- URL: https://raw.githubusercontent.com/alexdobin/STAR/master/extras/doc-latex/STARmanual.tex
- Keyword hits: 132
- What it contains: The LaTeX source of the official STAR manual (v2.7.11b, Alexander
  Dobin) -- installation, genome indexing (`genomeGenerate`), read mapping workflows,
  output file formats, chimeric alignment detection, and STARsolo for scRNA-seq.

```toml
[[html_sources]]
label = "STAR Manual source (raw GitHub .tex)"
url = "https://raw.githubusercontent.com/alexdobin/STAR/master/extras/doc-latex/STARmanual.tex"
tool = "star"
```

#### Cornell Physiology - STAR Manual mirror (PDF)
- URL: https://physiology.med.cornell.edu/faculty/skrabanek/lab/angsd/lecture_notes/STARmanual.pdf
- Keyword hits: 342
- What it contains: A university-hosted mirror of the official rendered STAR manual PDF --
  same comprehensive coverage of genome indexing, mapping jobs, output files, and the full
  parameter reference.

```toml
[[html_sources]]
label = "Cornell Physiology - STAR Manual mirror (PDF)"
url = "https://physiology.med.cornell.edu/faculty/skrabanek/lab/angsd/lecture_notes/STARmanual.pdf"
tool = "star"
```

#### Harvard HBC Training - Alignment with STAR
- URL: https://hbctraining.github.io/Intro-to-rnaseq-hpc-O2/lessons/03_alignment.html
- Keyword hits: 46
- What it contains: A detailed HPC-course lesson explaining STAR's two-step seed-search /
  clustering-and-scoring alignment algorithm, MMPs, and hands-on commands for running STAR
  on an HPC cluster (O2/SLURM).

```toml
[[html_sources]]
label = "Harvard HBC Training - Alignment with STAR"
url = "https://hbctraining.github.io/Intro-to-rnaseq-hpc-O2/lessons/03_alignment.html"
tool = "star"
```

#### Cornell BioHPC - RNA-Seq Exercise 1: STAR/TopHat (PDF)
- URL: https://biohpc.cornell.edu/doc/RNA-Seq-2017-exercise1.pdf
- Keyword hits: 80
- What it contains: A hands-on Cornell BioHPC exercise walking through FastQC quality
  checks and read mapping with both TopHat and STAR, including working-directory setup and
  file inspection steps.

```toml
[[html_sources]]
label = "Cornell BioHPC - RNA-Seq Exercise 1: STAR/TopHat (PDF)"
url = "https://biohpc.cornell.edu/doc/RNA-Seq-2017-exercise1.pdf"
tool = "star"
```

#### Cornell BioHPC - RNA-Seq Exercise 2 (PDF)
- URL: https://biohpc.cornell.edu/doc/RNA-Seq-2017-exercise2.pdf
- Keyword hits: 28
- What it contains: A follow-on Cornell BioHPC exercise specifically on STAR: genome
  indexing with `--runMode genomeGenerate --sjdbOverhang`, then a batch script running
  `STAR --quantMode GeneCounts` across four RNA-seq FASTQ libraries.

```toml
[[html_sources]]
label = "Cornell BioHPC - RNA-Seq Exercise 2 (PDF)"
url = "https://biohpc.cornell.edu/doc/RNA-Seq-2017-exercise2.pdf"
tool = "star"
```

#### UCLA QCB - Intro to RNAseq Day 3 (PDF)
- URL: https://qcb.ucla.edu/wp-content/uploads/sites/14/2020/04/RNAseq1-day3.pdf
- Keyword hits: 29
- What it contains: A UCLA workshop slide deck on RNA-seq quantification (htseq-count,
  EdgeR) that includes a substantive aligner comparison section covering STAR (recommended,
  memory-intensive) and HISAT2 (Tophat2 successor, similar performance).

```toml
[[html_sources]]
label = "UCLA QCB - Intro to RNAseq Day 3 (PDF)"
url = "https://qcb.ucla.edu/wp-content/uploads/sites/14/2020/04/RNAseq1-day3.pdf"
tool = "star"
```

### WEAK -- needs a human look (3)

- **STAR GitHub (alexdobin)** -- https://github.com/alexdobin/STAR
  only 7 keyword hit(s) -- review before trusting (the README is STAR-specific and doesn't
  land many hits on the broader domain keyword list, but it is the tool's own official repo)
- **MSU ICER - STAR** -- https://docs.icer.msu.edu/available_software/detail/STAR
  only 1 keyword hit(s) -- review before trusting
- **OSC - STAR** -- https://www.osc.edu/resources/available_software/software_list/star
  scored 14 keyword hits (would auto-qualify as GOOD) but the actual page is a thin stub --
  one-line description, version list, `module load` command, and a link out to GitHub for
  "further reading." Flagged here rather than recommended.

### Not usable

4 candidate(s) came back EMPTY or FAIL and aren't listed individually: STAR Manual /
software.cqls.oregonstate.edu mirror (server returned an HTML error page instead of the
PDF), UFRC - STAR (no keyword matches, likely JS-rendered), UKY CCS - STAR (network error),
Cornell Chagall - STAR Manual mirror (network error).

## HISAT2

### GOOD (4)

#### HISAT2 GitHub (DaehwanKimLab)
- URL: https://github.com/DaehwanKimLab/hisat2
- Keyword hits: 27
- What it contains: The official HISAT2 README -- explains the Hierarchical Graph FM index
  (HGFM), install-from-source steps, and worked `hisat2-build` / `hisat2` command examples
  for both single-end and paired-end alignment.

```toml
[[html_sources]]
label = "HISAT2 GitHub (DaehwanKimLab)"
url = "https://github.com/DaehwanKimLab/hisat2"
tool = "hisat2"
```

#### HISAT2 MANUAL (raw GitHub)
- URL: https://raw.githubusercontent.com/DaehwanKimLab/hisat2/master/MANUAL
- Keyword hits: 182
- What it contains: The full official HISAT2 manual text -- hierarchical indexing design,
  `hisat2-build`/`hisat2-inspect` options, alignment strategies, SAM output, and getting-
  started examples including a paired-end walkthrough with downstream SAMtools/BCFtools use.

```toml
[[html_sources]]
label = "HISAT2 MANUAL (raw GitHub)"
url = "https://raw.githubusercontent.com/DaehwanKimLab/hisat2/master/MANUAL"
tool = "hisat2"
```

#### CU Boulder - HISAT2 Worksheet (PDF)
- URL: https://biodatasci.colorado.edu/static/sr2019/6_RNA-seq/6_worksheet_6.1_HISAT2.pdf
- Keyword hits: 51
- What it contains: A CU Boulder workshop worksheet with a full hands-on SLURM/sbatch
  walkthrough of building a HISAT2 index (`hisat2-build`) and mapping RNA-seq reads on an
  HPC cluster.

```toml
[[html_sources]]
label = "CU Boulder - HISAT2 Worksheet (PDF)"
url = "https://biodatasci.colorado.edu/static/sr2019/6_RNA-seq/6_worksheet_6.1_HISAT2.pdf"
tool = "hisat2"
```

#### UND Genomics Core - RNA-seq Alignment Workshop (PDF)
- URL: https://med.und.edu/research/genomics-core/_files/docs/workshop-2019-rnaseq-alignment-handson.pdf
- Keyword hits: 64
- What it contains: A University of North Dakota genomics-core workshop hands-on covering
  FastQC quality assessment and read alignment against a HISAT-indexed mouse genome
  reference, with full terminal command walkthroughs.

```toml
[[html_sources]]
label = "UND Genomics Core - RNA-seq Alignment Workshop (PDF)"
url = "https://med.und.edu/research/genomics-core/_files/docs/workshop-2019-rnaseq-alignment-handson.pdf"
tool = "hisat2"
```

### WEAK -- needs a human look (5)

- **MSI Minnesota - HISAT2** -- https://msi.umn.edu/our-resources/msi-software/hisat2
  only 7 keyword hit(s) -- review before trusting
- **MSU ICER - HISAT2** -- https://docs.icer.msu.edu/available_software/detail/HISAT2
  only 1 keyword hit(s) -- review before trusting
- **UF RC - HISAT2** -- https://docs.rc.ufl.edu/software/apps/hisat2
  only 2 keyword hit(s) -- review before trusting
- **OSC - HISAT2** -- https://www.osc.edu/resources/available_software/software_list/hisat2
  scored 14 keyword hits (would auto-qualify as GOOD) but is the same thin OSC stub pattern
  seen for Bowtie2 and STAR -- one-line description plus `module load` command only.
- **CCB JHU - "HISAT" Manual** -- https://ccb.jhu.edu/software/hisat/manual.shtml
  scored 131 keyword hits (would auto-qualify as GOOD) but reading the content shows this
  documents **HISAT (version 1)**, the predecessor tool, not HISAT2 -- it explicitly lists
  HISAT2 as a separate, related tool. Mistagging this as `tool = "hisat2"` would be
  inaccurate, so it needs a human decision (e.g. add it untagged, or tagged as a different
  tool, rather than as hisat2).

### Not usable

1 candidate(s) came back EMPTY or FAIL and aren't listed individually: HISAT2 Official
Manual / daehwankimlab.github.io (network error).

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a GOOD candidate, copy its TOML block above into
`configs/bioinformatics.toml`. Note that `presets.py` (the wizard's built-in seed file)
isn't kept in sync with `configs/*.toml` automatically in this repo -- if you want an
accepted source to also show up for future fresh wizard runs, add it there too.
