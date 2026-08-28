# Discovered PPTX sources for bioinformatics -- 2026-08-28

PPTX-focused pass for bioinformatics (domain-wide, not tool-scoped). Searched specifically
for raw `.pptx` files -- general bioinformatics/NGS workshop slides plus tool-specific
searches for samtools, bwa, gatk, and blast. As expected going in, real linkable `.pptx`
files are scarce for this domain too -- most bioinformatics cores (UC Davis, HBC, Melbourne
Bioinformatics, etc.) publish training material as HTML/Markdown sites or PDF, or host
slides on SlideShare, none of which yield a stable raw-`.pptx` URL. 3 real `.pptx` files
were found and checked; none are usable, though one is worth a note.

## GOOD (0)

No candidate scored >=10 keyword hits.

## WEAK -- needs a human look (1)

- **MIT S62.12 - Biological Processes (PPTX)** -- http://fab.cba.mit.edu/classes/S62.12/docs/biological_processes.pptx
  Real, cleanly-extracted deck (confirmed by fetching the actual text, not just the hit
  count) -- MIT Media Lab course MAS.S62 "FAB2", covering genetic switches, gene circuit
  design (the repressilator), and DNA origami. Only 7 keyword hits, and reading the slide
  text confirms it's a molecular/synthetic-biology course, not an HPC bioinformatics-tools
  resource -- no samtools, bwa, gatk, alignment, or sequencing-pipeline content anywhere in
  it. Real and thin *and* off-topic for this domain's HPC-tools focus; not recommended.

## Not usable

2 candidates could not be verified as usable:

- **Stanford CCSB - "Discovery of analysis-ready variants" (PPTX)** --
  https://ccsb.stanford.edu/content/dam/sm/ccsb/documents/education/ngs/2014-NGS-Nair.pptx
  This looked like the most promising find of the batch by title/context -- a 2014
  Stanford NGS-workshop deck on variant discovery, plausibly GATK-adjacent -- but the URL
  now returns HTTP 404. Real-world link rot (course page from 2014), not a code issue.
- **UW-Madison BMI826 - Cancer Bioinformatics Data Types and Resources (PPTX)** --
  https://www.biostat.wisc.edu/~gitter/BMI826-S15/slides/CancerBioinformatics_DataTypesResources_012215.pptx
  Consistently returns HTTP 202 with an empty response body (verified across 3 repeated
  direct requests) instead of the actual file -- looks like a server-side quirk blocking
  direct/non-browser fetches rather than a dead link, but no content could be retrieved
  either way.

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and
`gaussian_scraper/presets.py` were not touched. No candidate in this batch is recommended
for addition.
