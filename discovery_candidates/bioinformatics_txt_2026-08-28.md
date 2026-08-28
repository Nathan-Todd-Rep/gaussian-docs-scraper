# Discovered txt sources for bioinformatics -- 2026-08-28

First plain-text (.txt) pass for bioinformatics. As expected, directly-linked .txt files
with real documentation are uncommon (most tool docs live as HTML or GitHub-rendered
Markdown) -- this batch found 4 real candidates, 3 GOOD and 1 that came back empty and was
rejected. None of the GOOD candidates are specific to samtools/bwa/gatk/blast themselves
(they're adjacent tools -- a genome assembler, a read mapper, and a BLAST-based homology
tool), so per the proposal format no `tool` field is included on any of them. All GOOD
candidates were fetched and read directly via `fetch_page_text` to confirm real,
substantive, on-topic content before being listed here.

## GOOD (3)

### VCRU Wisconsin - BBMap README.txt
- URL: https://vcru.wisc.edu/simonlab/bioinformatics/programs/bbmap/readme.txt
- Keyword hits: 107 (highest of this batch -- verified genuine, not a stub or mismatch)
- Verified: genuine, long (77KB), substantive README for BBMap, a short-read
  aligner/mapper by Brian Bushnell (Joint Genome Institute/LBL). Covers indexing and
  mapping syntax (`bbmap.sh ref=... `, `.fq`/`.sam` I/O), memory tuning, and extensive
  advanced parameters -- real working documentation, not a thin catalog page, despite the
  highest hit count in the batch.

```toml
[[html_sources]]
label = "VCRU Wisconsin - BBMap README.txt"
url = "https://vcru.wisc.edu/simonlab/bioinformatics/programs/bbmap/readme.txt"
```

### DarkHorse2 GitHub - README.txt
- URL: https://raw.githubusercontent.com/spodell/Darkhorse2/master/README.txt
- Keyword hits: 42
- Verified: genuine plain-text (raw.githubusercontent.com serves it as real `text/plain`,
  not GitHub's rendered HTML) README for DarkHorse 2.0, a phylogenetic-relatedness tool
  that runs blastp hits against a reference database (e.g. NCBI GenBank nr) to compute a
  lineage probability index. Real, detailed sections: description, requirements,
  installation, usage instructions, version history.

```toml
[[html_sources]]
label = "DarkHorse2 GitHub - README.txt"
url = "https://raw.githubusercontent.com/spodell/Darkhorse2/master/README.txt"
```

### VCRU Wisconsin - Platanus README.txt
- URL: https://vcru.wisc.edu/simonlab/bioinformatics/programs/platanus/README.txt
- Keyword hits: 10 (right at the GOOD threshold)
- Verified: genuine README for Platanus, a de novo genome assembler for high-throughput
  sequencing data (contig construction via de Bruijn graph, scaffolding from paired-end
  data, gap closing). Despite the low hit count, the content itself is real and complete
  -- description, requirements, installation, synopsis, and a detailed usage/options
  section -- not a stub; it simply doesn't use as many of this domain's exact keyword
  strings (no literal "bam"/"vcf"/"samtools" text) as the other two candidates.

```toml
[[html_sources]]
label = "VCRU Wisconsin - Platanus README.txt"
url = "https://vcru.wisc.edu/simonlab/bioinformatics/programs/platanus/README.txt"
```

## WEAK -- needs a human look (0)

None found in this batch.

## Not usable

1 candidate came back EMPTY (no usable keyword matches -- off-topic/unrelated content) and
isn't listed individually here: `https://vcru.wisc.edu/simonlab/bioinformatics/programs/structureharvester/README.md.txt`
(Structure Harvester, a population-genetics/STRUCTURE-output analysis tool -- real content
exists at that URL, but it doesn't overlap with this domain's keyword set).

`https://ftp.ncbi.nlm.nih.gov/blast/documents/README` was found and read but not proposed:
it's real and on-topic (official NCBI BLAST documents directory) but is a ~1KB stub that
just points elsewhere (to the BLAST+ user manual, release notes, and help pages) rather
than containing substantive documentation itself.

## Nothing was added automatically

This file is a proposal only. `configs/bioinformatics.toml` and
`gaussian_scraper/presets.py` were not touched. To accept a GOOD candidate, copy its TOML
block above into `configs/bioinformatics.toml`. Note that `presets.py` (the wizard's
built-in seed file) isn't kept in sync with `configs/*.toml` automatically in this repo --
if you want an accepted source to also show up for future fresh wizard runs, add it there
too.
