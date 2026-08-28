# Discovered PDF sources for gaussian -- 2026-08-28

Follow-up PDF pass for gaussian, more thorough than the first (3 candidates) -- this one
covers 11 candidates from manuals, lab exercises, and university tutorial series found
during PDF research. All GOOD candidates verified by inspecting real extracted text
directly (not just the keyword count).

## GOOD (7, all confirmed on-topic and substantial; 1 additional GOOD verdict rejected as a false positive)

### UBA - GaussView/Gaussian Guide and Exercise Manual (PDF)
- URL: http://users.df.uba.ar/rboc/em3/GAUSSIAN_TRAIN.pdf
- Keyword hits: 16
- Verified: genuine student-facing guide to GaussView/Gaussian's principal features.

```toml
[[html_sources]]
label = "UBA - GaussView/Gaussian Guide and Exercise Manual (PDF)"
url = "http://users.df.uba.ar/rboc/em3/GAUSSIAN_TRAIN.pdf"
```

### Tel Aviv Uni - Gaussian Manual (PDF)
- URL: https://www.tau.ac.il/~ephraim/Gaussian_manual.pdf
- Keyword hits: 51
- Verified: real lab manual, "Introduction to Gaussian program," covers predicting
  molecular energies/structures.

```toml
[[html_sources]]
label = "Tel Aviv Uni - Gaussian Manual (PDF)"
url = "https://www.tau.ac.il/~ephraim/Gaussian_manual.pdf"
```

### Illinois Pogorelov Lab - Gaussian Intro Tutorial (PDF)
- URL: http://pogorelov.scs.illinois.edu/wp-content/uploads/2020/06/qm-gaussian-intro-1-tutorial-PogorelovLab.2011.v1.web_.pdf
- Keyword hits: 24
- Verified: genuine tutorial part 1, single point energy / molecular orbital calculations.

```toml
[[html_sources]]
label = "Illinois Pogorelov Lab - Gaussian Intro Tutorial (PDF)"
url = "http://pogorelov.scs.illinois.edu/wp-content/uploads/2020/06/qm-gaussian-intro-1-tutorial-PogorelovLab.2011.v1.web_.pdf"
```

### Illinois SCS - Gaussian Intro 2 (PDF)
- URL: https://scs.illinois.edu/system/files/inline-files/gaussian-intro-2.pdf
- Keyword hits: 26
- Verified: this is Part 2 of the same Pogorelov Lab tutorial series above -- geometry
  optimization, continuing directly from Part 1.

```toml
[[html_sources]]
label = "Illinois SCS - Gaussian Intro 2 (PDF)"
url = "https://scs.illinois.edu/system/files/inline-files/gaussian-intro-2.pdf"
```

### Texas A&M - Computational Chemistry Handout (PDF)
- URL: https://www.chem.tamu.edu/class/majors/chem101h-lab/chem/Computational%20Chemistry%20Handout%20-%202016.pdf
- Keyword hits: 35
- Verified: real course handout, "Computational Chemistry Experiment," Texas A&M chem101h lab.

```toml
[[html_sources]]
label = "Texas A&M - Computational Chemistry Handout (PDF)"
url = "https://www.chem.tamu.edu/class/majors/chem101h-lab/chem/Computational%20Chemistry%20Handout%20-%202016.pdf"
```

### UW Faculty - Computational Chemistry Tutorial (PDF)
- URL: https://faculty.washington.edu/tingcao/wordpress/wp-content/uploads/2020/05/Comp_Chem_Tutorial__Spr2020.pdf
- Keyword hits: 11
- Verified: real workshop material with named instructors and TAs (UW, Spring 2020).

```toml
[[html_sources]]
label = "UW Faculty - Computational Chemistry Tutorial (PDF)"
url = "https://faculty.washington.edu/tingcao/wordpress/wp-content/uploads/2020/05/Comp_Chem_Tutorial__Spr2020.pdf"
```

### Illinois SCS - Gaussian GaussView Tutorial (PDF)
- URL: https://scs.illinois.edu/system/files/inline-files/SCS-Gaussian-GaussView-tutorial_1.pdf
- Keyword hits: 17
- Verified genuine, though this PDF has the same kind of font-ligature extraction quirk
  seen in the UCLA GATK Primer (extra tabs/spaces around syllables) -- still readable and
  substantively about Gaussian/GaussView usage.

```toml
[[html_sources]]
label = "Illinois SCS - Gaussian GaussView Tutorial (PDF)"
url = "https://scs.illinois.edu/system/files/inline-files/SCS-Gaussian-GaussView-tutorial_1.pdf"
```

### UMD Math - GAUSSIAN User's Manual (PDF) -- REJECTED, false positive
- URL: https://www.math.umd.edu/~bnk/bak/SOURCE/manual.pdf
- Keyword hits: 100 (highest of this whole batch)
- Verified by direct fetch: **this is a different "Gaussian" entirely.** It's a C library
  manual for generating stationary Gaussian random fields over regular grids (a statistics/
  numerical-methods tool), not the Gaussian quantum chemistry software. The 100 keyword
  hits came from "Gaussian" appearing constantly in an off-topic context -- a genuinely new
  false-positive pattern for this project (name collision, not thinness). Do not add.

## Not usable

UT Dallas - Computational Chemistry (PDF) came back EMPTY (likely serving an HTML error
page instead of a real PDF, or JS-rendered). LSU HPC Training (HTTP 404) and UMN GaussView
Intro (network error) both FAILed -- real-world link rot, not code issues.

## Nothing was added automatically

This file is a proposal only. `configs/gaussian.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a candidate, copy its TOML block above into
`configs/gaussian.toml`. Note that `presets.py` isn't kept in sync with `configs/*.toml`
automatically -- add accepted sources there too for consistency with future wizard runs.
