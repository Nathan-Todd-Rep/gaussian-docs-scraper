from __future__ import annotations

# Built-in presets offered by the interactive wizard.
#
# Each preset pre-populates keywords AND html_sources (not just keywords).
# This is intentional: curated, validated sources reduce the risk of pulling
# in low-quality or off-topic passages that could lead to inaccurate
# downstream summaries. SE tags are offered as a starting point but the
# wizard also re-runs live tag discovery so results stay current.

GAUSSIAN_PRESET = {
    "name": "gaussian",
    "display_name": "Gaussian (computational chemistry)",
    "keywords": [
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
    ],
    "html_sources": [
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
        {
            "label": "HPC Wiki - Gaussian",
            "url": "https://hpc-wiki.info/hpc/Gaussian",
        },
        {
            "label": "CSC Finland - Gaussian",
            "url": "https://docs.csc.fi/apps/gaussian/",
        },
        {
            "label": "U Florida RC - Gaussian",
            "url": "https://docs.rc.ufl.edu/software/apps/gaussian",
        },
        {
            "label": "U Chicago RCC - Gaussian",
            "url": "https://docs.rcc.uchicago.edu/software/apps-and-envs/gaussian/",
        },
        {
            "label": "Yale YCRC - Gaussian",
            "url": "https://docs.ycrc.yale.edu/clusters-at-yale/guides/gaussian",
        },
        {
            "label": "FSU RCC - Gaussian",
            "url": "https://docs.rcc.fsu.edu/software/gaussian/",
        },
        {
            "label": "Utah CHPC - Gaussian09",
            "url": "https://www.chpc.utah.edu/documentation/software/gaussian09.php",
        },
        {
            "label": "Utah CHPC - Gaussian16",
            "url": "https://www.chpc.utah.edu/documentation/software/gaussian16/index.php",
        },
        {
            "label": "NC State HPC - Gaussian",
            "url": "https://hpc.ncsu.edu/Software/Apps.php?app=Gaussian",
        },
        {
            "label": "GWDG - Gaussian",
            "url": "https://docs.hpc.gwdg.de/software_stacks/applications/gaussian/index.html",
        },
    ],
    "se_sources": [
        {
            "label": "Matter Modeling Stack Exchange - gaussian tag",
            "tag": "gaussian",
            "site": "mattermodeling",
        },
        {
            "label": "Matter Modeling Stack Exchange - density-functional-theory tag",
            "tag": "density-functional-theory",
            "site": "mattermodeling",
        },
        {
            "label": "Matter Modeling Stack Exchange - computational-chemistry tag",
            "tag": "computational-chemistry",
            "site": "mattermodeling",
        },
        {
            "label": "Matter Modeling Stack Exchange - quantum-chemistry tag",
            "tag": "quantum-chemistry",
            "site": "mattermodeling",
        },
        {
            "label": "Matter Modeling Stack Exchange - high-performance-computing tag",
            "tag": "high-performance-computing",
            "site": "mattermodeling",
        },
        {
            "label": "Chemistry Stack Exchange - quantum-chemistry tag",
            "tag": "quantum-chemistry",
            "site": "chemistry",
        },
        {
            "label": "Chemistry Stack Exchange - computational-chemistry tag",
            "tag": "computational-chemistry",
            "site": "chemistry",
        },
        {
            "label": "Matter Modeling Stack Exchange - basis-sets tag",
            "tag": "basis-sets",
            "site": "mattermodeling",
        },
        {
            "label": "Chemistry Stack Exchange - basis-set tag",
            "tag": "basis-set",
            "site": "chemistry",
        },
        {
            "label": "Matter Modeling Stack Exchange - td-dft tag",
            "tag": "td-dft",
            "site": "mattermodeling",
        },
        {
            "label": "SciComp Stack Exchange - hpc tag",
            "tag": "hpc",
            "site": "scicomp",
        },
    ],
}

BIOINFORMATICS_PRESET = {
    "name": "bioinformatics",
    "display_name": "Bioinformatics",
    "keywords": [
        "rna-seq",
        "fastq",
        "samtools",
        "bwa",
        "gatk",
        "genome",
        "variant-calling",
        "ngs",
        "vcf",
        "alignment",
        "bam",
        "blast",
    ],
    "html_sources": [
        {
            "label": "Ohio Supercomputer Center - BWA",
            "url": "https://www.osc.edu/resources/available_software/software_list/bwa",
        },
        {
            "label": "Ohio Supercomputer Center - Samtools",
            "url": "https://www.osc.edu/resources/available_software/software_list/samtools",
        },
        {
            "label": "Ohio Supercomputer Center - GATK",
            "url": "https://www.osc.edu/resources/available_software/software_list/gatk",
        },
        {
            "label": "NIH HPC - Samtools",
            "url": "https://hpc.nih.gov/apps/samtools.html",
        },
        {
            "label": "NIH HPC - BWA",
            "url": "https://hpc.nih.gov/apps/bwa.html",
        },
        {
            "label": "Utah CHPC - BLAST",
            "url": "https://www.chpc.utah.edu/documentation/software/blast.php",
        },
        {
            "label": "QMUL HPC - GATK",
            "url": "https://docs.hpc.qmul.ac.uk/apps/bio/gatk/",
        },
        {
            "label": "UL HPC - Bioinformatics Basics",
            "url": "https://ulhpc-tutorials.readthedocs.io/en/latest/bio/basics/",
        },
        {
            "label": "GATK - Local HPC Infrastructure",
            "url": "https://gatk.broadinstitute.org/hc/en-us/articles/360046877112-GATK-on-local-HPC-infrastructure",
        },
        {
            "label": "Cornell BioHPC - Software Guide",
            "url": "https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=445",
        },
    ],
    "se_sources": [
        {
            "label": "Bioinformatics Stack Exchange - rna-seq tag",
            "tag": "rna-seq",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - ngs tag",
            "tag": "ngs",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - vcf tag",
            "tag": "vcf",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - genome tag",
            "tag": "genome",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - samtools tag",
            "tag": "samtools",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - fastq tag",
            "tag": "fastq",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - assembly tag",
            "tag": "assembly",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - variant-calling tag",
            "tag": "variant-calling",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - blast tag",
            "tag": "blast",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - multiple-sequence-alignment tag",
            "tag": "multiple-sequence-alignment",
            "site": "bioinformatics",
        },
        {
            "label": "Bioinformatics Stack Exchange - gatk tag",
            "tag": "gatk",
            "site": "bioinformatics",
        },
    ],
}

# Ordered list of presets offered by the wizard. "Custom topic" is handled
# separately by the wizard itself and is not part of this list.
PRESETS = [GAUSSIAN_PRESET, BIOINFORMATICS_PRESET]
