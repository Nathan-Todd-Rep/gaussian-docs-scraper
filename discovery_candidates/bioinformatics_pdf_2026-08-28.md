# Discovered PDF sources for bioinformatics -- 2026-08-28

First PDF-focused discovery pass for bioinformatics, following the PDF support added this
session (verified for real against gaussian). All candidates below were verified twice: once
via `check_sources.py`'s keyword-hit count, and again by directly inspecting the actual
extracted text through `fetch_page_text` (not just trusting the count) -- unlike the earlier
HTML batches, every candidate here turned out to be genuinely substantial tutorial/workshop
material, not a stub. One (PKU BLAST guide) correctly came back EMPTY, likely a scanned/
image-only PDF with no embedded text layer.

## BWA / samtools (4, all verified genuine)

### Glasgow Uni - BWA Tutorial (PDF)
- URL: https://userweb.eng.gla.ac.uk/umer.ijaz/bioinformatics/BWA_tutorial.pdf
- Keyword hits: 50
- Verified: real step-by-step tutorial with actual shell commands (bwa index, bwa mem).

```toml
[[html_sources]]
label = "Glasgow Uni - BWA Tutorial (PDF)"
url = "https://userweb.eng.gla.ac.uk/umer.ijaz/bioinformatics/BWA_tutorial.pdf"
tool = "bwa"
```

### Evomics - Alignment Workshop 2022 (PDF)
- URL: https://evomics.org/wp-content/uploads/2022/05/Alignment-Workshop-2022.pdf
- Keyword hits: 44

```toml
[[html_sources]]
label = "Evomics - Alignment Workshop 2022 (PDF)"
url = "https://evomics.org/wp-content/uploads/2022/05/Alignment-Workshop-2022.pdf"
tool = "bwa"
```

### CRUK Bioinformatics - Sequence Alignment with BWA (PDF)
- URL: http://bioinformatics-core-shared-training.github.io/cruk-bioinf-sschool/Day1/Sequence%20Alignment_July2015_ShamithSamarajiwa.pdf
- Keyword hits: 40

```toml
[[html_sources]]
label = "CRUK Bioinformatics - Sequence Alignment with BWA (PDF)"
url = "http://bioinformatics-core-shared-training.github.io/cruk-bioinf-sschool/Day1/Sequence%20Alignment_July2015_ShamithSamarajiwa.pdf"
tool = "bwa"
```

### UBC MICB405 - BWA SAMtools BCFtools Tutorial (PDF)
- URL: https://educe-ubc.github.io/MICB405/slides/tutorials/samtools_bcftools.pdf
- Keyword hits: 29
- Verified: real course tutorial ("MICB405 - BIOINFORMATICS - 2021W-T1"), covers both tools.

```toml
[[html_sources]]
label = "UBC MICB405 - BWA SAMtools BCFtools Tutorial (PDF)"
url = "https://educe-ubc.github.io/MICB405/slides/tutorials/samtools_bcftools.pdf"
tool = "samtools"
```

## GATK (4, all verified genuine)

### UCLA QCB - GATK Primer (PDF)
- URL: https://qcb.ucla.edu/wp-content/uploads/sites/14/2016/03/GATKwr12-1-GATK_primer.pdf
- Keyword hits: 51
- Note: this PDF has a font-encoding quirk -- "ti" ligatures extract as ")" (e.g.
  "Introduc)on" instead of "Introduction"). Content is still substantively readable and a
  majority of lines extract cleanly; flagging so it's not mistaken for corruption.

```toml
[[html_sources]]
label = "UCLA QCB - GATK Primer (PDF)"
url = "https://qcb.ucla.edu/wp-content/uploads/sites/14/2016/03/GATKwr12-1-GATK_primer.pdf"
tool = "gatk"
```

### Cornell BioHPC - Variant Calling Exercise 1 (PDF)
- URL: https://biohpc.cornell.edu/lab/doc/Variant_exercise1.pdf
- Keyword hits: 78

```toml
[[html_sources]]
label = "Cornell BioHPC - Variant Calling Exercise 1 (PDF)"
url = "https://biohpc.cornell.edu/lab/doc/Variant_exercise1.pdf"
tool = "gatk"
```

### UCLA QCB - Variant Calling with GATK Winter2020 (PDF)
- URL: https://qcb.ucla.edu/wp-content/uploads/sites/14/2020/03/VariantCallingWithGATK_WINTER2020.pdf
- Keyword hits: 83

```toml
[[html_sources]]
label = "UCLA QCB - Variant Calling with GATK Winter2020 (PDF)"
url = "https://qcb.ucla.edu/wp-content/uploads/sites/14/2020/03/VariantCallingWithGATK_WINTER2020.pdf"
tool = "gatk"
```

### Evomics - Human Variant Calling Workshop (PDF)
- URL: https://evomics.org/wp-content/uploads/2020/01/Human-Variant-Calling-Workshop.pdf
- Keyword hits: 92
- Verified: real workshop material, "Cesky Krumlov, January 8, 2020", actual data-finding
  and command instructions.

```toml
[[html_sources]]
label = "Evomics - Human Variant Calling Workshop (PDF)"
url = "https://evomics.org/wp-content/uploads/2020/01/Human-Variant-Calling-Workshop.pdf"
tool = "gatk"
```

## BLAST (1 GOOD, 1 EMPTY)

### QIAGEN - BLAST Tips Tutorial (PDF)
- URL: https://resources.qiagenbioinformatics.com/tutorials/BLAST_tips.pdf
- Keyword hits: 80
- Verified: genuine tutorial content (vendor-published, not university, but substantively a
  real BLAST usage tutorial).

```toml
[[html_sources]]
label = "QIAGEN - BLAST Tips Tutorial (PDF)"
url = "https://resources.qiagenbioinformatics.com/tutorials/BLAST_tips.pdf"
tool = "blast"
```

PKU CBI - BLAST Guide (http://abc.cbi.pku.edu.cn/man/guide-blast.pdf) came back EMPTY --
likely a scanned/image-only PDF with no embedded text layer, the PDF equivalent of a
JS-rendered page. Not usable as-is.

## Domain-wide (4, all verified genuine)

### Cornell BioHPC - Lab and Linux Basics Workshop (PDF)
- URL: https://biohpc.cornell.edu/lab/doc/BioHPC_Lab_and_Linux_Basics.pdf
- Keyword hits: 67

```toml
[[html_sources]]
label = "Cornell BioHPC - Lab and Linux Basics Workshop (PDF)"
url = "https://biohpc.cornell.edu/lab/doc/BioHPC_Lab_and_Linux_Basics.pdf"
```

### Cornell BioHPC - Linux for Biologists (PDF)
- URL: https://biohpc.cornell.edu/lab/doc/Linux_workshop.pdf
- Keyword hits: 153
- Verified: real workshop material from Cornell's Bioinformatics Facility (CBSU).

```toml
[[html_sources]]
label = "Cornell BioHPC - Linux for Biologists (PDF)"
url = "https://biohpc.cornell.edu/lab/doc/Linux_workshop.pdf"
```

### Evomics - Genomics Tutorial 2019 (PDF)
- URL: https://files.evomics.org/2019/01/genomics_tutorial_2019.pdf
- Keyword hits: 374 (highest of this whole batch)
- Verified: real multi-week workshop tutorial. URL corrected to its canonical
  non-redirecting address (the originally-found evomics.org URL 308-redirects here);
  re-validated on the corrected URL before including it, same as the HPC2N Umea case from
  the earlier gaussian discovery run.

```toml
[[html_sources]]
label = "Evomics - Genomics Tutorial 2019 (PDF)"
url = "https://files.evomics.org/2019/01/genomics_tutorial_2019.pdf"
```

### CRUK Bioinformatics - Short Read Alignment Lecture (PDF)
- URL: https://bioinformatics-core-shared-training.github.io/cruk-autumn-school-2017/Introduction/SS_DB/Materials/Lectures/Lecture3_ShortRead_Alignment_SS.pdf
- Keyword hits: 81
- General alignment-tool lecture (covers multiple aligners), left untagged rather than
  tool-specific to bwa.

```toml
[[html_sources]]
label = "CRUK Bioinformatics - Short Read Alignment Lecture (PDF)"
url = "https://bioinformatics-core-shared-training.github.io/cruk-autumn-school-2017/Introduction/SS_DB/Materials/Lectures/Lecture3_ShortRead_Alignment_SS.pdf"
```

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a candidate, copy its TOML block above into
`configs/bioinformatics.toml`. Note that `presets.py` isn't kept in sync with `configs/*.toml`
automatically -- add accepted sources there too for consistency with future wizard runs.
