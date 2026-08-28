# Discovered Asia-Pacific / rest-of-world HPC center sources for gaussian -- 2026-08-28

## GOOD (9)

### NCI Australia (Gadi) - Gaussian 09
- URL: https://opus.nci.org.au/spaces/Help/pages/248840500/Gaussian+09...
- Keyword hits: 17
- What it contains: NCI's official Gadi supercomputer guide for Gaussian 09 -- `module load gaussian/g09e01`, a full PBS job script (48 CPUs, 12 GiB memory, 200 GiB scratch), and detailed notes on `%mem`/`%NprocShared`/`Maxdisk` equivalencies and PBS memory overhead. Authored by NCI HPC staff (Yue Sun, Mohsin Ali, Rika Kobayashi).

```toml
[[html_sources]]
label = "NCI Australia (Gadi) - Gaussian 09"
url = "https://opus.nci.org.au/spaces/Help/pages/248840500/Gaussian+09..."
```

### NUS Singapore - Gaussian
- URL: https://nusit.nus.edu.sg/hpc/application-software/gaussian
- Keyword hits: n/a (blocked -- see note)
- What it contains: NUS IT's HPC application-software page states Gaussian 16 Rev. A.03 is available across NUS HPC clusters, submitted via PBS Pro, with scratch folders auto-generated per job. Content confirmed by reading Google's cached snippet and search excerpts; the live page returns HTTP 403 to this repo's fetcher (likely bot/user-agent blocking), so it is listed here for a human to verify manually rather than under GOOD-and-verified. Moved to WEAK below out of caution.

### ACENET (Digital Research Alliance of Canada, Atlantic Canada) - Gaussian Training Session
- URL: https://acenet-arc.github.io/gaussian_training/Gaussian_training_session.html
- Keyword hits: 87
- What it contains: A full ACENET training session on Gaussian covering shared-memory (not Linda) parallelism, `#SBATCH` job scripts, `%mem`/`%NProcS` memory-per-process estimation rules, and `freqmem` resource-estimation guidance for Compute Canada's Graham/Cedar clusters.

```toml
[[html_sources]]
label = "ACENET Canada - Gaussian Training Session"
url = "https://acenet-arc.github.io/gaussian_training/Gaussian_training_session.html"
```

### KISTI Korea (Nurion) - Gaussian16
- URL: https://docs-ksc.gitbook.io/nurion-user-guide-eng/software/gaussian16
- Keyword hits: 51
- What it contains: KISTI's official English-language user guide for Gaussian16 on the Nurion supercomputer -- `module load gaussian/g16.a03`, mandatory PBS Pro submission (`#PBS -A gaussian`) from the scratch directory, `GAUSS_PDEF` core-count guidance for KNL (68 cores) vs SKL (40 cores) nodes, and Gaussian-group access-control requirements.

```toml
[[html_sources]]
label = "KISTI Korea (Nurion) - Gaussian16"
url = "https://docs-ksc.gitbook.io/nurion-user-guide-eng/software/gaussian16"
```

### KISTI Korea (Nurion) - Gaussian16 LINDA
- URL: https://docs-ksc.gitbook.io/nurion-user-guide-eng/software/gaussian16-linda
- Keyword hits: 50
- What it contains: Companion KISTI page covering multi-node LINDA-parallel Gaussian16 execution on Nurion, including PBS job scripts and LINDA-specific worker configuration.

```toml
[[html_sources]]
label = "KISTI Korea (Nurion) - Gaussian16 LINDA"
url = "https://docs-ksc.gitbook.io/nurion-user-guide-eng/software/gaussian16-linda"
```

### NeSI New Zealand - Gaussian
- URL: https://docs.nesi.org.nz/Software/Available_Applications/Gaussian/
- Keyword hits: 76
- What it contains: New Zealand eScience Infrastructure's official Gaussian page for the Mahuika cluster -- licence/access-group policy, a full `#SBATCH` shared-memory job script noting Gaussian uses twice the requested `--cpus-per-task`, and memory-overhead guidance (2 GB base + 2 GB buffer minimum).

```toml
[[html_sources]]
label = "NeSI New Zealand - Gaussian"
url = "https://docs.nesi.org.nz/Software/Available_Applications/Gaussian/"
```

### CHPC South Africa - Gaussian
- URL: https://wiki.chpc.ac.za/howto:gaussian
- Keyword hits: 13
- What it contains: South Africa's national Centre for High Performance Computing howto page -- loading `chpc/easy_scripts` and using pre-built `qg09_E01`/`qg16_A03` submission scripts that automate multi-node LINDA setup, checkpoint-file (.chk) restart guidance, and geometry-validation tips. Introductory but genuine, CHPC-specific operational content.

```toml
[[html_sources]]
label = "CHPC South Africa - Gaussian"
url = "https://wiki.chpc.ac.za/howto:gaussian"
```

### University of Calgary ARC - Gaussian
- URL: https://rcs.ucalgary.ca/Gaussian_on_ARC
- Keyword hits: 78
- What it contains: University of Calgary Research Computing Services' full Gaussian 16 guide for the ARC cluster -- site-license/access-request process, module usage, input/output file conventions, multi-node execution via TCP Linda on the Skylake `cpu2019` partition, and a GPU section.

```toml
[[html_sources]]
label = "University of Calgary ARC - Gaussian"
url = "https://rcs.ucalgary.ca/Gaussian_on_ARC"
```

### SHARCNET Canada - Gaussian16 and NBO7 on Graham and Cedar (PDF slides)
- URL: https://helpwiki.sharcnet.ca/wiki/images/6/68/Gaussian16_NBO7.pdf
- Keyword hits: 72
- What it contains: Jemmy Hu's (SHARCNET/Compute Canada) 2022 seminar slides -- `module spider gaussian`, a complete `#SBATCH` script (`--mem`, `--cpus-per-task`, `%nproc`/`%mem` correspondence), interactive `salloc` usage, and sample Gaussian input decks for serial and 16-CPU parallel jobs on Graham/Cedar.

```toml
[[html_sources]]
label = "SHARCNET Canada - Gaussian16 NBO7 Slides (PDF)"
url = "https://helpwiki.sharcnet.ca/wiki/images/6/68/Gaussian16_NBO7.pdf"
```

## WEAK -- needs a human look (6)
- **NUS Singapore - Gaussian** -- https://nusit.nus.edu.sg/hpc/application-software/gaussian
  Returns HTTP 403 to this repo's fetcher (bot/user-agent blocking), so it could not be scored by `check_sources.py`. Search-result excerpts strongly suggest substantive content (Gaussian 16 Rev. A.03, PBS Pro submission, scratch-folder handling) but a human should verify by opening it in a browser before adding.
- **SHARCNET Canada - Gaussian Usage Tutorial (PDF), 2010** -- https://staff.sharcnet.ca/jemmyhu/tutorials/Gaussian_SHARCNET.pdf
  Scored GOOD (22 hits) and content is genuine (`sqsub` job examples, `%nproc`/`%mem`, scaling benchmarks), but it's dated November 2010 and references long-decommissioned clusters (orca/whale/saw). Kept out of the GOOD list because the operational commands (sqsub, not sbatch) no longer match SHARCNET's current Slurm-based systems -- a human should judge whether historical value outweighs staleness.
- **SHARCNET Canada - Gaussian16/NBO7 Webinar announcement** -- https://helpwiki.sharcnet.ca/wiki/Webinar_2022_Gaussian16_and_NBO7_on_Graham_and_Cedar
  Only 3 keyword hits -- this is a thin webinar-announcement stub, not the actual slide content (the real content is the separate PDF listed above under GOOD).
- **SHARCNET Canada - Computational Chemistry Webinar 2018** -- https://helpwiki.sharcnet.ca/wiki/Webinar_2018_Using_Computational_Chemistry_software_effectively_on_Graham
  Only 4 keyword hits -- another thin webinar-announcement stub rather than substantive documentation.
- **IIT Kanpur - HPC2013 Instructions (PDF)** -- https://iitk.ac.in/cc/images/HPC/hpc2013.pdf
  Only 1 keyword hit -- a general legacy HPC-cluster instructions document with a single passing mention of a `submitLinda` script for Gaussian; not focused documentation.
- **IISc SERC India - Gaussian install guide** -- https://www.serc.iisc.ac.in/software/gaussian/
  Fetch failed with a TLS "self-signed certificate in certificate chain" error, both via this repo's fetcher and via a separate fetch tool. The site's certificate configuration appears broken; worth a human recheck later but not usable as-is.

## Not usable (4)
4 candidate(s) came back EMPTY or FAIL and aren't listed individually: the Digital Research Alliance of Canada wiki (`docs.alliancecan.ca/wiki/Gaussian`, blocked by a bot-detection service returning an "Access Denied" page to automated fetchers), the University of Melbourne Spartan modules page (`dashboard.hpc.unimelb.edu.au/software/modules/`, a JS-rendered/generic module list with no extractable Gaussian-specific text), the University of Manitoba Grex guide (`monitor.hpc.umanitoba.ca/...`, connection refused), and the ACENET wiki (`wiki.ace-net.ca/wiki/Gaussian`, HTTP 404 -- page appears to have moved or been retired; its content is superseded by the ACENET Gaussian Training Session listed under GOOD).

## Nothing was added automatically
This file is a proposal only. `configs/gaussian.toml` and `gaussian_scraper/presets.py` were not touched.
