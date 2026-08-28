# Discovered txt sources for gaussian -- 2026-08-28

First plain-text (.txt) pass for gaussian. Real, directly-linked .txt files with
substantive documentation are uncommon for this domain -- Gaussian16/G09 is closed-source
commercial software with no public README.txt of its own -- so this batch is narrower than
the HTML/PDF passes. Both GOOD candidates found come from the same source (the NBO project
at UW-Madison, which interfaces with Gaussian for natural bond orbital analysis) and are
genuine plain-text installation guides, not GitHub-rendered Markdown. Both verified by
fetching the real extracted text via `fetch_page_text` directly (not just the keyword
count) -- including the higher-scoring one, per the standing false-positive risk with this
domain's ambiguous keyword ("Gaussian" the stats term vs. the chemistry software); both are
unambiguously about the chemistry software.

## GOOD (2)

### NBO Wisconsin - INSTALL.gaussian (Gaussian-09 D.01/NBO6 Installation Guide)
- URL: https://nbo.chem.wisc.edu/INSTALL.gaussian
- Keyword hits: 28
- Verified: genuine plain-text (`text/plain`) installation guide for interfacing NBO6 with
  Gaussian-09 Revision D.01. Real content throughout -- describes G09's external program
  interface (Link 612), the gaunbo6/g09nbo6/nbo6 executables, and step-by-step install
  instructions. Unambiguously about the Gaussian quantum chemistry software, not the
  unrelated statistics sense of "Gaussian".

```toml
[[html_sources]]
label = "NBO Wisconsin - INSTALL.gaussian (Gaussian-09 D.01/NBO6 txt)"
url = "https://nbo.chem.wisc.edu/INSTALL.gaussian"
```

### NBO Wisconsin - INSTALL.g09c01 (Gaussian-09 C.01/NBO6 Installation Guide)
- URL: https://nbo.chem.wisc.edu/INSTALL.g09c01
- Keyword hits: 51 (highest of this batch -- verified genuine, not a false positive)
- Verified: genuine plain-text companion guide to the one above, covering the older G09
  pre-Rev.D interface (building an NBO6-compatible G09 executable from source). Same
  project, same author, real substantive install content -- confirmed on-topic despite
  scoring highest, which is exactly the pattern that has burned this project before, so it
  got the same direct-fetch scrutiny as the lower scorer.

```toml
[[html_sources]]
label = "NBO Wisconsin - INSTALL.g09c01 (Gaussian-09 C.01/NBO6 txt)"
url = "https://nbo.chem.wisc.edu/INSTALL.g09c01"
```

## WEAK -- needs a human look (0)

None found. Other txt-shaped leads either weren't real .txt files (GitHub-rendered .md
READMEs, e.g. several Gaussian16 utility-script repos) or turned out to be plain code (a
bash-functions file) rather than documentation prose, and weren't pursued further as
candidates.

## Not usable

No candidate came back EMPTY or FAIL in this batch -- both real .txt leads found were
GOOD.

## Nothing was added automatically

This file is a proposal only. `configs/gaussian.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a GOOD candidate, copy its TOML block above into
`configs/gaussian.toml`. Note that `presets.py` (the wizard's built-in seed file) isn't
kept in sync with `configs/*.toml` automatically in this repo -- if you want an accepted
source to also show up for future fresh wizard runs, add it there too.
