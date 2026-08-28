# Discovered quantification/assembly/utility tool sources for bioinformatics -- 2026-08-28

Checked against: `py check_sources.py --keywords "rna-seq,fastq,samtools,bwa,gatk,genome,variant-calling,ngs,vcf,alignment,bam,blast"`

Note: these six tools (RNA-seq quantifiers Salmon/kallisto/featureCounts, assembler SPAdes,
and general utilities BEDTools/IGV) skew away from the domain keyword list's alignment/variant
vocabulary, so GOOD counts run lower here than for samtools/bwa/gatk/blast. Every GOOD candidate
below was fetched and read (via the scraper's own `fetch_page_text`, or WebFetch for HTML pages)
to confirm it is genuinely substantive, not just keyword-dense.

## Salmon

### GOOD (4)

#### Salmon GitHub
- URL: https://github.com/COMBINE-lab/salmon
- Keyword hits: 10
- What it contains: The official COMBINE-lab README describing Salmon as a Rust-based, single-binary tool for transcript-level quantification from RNA-seq reads via selective alignment or sketch-based mapping, with pointers to downstream tools (tximport/tximeta).

```toml
[[html_sources]]
label = "Salmon GitHub"
url = "https://github.com/COMBINE-lab/salmon"
tool = "salmon"
```

#### Salmon ReadTheDocs Manual
- URL: https://salmon.readthedocs.io/en/latest/salmon.html
- Keyword hits: 144
- What it contains: The full official Salmon 1.12.0 manual -- covers mapping-based vs. alignment-based (BAM) quant modes, index preparation, the complete CLI option reference, bias-correction flags, library-type specification, and output formats.

```toml
[[html_sources]]
label = "Salmon ReadTheDocs Manual"
url = "https://salmon.readthedocs.io/en/latest/salmon.html"
tool = "salmon"
```

#### ANGUS Workshop - Salmon Quant Tutorial
- URL: https://angus.readthedocs.io/en/2019/salmon-quant.html
- Keyword hits: 13
- What it contains: A hands-on RNA-seq quantification walkthrough (UC Davis ANGUS workshop): installing Salmon via conda, quality-trimming reads, indexing a yeast transcriptome, and running quantification across multiple samples with bias-correction flags, plus an exercise on extracting mapping stats.

```toml
[[html_sources]]
label = "ANGUS Workshop - Salmon Quant Tutorial"
url = "https://angus.readthedocs.io/en/2019/salmon-quant.html"
tool = "salmon"
```

#### NYU Genomics Core - Salmon & kallisto
- URL: https://gencore.bio.nyu.edu/salmon-kallisto-rapid-transcript-quantification-for-rna-seq-data/
- Keyword hits: 18
- What it contains: An NYU CGSB core-facility guide comparing Salmon and kallisto's pseudoalignment approach against traditional alignment (Tophat+Cufflinks), with concrete commands for both tools run on NYU's Mercer cluster and guidance on feeding results into sleuth for differential expression.

```toml
[[html_sources]]
label = "NYU Genomics Core - Salmon & kallisto"
url = "https://gencore.bio.nyu.edu/salmon-kallisto-rapid-transcript-quantification-for-rna-seq-data/"
tool = "salmon"
```

### WEAK -- needs a human look (2)
- **Salmon Official Docs** -- https://combine-lab.github.io/salmon/ -- only 3 keyword hits; this is the project's marketing/landing page rather than the manual itself (the manual is the separate ReadTheDocs GOOD entry above), so it's largely redundant.
- **MSU ICER - Salmon** -- https://docs.icer.msu.edu/available_software/detail/Salmon -- only 1 keyword hit; looks like a thin module-catalog stub (name + module-load command) rather than substantive documentation.

### Not usable
1 candidate came back FAIL and isn't listed individually (OSC - Salmon, HTTP 403).

## kallisto

### GOOD (2)

#### kallisto GitHub
- URL: https://github.com/pachterlab/kallisto
- Keyword hits: 11
- What it contains: The official Pachter Lab README explaining kallisto's pseudoalignment method for RNA-seq quantification and its speed benchmark (30M human reads in under 3 minutes).

```toml
[[html_sources]]
label = "kallisto GitHub"
url = "https://github.com/pachterlab/kallisto"
tool = "kallisto"
```

#### kallisto Manual
- URL: https://pachterlab.github.io/kallisto/manual
- Keyword hits: 42
- What it contains: The official kallisto manual documenting installation and every subcommand (`index`, `quant`, `bus`, `h5dump`, `inspect`) with concrete CLI examples and parameter descriptions.

```toml
[[html_sources]]
label = "kallisto Manual"
url = "https://pachterlab.github.io/kallisto/manual"
tool = "kallisto"
```

### WEAK -- needs a human look (2)
- **UF Research Computing - kallisto** -- https://docs.rc.ufl.edu/software/apps/kallisto -- only 2 keyword hits; appears to be a brief module-environment-variable stub rather than usage documentation.
- **Arkansas HPC Wiki - kallisto** -- https://hpcwiki.uark.edu/doku.php?id=kallisto -- only 3 keyword hits; short wiki page, mostly install/module notes.

### Not usable
2 candidates came back FAIL and aren't listed individually (OSC - kallisto, HTTP 403; HPC@UMD - kallisto, network error -- retried once, failed again).

## featureCounts

### GOOD (1)

#### Rsubread/Subread Users Guide (PDF)
- URL: https://bioconductor.org/packages/release/bioc/vignettes/Rsubread/inst/doc/SubreadUsersGuide.pdf
- Keyword hits: 298
- What it contains: The official Bioconductor Rsubread/Subread User's Guide (16 April 2025 edition) -- the authoritative manual for the Subread package that ships featureCounts, covering the seed-and-vote alignment paradigm, indel/exon-junction/structural-variant detection, installation, and (later in the document) the featureCounts read-summarization workflow itself. Confirmed by direct extraction: opens with the real table of contents and author/citation info, not a stub.

```toml
[[html_sources]]
label = "Rsubread/Subread Users Guide (PDF)"
url = "https://bioconductor.org/packages/release/bioc/vignettes/Rsubread/inst/doc/SubreadUsersGuide.pdf"
tool = "featurecounts"
```

### WEAK -- needs a human look (4)
- **Subread GitHub** -- https://github.com/ShiLab-Bioinformatics/subread -- only 3 keyword hits; repo landing page is mostly code/file listing rather than prose documentation.
- **Purdue RCAC - Subread** -- https://www.rcac.purdue.edu/software/subread -- only 4 keyword hits; thin software-catalog entry.
- **Cornell BioHPC - featureCounts** -- https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=856 -- 8 keyword hits, just below the GOOD threshold; worth a look since it's close.
- **CU Boulder BioDataSci - featureCounts Worksheet (PDF)** -- https://biodatasci.colorado.edu/static/sr2023/07_counting_deseq/Day7_featurecounts_worksheet.pdf -- 6 keyword hits; a real workshop worksheet on featureCounts, but quantification-focused content naturally scores lower against this domain's alignment/variant-skewed keyword list -- flagged per the batch's guidance rather than discarded.

### Not usable
2 candidates came back FAIL and aren't listed individually (Subread official featureCounts page, HTTP 403; USF Research Computing - Subread, network error -- retried once, failed again).

## SPAdes

### GOOD (3)

#### SPAdes GitHub
- URL: https://github.com/ablab/spades
- Keyword hits: 13
- What it contains: The official ablab README describing SPAdes as an assembly toolkit for Illumina/IonTorrent data with PacBio/Nanopore hybrid support, and its specialized pipelines for bacterial genomes, metagenomes, transcriptomes, and viral genomes.

```toml
[[html_sources]]
label = "SPAdes GitHub"
url = "https://github.com/ablab/spades"
tool = "spades"
```

#### SPAdes Quick Start
- URL: https://ablab.github.io/spades/getting-started.html
- Keyword hits: 49
- What it contains: The official Quick Start page with concrete installation and command examples for paired-end and metagenome assembly, a rundown of assembly modes (isolate, single-cell, transcriptome), and links to standalone tools (k-mer counting, graph construction).

```toml
[[html_sources]]
label = "SPAdes Quick Start"
url = "https://ablab.github.io/spades/getting-started.html"
tool = "spades"
```

#### UT Austin BioITeam - SPAdes Genome Assembly Tutorial
- URL: https://cloud.wikis.utexas.edu/wiki/spaces/bioiteam/pages/47728891
- Keyword hits: 40
- What it contains: A structured hands-on GVA2023 course tutorial -- installing and self-testing SPAdes, a plasmid-assembly exercise on real data, a whole-genome simulated-data exercise, and evaluating/visualizing assembly output. Confirmed by direct extraction to be the real tutorial body, not just a navigation shell.

```toml
[[html_sources]]
label = "UT Austin BioITeam - SPAdes Genome Assembly Tutorial"
url = "https://cloud.wikis.utexas.edu/wiki/spaces/bioiteam/pages/47728891"
tool = "spades"
```

### WEAK -- needs a human look (2)
- **SPAdes Official Docs** -- https://ablab.github.io/spades/ -- only 2 keyword hits; this is the toolkit's landing page (the substantive content is the separate Quick Start GOOD entry above).
- **Arkansas HPC Wiki - SPAdes** -- https://hpcwiki.uark.edu/doku.php?id=spades -- only 1 keyword hit; thin wiki stub.

### Not usable
2 candidates came back EMPTY or FAIL and aren't listed individually (UF Research Computing - SPAdes, no keyword matches -- likely JS-rendered; Kennesaw State HPC - SPAdes, HTTP 404).

## BEDTools

### GOOD (3)

#### BEDTools Official Docs (ReadTheDocs)
- URL: https://bedtools.readthedocs.io/en/latest/content/overview.html
- Keyword hits: 65
- What it contains: The official bedtools v2.31.0 overview -- background/motivation, a table of 40+ bundled tools, and core concepts (coordinate systems, BED/GFF/VCF/BAM formats, piping conventions).

```toml
[[html_sources]]
label = "BEDTools Official Docs (ReadTheDocs)"
url = "https://bedtools.readthedocs.io/en/latest/content/overview.html"
tool = "bedtools"
```

#### UT Austin BioITeam - BEDTools Tutorial
- URL: https://wikis.utexas.edu/display/bioiteam/Bedtools+tutorial+--+GVA2020
- Keyword hits: 22
- What it contains: A hands-on GVA2020 course tutorial comparing the results of different read mappers using `bedtools intersect` (common regions) and `bedtools subtract` (differential comparison), with a version-control checkpoint and worked evaluation steps. Confirmed genuine by direct extraction of the real tutorial outline.

```toml
[[html_sources]]
label = "UT Austin BioITeam - BEDTools Tutorial"
url = "https://wikis.utexas.edu/display/bioiteam/Bedtools+tutorial+--+GVA2020"
tool = "bedtools"
```

#### UVA BIOL4230 - BEDTools Lecture (PDF)
- URL: https://fasta.bioch.virginia.edu/biol4230/lects/biol4230_29_BedTools.pdf
- Keyword hits: 46
- What it contains: University of Virginia course lecture slides (Bill Pearson, Biol4230) on "BEDTools - Genome Arithmetic" -- genome file formats, the UCSC binning algorithm, and intersection/window operations, citing Quinlan's own BEDTools paper and docs. Confirmed by direct extraction to be real slide content, not a stub.

```toml
[[html_sources]]
label = "UVA BIOL4230 - BEDTools Lecture (PDF)"
url = "https://fasta.bioch.virginia.edu/biol4230/lects/biol4230_29_BedTools.pdf"
tool = "bedtools"
```

### WEAK -- needs a human look (3)
- **BEDTools2 GitHub** -- https://github.com/arq5x/bedtools2 -- 7 keyword hits, just below the GOOD threshold; the Quinlan lab's own repo, worth a look since it's close.
- **FSU RCC - BEDTools** -- https://docs.rcc.fsu.edu/software/bedtools/ -- only 4 keyword hits; brief module-usage page.
- **UF Research Computing - BEDTools** -- https://docs.rc.ufl.edu/software/apps/bedtools -- only 6 keyword hits; brief module-usage page.

### Not usable
1 candidate came back FAIL and isn't listed individually (Georgia Tech PACE - BEDTools, network error -- retried once, failed again).

## IGV

### GOOD (2)

#### UT Austin BioITeam - IGV Tutorial
- URL: https://wikis.utexas.edu/display/bioiteam/Integrative+Genomics+Viewer+(IGV)+tutorial
- Keyword hits: 29
- What it contains: A hands-on BioITeam course tutorial covering creating/loading a reference genome in IGV, loading read-mapping output, loading variant-calling output, and navigating the genome view. Confirmed genuine by direct extraction of the tutorial's actual learning-objectives text.

```toml
[[html_sources]]
label = "UT Austin BioITeam - IGV Tutorial"
url = "https://wikis.utexas.edu/display/bioiteam/Integrative+Genomics+Viewer+(IGV)+tutorial"
tool = "igv"
```

#### RNA-Bio (Broad Institute) - IGV Tutorial (PDF)
- URL: https://rnabio.org/assets/module_2/IGV_Tutorial_Long_BroadInstitute.pdf
- Keyword hits: 140
- What it contains: The Broad Institute's own "Introduction to NGS Visualization with IGV" workshop slide deck -- launching IGV, selecting a reference genome, loading data from local/remote/cloud sources, and a hands-on exercise loading ENCODE UI-basics tutorial data. Confirmed by direct extraction to be the real slide content.

```toml
[[html_sources]]
label = "RNA-Bio (Broad Institute) - IGV Tutorial (PDF)"
url = "https://rnabio.org/assets/module_2/IGV_Tutorial_Long_BroadInstitute.pdf"
tool = "igv"
```

### WEAK -- needs a human look (3)
- **IGV GitHub** -- https://github.com/igvteam/igv -- only 2 keyword hits; a visualization-tool README naturally scores low against this domain's alignment/variant vocabulary, but it is the genuine official repo.
- **IGV Official Site** -- https://igv.org/ -- only 1 keyword hit; marketing/landing page.
- **UF Research Computing - IGV** -- https://docs.rc.ufl.edu/software/apps/igv/ -- only 1 keyword hit; brief module-usage stub.

### Not usable
2 candidates came back FAIL and aren't listed individually (HPC@UMD - IGV, network error -- retried once, failed again; Minnesota Supercomputing Institute - IGV, HTTP 302 redirect not followed).

## Nothing was added automatically
This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py` were not touched.
