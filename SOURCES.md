# Source and verification record

Last checked: **2026-10-12**. This repository targets **arXiv:2609.37226v1**, not an automatically updated latest version.

## Canonical primary sources

| Source | Role | Verified information |
| --- | --- | --- |
| [arXiv v1 record](https://arxiv.org/abs/2609.37226v1) | Canonical metadata and submission record | Exact title, ordered authors, September 29, 2026 v1 submission, subjects, arXiv-issued DOI, and license link |
| [Versioned PDF](https://arxiv.org/pdf/2609.37226v1) | Authoritative paper layout and contents | 29 pages, exact-v1 stamp, full text, title-page affiliations, all main/appendix figures and tables |
| [Versioned HTML](https://arxiv.org/html/2609.37226v1) | Accessible text and section navigation | Corroborating metadata, section structure, figures/tables, and license banner; PDF governs layout-sensitive interpretation |
| [arXiv license text](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html) | Rights verification | The submitter grants a perpetual non-exclusive distribution license to arXiv |

**Title:** Follow the Entities: A Corpus Map for Agentic Search.

**Authors, in source order:** Soyeong Jeong; Sujay Kumar Jauhar; Sung Ju Hwang; Andrew Joohun Nam.

**Affiliations in the paper:** KAIST (Jeong, Hwang), Microsoft (Jauhar, Nam). The title-page footnote says Jeong's work was done during an internship at Microsoft. The companion curator `0xHayd3n` is not an author of the paper.

**Submission:** v1, September 29, 2026, 10:39:57 UTC according to the arXiv record. The source is labeled a preprint. No conference/journal acceptance is asserted here.

**DOI:** `10.48550/arXiv.2609.37226`, as listed by arXiv. The checked arXiv record labels DOI registration as pending. This identifier is work-level; use the v1 arXiv URL for exact-version citation. The companion does not claim successful DOI registration or resolution.

## Attachment and public-source provenance

The supplied Library attachment was read through native Library content access. Its first pages establish the same title, ordered authors, arXiv v1 date/stamp, and 29-page count as the public source. Its reported byte length is 523,503 bytes.

Supported local Library transfer could not complete the required metadata persistence on the Windows host. The companion used the independently downloaded **public arXiv v1 PDF** for complete local text extraction and pixel inspection. That file is also 523,503 bytes. Equal file size is corroboration, not proof of byte equality; **byte-for-byte identity with the attachment was not established**.

For the independently downloaded public PDF inspected on 2026-10-12:

```text
Source:  https://arxiv.org/pdf/2609.37226v1
Pages:   29
Bytes:   523503
SHA-256: de52222fe3bc1d16ba62d3f193d2986b5a183a60913d5c17829cd01922e16373
```

This hash records the locally inspected public artifact; arXiv delivery bytes may change without a scientific version change. The source PDF, extracted text, signed transfer data, and rendered page images are not committed or redistributed by this repository. No private attachment identifier appears in the public metadata.

## What was reviewed

The complete 29-page public PDF was read, including references and Appendix C. Rendered pixels were inspected for Figures 1–6, Tables 1–10, Algorithm 1 and the method layout, and all Appendix C prompt figures (7–13). The [visual guide](docs/visual-guide.md) supplies locators and interpretation cautions.

Key consistency checks included:

- Dataset/subset sizes against §4 and Appendix A.
- Main score columns and aggregate arithmetic against Table 1 pixels.
- Confidence intervals and statistical procedure against Table 6 and B.1.
- Token exceptions, candidate ablations, upper-bound cost notation, and amortization labels against original table/figure pixels.
- The distinction between LLM-based Cataloging and the off-the-shelf substitutions in §5.2.
- Paper author ordering and version agreement across the attachment, arXiv record, PDF, and HTML.
- Repository links, anchors, citations, UTF-8 text, structured metadata, and prohibited source/private-file exclusions.

These are documentation checks. They do not reproduce or independently validate the paper's empirical experiments.

Before publication, the CFF citation parsed as YAML and passed the official [Citation File Format 1.2.0 schema](https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json). The versioned arXiv record, HTML, PDF, and license links returned HTTP 200. Independent reviews of the mechanism, numeric summaries, source metadata, and page locators found no unresolved factual issue.

## Official project and code status

No author-designated CorpusMap project site or implementation repository URL was identified in the **checked v1 PDF and arXiv metadata/HTML**. The PDF's URI annotations were also inspected. Links in its bibliography concern cited prior work, benchmarks, or model resources; the LLM Wiki gist, for example, is a baseline reference rather than CorpusMap's code.

This is a bounded verification result as of 2026-10-12. It does not prove that the authors have no code or that a later release will not appear. `official_project_url` and `official_code_url` remain `null` in [metadata.json](metadata.json). Add a link only after checking provenance from the paper authors or their institutions. Do not treat this reading repository as the missing official implementation.

## Rights decision

The arXiv page and HTML identify the **arXiv perpetual non-exclusive distribution license**. The linked terms grant distribution rights to arXiv, rather than giving this companion a general license to redistribute the work. Therefore the full paper/PDF, original figures, screenshots, complete tables, prompts, code, and datasets are omitted. Readers are directed to the primary source.

Original explanatory notes and diagrams, selective scientific facts with source locators, and the repository's validation code are covered by the [scoped MIT license](LICENSE). No third-party work is blanket-licensed. See [NOTICE.md](NOTICE.md) for attribution and exclusions.
