# Discovered PPTX sources for gaussian -- 2026-08-28

PPTX-focused pass for gaussian. Searched specifically for raw `.pptx` files (workshop/
course slides, HPC-center training decks) rather than HTML/PDF. As expected going in,
real linkable `.pptx` files for this domain are scarce -- most HPC centers and chemistry
departments publish slides as PDF or host them on SlideShare/SlideServe (which don't serve
a raw `.pptx` file at a stable URL, so they're not usable as `html_sources` entries).
4 real `.pptx`/`.ppt` files were found and checked; none are usable.

## GOOD (0; 1 additional GOOD-by-keyword-count verdict rejected as corrupted extraction)

### UNC Research Computing - Introduction to Gaussian and GaussView 2010 (PPT) -- REJECTED, corrupted extraction
- URL: https://help.rc.unc.edu/Assets/New_Course_Material/Research_Application/IntroductiontoGaussian_2010.ppt
- Keyword hits: 49 (highest of this batch)
- **Do not add.** This file is legacy binary PowerPoint 97-2003 format (`.ppt`, OLE
  compound-file magic bytes `D0 CF 11 E0`, server Content-Type
  `application/vnd.ms-powerpoint`) -- not OOXML `.pptx`. `gaussian_scraper/fetcher.py`
  only routes to `_extract_pptx_text` for a `.pptx` URL suffix or a
  `presentationml.presentation` content-type, so this legacy file falls through to the
  generic BeautifulSoup HTML-parsing branch instead. Fetching and reading the actual
  "extracted" text directly (via `fetch_page_text`) confirms it is pure binary noise --
  15,346 lines of garbled, mostly non-ASCII byte soup with no coherent sentences, e.g.:
  `????a/8?8????|:d?S??d???BE? ?s ?$??6( T???V/??*??$?2?;?Q??\FD???6??_bT???\^?? P?(QZ?UBY`.
  The 49 keyword "hits" are almost certainly coincidental ASCII substrings inside binary
  noise, not real slide content -- this is genuinely UNC's real Gaussian/GaussView
  training deck, but this repo's PPTX pipeline cannot read it because it's the wrong
  (legacy) binary format. Would need a legacy-`.ppt`-specific extractor to ever be usable;
  out of scope for the current PPTX support. No TOML block given.

## WEAK -- needs a human look (0)

No candidate scored 1-9 keyword hits; the other three real `.pptx` files found all came
back EMPTY (0 hits).

## Not usable

3 candidates came back EMPTY (fetched fine as real, valid `.pptx` files -- extraction
worked -- but scored zero keyword matches):

- **UMD Chem481 - Quantum Mechanics Intro (PPTX)** -- https://www2.chem.umd.edu/groups/alexander/chem481/quantum_mechanics/qm.pptx
  A general quantum-mechanics course deck, not about the Gaussian software.
- **Illinois Physics - Leggett LPK (PPTX)** -- https://people.physics.illinois.edu/Leggett/LPK.pptx
  A physics colloquium deck (Leggett), unrelated to computational chemistry software.
- **UCI ICS-90 Sandy (PPTX)** -- https://ics.uci.edu/~pattis/ICS-90/sandy.pptx
  An intro CS course deck, entirely unrelated.

These three are legitimate, fetchable `.pptx` files -- just off-topic for this domain, not
extraction failures.

## Nothing was added automatically

This file is a proposal only. `configs/gaussian.toml` and `gaussian_scraper/presets.py`
were not touched. No candidate in this batch is recommended for addition -- the one GOOD-
by-score result is a corrupted extraction of the wrong file format, not real content.
