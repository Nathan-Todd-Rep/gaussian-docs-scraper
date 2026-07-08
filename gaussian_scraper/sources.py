from __future__ import annotations

# Curated list of trusted HPC documentation sources known to contain
# Gaussian-related content. Each entry has a URL to scrape and a label
# used to identify the source in stored snippets.
#
# These are all public-facing research computing documentation sites from
# universities and national labs. Adding a new source is as simple as
# appending an entry to this list.

GAUSSIAN_SOURCES = [
    {
        "label": "Harvard RC - Gaussian",
        "url": "https://docs.rc.fas.harvard.edu/kb/gaussian/",
    },
    {
        "label": "TACC - Gaussian",
        "url": "https://docs.tacc.utexas.edu/software/gaussian/",
    },
    {
        "label": "NSC Sweden - Gaussian",
        "url": "https://www.nsc.liu.se/software/installed/tetralith/gaussian/",
    },
    {
        "label": "Ohio Supercomputer Center - Gaussian",
        "url": "https://www.osc.edu/resources/available_software/software_list/gaussian",
    },
]

# Stack Exchange sources for Gaussian-related questions and answers.
# Matter Modeling SE has an active gaussian tag (215 questions).
# Chemistry SE's gaussian tag no longer exists.
STACKEXCHANGE_SOURCES = [
    {
        "label": "Matter Modeling Stack Exchange - gaussian tag",
        "tag": "gaussian",
        "site": "mattermodeling",
    },
]

# Keywords used to decide whether a paragraph is relevant enough to keep.
# A passage must contain at least one of these (case-insensitive) to be retained.
GAUSSIAN_KEYWORDS = [
    "gaussian",
    "g09",
    "g16",
    "computational chemistry",
    "quantum chemistry",
    "slurm",
    "sbatch",
    "module load",
    "mem=",
    "nproc=",
    "%mem",
    "%nproc",
    "basis set",
    "dft",
    "density functional",
]
