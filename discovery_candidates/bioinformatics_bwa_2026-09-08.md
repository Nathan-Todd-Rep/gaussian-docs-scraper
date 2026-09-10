# Discovered bwa sources for bioinformatics -- 2026-09-08

Rotation note: bwa was the roster entry with the oldest previous proposal
(2026-08-27, vs. 2026-08-28 for gatk/blast/domain-wide and 2026-08-31 for
samtools), so it was selected for this run per the self-correcting rotation.

## GOOD (3)

### Minnesota Supercomputing Institute - BWA
- URL: https://msi.umn.edu/software/msi-software/bwa
- Keyword hits: 56

```toml
[[html_sources]]
label = "Minnesota Supercomputing Institute - BWA"
url = "https://msi.umn.edu/software/msi-software/bwa"
tool = "bwa"
```

### UT Austin BioITeam - Mapping with BWA
- URL: https://cloud.wikis.utexas.edu/wiki/display/bioiteam/Mapping+with+BWA
- Keyword hits: 16

Note: the original URL found in search (wikis.utexas.edu/...) 301-redirects to
this cloud.wikis.utexas.edu URL -- used the canonical target here. This is a
Confluence-hosted page; a naive fetch of the redirect target alone can return
only nav-menu text (a JS-rendered shell), but a browser-rendered check
confirmed the page itself carries a genuine hands-on lab (objectives, `bwa
index`/`bwa mem` commands for paired-end RNA-seq reads, full walkthrough) --
not a stub.

```toml
[[html_sources]]
label = "UT Austin BioITeam - Mapping with BWA"
url = "https://cloud.wikis.utexas.edu/wiki/display/bioiteam/Mapping+with+BWA"
tool = "bwa"
```

### UCLA Pellegrini Lab - SCP BWA Guide (PDF)
- URL: https://www.pellegrini.mcdb.ucla.edu/pellegrini/pellegrinilabscps/SCP-BWA_Final.pdf
- Keyword hits: 29

Verified by direct read: a genuine 2-page practical guide covering `bwa
index`, `bwa mem` for single-end/paired-end/interleaved reads, SAM-to-BAM
conversion with samtools, sorting, indexing, and interpreting `samtools
flagstat` output -- substantive, not a stub.

```toml
[[html_sources]]
label = "UCLA Pellegrini Lab - SCP BWA Guide (PDF)"
url = "https://www.pellegrini.mcdb.ucla.edu/pellegrini/pellegrinilabscps/SCP-BWA_Final.pdf"
tool = "bwa"
```

## WEAK -- needs a human look (3)

- **MSU ICER - BWA** -- https://docs.icer.msu.edu/available_software/detail/BWA
  only 7 keyword hit(s) -- review before trusting
- **Drexel URCF - BWA** -- https://docs.urcf.drexel.edu/software/installed/BWA/
  only 7 keyword hit(s) -- review before trusting
- **GeneCodes - Next-Generation Sequence Alignment Tutorial (PDF)** -- https://www.genecodes.com/sites/default/files/documents/Tutorials/Next%20Gen%20Sequence%20Alignment.pdf
  81 keyword hits, and verified by direct read to be a real, substantive
  tutorial -- but it's vendor documentation for a commercial GUI product
  (Gene Codes' "Sequencher"), walking through point-and-click steps to invoke
  BWA-MEM/GSNAP/Maq from within that app, rather than command-line BWA
  documentation in the style of this repo's existing sources. Flagging for a
  human call on whether GUI vendor tutorials fit the intended source tier.

## Not usable

5 candidate(s) came back EMPTY or FAIL (no usable content, or the page couldn't be
fetched) and aren't listed individually here: UFRC - BWA (no keyword matches,
possibly JS-rendered), UMD HPCC - BWA (network error), BWA SourceForge Manual
(HTTP 403), Broad Institute - Aligning NGS Reads with BWA / Heng Li PDF
(HTTP 403), UGA GACRC - BWA Teaching (HTTP 404).

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and
`gaussian_scraper/presets.py` were not touched. To accept a GOOD candidate, copy its TOML
block above into `configs/bioinformatics.toml`. Note that `presets.py` (the wizard's
built-in seed file) isn't kept in sync with `configs/*.toml` automatically in this repo --
if you want an accepted source to also show up for future fresh wizard runs, add it there
too.
