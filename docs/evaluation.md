# Evaluation protocol

[Repository overview](../README.md) · [Results and analyses](results.md)

These are original reading notes on Soyeong Jeong, Sujay Kumar Jauhar, Sung Ju Hwang, and Andrew Joohun Nam's *Follow the Entities: A Corpus Map for Agentic Search*, **arXiv:2609.37226v1**. Experimental statements below describe the authors' reported protocol. This repository did not run their experiments. Page references use the PDF's printed page numbers, which match its PDF page positions.

Primary reading: [Section 4, p. 6](https://arxiv.org/pdf/2609.37226v1#page=6), [Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16), and [Appendix B, pp. 17-20](https://arxiv.org/pdf/2609.37226v1#page=17).

## What is being tested?

The central question is whether a reusable entity-based navigation layer helps an agent find and combine evidence spread across documents. All navigation-layer methods retain access to the original documents. The intervention is how the same corpus is organized for exploration, rather than whether the agent can access it at all. Raw Corpus exposes documents without an added navigation layer; CorpusMap adds Entity Pages and links to their source documents. The agent can still search raw files when a useful entity link is missing. [Section 4, p. 6](https://arxiv.org/pdf/2609.37226v1#page=6)

The main evaluation deliberately emphasizes multi-document questions. Its results therefore describe the selected subsets below, rather than every question in each benchmark or an arbitrary enterprise corpus.

## Benchmark selection and corpus composition

| Benchmark | Questions used in the main evaluation | Corpus presented to every method | Scope qualification |
| --- | --- | --- | --- |
| EnterpriseRAG-Bench | 80: Project Related (40), Conflicting Info (20), Completeness (20) | A fixed 2,819-document set containing the gold documents of all benchmark questions and their one-hop linked distractors | These are the categories in which every question has at least two annotated gold documents. Other categories include single-document and no-gold-document questions. |
| WixQA | 79 multi-article questions: ExpertWritten (52), Simulated (27) | The entire 6,221-article support knowledge base | Every Synthetic question and the other single-article questions are excluded from the main subset. |
| HERB | 238 content-based questions | 6,362 artifacts cited as evidence for those questions, plus three metadata files, totaling 6,365 documents | HERB simulates a software-company workspace; the evaluation uses one of its four answerable-question types. |

Source: [Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16). These are fixed, benchmark-specific corpora. In particular, the HERB corpus is constructed around the evidence artifacts for the selected questions; it should not be read as an unrestricted full-workspace retrieval test. Figure 4 separately expands the EnterpriseRAG-Bench corpus with distractors while retaining all gold documents.

Table 5 tests the remaining EnterpriseRAG-Bench questions with GPT-5.5. This is a separate extension; document recall there is calculated only for questions that have gold documents. The paper does not state the remaining-question count in that table. [Table 5, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16)

## Metrics: three axes with different meanings

| Metric | What the paper measures | Evaluation mechanism |
| --- | --- | --- |
| EnterpriseRAG-Bench document recall | Fraction of annotated gold documents present in the agent's selected supporting set | Computed directly, without an LLM judge |
| EnterpriseRAG-Bench correctness | Whether the answer addresses the core of the gold answer without contradicting it | Binary LLM judgment, averaged across questions |
| EnterpriseRAG-Bench completeness | Fraction of benchmark atomic answer facts supported by the generated answer | LLM judgment |
| WixQA context recall | How much essential reference-answer information appears in the context gathered by the agent | Official judge prompts; context includes tool outputs and any candidate list supplied with the question |
| WixQA factuality | How well the answer includes essential ground-truth information | Official judge prompts |
| HERB content | Answer agreement with the reference in factual accuracy, completeness, and relevance | Official evaluator |
| Input tokens | Input-token consumption accumulated across all agent LLM calls for one question | A trajectory-level efficiency measure |

All LLM-judged metrics in the main evaluation use **GPT-5.6 Sol**. Recall is not interchangeable across benchmarks: EnterpriseRAG-Bench checks selected document IDs, while WixQA checks information present in gathered context. Neither is a direct measurement of human trust, factual accuracy outside the reference, or task completion in a production workflow. [Section 4, p. 6; Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16)

### How Table 1's Overall Quality is aggregated

Overall Quality gives each benchmark equal weight after averaging that benchmark's reported quality metrics. It combines **answer and retrieval quality**, not just answer accuracy. A readable expansion of the paper's definition is:

```text
Q_Enterprise = (document_recall + correctness + completeness) / 3
Q_Wix        = (context_recall + factuality) / 2
Q_HERB       = content
Overall_Q    = (Q_Enterprise + Q_Wix + Q_HERB) / 3
```

For example, the GPT-5.5 Raw Corpus row gives approximately 66.11 after applying this formula to the displayed values. The 238 HERB questions do not receive more aggregate weight than the 80 EnterpriseRAG-Bench questions. Tables 2-4 and 8 evaluate only EnterpriseRAG-Bench; their Quality scores are the within-benchmark composite, not Table 1's three-benchmark aggregate. [Table 1, p. 7; Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=7)

### How relative input tokens are aggregated

For each model and benchmark, divide a method's average input-token count by Raw Corpus's count. Table 1 takes the geometric mean of those three ratios:

```text
r_benchmark = tokens_method / tokens_raw_corpus
Relative_Tokens = (r_Enterprise * r_Wix * r_HERB) ** (1 / 3)
```

A displayed ratio of 0.43 means a roughly 57% reduction in this aggregate. It does not mean 57% fewer tokens on every question, 57% less total token volume in the combined dataset, or 57% lower total system cost. These counts cover answering trajectories; construction has a separate one-time cost. The metric does not itself report output tokens, latency, memory, operational upkeep, or end-to-end financial cost. [Table 1, p. 7; Appendix A, p. 16; Section 5.2, p. 8](https://arxiv.org/pdf/2609.37226v1#page=16)

## Baselines and comparison boundaries

| Comparator | Added organization or context | What to remember |
| --- | --- | --- |
| Raw Corpus | No added navigation layer | Agent explores the original files. |
| Document Page | An LLM-generated key-fact page for each document | Organization remains centered on individual documents. |
| Group Page | One consolidated page per corpus-defined group, such as a folder | Group membership is supplied by the corpus. |
| LLM Wiki | LLM-written, cross-linked pages | The model has freedom to choose page organization. |
| Corpus2Skill | A topical hierarchy of summarized document clusters | Exploration proceeds through a hierarchy. |
| CorpusMap | Entity Pages linked to the documents referring to each entity | Documents can participate in several entity neighborhoods. |
| Gold Documents (Oracle) | Only annotated gold documents are provided | An idealized reference, not a comparable retrieval method. |

The same LLM builds the method artifacts and answers questions in Table 1. Its four models are GPT-5.5 and GPT-5.6 Luna, Terra, and Sol. Main table quality metrics are means and standard deviations over **three runs**. API calls for construction, answering, and judging occurred during August-September 2026. The auxiliary analyses mainly use GPT-5.5 and Luna, with DeepSeek-V4-Pro, MAI-Thinking-1, and Qwen3.8-27B added in specified settings. [Section 4, p. 6; Table 1, p. 7; Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=6)

The terminal-based agent follows the cited EnterpriseRAG-Bench agent protocol. It can list, search, inspect, and transform file text using shell tools, and add or remove documents from its supporting set. The paper says it uses a fixed per-question execution budget, but Sections 4 and Appendix A do not spell out a numeric budget. This companion does not infer one. [Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16)

Table 3 additionally compares BM25, dense retrieval, HippoRAG, and GraphRAG in a **retrieve-then-generate** setting. Their generator receives fixed retrieved context and does not explore the full corpus itself. This comparison evaluates the reported configurations of two interaction paradigms; it does not isolate graph representation alone or establish that every implementation of those systems must perform worse. [Section 5.1 and Table 3, p. 7](https://arxiv.org/pdf/2609.37226v1#page=7)

## Candidate paths are part of the default method

CorpusMap does not rely only on an unguided agent browsing Entity Pages. The default gives the agent candidate **linked-document file paths** selected for the question. Appendix B.3 describes the procedure:

1. Rank Entity Pages with BM25 using page name, type, overview, key facts, and entity aliases.
2. Pool the documents linked to the leading pages.
3. Rerank that pool with BM25 on document titles and contents.
4. Supply top candidates by title when available, path, and document ID, without document contents.

The agent can read those files or keep searching. Table 8 compares candidate Entity Pages, linked documents, both, no candidates, random candidates, and raw-corpus document candidates. Its results separate some of the map's benefit from the benefit of a relevant starting list. Figure 6 varies candidate counts while holding the other candidate-selection count fixed. [Appendix B.3, pp. 18-19](https://arxiv.org/pdf/2609.37226v1#page=18)

## What received a statistical test?

Appendix B.1 tests the **Overall Quality differences in Table 1** between CorpusMap and five baselines, separately for each of the four main GPT models. The procedure is:

1. Average each question's score across the three runs for each method.
2. Resample questions with replacement within each benchmark 100,000 times.
3. Recompute both methods' Overall Quality on the same sampled questions.
4. Correct the five baseline-comparison p-values within each LLM using Holm-Bonferroni.

The authors report 95% confidence intervals above zero for every comparison and Holm-corrected **p < 10^-4**. These are paired bootstrap intervals over questions after run averaging. They are distinct from Table 1's run standard deviations and are not an uncertainty model for new corpora, new model versions, or deployment costs. Table 6 does not establish significance for each individual metric, token difference, auxiliary analysis, or Table 2's additional model families. [Appendix B.1 and Table 6, p. 17](https://arxiv.org/pdf/2609.37226v1#page=17)

## Judge robustness and its limits

Appendix B.2 re-evaluates the **GPT-5.5 answers from Table 1**, using DeepSeek-V4-Pro with the same judging prompts. It changes the judge, rather than rerunning agents. CorpusMap remains highest among the retrieval methods on all five judged metrics. Rankings agree perfectly for correctness, completeness, and HERB content (Kendall's tau 1.00); agreement is lower for WixQA context recall (0.47) and factuality (0.83). [Table 7, p. 17; continuation on p. 18](https://arxiv.org/pdf/2609.37226v1#page=17)

This supports robustness of the leading method in that rejudged setting. It does not show that judges agree on absolute scores, that every rank is stable, or that all models and benchmark conditions were independently checked by humans. For the findings themselves, continue to [Results and analyses](results.md).
