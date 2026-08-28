# Discovered US HPC center sources for gaussian -- 2026-08-28

Targeted pass for US HPC centers and national labs not already covered by prior gaussian
discovery runs. Dedup baseline was every URL already in `configs/gaussian.toml` plus every
URL mentioned (GOOD, WEAK, EMPTY, FAIL, or rejected) in the four prior
`discovery_candidates/gaussian_*.md` files. 33 new candidate URLs across ~30 institutions
were searched for and checked; several previously-covered institutions (Harvard, TACC, OSC,
U Florida, U Chicago, Yale, FSU, Utah CHPC, NC State, George Mason, William and Mary,
Delaware, HPC2N, GWDG) were deliberately skipped in favor of new ground: Ivy League and
other private research universities, UC/Big Ten/SEC/ACC public flagships, and national labs.

## GOOD (11)

### BYU Office of Research Computing - Gaussian16
- URL: https://rc.byu.edu/wiki/?page=Gaussian+16
- Keyword hits: 27
- What it contains: Genuine technical guidance covering module loading, mandatory AVX2 CPU
  feature requirements, single-node multi-core execution via `--cpus-per-task` (vs.
  multi-node Linda), and BYU's `gbatch` job-submission utility.

```toml
[[html_sources]]
label = "BYU Office of Research Computing - Gaussian16"
url = "https://rc.byu.edu/wiki/?page=Gaussian+16"
```

### CU Boulder Research Computing - Gaussian
- URL: https://curc.readthedocs.io/en/latest/software/gaussian.html
- Keyword hits: 29
- What it contains: Substantial documentation for running G16 on the Alpine and Blanca
  clusters -- shared-memory single-node jobs (up to 64 cores), multi-node Linda jobs, GPU
  acceleration on A100s, `GAUSS_SCRDIR` scratch-directory guidance, and sample SLURM scripts
  plus a test molecular input file.

```toml
[[html_sources]]
label = "CU Boulder Research Computing - Gaussian"
url = "https://curc.readthedocs.io/en/latest/software/gaussian.html"
```

### NDSU CCAST - Running Gaussian 16
- URL: https://kb.ndsu.edu/it/page.php?id=135576
- Keyword hits: 56
- What it contains: A full tutorial -- input-file/basis-set/model-chemistry setup, PBS
  submission for single- and multi-node jobs, memory/scratch guidance, multi-node scaling
  benchmarks, and a troubleshooting section for convergence and basis-set errors.

```toml
[[html_sources]]
label = "NDSU CCAST - Running Gaussian 16"
url = "https://kb.ndsu.edu/it/page.php?id=135576"
```

### Minnesota Supercomputing Institute - Gaussian
- URL: https://msi.umn.edu/our-resources/msi-software/gaussian
- Keyword hits: 53
- What it contains: Current (non-archived) MSI software page for Gaussian -- module loading,
  Slurm job-submission examples, access-request process, and version deprecation notices
  (g09.d01 to g09.e01, g03 to g16.b01). Supersedes the stale `www-archive.msi.umn.edu` page
  that came back EMPTY in the 2026-08-28 first-pass run.

```toml
[[html_sources]]
label = "Minnesota Supercomputing Institute - Gaussian"
url = "https://msi.umn.edu/our-resources/msi-software/gaussian"
```

### Purdue RCAC (Bell) - Gaussian
- URL: https://www.rcac.purdue.edu/knowledge/bell/run/examples/apps/gaussian
- Keyword hits: 51
- What it contains: Cluster-specific guide for the Bell cluster -- input-file preparation
  for a molecular optimization, job submission via Purdue's `subg16` wrapper script with
  SLURM node/core parameters, and monitoring/output retrieval. (Purdue's main gaussian16
  hub page and the Negishi/Scholar cluster-specific pages all 404'd; Bell's held up.)

```toml
[[html_sources]]
label = "Purdue RCAC (Bell) - Gaussian"
url = "https://www.rcac.purdue.edu/knowledge/bell/run/examples/apps/gaussian"
```

### Argonne National Laboratory CNM - Gaussian
- URL: https://wiki.anl.gov/cnm/HPC/Applications/Gaussian
- Keyword hits: 45
- What it contains: A genuine national-lab source -- detailed documentation for Gaussian on
  Argonne's Carbon cluster, covering module versions, PBS job-script templates, a
  custom `gauss-parse` output-parsing tool with usage examples, and an in-depth section on
  Linda parallelization (shared-memory vs. cross-node semantics, error-message
  interpretation). Verified by direct fetch through the repo's own fetcher (WebFetch itself
  hit an HTTP 403 on this URL, but the repo's `fetch_page_text` succeeded, matching what
  `check_sources.py` would see in real use).

```toml
[[html_sources]]
label = "Argonne National Laboratory CNM - Gaussian"
url = "https://wiki.anl.gov/cnm/HPC/Applications/Gaussian"
```

### UW-Madison Chemistry HPC - Gaussian
- URL: https://hpc.chem.wisc.edu/software/kestrel-software/gaussian/
- Keyword hits: 26
- What it contains: A distinct, substantive source from the same university as the existing
  NBO Wisconsin txt sources but a different group (Chemistry Dept HPC, not NBO project) --
  covers input-file structure, memory/processor specification, calculation types (energy,
  optimization, frequency, TS/QST2/QST3, IRC, NMR), and version differences between G09 and
  G16 (integral accuracy defaults, DFT grids, memory allocation).

```toml
[[html_sources]]
label = "UW-Madison Chemistry HPC - Gaussian"
url = "https://hpc.chem.wisc.edu/software/kestrel-software/gaussian/"
```

### NIH HPC (Biowulf) - Gaussian
- URL: https://hpc.nih.gov/apps/Gaussian.html
- Keyword hits: 37
- What it contains: A federal research-computing source (NIH's Biowulf cluster) -- covers
  interactive sessions, batch and swarm job submission, resource configuration (CPUs,
  memory, scratch disk), Linda-based distributed computing, and a troubleshooting table
  mapping cryptic Gaussian error messages to their causes.

```toml
[[html_sources]]
label = "NIH HPC (Biowulf) - Gaussian"
url = "https://hpc.nih.gov/apps/Gaussian.html"
```

### Oakland University HPC - Gaussian on Matilda
- URL: https://support.oakland.edu/TDClient/33/Support-Center/KB/PrintArticle?ID=257
- Keyword hits: 34
- What it contains: Genuine site-specific guidance for Gaussian on Oakland's Matilda HPC
  cluster -- CPU/GPU job configuration, the requirement that CPU counts in the job script
  match the Link 0 command in the input file, a note that multi-node MPI mode is unavailable
  due to licensing, and GPU affinity/node-configuration details (up to 4 GPUs/node).

```toml
[[html_sources]]
label = "Oakland University HPC - Gaussian on Matilda"
url = "https://support.oakland.edu/TDClient/33/Support-Center/KB/PrintArticle?ID=257"
```

### Kennesaw State CRC - Gaussian Quickstart
- URL: https://campus.kennesaw.edu/offices-services/research/centers-facilities/center-research-computing/resources/quickstart/gaussian.php
- Keyword hits: 19
- What it contains: Verified genuine but narrow -- VPN/SSH connection setup, module-based
  interactive execution, and a sample PBS job-script template. It is a real quickstart guide
  (not a stub repeating keywords), but thinner than the other GOOD candidates here; it links
  out to official Gaussian docs for anything beyond the basics.

```toml
[[html_sources]]
label = "Kennesaw State CRC - Gaussian Quickstart"
url = "https://campus.kennesaw.edu/offices-services/research/centers-facilities/center-research-computing/resources/quickstart/gaussian.php"
```

### University of Arizona HPC - Gaussian
- URL: https://hpcdocs.hpc.arizona.edu/software/popular_software/gaussian/
- Keyword hits: 12
- What it contains: Verified genuine but thin -- access-group requirements plus real,
  specific GPU guidance for Ocelote's P100 nodes (CPU-GPU affinity, memory allocation, and
  when GPUs help vs. don't for DFT jobs). No general usage examples or install notes; useful
  mainly as a site-specific supplement rather than a standalone tutorial.

```toml
[[html_sources]]
label = "University of Arizona HPC - Gaussian"
url = "https://hpcdocs.hpc.arizona.edu/software/popular_software/gaussian/"
```

## WEAK -- needs a human look (1)

- **Purdue RCAC - Computational Chemistry Catalog** -- https://docs.rcac.purdue.edu/software/chemistry_catalog/
  Only 4 keyword hits -- appears to be a catalog/index page listing several computational
  chemistry packages rather than a Gaussian-specific deep dive. Review before trusting.

## Excluded: wrong institution, not US (1)

- **"Michigan ARC Software Guide"** -- https://arc-software-guide.readthedocs.io/en/latest/apps/arc_gaussian.html
  This surfaced repeatedly under searches for "University of Michigan ARC" (both institutions
  use the acronym "ARC" for their research-computing program) but direct fetch confirms it is
  actually the **University of Oxford's** Advanced Research Computing / HTC cluster software
  guide (`arc.ox.ac.uk`), not Michigan's. Genuine, substantial Gaussian content (25 keyword
  hits) but out of scope for a US-HPC-centers pass -- not proposed. Michigan's actual ARC-TS
  Gaussian pages (`arc-ts.umich.edu/software/gaussian/`, `arc.umich.edu/software-item/gaussian/`,
  `documentation.its.umich.edu/arc-hpc/greatlakes/user-guide`) were also tried and all came
  back FAIL (network error or HTTP 403), so Michigan has no usable source in this batch.

## Not usable (17)

17 other candidates came back EMPTY or FAIL and aren't described individually:

- **EMPTY** (3): UCLA Hoffman2 (`hoffman2.idre.ucla.edu/gaussian/`, likely JS-rendered),
  Georgetown HPC (`hpc.georgetown.edu/software/gaussian`, likely JS-rendered), Old Dominion
  University (`wiki.hpc.odu.edu/Software/Gaussian`, likely JS-rendered).
- **FAIL -- HTTP 403** (4): Princeton Research Computing, UVA Research Computing, Michigan
  ARC-TS software-item page, Michigan Great Lakes user guide -- all likely block non-browser
  requests.
- **FAIL -- HTTP 404** (6): Purdue RCAC main gaussian16 hub page, Purdue RCAC Negishi guide,
  Purdue RCAC Scholar guide, University of Maryland GLUE HPCC, Alabama Supercomputer
  Authority, LSU HPC and LONI (both under `hpc.lsu.edu` / `hpc.loni.org`, both http and https
  tried) -- stale or restructured links.
- **FAIL -- network error** (5, each retried once): Georgia Tech PACE, Michigan ARC-TS
  software page, University of New Mexico CARC, USC HPC (Gaussian03 page), UConn Storrs HPC
  wiki, University of Missouri How2RunGAUSSIAN page.

## Nothing was added automatically

This file is a proposal only. `configs/gaussian.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a GOOD candidate, copy its TOML block above into
`configs/gaussian.toml`. Note that `presets.py` (the wizard's built-in seed file) isn't
kept in sync with `configs/*.toml` automatically in this repo -- if you want an accepted
source to also show up for future fresh wizard runs, add it there too.
