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
        {
            "label": "George Mason ORC - Gaussian",
            "url": "https://wiki.orc.gmu.edu/mkdocs/Running_Gaussian/",
        },
        {
            "label": "HPC2N Umea - Gaussian",
            "url": "https://docs.hpc2n.umu.se/software/apps/gaussian/",
        },
        {
            "label": "Flinders DeepThought - Gaussian",
            "url": "https://deepthoughtdocs.flinders.edu.au/en/develop/software/gaussian16.html",
        },
        {
            "label": "William and Mary - Gaussian",
            "url": "https://www.wm.edu/offices/it/services/researchcomputing/using/software/gaussian/",
        },
        {
            "label": "Delaware IT-RCI - Gaussian on Darwin",
            "url": "https://docs.hpc.udel.edu/software/gaussian/darwin",
        },
        {
            "label": "UTEP - Gaussian16 HPC Usage Guide (PDF)",
            "url": "https://www.utep.edu/information-resources/research/resources/hpc%20usage%20guide%20for%20gaussian%2016%20on%20jakar.docx.pdf",
        },
        {
            "label": "MSU ICER - Computational Quantum Chemistry Tools (PDF)",
            "url": "https://docs.icer.msu.edu/attachments/Computational_Quantum_Chemistry_Tools.pdf",
        },
        {
            "label": "UBA - GaussView/Gaussian Guide and Exercise Manual (PDF)",
            "url": "http://users.df.uba.ar/rboc/em3/GAUSSIAN_TRAIN.pdf",
        },
        {
            "label": "Tel Aviv Uni - Gaussian Manual (PDF)",
            "url": "https://www.tau.ac.il/~ephraim/Gaussian_manual.pdf",
        },
        {
            "label": "Illinois Pogorelov Lab - Gaussian Intro Tutorial (PDF)",
            "url": "http://pogorelov.scs.illinois.edu/wp-content/uploads/2020/06/qm-gaussian-intro-1-tutorial-PogorelovLab.2011.v1.web_.pdf",
        },
        {
            "label": "Illinois SCS - Gaussian Intro 2 (PDF)",
            "url": "https://scs.illinois.edu/system/files/inline-files/gaussian-intro-2.pdf",
        },
        {
            "label": "Texas A&M - Computational Chemistry Handout (PDF)",
            "url": "https://www.chem.tamu.edu/class/majors/chem101h-lab/chem/Computational%20Chemistry%20Handout%20-%202016.pdf",
        },
        {
            "label": "UW Faculty - Computational Chemistry Tutorial (PDF)",
            "url": "https://faculty.washington.edu/tingcao/wordpress/wp-content/uploads/2020/05/Comp_Chem_Tutorial__Spr2020.pdf",
        },
        {
            "label": "Illinois SCS - Gaussian GaussView Tutorial (PDF)",
            "url": "https://scs.illinois.edu/system/files/inline-files/SCS-Gaussian-GaussView-tutorial_1.pdf",
        },
        {
            "label": "NBO Wisconsin - INSTALL.gaussian (Gaussian-09 D.01/NBO6 txt)",
            "url": "https://nbo.chem.wisc.edu/INSTALL.gaussian",
        },
        {
            "label": "NBO Wisconsin - INSTALL.g09c01 (Gaussian-09 C.01/NBO6 txt)",
            "url": "https://nbo.chem.wisc.edu/INSTALL.g09c01",
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
            "label": "Samtools GitHub",
            "url": "https://github.com/samtools/samtools",
            "tool": "samtools",
        },
        {
            "label": "BWA GitHub (lh3)",
            "url": "https://github.com/lh3/bwa",
            "tool": "bwa",
        },
        {
            "label": "OSG Connect - BWA Tutorial",
            "url": "https://github.com/OSGConnect/tutorial-bwa",
            "tool": "bwa",
        },
        {
            "label": "QMUL HPC - Samtools",
            "url": "https://docs.hpc.qmul.ac.uk/apps/bio/samtools/",
            "tool": "samtools",
        },
        {
            "label": "NCSA UIUC - Samtools",
            "url": "https://docs.ncsa.illinois.edu/en/latest/software/bio/samtools.html",
            "tool": "samtools",
        },
        {
            "label": "FSU RCC - BWA",
            "url": "https://docs.rcc.fsu.edu/software/bwa/",
            "tool": "bwa",
        },
        {
            "label": "HPC @ QMUL - BWA",
            "url": "https://docs.hpc.qmul.ac.uk/apps/bio/bwa/",
            "tool": "bwa",
        },
        {
            "label": "CSC Docs - BWA",
            "url": "https://docs.csc.fi/apps/bwa/",
            "tool": "bwa",
        },
        {
            "label": "USC CARC - GATK",
            "url": "https://www.carc.usc.edu/user-guides/life-sciences-computing/software-packages/gatk",
            "tool": "gatk",
        },
        {
            "label": "UWEC Blugold HPC - BLAST",
            "url": "https://docs.hpc.uwec.edu/software/guides/blast/",
            "tool": "blast",
        },
        {
            "label": "MSU ICER - BLAST+",
            "url": "https://docs.icer.msu.edu/BLAST_BLAST+_with_Multiple_Processors/",
            "tool": "blast",
        },
        {
            "label": "UGA GACRC - BLAST+ Teaching",
            "url": "https://wiki.gacrc.uga.edu/wiki/BLAST+-Teaching",
            "tool": "blast",
        },
        {
            "label": "Iowa State Pronto - BLAST",
            "url": "https://research.it.iastate.edu/guides/pronto/bioinformatics/blast/",
            "tool": "blast",
        },
        {
            "label": "NC State HPC - BLAST",
            "url": "https://hpc.ncsu.edu/Software/Apps.php?app=BLAST",
            "tool": "blast",
        },
        {
            "label": "Purdue RCAC - HPC Orientation for Biologists",
            "url": "https://docs.rcac.purdue.edu/lifesciences/guides/hpc-orientation/",
        },
        {
            "label": "Harvard FAS - Snakemake Workshop",
            "url": "https://informatics.fas.harvard.edu/workshops/snakemake/run/",
        },
        {
            "label": "Glasgow Uni - BWA Tutorial (PDF)",
            "url": "https://userweb.eng.gla.ac.uk/umer.ijaz/bioinformatics/BWA_tutorial.pdf",
            "tool": "bwa",
        },
        {
            "label": "Evomics - Alignment Workshop 2022 (PDF)",
            "url": "https://evomics.org/wp-content/uploads/2022/05/Alignment-Workshop-2022.pdf",
            "tool": "bwa",
        },
        {
            "label": "CRUK Bioinformatics - Sequence Alignment with BWA (PDF)",
            "url": "http://bioinformatics-core-shared-training.github.io/cruk-bioinf-sschool/Day1/Sequence%20Alignment_July2015_ShamithSamarajiwa.pdf",
            "tool": "bwa",
        },
        {
            "label": "UBC MICB405 - BWA SAMtools BCFtools Tutorial (PDF)",
            "url": "https://educe-ubc.github.io/MICB405/slides/tutorials/samtools_bcftools.pdf",
            "tool": "samtools",
        },
        {
            "label": "UCLA QCB - GATK Primer (PDF)",
            "url": "https://qcb.ucla.edu/wp-content/uploads/sites/14/2016/03/GATKwr12-1-GATK_primer.pdf",
            "tool": "gatk",
        },
        {
            "label": "Cornell BioHPC - Variant Calling Exercise 1 (PDF)",
            "url": "https://biohpc.cornell.edu/lab/doc/Variant_exercise1.pdf",
            "tool": "gatk",
        },
        {
            "label": "UCLA QCB - Variant Calling with GATK Winter2020 (PDF)",
            "url": "https://qcb.ucla.edu/wp-content/uploads/sites/14/2020/03/VariantCallingWithGATK_WINTER2020.pdf",
            "tool": "gatk",
        },
        {
            "label": "Evomics - Human Variant Calling Workshop (PDF)",
            "url": "https://evomics.org/wp-content/uploads/2020/01/Human-Variant-Calling-Workshop.pdf",
            "tool": "gatk",
        },
        {
            "label": "QIAGEN - BLAST Tips Tutorial (PDF)",
            "url": "https://resources.qiagenbioinformatics.com/tutorials/BLAST_tips.pdf",
            "tool": "blast",
        },
        {
            "label": "Cornell BioHPC - Lab and Linux Basics Workshop (PDF)",
            "url": "https://biohpc.cornell.edu/lab/doc/BioHPC_Lab_and_Linux_Basics.pdf",
        },
        {
            "label": "Cornell BioHPC - Linux for Biologists (PDF)",
            "url": "https://biohpc.cornell.edu/lab/doc/Linux_workshop.pdf",
        },
        {
            "label": "Evomics - Genomics Tutorial 2019 (PDF)",
            "url": "https://files.evomics.org/2019/01/genomics_tutorial_2019.pdf",
        },
        {
            "label": "CRUK Bioinformatics - Short Read Alignment Lecture (PDF)",
            "url": "https://bioinformatics-core-shared-training.github.io/cruk-autumn-school-2017/Introduction/SS_DB/Materials/Lectures/Lecture3_ShortRead_Alignment_SS.pdf",
        },
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
        {
            "label": "Babraham - Analysing RNA-Seq data Exercise (DOCX)",
            "url": "https://www.bioinformatics.babraham.ac.uk/training/RNASeq_Course/Analysing%20RNA-Seq%20data%20Exercise.docx",
        },
        {
            "label": "Babraham - Sequencing QC Exercise (DOCX)",
            "url": "https://www.bioinformatics.babraham.ac.uk/training/Sequence_QC_Course/Sequencing%20QC%20Exercise.docx",
        },
        {
            "label": "Babraham - Linux Bootcamp Exercises (DOCX)",
            "url": "https://www.bioinformatics.babraham.ac.uk/training/Linux%20bootcamp/Linux%20Bootcamp%20Exercises.docx",
        },
        {
            "label": "VCRU Wisconsin - BBMap README.txt",
            "url": "https://vcru.wisc.edu/simonlab/bioinformatics/programs/bbmap/readme.txt",
        },
        {
            "label": "DarkHorse2 GitHub - README.txt",
            "url": "https://raw.githubusercontent.com/spodell/Darkhorse2/master/README.txt",
        },
        {
            "label": "VCRU Wisconsin - Platanus README.txt",
            "url": "https://vcru.wisc.edu/simonlab/bioinformatics/programs/platanus/README.txt",
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
