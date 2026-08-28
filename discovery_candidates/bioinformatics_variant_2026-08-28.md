# Discovered variant tool sources for bioinformatics -- 2026-08-28

## bcftools

### GOOD (4)

#### BCFtools GitHub
- URL: https://github.com/samtools/bcftools
- Keyword hits: 13
- What it contains: The official development repository README. Describes bcftools as containing the `vcf*` commands (vcfcheck, vcfmerge, vcfisec, etc.) migrated from htslib plus samtools' BCF calling code, links out to the full docs and format specs, and gives the canonical citation for the tool.

```toml
[[html_sources]]
label = "BCFtools GitHub"
url = "https://github.com/samtools/bcftools"
tool = "bcftools"
```

#### BCFtools Manual Page
- URL: https://samtools.github.io/bcftools/bcftools.html
- Keyword hits: 306
- What it contains: The full official `bcftools(1)` man page (147KB of text) -- name, synopsis, description of VCF/BCF stream handling, versioning notes, and detailed per-subcommand documentation. This is the primary reference manual for the tool.

```toml
[[html_sources]]
label = "BCFtools Manual Page"
url = "https://samtools.github.io/bcftools/bcftools.html"
tool = "bcftools"
```

#### Cornell BioHPC - Variant Calling Workshop Part 2 (PDF)
- URL: https://biohpc.cornell.edu/lab/doc/variant_workshop_part2.pdf
- Keyword hits: 184
- What it contains: A Cornell Bioinformatics Facility workshop slide deck on DNA-Seq variant-calling best practices -- duplicate-read handling with Picard MarkDuplicates, base quality recalibration, and downstream bcftools/GATK variant calling steps, with real command examples.

```toml
[[html_sources]]
label = "Cornell BioHPC - Variant Calling Workshop Part 2 (PDF)"
url = "https://biohpc.cornell.edu/lab/doc/variant_workshop_part2.pdf"
tool = "bcftools"
```

#### UConn Bioinformatics - Data Therapy Variants (PDF)
- URL: https://bioinformatics.uconn.edu/wp-content/uploads/sites/15/2018/03/DataTherapy_Variants_2018week04.pdf
- Keyword hits: 44
- What it contains: A UConn "Data Therapy" workshop slide deck covering SNP/indel variant calling concepts, pipeline concordance issues, and use of samtools mpileup piped into bcftools call to produce VCF/BCF output.

```toml
[[html_sources]]
label = "UConn Bioinformatics - Data Therapy Variants (PDF)"
url = "https://bioinformatics.uconn.edu/wp-content/uploads/sites/15/2018/03/DataTherapy_Variants_2018week04.pdf"
tool = "bcftools"
```

### WEAK -- needs a human look (3)
- **BCFtools HowTo - Variant Calling** -- https://samtools.github.io/bcftools/howtos/variant-calling.html
  Only 9 keyword hits. Official bcftools mpileup/call howto, but the page is short and terse -- worth a manual look before adding.
- **Tufts HPC Bioinformatics - BCFtools** -- https://bioinformaticstuftshpc.readthedocs.io/en/latest/source/bcftools/bcftools.html
  Only 6 keyword hits. Thin readthedocs stub page.
- **MSU ICER - BCFtools** -- https://docs.icer.msu.edu/available_software/detail/BCFtools
  Only 1 keyword hit. Looks like a bare module-availability listing with little else.

### Not usable
3 candidate(s) came back EMPTY or FAIL and aren't listed individually (UMD HPC - network error, LSU HPC - HTTP 404, UNT HPC - HTTP 404).

## Picard

### GOOD (5)

#### Picard Tools - Broad Institute
- URL: https://broadinstitute.github.io/picard/
- Keyword hits: 92
- What it contains: The official Picard homepage -- describes what Picard is (command-line tools for SAM/BAM/CRAM/VCF manipulation), licensing, and a full Quick Start with download, install, and Java-version setup instructions.

```toml
[[html_sources]]
label = "Picard Tools - Broad Institute"
url = "https://broadinstitute.github.io/picard/"
tool = "picard"
```

#### Picard - Tool Documentation Overview
- URL: http://broadinstitute.github.io/picard/command-line-overview.html
- Keyword hits: 189
- What it contains: The official command-line syntax reference (130KB) -- explains invocation syntax, JVM args, and lists/documents the individual tools (CollectAlignmentSummaryMetrics, BuildBamIndex, CreateSequenceDictionary, MarkDuplicates, SortSam, etc.) with options and usage recommendations.

```toml
[[html_sources]]
label = "Picard - Tool Documentation Overview"
url = "http://broadinstitute.github.io/picard/command-line-overview.html"
tool = "picard"
```

#### CSC Docs - Picard
- URL: https://docs.csc.fi/apps/picard/
- Keyword hits: 10
- What it contains: CSC (Finland) HPC center page describing Picard's purpose, license, which cluster versions are installed, and real module-load usage instructions (`module load picard`, `module load biokit`) including a note that Picard's own docs use `java -jar picard.jar` syntax.

```toml
[[html_sources]]
label = "CSC Docs - Picard"
url = "https://docs.csc.fi/apps/picard/"
tool = "picard"
```

#### QMUL - Intro to HPC Tutorials MSc Bioinformatics (PDF)
- URL: https://learn.hpc.qmul.ac.uk/assets/MSc_Bioinformatics.pdf
- Keyword hits: 13
- What it contains: A QMUL IT Services HPC-orientation tutorial packet for MSc Bioinformatics students -- covers SSH login, HPC basics, and bioinformatics-specific module usage on the QMUL cluster (relevant HPC onboarding material, not Picard-exclusive but substantive and on-topic).

```toml
[[html_sources]]
label = "QMUL - Intro to HPC Tutorials MSc Bioinformatics (PDF)"
url = "https://learn.hpc.qmul.ac.uk/assets/MSc_Bioinformatics.pdf"
tool = "picard"
```

#### GATK Broad - MarkDuplicates (Picard)
- URL: https://gatk.broadinstitute.org/hc/en-us/articles/360037052812-MarkDuplicates-Picard
- Keyword hits: 30
- What it contains: Broad Institute's official GATK-hosted documentation page for Picard's MarkDuplicates tool -- explains what duplicate reads are, how the tool identifies and tags them, and related options (BARCODE_TAG, EstimateLibraryComplexity).

```toml
[[html_sources]]
label = "GATK Broad - MarkDuplicates (Picard)"
url = "https://gatk.broadinstitute.org/hc/en-us/articles/360037052812-MarkDuplicates-Picard"
tool = "picard"
```

### WEAK -- needs a human look (5)
- **Picard GitHub** -- https://github.com/broadinstitute/picard
  Only 7 keyword hits. GitHub READMEs render thin for this scraper's fetcher; real content lives at the official docs site instead (already covered by GOOD entries above).
- **UF HPC - Picard** -- https://docs.rc.ufl.edu/software/apps/picard/
  Only 6 keyword hits. Likely a short module-usage page.
- **NIH HPC - Picard** -- https://hpc.nih.gov/apps/picard.html
  Only 3 keyword hits.
- **Tufts HPC Bioinformatics - Picard** -- https://bioinformaticstuftshpc.readthedocs.io/en/latest/source/picard/picard.html
  Only 2 keyword hits. Thin readthedocs stub, mirrors the Tufts bcftools page.
- **Ohio Supercomputer Center - Picard** -- https://www.osc.edu/book/export/html/4367
  Only 1 keyword hit.

### Not usable
4 candidate(s) came back EMPTY or FAIL and aren't listed individually (FSU RCC - no keyword matches/possibly JS-rendered, UPenn HPC Wiki - no extractable content, UMD HPC - network error, UKY CCS HPC - network error).

## VCFtools

### GOOD (5)

#### VCFtools GitHub
- URL: https://github.com/vcftools/vcftools
- Keyword hits: 17
- What it contains: The official repository README -- describes VCFtools as a Perl/C++ toolset for VCF files, gives build/install instructions (`./configure && make && make install`), credits, license, and links to the documentation and manual page.

```toml
[[html_sources]]
label = "VCFtools GitHub"
url = "https://github.com/vcftools/vcftools"
tool = "vcftools"
```

#### VCFtools Manual
- URL: https://vcftools.github.io/man_latest.html
- Keyword hits: 49
- What it contains: The full official VCFtools man page -- name, synopsis, description, and numerous concrete usage examples (allele frequency output, indel removal, site comparison between VCFs, Hardy-Weinberg p-values, nucleotide diversity). This is the primary reference manual.

```toml
[[html_sources]]
label = "VCFtools Manual"
url = "https://vcftools.github.io/man_latest.html"
tool = "vcftools"
```

#### QMUL HPC - VCFtools
- URL: https://docs.hpc.qmul.ac.uk/apps/bio/vcftools/
- Keyword hits: 29
- What it contains: QMUL's Apocrita cluster docs page for VCFtools -- module-load usage, a note on which subcommand (vcf-sort) supports multi-threading, and a full example SLURM batch script running a real vcftools variant-count command.

```toml
[[html_sources]]
label = "QMUL HPC - VCFtools"
url = "https://docs.hpc.qmul.ac.uk/apps/bio/vcftools/"
tool = "vcftools"
```

#### UF HPC - VCFtools
- URL: https://docs.rc.ufl.edu/software/apps/vcftools
- Keyword hits: 12
- What it contains: University of Florida HiPerGator docs page -- describes VCFtools' purpose, environment module variables, and a specific, non-generic gotcha (redirecting the `--temp` directory off the diskless `/tmp` to `/blue` scratch space) plus the citation.

```toml
[[html_sources]]
label = "UF HPC - VCFtools"
url = "https://docs.rc.ufl.edu/software/apps/vcftools"
tool = "vcftools"
```

#### Sheffield HPC - VCFtools
- URL: https://docs.hpc.shef.ac.uk/en/latest/stanage/software/stacks/el7-icelake-znver-stanage/Bio/VCFtools.html
- Keyword hits: 10
- What it contains: Sheffield's Stanage cluster software-stack page for VCFtools -- version/build info, module-load command, and its EasyBuild dependency chain (GCC, HTSlib, Perl, zlib). It is a short auto-generated module page rather than a full tutorial, but the content is real and on-topic.

```toml
[[html_sources]]
label = "Sheffield HPC - VCFtools"
url = "https://docs.hpc.shef.ac.uk/en/latest/stanage/software/stacks/el7-icelake-znver-stanage/Bio/VCFtools.html"
tool = "vcftools"
```

### WEAK -- needs a human look (2)
- **VCFtools - Official Site** -- https://vcftools.github.io/
  Only 8 keyword hits. Project homepage; most of the real content lives on the linked manual/examples pages (already covered by the GOOD manual entry above).
- **MSU ICER - VCFtools** -- https://docs.icer.msu.edu/available_software/detail/VCFtools
  Only 7 keyword hits. Likely a bare module-availability listing similar to the MSU BCFtools page above.

### Not usable
2 candidate(s) came back EMPTY or FAIL and aren't listed individually (UKY CCS HPC - network error, UGA GACRC "VCFtools Teaching" - HTTP 404).

## Nothing was added automatically
This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py` were not touched.
