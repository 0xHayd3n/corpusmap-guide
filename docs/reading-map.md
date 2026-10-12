# Reading map

[Home](../README.md) · [Method](method.md) · [Evaluation](evaluation.md) · [Results](results.md)

**Pinned source:** [Follow the Entities: A Corpus Map for Agentic Search, arXiv:2609.37226v1](https://arxiv.org/abs/2609.37226v1), by Soyeong Jeong, Sujay Kumar Jauhar, Sung Ju Hwang, and Andrew Joohun Nam. Page numbers below are 1-based PDF pages and match printed pages.

## Source section index

| Paper location | PDF pages | What to look for | Companion route |
| --- | --- | --- | --- |
| Abstract and §1 Introduction | 1–3 | The distinction between corpus access and navigation; reusable entity anchors | [README](../README.md) |
| §2 Related Work | 3–4 | Fixed retrieved context, agent-facing structures, and entity resolution | [Method](method.md) |
| §3.1 Preliminaries | 4 | Answer, selected support set, retrieval, and context consumption | [Notation](notation.md) |
| §3.2 CorpusMap | 4 | Bipartite entity–document graph and source-grounded pages | [Method](method.md) |
| §3.3 Construction; Algorithm 1 | 5 | Cataloging, Extraction, Resolution, Rendering | [Method](method.md) |
| §3.4 Navigation | 5–6 | Pages as files; relevant candidate document paths; continued search | [Method](method.md) |
| §4 Experimental Setup | 6 | Selected question sets, corpora, baselines, models | [Evaluation](evaluation.md) |
| §5.1 Effectiveness | 6–8 | Table 1 main comparison, Tables 2–3 extensions, Table 10 case | [Results](results.md) |
| §5.2 Practical Aspects | 8–9 | Builder reuse, amortization, incremental additions, GLinker, scaling, Qwen | [Results](results.md) |
| §6 Conclusion | 9–10 | The proposed direction for corpus interfaces | [Limitations](limitations.md) |
| AI use, Ethics, Reproducibility statements | 10 | Author disclosures, permissions/privacy risks, available experimental detail | [Limitations](limitations.md), [Reproduction](reproduction.md) |
| References | 10–15 | Primary literature and benchmark citations; these are not CorpusMap release links | [Sources](../SOURCES.md) |
| Appendix A Additional Experimental Details | 16 | Subset definitions, metric aggregation, terminal tools, API-call period | [Evaluation](evaluation.md) |
| Appendix B.1 Statistical Significance | 17 | Paired bootstrap and Holm correction, Table 6 | [Results](results.md) |
| Appendix B.2 Judge Robustness | 17–18 | DeepSeek re-judging of GPT-5.5 answers, Table 7 | [Results](results.md) |
| Appendix B.3 Candidate File Paths | 18–19 | Candidate ranking, Table 8, Figure 6 | [Method](method.md), [Results](results.md) |
| Appendix B.4 Entity–Entity Edges | 19 | Reachability, costs, Table 9 example | [Method](method.md), [Results](results.md) |
| Appendix B.5 Case Study | 20 | Earlier manifest draft versus revised v1 evidence, Table 10 | [Visual guide](visual-guide.md) |
| Appendix C Prompts | 21–29 | Figures 7–13: catalog proposal/synthesis/verification/revision and entity processing | [Method](method.md), [Visual guide](visual-guide.md) |

## Three passes through the paper

**First pass, about 10 minutes:** read the abstract, Figure 2 (p. 2), the graph definition (p. 4), and Table 1 (p. 7). Then read Appendix A's metric definition (p. 16) and Table 8 (p. 18). The latter two prevent an overly broad reading of the headline efficiency claim.

**Second pass, mechanism and evidence:** read §3, §4, §5, and Appendices A/B. Track which results use a full three-benchmark evaluation, which use EnterpriseRAG-Bench only, and which change the map builder or candidate interface. Inspect Figures 3–6 rather than estimating curves from extracted text.

**Third pass, implementation questions:** examine Appendix C as source specifications, not ready-to-run software. Notice how identity uncertainty is preserved, how synthesis tries to account for source proposals, and how factual page content must be justified by raw documents. Use [reproduction notes](reproduction.md) to identify details still needed for an independent build.

## Keep five distinctions visible

1. A recurring entity versus a single document-local mention.
2. A resolved mention link versus evidence that supports a factual assertion.
3. Initial candidate file paths versus the contents the agent actually reads.
4. Per-query inference tokens versus offline map construction and maintenance.
5. A paper-reported finding versus this companion's interpretation.

All five recur in the paper and materially affect how to explain its contribution.
