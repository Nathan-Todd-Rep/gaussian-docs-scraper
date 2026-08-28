# Discovered European HPC center sources for gaussian -- 2026-08-28

Large discovery push targeting European national and university HPC centers not already
covered by `configs/gaussian.toml` or any prior `discovery_candidates/gaussian_*.md` file
(existing European coverage before this run: NSC Sweden, CSC Finland, GWDG Germany, and
HPC2N Umea Sweden). Searched across the UK, Germany, France, Italy, Switzerland, Ireland,
the Nordics, and Central/Eastern Europe. All GOOD candidates below were verified by reading
the actual extracted text (via this repo's own `fetch_page_text`, not just the keyword
count), watching specifically for the "wrong Gaussian" trap (statistics/random-fields sense
vs. the quantum-chemistry software) -- none of this batch hit that trap.

## GOOD (17)

### Cambridge Chemistry Dept - Gaussian16
- URL: https://computing.ch.cam.ac.uk/software/gaussian-16
- Keyword hits: 24
- What it contains: University of Cambridge Chemistry Department computing page covering
  Gaussian 16 usage on departmental/HPC resources -- module setup and job basics.

```toml
[[html_sources]]
label = "Cambridge Chemistry Dept - Gaussian16"
url = "https://computing.ch.cam.ac.uk/software/gaussian-16"
```

### Oxford ARC - Gaussian
- URL: https://arc-software-guide.readthedocs.io/en/latest/apps/arc_gaussian.html
- Keyword hits: 25
- What it contains: Oxford Advanced Research Computing's software guide for Gaussian 03/09/16
  on the ARC clusters -- access-request process, a SLURM submission script with multi-
  threading configuration, and notes on running GaussView on interactive nodes.

```toml
[[html_sources]]
label = "Oxford ARC - Gaussian"
url = "https://arc-software-guide.readthedocs.io/en/latest/apps/arc_gaussian.html"
```

### UCL Research Computing - Other Software (Gaussian section)
- URL: https://www.rc.ucl.ac.uk/docs/Software_Guides/Other_Software/
- Keyword hits: 446 (high because this is a combined page covering ~40 packages; verified
  the Gaussian section itself is real and substantial, not just repeated nav)
- What it contains: A genuine, detailed Gaussian section within UCL's general software
  guide -- site-license access process, $GAUSS_SCRDIR/$TMPDIR behavior on Myriad, full
  module-load + source-profile examples for both G16 and G09, and a complete Linda
  multi-node parallel job script with GAUSS_LFLAGS ssh configuration.

```toml
[[html_sources]]
label = "UCL Research Computing - Other Software (Gaussian)"
url = "https://www.rc.ucl.ac.uk/docs/Software_Guides/Other_Software/"
```

### Manchester CSF4 - Gaussian16
- URL: https://ri.itservices.manchester.ac.uk/csf4/software/applications/gaussian16/
- Keyword hits: 70
- What it contains: University of Manchester's Computational Shared Facility 4 docs for
  Gaussian16 -- module load command, GAUSS_SCRDIR/GAUSS_MDEF/GAUSS_PDEF environment
  variables, and core/memory limits (40 cores per node, 4GB/core).

```toml
[[html_sources]]
label = "Manchester CSF4 - Gaussian16"
url = "https://ri.itservices.manchester.ac.uk/csf4/software/applications/gaussian16/"
```

### Bristol ACRC - Gaussian
- URL: https://www.acrc.bris.ac.uk/packages/gaussian.htm
- Keyword hits: 38
- What it contains: University of Bristol Advanced Computing Research Centre page on
  Gaussian 03 for BlueCrystal -- academic-only licensing restrictions, access-request
  process, and guidance on scratch-space usage and integral recalculation.

```toml
[[html_sources]]
label = "Bristol ACRC - Gaussian"
url = "https://www.acrc.bris.ac.uk/packages/gaussian.htm"
```

### RWTH Aachen - Gaussian (CLAIX)
- URL: https://help.itc.rwth-aachen.de/en/service/rhr4fjjutttf/article/33bc9a6953bc4621a510b2102f25df94/
- Keyword hits: 66
- What it contains: RWTH Aachen IT Center's Gaussian guide for the CLAIX cluster --
  module load command, --cpus-per-task batch script guidance, and warnings about setting
  Slurm memory higher than the Gaussian %mem directive plus MaxDisk in the input file.

```toml
[[html_sources]]
label = "RWTH Aachen - Gaussian (CLAIX)"
url = "https://help.itc.rwth-aachen.de/en/service/rhr4fjjutttf/article/33bc9a6953bc4621a510b2102f25df94/"
```

### bwHPC Germany - Gaussian
- URL: https://wiki.bwhpc.de/e/Gaussian
- Keyword hits: 44
- What it contains: The Baden-Wurttemberg HPC consortium wiki's Gaussian page --
  module load chem/gaussian, %NProcShare and %Mem configuration in the input file, and
  the gauss_sub batch-submission helper command.

```toml
[[html_sources]]
label = "bwHPC Germany - Gaussian"
url = "https://wiki.bwhpc.de/e/Gaussian"
```

### QMUL - Gaussian
- URL: https://docs.hpc.qmul.ac.uk/apps/chem/gaussian/
- Keyword hits: 41
- What it contains: Queen Mary University of London HPC docs for Gaussian -- module load,
  automatic SLURM-driven core configuration, and a serial job example with per-core memory
  settings in both the job script and the .com file.

```toml
[[html_sources]]
label = "QMUL - Gaussian"
url = "https://docs.hpc.qmul.ac.uk/apps/chem/gaussian/"
```

### Paderborn PC2 - Gaussian
- URL: https://upb-pc2.atlassian.net/wiki/spaces/PC2DOK/pages/105152525
- Keyword hits: 67
- What it contains: Paderborn Center for Parallel Computing's very thorough Gaussian page
  for the Noctua 2 / Otus clusters -- full licensing tiers (Campus vs. Supercomputing
  license), complete multi-node CPU and multi-GPU (A100) Slurm job scripts with a real
  caffeine-molecule input file, and %cpu/%gpucpu core-affinity directives.

```toml
[[html_sources]]
label = "Paderborn PC2 - Gaussian"
url = "https://upb-pc2.atlassian.net/wiki/spaces/PC2DOK/pages/105152525"
```

### IDRIS France - Gaussian (Jean Zay)
- URL: http://www.idris.fr/docs/jean-zay/logiciels_bibliotheques/logiciels_simulato/gaussian/
- Keyword hits: 16
- What it contains: IDRIS's (French, CNRS) Gaussian page for the Jean Zay supercomputer --
  access-authorization process, g16_cpu_list/g16_gpu_list helper scripts, memory-sizing
  rule of thumb (80% of available memory), and complete Slurm scripts for CPU, V100, and
  A100 partitions.

```toml
[[html_sources]]
label = "IDRIS France - Gaussian (Jean Zay)"
url = "http://www.idris.fr/docs/jean-zay/logiciels_bibliotheques/logiciels_simulato/gaussian/"
```

### CINES France - Optimal Gaussian Usage Memo (PDF)
- URL: https://www.cines.fr/wp-content/uploads/2016/02/memo-gaussian.pdf
- Keyword hits: 31
- What it contains: CINES's (French) "Utilisation optimale du code Gaussian" memo for the
  Occigen supercomputer -- a complete Slurm launch script, %NprocShared/%Mem parameter
  guidance, and scaling-performance benchmarks for two test molecules.

```toml
[[html_sources]]
label = "CINES France - Optimal Gaussian Usage Memo (PDF)"
url = "https://www.cines.fr/wp-content/uploads/2016/02/memo-gaussian.pdf"
```

### ETH Zurich Euler - Gaussian
- URL: https://docs.hpc.ethz.ch/software/chemistry/gaussian/
- Keyword hits: 23
- What it contains: ETH Zurich's official HPC docs for Gaussian on Euler -- module load
  command, license-agreement/access process, and the requirement to set %NProcShared in
  the input file in addition to requesting cores from the batch system.

```toml
[[html_sources]]
label = "ETH Zurich Euler - Gaussian"
url = "https://docs.hpc.ethz.ch/software/chemistry/gaussian/"
```

### ICHEC Ireland - Gaussian
- URL: https://www.ichec.ie/academic/national-hpc-service/software/gaussian
- Keyword hits: 24
- What it contains: Ireland's national HPC service (ICHEC) page for Gaussian on the Kay
  supercomputer -- module name, recommended 40-process/100GB memory configuration, and
  notes that jobs run shared-memory-only on a single node.

```toml
[[html_sources]]
label = "ICHEC Ireland - Gaussian"
url = "https://www.ichec.ie/academic/national-hpc-service/software/gaussian"
```

### DTU Denmark - Gaussian jobs under LSF
- URL: https://www.hpc.dtu.dk/?page_id=2036
- Keyword hits: 33
- What it contains: Technical University of Denmark's guide to running Gaussian under the
  LSF scheduler -- group-membership/scratch-access process, #BSUB directives for single-
  node core reservation, and %NProcShared/%Mem/%RWF/%NoSave input-file settings.

```toml
[[html_sources]]
label = "DTU Denmark - Gaussian jobs under LSF"
url = "https://www.hpc.dtu.dk/?page_id=2036"
```

### Sigma2/NRIS Norway - Gaussian
- URL: https://documentation.sigma2.no/software/application_guides/gaussian/gaussian.html
- Keyword hits: 23
- What it contains: Norway's national research infrastructure (Sigma2/NRIS) Gaussian guide
  covering the Saga, Betzy, and Olivia machines -- group-access/license-documentation
  requirements and machine-specific setup notes (e.g. Saga's rsocket configuration).

```toml
[[html_sources]]
label = "Sigma2/NRIS Norway - Gaussian"
url = "https://documentation.sigma2.no/software/application_guides/gaussian/gaussian.html"
```

### IT4Innovations Czech - Gaussian
- URL: https://docs.it4i.cz/en/docs/software/chemistry/gaussian
- Keyword hits: 41
- What it contains: Czech national supercomputing center (IT4Innovations) Gaussian docs for
  the Karolina and Barbora systems -- SMP/Linda/GPU (V100/A100) build variants and current
  access-restriction policy limiting external e-INFRA users.

```toml
[[html_sources]]
label = "IT4Innovations Czech - Gaussian"
url = "https://docs.it4i.cz/en/docs/software/chemistry/gaussian"
```

### TalTech Estonia - Gaussian
- URL: https://hpc.pages.taltech.ee/user-guides-new4/chemistry/gaussian.html
- Keyword hits: 105
- What it contains: Tallinn University of Technology HPC guide for Gaussian (g09/g16) --
  confirmed to be about the quantum-chemistry software, not statistics. Covers module
  loading, SLURM batch submission with core/memory flags, and %Mem input-file guidance.

```toml
[[html_sources]]
label = "TalTech Estonia - Gaussian"
url = "https://hpc.pages.taltech.ee/user-guides-new4/chemistry/gaussian.html"
```

## WEAK -- needs a human look (1)

- **CINECA - Gaussian G16** -- https://www.hpc.cineca.it/systems/software/scientific-field/chemistry/gaussian-g16/
  9 keyword hits, and confirmed by direct read to be a thin catalog stub: a one-line
  description, version numbers across three systems, and two bare `module load` commands,
  with no actual job script, memory/core settings, or usage examples -- it just points to
  `module help g16` for the real details. Italy's national center (CINECA) is otherwise
  unrepresented in this preset, so it may be worth a deeper look for a better CINECA page,
  but this specific URL isn't substantial enough to add as-is.

## Not usable

3 candidates came back FAIL and aren't listed individually above:
- **Cambridge CSD3 - Gaussian** -- https://docs.hpc.cam.ac.uk/hpc/software-packages/gaussian.html
  (HTTP 404 on direct fetch, despite appearing in search results/snippets with real-looking
  content -- the search index is stale and the site has evidently restructured or removed
  this page since it was indexed.)
- **PDC KTH Sweden - How to use Gaussian** -- https://www.kth.se/en/2.79567/software/software/Gaussian/centos7/g09.D01/index_using.html
  (Same pattern: HTTP 404 on direct fetch despite a plausible-looking indexed snippet.)
- **ETH Zurich SciComp Wiki - Using Gaussian on Euler** -- https://scicomp.ethz.ch/wiki/Using_Gaussian_on_Euler
  (Network error on fetch; redundant anyway since the official docs.hpc.ethz.ch Gaussian
  page above already covers Euler.)

Also investigated but found to have no dedicated/substantive Gaussian documentation page:
ARCHER2 (UK, no Gaussian offering found -- likely excluded by license terms on that
service), University of Edinburgh Eddie, Imperial College London (only a teaching page
from an individual research group, not central HPC docs), Vienna Scientific Cluster,
VSC Flemish Supercomputer Center / KU Leuven, Barcelona Supercomputing Center, GRNET/ARIS
(Greece), MACC/Deucalion (Portugal), University of Southampton Iridis (docs are behind an
internal SharePoint login), Warwick SCRTP, TU Delft DHPC, Aalto University Triton, and
PLGrid/Cyfronet Ares (Poland).

## Nothing was added automatically

This file is a proposal only. `configs/gaussian.toml` and `gaussian_scraper/presets.py`
were not touched. To accept a GOOD candidate, copy its TOML block above into
`configs/gaussian.toml`. Note that `presets.py` (the wizard's built-in seed file) isn't
kept in sync with `configs/*.toml` automatically in this repo -- if you want an accepted
source to also show up for future fresh wizard runs, add it there too.
