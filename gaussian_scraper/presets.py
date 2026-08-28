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
        {
            "label": "BYU Office of Research Computing - Gaussian16",
            "url": "https://rc.byu.edu/wiki/?page=Gaussian+16",
        },
        {
            "label": "CU Boulder Research Computing - Gaussian",
            "url": "https://curc.readthedocs.io/en/latest/software/gaussian.html",
        },
        {
            "label": "NDSU CCAST - Running Gaussian 16",
            "url": "https://kb.ndsu.edu/it/page.php?id=135576",
        },
        {
            "label": "Minnesota Supercomputing Institute - Gaussian",
            "url": "https://msi.umn.edu/our-resources/msi-software/gaussian",
        },
        {
            "label": "Purdue RCAC (Bell) - Gaussian",
            "url": "https://www.rcac.purdue.edu/knowledge/bell/run/examples/apps/gaussian",
        },
        {
            "label": "Argonne National Laboratory CNM - Gaussian",
            "url": "https://wiki.anl.gov/cnm/HPC/Applications/Gaussian",
        },
        {
            "label": "UW-Madison Chemistry HPC - Gaussian",
            "url": "https://hpc.chem.wisc.edu/software/kestrel-software/gaussian/",
        },
        {
            "label": "NIH HPC (Biowulf) - Gaussian",
            "url": "https://hpc.nih.gov/apps/Gaussian.html",
        },
        {
            "label": "Oakland University HPC - Gaussian on Matilda",
            "url": "https://support.oakland.edu/TDClient/33/Support-Center/KB/PrintArticle?ID=257",
        },
        {
            "label": "Kennesaw State CRC - Gaussian Quickstart",
            "url": "https://campus.kennesaw.edu/offices-services/research/centers-facilities/center-research-computing/resources/quickstart/gaussian.php",
        },
        {
            "label": "University of Arizona HPC - Gaussian",
            "url": "https://hpcdocs.hpc.arizona.edu/software/popular_software/gaussian/",
        },
        {
            "label": "Cambridge Chemistry Dept - Gaussian16",
            "url": "https://computing.ch.cam.ac.uk/software/gaussian-16",
        },
        {
            "label": "Oxford ARC - Gaussian",
            "url": "https://arc-software-guide.readthedocs.io/en/latest/apps/arc_gaussian.html",
        },
        {
            "label": "UCL Research Computing - Other Software (Gaussian)",
            "url": "https://www.rc.ucl.ac.uk/docs/Software_Guides/Other_Software/",
        },
        {
            "label": "Manchester CSF4 - Gaussian16",
            "url": "https://ri.itservices.manchester.ac.uk/csf4/software/applications/gaussian16/",
        },
        {
            "label": "Bristol ACRC - Gaussian",
            "url": "https://www.acrc.bris.ac.uk/packages/gaussian.htm",
        },
        {
            "label": "RWTH Aachen - Gaussian (CLAIX)",
            "url": "https://help.itc.rwth-aachen.de/en/service/rhr4fjjutttf/article/33bc9a6953bc4621a510b2102f25df94/",
        },
        {
            "label": "bwHPC Germany - Gaussian",
            "url": "https://wiki.bwhpc.de/e/Gaussian",
        },
        {
            "label": "QMUL - Gaussian",
            "url": "https://docs.hpc.qmul.ac.uk/apps/chem/gaussian/",
        },
        {
            "label": "Paderborn PC2 - Gaussian",
            "url": "https://upb-pc2.atlassian.net/wiki/spaces/PC2DOK/pages/105152525",
        },
        {
            "label": "IDRIS France - Gaussian (Jean Zay)",
            "url": "http://www.idris.fr/docs/jean-zay/logiciels_bibliotheques/logiciels_simulato/gaussian/",
        },
        {
            "label": "CINES France - Optimal Gaussian Usage Memo (PDF)",
            "url": "https://www.cines.fr/wp-content/uploads/2016/02/memo-gaussian.pdf",
        },
        {
            "label": "ETH Zurich Euler - Gaussian",
            "url": "https://docs.hpc.ethz.ch/software/chemistry/gaussian/",
        },
        {
            "label": "ICHEC Ireland - Gaussian",
            "url": "https://www.ichec.ie/academic/national-hpc-service/software/gaussian",
        },
        {
            "label": "DTU Denmark - Gaussian jobs under LSF",
            "url": "https://www.hpc.dtu.dk/?page_id=2036",
        },
        {
            "label": "Sigma2/NRIS Norway - Gaussian",
            "url": "https://documentation.sigma2.no/software/application_guides/gaussian/gaussian.html",
        },
        {
            "label": "IT4Innovations Czech - Gaussian",
            "url": "https://docs.it4i.cz/en/docs/software/chemistry/gaussian",
        },
        {
            "label": "TalTech Estonia - Gaussian",
            "url": "https://hpc.pages.taltech.ee/user-guides-new4/chemistry/gaussian.html",
        },
        {
            "label": "NCI Australia (Gadi) - Gaussian 09",
            "url": "https://opus.nci.org.au/spaces/Help/pages/248840500/Gaussian+09...",
        },
        {
            "label": "ACENET Canada - Gaussian Training Session",
            "url": "https://acenet-arc.github.io/gaussian_training/Gaussian_training_session.html",
        },
        {
            "label": "KISTI Korea (Nurion) - Gaussian16",
            "url": "https://docs-ksc.gitbook.io/nurion-user-guide-eng/software/gaussian16",
        },
        {
            "label": "KISTI Korea (Nurion) - Gaussian16 LINDA",
            "url": "https://docs-ksc.gitbook.io/nurion-user-guide-eng/software/gaussian16-linda",
        },
        {
            "label": "NeSI New Zealand - Gaussian",
            "url": "https://docs.nesi.org.nz/Software/Available_Applications/Gaussian/",
        },
        {
            "label": "CHPC South Africa - Gaussian",
            "url": "https://wiki.chpc.ac.za/howto:gaussian",
        },
        {
            "label": "University of Calgary ARC - Gaussian",
            "url": "https://rcs.ucalgary.ca/Gaussian_on_ARC",
        },
        {
            "label": "SHARCNET Canada - Gaussian16 NBO7 Slides (PDF)",
            "url": "https://helpwiki.sharcnet.ca/wiki/images/6/68/Gaussian16_NBO7.pdf",
        },
        {
            "label": "Princeton MacMillan Group - Introduction to Computational Chemistry (PDF)",
            "url": "https://macmillan.princeton.edu/wp-content/uploads/CompChemIntro_NoLayer.pdf",
        },
        {
            "label": "Princeton MacMillan Group - Fundamentals of Computational Chemistry (PDF)",
            "url": "https://macmillan.princeton.edu/wp-content/uploads/HWS_computational.pdf",
        },
        {
            "label": "Montana State - Introduction to Ab Initio Quantum Chemical Computation (PDF)",
            "url": "https://chemistry.montana.edu/callis/courses/chmy374/374Computation18.pdf",
        },
        {
            "label": "Illinois Pogorelov Lab - Gaussian Intro Tutorial Part 2 (PDF)",
            "url": "http://pogorelov.scs.illinois.edu/wp-content/uploads/2020/06/qm-gaussian-intro-2-tutorial-PogorelovLab.2011.v1.web_.pdf",
        },
        {
            "label": "Southampton CHEM3023 - Gaussian Basis Sets Lecture (PDF)",
            "url": "https://www.southampton.ac.uk/assets/centresresearch/documents/compchem/chem3023_L6.pdf",
        },
        {
            "label": "Southampton CHEM6085 - DFT Gaussian Basis Sets Lecture (PDF)",
            "url": "https://www.southampton.ac.uk/assets/centresresearch/documents/compchem/DFT_L8.pdf",
        },
        {
            "label": "McGill Barrett Group - Gaussian 09W Tutorial (PDF)",
            "url": "https://barrett-group.mcgill.ca/tutorials/Gaussian%20tutorial.pdf",
        },
        {
            "label": "Uni Rostock - Basis Sets Used in Molecular Orbital Calculations (PDF)",
            "url": "https://www.schulz.chemie.uni-rostock.de/storages/uni-rostock/Alle_MNF/Chemie_Schulz/Computerchemie_3/basis_sets.pdf",
        },
        {
            "label": "Lakehead University - CHEM 3451 Computational Chemistry Lab Manual (PDF)",
            "url": "https://www.lakeheadu.ca/sites/default/files/uploads/31/CHEM_3451_lab_manual_F2013_Comp-Chem.pdf",
        },
        {
            "label": "Harvard (Kwan) - Chem 117 Lecture 9: Intro to Computational Chemistry (PDF)",
            "url": "https://ekwan.github.io/pdfs/nmr/lecture%209.pdf",
        },
        {
            "label": "Tel Aviv Uni - Introduction to GaussView (PDF)",
            "url": "https://www.tau.ac.il/~ephraim/intro2gaussview.pdf",
        },
        {
            "label": "Tel Aviv Uni - Lab 4: Transition States and Reaction Paths (PDF)",
            "url": "https://www.tau.ac.il/~ephraim/glab-4.pdf",
        },
        {
            "label": "Sir Syed College (India) - Computational Analysis Add-On Course Syllabus (PDF)",
            "url": "https://sirsyedcollege.ac.in/crm/public/uploads/otherpgm_syllabus/Ph9Th4TujUsKRCFPu3pGVWgMpDnCyb.pdf",
        },
        {
            "label": "U Tokyo IIS - Gaussian Usage Guide (PDF, Japanese)",
            "url": "http://www.iis.u-tokyo.ac.jp/~houjou/kinozai/Gaussian.pdf",
        },
        {
            "label": "ENS Lyon - Gaussian/Avogadro TP Mode d'Emploi (PDF, French)",
            "url": "https://perso.ens-lyon.fr/carine.michel/wp-content/uploads/2019/04/TP.pdf",
        },
        {
            "label": "Univ. Toulouse - Doctoral Course: Introduction to Gaussian 16 (PDF, French)",
            "url": "https://scout.univ-toulouse.fr/pub/docs/group-ED-SDM/web/COURS_DOCTORAUX/3.pdf",
        },
        {
            "label": "UNAD Colombia - Quimica Computacional Course Content (PDF, Spanish)",
            "url": "https://repository.unad.edu.co/bitstream/handle/10596/12499/210116-contenido%20del%20curso.pdf?sequence=1",
        },
        {
            "label": "Universidad de Valencia - Introduccion a la Quimica Computacional (PDF, Spanish)",
            "url": "https://www.uv.es/tunon/QComp/Sesion_QC_Entorno.pdf",
        },
        {
            "label": "Uni Kiel - Einfuhrung in die Computerchemie (PDF, German)",
            "url": "http://ravel.pctc.uni-kiel.de/scripts/Intro_TC/Intro_TC.pdf",
        },
        {
            "label": "Illinois SCS Answers - Intro to Gaussian I (HTML)",
            "url": "https://answers.uillinois.edu/scs/103204",
        },
        {
            "label": "Illinois SCS Answers - GaussView Tutorial (HTML)",
            "url": "https://answers.uillinois.edu/scs/103608",
        },
        {
            "label": "Illinois SCS Answers - pKa Estimations Using Gaussian (HTML)",
            "url": "https://answers.uillinois.edu/scs/103621",
        },
        {
            "label": "Brent Westbrook - Computational Chemistry Tutorial (PDF)",
            "url": "https://bwestbro.com/misc/gauss.pdf",
        },
        {
            "label": "UC Berkeley MGCF - Computational Methods Tutorials Index (HTML)",
            "url": "https://glab.cchem.berkeley.edu/mgcf/tutorials.html",
        },
        {
            "label": "Leddin Computational Chemistry Resources - Gaussian Overview (HTML)",
            "url": "https://emleddin.github.io/comp-chem-website/Otherguide-gaussian-overview.html",
        },
        {
            "label": "Leddin Computational Chemistry Resources - Gaussian Input Files (HTML)",
            "url": "https://emleddin.github.io/comp-chem-website/Otherguide-gaussian-input.html",
        },
        {
            "label": "Illinois SCS Answers - Intro to Gaussian II (HTML)",
            "url": "https://answers.uillinois.edu/scs/103413",
        },
        {
            "label": "UCSB (Kahn) Chem126 - Transition State Optimization Tutorial",
            "url": "https://people.chem.ucsb.edu/kahn/kalju/chem126/public/qm_ts_optim.html",
        },
        {
            "label": "Harvard (Kwan) Chem106 - Transition State for an SN2 Reaction (PDF)",
            "url": "https://ekwan.github.io/pdfs/computations/2%20-%20Transition%20State%20for%20an%20SN2%20Reaction.pdf",
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
        {
            "label": "Babraham Bioinformatics - FastQC",
            "url": "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/",
            "tool": "fastqc",
        },
        {
            "label": "GitHub - s-andrews/FastQC",
            "url": "https://github.com/s-andrews/FastQC",
            "tool": "fastqc",
        },
        {
            "label": "Bucknell BisonNet - FastQC Guide (PDF)",
            "url": "https://bisonnet.bucknell.edu/files/2021/02/FASTQC-Help-Page-Final.pdf",
            "tool": "fastqc",
        },
        {
            "label": "Missouri Genomics Core - FastQC Manual (PDF)",
            "url": "https://mugenomicscore.missouri.edu/PDF/FastQC_Manual.pdf",
            "tool": "fastqc",
        },
        {
            "label": "MSU RTSF - FastQC Tutorial and FAQ (PDF)",
            "url": "https://rtsf.natsci.msu.edu/sites/_rtsf/assets/File/FastQC_TutorialAndFAQ_080717.pdf",
            "tool": "fastqc",
        },
        {
            "label": "USADELLAB - Trimmomatic Manual V0.32 (PDF)",
            "url": "http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf",
            "tool": "trimmomatic",
        },
        {
            "label": "Ohio Supercomputer Center - Trimmomatic",
            "url": "https://www.osc.edu/resources/available_software/software_list/trimmomatic",
            "tool": "trimmomatic",
        },
        {
            "label": "CyVerse - Trimmomatic Quick Start",
            "url": "https://cyverse-trimmomatic-quickstart.readthedocs-hosted.com/en/latest/",
            "tool": "trimmomatic",
        },
        {
            "label": "Data Carpentry - Trimming and Filtering",
            "url": "https://datacarpentry.github.io/wrangling-genomics/03-trimming.html",
            "tool": "trimmomatic",
        },
        {
            "label": "NIH HPC (Biowulf) - Trimmomatic",
            "url": "https://hpc.nih.gov/apps/trimmomatic.html",
            "tool": "trimmomatic",
        },
        {
            "label": "UT Austin Core NGS Tools - Pre-processing Raw Sequences",
            "url": "https://cloud.wikis.utexas.edu/wiki/spaces/CoreNGSTools/pages/54068284/2021+Pre-processing+raw+sequences",
            "tool": "cutadapt",
        },
        {
            "label": "UNL HCC - cutadapt",
            "url": "https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/pre_processing_tools/cutadapt",
            "tool": "cutadapt",
        },
        {
            "label": "Emory Cores - MicroRNAseq Processing Pipeline (PDF)",
            "url": "https://www.cores.emory.edu/eicc/_includes/documents/sections/resources/miRNAseq_HRJ.pdf",
            "tool": "cutadapt",
        },
        {
            "label": "Augusta University HPC - cutadapt",
            "url": "https://auhpcs.augusta.edu/user-kb/applications/cutadapt.html",
            "tool": "cutadapt",
        },
        {
            "label": "HBC Training (Harvard Chan Bioinformatics Core) - MultiQC Lesson",
            "url": "https://hbctraining.github.io/Intro-to-rnaseq-fasrc-salmon-flipped/lessons/11_multiQC.html",
            "tool": "multiqc",
        },
        {
            "label": "UT Austin BioITeam - Using MultiQC",
            "url": "https://cloud.wikis.utexas.edu/wiki/display/bioiteam/Using+MultiQC",
            "tool": "multiqc",
        },
        {
            "label": "Bowtie2 GitHub (BenLangmead)",
            "url": "https://github.com/BenLangmead/bowtie2",
            "tool": "bowtie2",
        },
        {
            "label": "Bowtie2 MANUAL (raw GitHub)",
            "url": "https://raw.githubusercontent.com/BenLangmead/bowtie2/master/MANUAL",
            "tool": "bowtie2",
        },
        {
            "label": "UGA GACRC - Bowtie2 Teaching",
            "url": "https://wiki.gacrc.uga.edu/wiki/Bowtie2-Teaching",
            "tool": "bowtie2",
        },
        {
            "label": "UMN Biostat - Intro to Linux and Bowtie (PDF)",
            "url": "http://www.biostat.umn.edu/~cavanr/NGSlecture3pubh74452016.pdf",
            "tool": "bowtie2",
        },
        {
            "label": "STAR Manual source (raw GitHub .tex)",
            "url": "https://raw.githubusercontent.com/alexdobin/STAR/master/extras/doc-latex/STARmanual.tex",
            "tool": "star",
        },
        {
            "label": "Cornell Physiology - STAR Manual mirror (PDF)",
            "url": "https://physiology.med.cornell.edu/faculty/skrabanek/lab/angsd/lecture_notes/STARmanual.pdf",
            "tool": "star",
        },
        {
            "label": "Harvard HBC Training - Alignment with STAR",
            "url": "https://hbctraining.github.io/Intro-to-rnaseq-hpc-O2/lessons/03_alignment.html",
            "tool": "star",
        },
        {
            "label": "Cornell BioHPC - RNA-Seq Exercise 1: STAR/TopHat (PDF)",
            "url": "https://biohpc.cornell.edu/doc/RNA-Seq-2017-exercise1.pdf",
            "tool": "star",
        },
        {
            "label": "Cornell BioHPC - RNA-Seq Exercise 2 (PDF)",
            "url": "https://biohpc.cornell.edu/doc/RNA-Seq-2017-exercise2.pdf",
            "tool": "star",
        },
        {
            "label": "UCLA QCB - Intro to RNAseq Day 3 (PDF)",
            "url": "https://qcb.ucla.edu/wp-content/uploads/sites/14/2020/04/RNAseq1-day3.pdf",
            "tool": "star",
        },
        {
            "label": "HISAT2 GitHub (DaehwanKimLab)",
            "url": "https://github.com/DaehwanKimLab/hisat2",
            "tool": "hisat2",
        },
        {
            "label": "HISAT2 MANUAL (raw GitHub)",
            "url": "https://raw.githubusercontent.com/DaehwanKimLab/hisat2/master/MANUAL",
            "tool": "hisat2",
        },
        {
            "label": "CU Boulder - HISAT2 Worksheet (PDF)",
            "url": "https://biodatasci.colorado.edu/static/sr2019/6_RNA-seq/6_worksheet_6.1_HISAT2.pdf",
            "tool": "hisat2",
        },
        {
            "label": "UND Genomics Core - RNA-seq Alignment Workshop (PDF)",
            "url": "https://med.und.edu/research/genomics-core/_files/docs/workshop-2019-rnaseq-alignment-handson.pdf",
            "tool": "hisat2",
        },
        {
            "label": "BCFtools GitHub",
            "url": "https://github.com/samtools/bcftools",
            "tool": "bcftools",
        },
        {
            "label": "BCFtools Manual Page",
            "url": "https://samtools.github.io/bcftools/bcftools.html",
            "tool": "bcftools",
        },
        {
            "label": "Cornell BioHPC - Variant Calling Workshop Part 2 (PDF)",
            "url": "https://biohpc.cornell.edu/lab/doc/variant_workshop_part2.pdf",
            "tool": "bcftools",
        },
        {
            "label": "UConn Bioinformatics - Data Therapy Variants (PDF)",
            "url": "https://bioinformatics.uconn.edu/wp-content/uploads/sites/15/2018/03/DataTherapy_Variants_2018week04.pdf",
            "tool": "bcftools",
        },
        {
            "label": "Picard Tools - Broad Institute",
            "url": "https://broadinstitute.github.io/picard/",
            "tool": "picard",
        },
        {
            "label": "Picard - Tool Documentation Overview",
            "url": "http://broadinstitute.github.io/picard/command-line-overview.html",
            "tool": "picard",
        },
        {
            "label": "CSC Docs - Picard",
            "url": "https://docs.csc.fi/apps/picard/",
            "tool": "picard",
        },
        {
            "label": "QMUL - Intro to HPC Tutorials MSc Bioinformatics (PDF)",
            "url": "https://learn.hpc.qmul.ac.uk/assets/MSc_Bioinformatics.pdf",
            "tool": "picard",
        },
        {
            "label": "GATK Broad - MarkDuplicates (Picard)",
            "url": "https://gatk.broadinstitute.org/hc/en-us/articles/360037052812-MarkDuplicates-Picard",
            "tool": "picard",
        },
        {
            "label": "VCFtools GitHub",
            "url": "https://github.com/vcftools/vcftools",
            "tool": "vcftools",
        },
        {
            "label": "VCFtools Manual",
            "url": "https://vcftools.github.io/man_latest.html",
            "tool": "vcftools",
        },
        {
            "label": "QMUL HPC - VCFtools",
            "url": "https://docs.hpc.qmul.ac.uk/apps/bio/vcftools/",
            "tool": "vcftools",
        },
        {
            "label": "UF HPC - VCFtools",
            "url": "https://docs.rc.ufl.edu/software/apps/vcftools",
            "tool": "vcftools",
        },
        {
            "label": "Sheffield HPC - VCFtools",
            "url": "https://docs.hpc.shef.ac.uk/en/latest/stanage/software/stacks/el7-icelake-znver-stanage/Bio/VCFtools.html",
            "tool": "vcftools",
        },
        {
            "label": "Salmon GitHub",
            "url": "https://github.com/COMBINE-lab/salmon",
            "tool": "salmon",
        },
        {
            "label": "Salmon ReadTheDocs Manual",
            "url": "https://salmon.readthedocs.io/en/latest/salmon.html",
            "tool": "salmon",
        },
        {
            "label": "ANGUS Workshop - Salmon Quant Tutorial",
            "url": "https://angus.readthedocs.io/en/2019/salmon-quant.html",
            "tool": "salmon",
        },
        {
            "label": "NYU Genomics Core - Salmon & kallisto",
            "url": "https://gencore.bio.nyu.edu/salmon-kallisto-rapid-transcript-quantification-for-rna-seq-data/",
            "tool": "salmon",
        },
        {
            "label": "kallisto GitHub",
            "url": "https://github.com/pachterlab/kallisto",
            "tool": "kallisto",
        },
        {
            "label": "kallisto Manual",
            "url": "https://pachterlab.github.io/kallisto/manual",
            "tool": "kallisto",
        },
        {
            "label": "Rsubread/Subread Users Guide (PDF)",
            "url": "https://bioconductor.org/packages/release/bioc/vignettes/Rsubread/inst/doc/SubreadUsersGuide.pdf",
            "tool": "featurecounts",
        },
        {
            "label": "SPAdes GitHub",
            "url": "https://github.com/ablab/spades",
            "tool": "spades",
        },
        {
            "label": "SPAdes Quick Start",
            "url": "https://ablab.github.io/spades/getting-started.html",
            "tool": "spades",
        },
        {
            "label": "UT Austin BioITeam - SPAdes Genome Assembly Tutorial",
            "url": "https://cloud.wikis.utexas.edu/wiki/spaces/bioiteam/pages/47728891",
            "tool": "spades",
        },
        {
            "label": "BEDTools Official Docs (ReadTheDocs)",
            "url": "https://bedtools.readthedocs.io/en/latest/content/overview.html",
            "tool": "bedtools",
        },
        {
            "label": "UT Austin BioITeam - BEDTools Tutorial",
            "url": "https://wikis.utexas.edu/display/bioiteam/Bedtools+tutorial+--+GVA2020",
            "tool": "bedtools",
        },
        {
            "label": "UVA BIOL4230 - BEDTools Lecture (PDF)",
            "url": "https://fasta.bioch.virginia.edu/biol4230/lects/biol4230_29_BedTools.pdf",
            "tool": "bedtools",
        },
        {
            "label": "UT Austin BioITeam - IGV Tutorial",
            "url": "https://wikis.utexas.edu/display/bioiteam/Integrative+Genomics+Viewer+(IGV)+tutorial",
            "tool": "igv",
        },
        {
            "label": "RNA-Bio (Broad Institute) - IGV Tutorial (PDF)",
            "url": "https://rnabio.org/assets/module_2/IGV_Tutorial_Long_BroadInstitute.pdf",
            "tool": "igv",
        },
        {
            "label": "GitHub - marcelm/cutadapt",
            "url": "https://github.com/marcelm/cutadapt/",
            "tool": "cutadapt",
        },
        {
            "label": "GitHub - MultiQC/MultiQC",
            "url": "https://github.com/MultiQC/MultiQC",
            "tool": "multiqc",
        },
        {
            "label": "STAR GitHub (alexdobin)",
            "url": "https://github.com/alexdobin/STAR",
            "tool": "star",
        },
        {
            "label": "BEDTools2 GitHub (arq5x)",
            "url": "https://github.com/arq5x/bedtools2",
            "tool": "bedtools",
        },
        {
            "label": "Cornell BioHPC - featureCounts",
            "url": "https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=856",
            "tool": "featurecounts",
        },
        {
            "label": "CU Boulder BioDataSci - featureCounts Worksheet (PDF)",
            "url": "https://biodatasci.colorado.edu/static/sr2023/07_counting_deseq/Day7_featurecounts_worksheet.pdf",
            "tool": "featurecounts",
        },
        {
            "label": "BCFtools HowTo - Variant Calling",
            "url": "https://samtools.github.io/bcftools/howtos/variant-calling.html",
            "tool": "bcftools",
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
