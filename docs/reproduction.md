# Before attempting an independent reproduction

[Home](../README.md) · [Method](method.md) · [Evaluation](evaluation.md) · [Limitations](limitations.md)

**Reproduction status: not attempted.** This repository contains a reading companion and documentation checks. It contains no CorpusMap implementation, experimental outputs, benchmark runner, copied prompts, or trained models. The checklist below is companion guidance for future work, not an implemented procedure or author-endorsed recipe.

## Start from the exact source

Use [arXiv:2609.37226v1](https://arxiv.org/abs/2609.37226v1), submitted September 29, 2026. Consult §3's method, §4's setup, Appendix A's corpus/metric details, and Appendix C's prompts. The reproducibility statement points to those locations. No author-designated project/code URL was identified in the checked v1 PDF and arXiv record. Obtain any official code only after verifying its provenance and license. [Reproducibility statement, p. 10.](https://arxiv.org/pdf/2609.37226v1#page=10)

## Experimental manifest to record

| Area | Record before running | Paper locator |
| --- | --- | --- |
| Data | Exact benchmark versions, selected question IDs, gold evidence, fixed corpus paths/IDs, and distractor selections | §4, p. 6; Appendix A, p. 16 |
| CorpusMap build | Catalog samples, proposal/synthesis/verification/revision settings, document order, extraction/linking backend, registry state, rendering settings | §3.3, p. 5; Appendix C, pp. 21–29 |
| Candidate interface | BM25 page fields, pooled-document ranking, candidate counts, and path/title/ID format | §3.4, pp. 5–6; B.3, pp. 18–19 |
| Agent | Exact prompt, allowed shell commands, budget/termination policy, context limits, selected-support tracking, tool-output handling | §4, p. 6; Appendix A, p. 16 |
| Models | Immutable model/API identifiers if available, inference parameters, API dates, backend versions | §4, p. 6; Appendix A, p. 16 |
| Baselines | Each navigation-layer build, same corpus access, same answering budget; retrieve-then-generate context for Table 3 | §4–5.1, pp. 6–8 |
| Evaluation | Official benchmark evaluator/prompt versions, judge settings, atomic facts, gold documents, score normalization | Appendix A, p. 16; B.2, pp. 17–18 |
| Statistics | Three runs for Table 1, per-question run averaging, paired question resampling and multiple-testing correction | Table 1, p. 7; B.1, p. 17 |
| Costs | Offline construction/refresh, input and output tokens, pricing date, cache effects, latency, query count per corpus | §5.2, pp. 8–9; Fig. 5, p. 17 |

Some details in this manifest may require author clarification or official implementation artifacts beyond the prose. For example, the paper states a fixed per-question execution budget but the companion should not invent a numeric budget, undocumented stopping condition, or a default candidate count from a plotted parameter sweep. The main API calls were made in August–September 2026; later calls may reach changed services even with similar model labels. [Appendix A, p. 16.](https://arxiv.org/pdf/2609.37226v1#page=16)

## Check the comparison before interpreting it

1. Freeze the same question/corpus selection for every compared agentic method. Verify every gold source remains in the intended corpus.
2. Separate building the map from answering queries. Keep held-out questions out of the query-independent build.
3. Preserve raw corpus access and make candidate path presentation comparable. Run the candidate ablation if the claim is about navigational structure alone.
4. Record answer text, selected support, tool-call context, and accumulated input tokens separately. Do not substitute final prompt length for trajectory tokens.
5. Recompute Overall Quality as equal benchmark weighting of the per-benchmark **retrieval plus answer** quality aggregates. Compute Relative Tokens geometrically over the three benchmark ratios.
6. Include both favorable results and token exceptions. Preserve per-metric run variability and paired-bootstrap confidence intervals where applicable.
7. Treat the oracle as an idealized reference and distinguish retrieval-then-generation baselines from agents with continuing full-corpus access.

This is a proposed validation sequence. No step above is evidence that this repository ran the paper's experiments.

## A bounded reproduction report

A future report should state which table/figure and exact settings it attempts, what source code/data rights were verified, which details match or differ, and whether measured scores agree within an appropriate uncertainty range. If only a toy illustration is built, describe it as an illustration; if only candidate ranking is recreated, do not call it a full CorpusMap reproduction.

The documentation validator here checks links, citations, metadata, and selected result arithmetic. It cannot verify extraction quality, registry resolution, factual page accuracy, model answers, or the empirical claims of the paper.
