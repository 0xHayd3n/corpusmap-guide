# Results and analyses

[Repository overview](../README.md) · [Evaluation protocol](evaluation.md)

These original notes summarize results **reported by the paper's authors** in *Follow the Entities: A Corpus Map for Agentic Search*, arXiv:2609.37226v1. This companion has not reproduced the experiments. Tables below selectively reorganize or compute comparisons from reported values; they are not copies of the paper's full result tables. Read the [metric definitions and aggregation rules](evaluation.md#metrics-three-axes-with-different-meanings) before interpreting the scores.

## Main finding: better aggregate quality, lower aggregate input-token ratio

Among the comparable retrieval/navigation methods, CorpusMap has the highest mean on every quality metric in Table 1 for the four main GPT models and three selected benchmark subsets. Its Overall Quality is a dataset-balanced combination of answer and retrieval metrics. The relative token column is a geometric mean of benchmark-specific input-token ratios to Raw Corpus. [Section 5.1, pp. 6-7; Table 1, p. 7](https://arxiv.org/pdf/2609.37226v1#page=7)

| Answering/building model | Overall Quality: Raw Corpus → CorpusMap | Reported bootstrap gain over Raw Corpus and 95% CI | Relative input tokens in Table 1 | Approximate aggregate reduction from the rounded ratio |
| --- | --- | --- | --- | --- |
| GPT-5.5 | 66.11 → 72.55 | +6.45 [4.30, 8.62] | 0.43 | 57% |
| GPT-5.6 Luna | 53.85 → 65.58 | +11.74 [9.40, 14.07] | 0.65 | 35% |
| GPT-5.6 Terra | 65.75 → 72.51 | +6.76 [4.34, 9.19] | 0.66 | 34% |
| GPT-5.6 Sol | 67.69 → 74.68 | +7.00 [5.05, 8.94] | 0.43 | 57% |

Quality/token entries come from Table 1; gains and intervals come from [Table 6, p. 17](https://arxiv.org/pdf/2609.37226v1#page=17). Tiny differences between subtracting the rounded Table 1 scores and Table 6's reported gains are consistent with rounding. The reduction column is this companion's calculation, `100 * (1 - displayed relative ratio)`.

Table 6 also reports significant Overall Quality gains over Document Page, Group Page, LLM Wiki, and Corpus2Skill for all four models, with Holm-corrected p < 10^-4. That statistical claim is specific to the main aggregate-quality comparisons; the [evaluation notes](evaluation.md#what-received-a-statistical-test) explain its resampling and correction. The weaker results of some other navigation layers support the authors' claim that adding structure alone does not ensure improvement. They do not prove that all non-entity organizations are intrinsically ineffective.

### Token savings are not uniform

The cross-benchmark aggregate hides individual increases. These are selected counterexamples from the visually checked columns of [Table 1, p. 7](https://arxiv.org/pdf/2609.37226v1#page=7):

| Setting | Raw Corpus input tokens → CorpusMap input tokens | Change computed from the displayed values |
| --- | --- | --- |
| Terra, EnterpriseRAG-Bench | 70.9k → 76.2k | About 7.5% more |
| Sol, EnterpriseRAG-Bench | 55.5k → 56.2k | About 1.3% more |
| Luna, HERB | 219.4k → 254.2k | About 15.9% more |
| Terra, HERB | 288.3k → 289.4k | About 0.4% more |

Conversely, WixQA shows large reductions for all four models. A defensible summary is therefore **lower geometric-mean input-token ratios across the three benchmarks**, together with higher reported quality, rather than savings for every model/benchmark pair.

### The Oracle is an idealized reference

The Gold Documents rows provide only gold evidence, bypassing the retrieval problem. CorpusMap narrows the aggregate gap to this reference, but the Oracle is not a competing deployable retrieval system. Its Overall Quality is about 79.6-80.0 in Table 1; CorpusMap's is about 65.6-74.7. Some individual CorpusMap means slightly exceed the corresponding Oracle means, so the Oracle should not be treated as a strict numerical upper bound on every judged metric. [Table 1, p. 7](https://arxiv.org/pdf/2609.37226v1#page=7)

## Extensions beyond the main table

### Additional model families: quality transfers, token reductions vary

Table 2 evaluates only EnterpriseRAG-Bench. CorpusMap's within-benchmark Quality is highest among the listed methods with both additional models:

- **DeepSeek-V4-Pro:** Raw Corpus 68.02 → CorpusMap 71.11, a computed +3.09 points; input tokens 1,349.4k → 1,043.3k, about 22.7% fewer.
- **MAI-Thinking-1:** Raw Corpus 34.06 → CorpusMap 45.07, a computed +11.01 points; input tokens 129.6k → 158.8k, about 22.5% more.

The MAI result is a useful counterexample to universal token-efficiency claims. Quality generalization is supported in these two reported configurations; token reduction is not shared by both. Table 2 does not provide the three-run deviations or bootstrap intervals shown for the main table. [Section 5.1 and Table 2, p. 7](https://arxiv.org/pdf/2609.37226v1#page=7)

### Retrieve-then-generate comparisons

On EnterpriseRAG-Bench, Table 3 gives CorpusMap Quality 76.60 with GPT-5.5 and 73.20 with Luna. The strongest listed fixed-context retrieval comparator is dense retrieval at 65.05 for GPT-5.5 and HippoRAG at 61.74 for Luna. The computed gaps are +11.55 and +11.46 points respectively. Raw Corpus agentic search scores 65.60 and 63.31 in the same table. [Table 3, p. 7](https://arxiv.org/pdf/2609.37226v1#page=7)

BM25, dense retrieval, HippoRAG, and GraphRAG here supply a fixed context to a generator that cannot search the whole corpus. CorpusMap's agent can continue exploration. The comparison therefore includes that interaction difference and should not be framed as a controlled proof that a bipartite graph alone is superior to every knowledge-graph retriever. [Section 5.1, pp. 7-8](https://arxiv.org/pdf/2609.37226v1#page=7)

### Questions outside the main multi-document subset

With GPT-5.5 on the remaining EnterpriseRAG-Bench questions, Table 5 reports increases over Raw Corpus of **+5.64 document-recall points, +5.71 correctness points, and +3.16 completeness points**, calculated from its displayed means. Input tokens fall from 250.7k to 171.7k, about 31.5%. The authors describe most of these questions as single-document; the remaining set also includes categories without annotated gold documents, and recall is evaluated only where gold documents exist. This is one model on one benchmark extension. [Section 5.1, p. 7; Table 5, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16)

## Reuse and construction economics

### Builder and answering model can differ

Table 4 is a map-builder × answering-model matrix for EnterpriseRAG-Bench. A Luna-built map improves over Raw Corpus for every tested answering model. Computed improvements are +7.99 points for GPT-5.5, +5.14 for Sol, +9.89 for Luna, and +2.88 for DeepSeek. This demonstrates cross-model reuse in the tested settings, including across model families. [Table 4, p. 8](https://arxiv.org/pdf/2609.37226v1#page=8)

The construction-cost column displays **upper bounds** for GPT-5.5 (≤$4,732.14), Sol (≤$2,681.76), and Luna (≤$74.65), and $310.58 for DeepSeek. Preserve those inequality signs when citing costs. The table is not a price quote for rebuilding a different corpus today. A more expensive builder is also not uniformly best: Sol-built maps lead for GPT-5.5 and Sol answering, while other builders lead in the remaining columns. The table does not report significance for those between-builder differences.

### Break-even requires repeated queries

The paper separates one-time map construction from answer-generation cost. Its amortization calculation has the form:

```text
amortized_map_cost_per_query(N) = construction_cost / N + map_query_cost
```

Figure 5 marks approximate break-even query counts per corpus: **9.0k for GPT-5.5, 12.4k for Sol, 17.3k for Terra, and 26.3k for Luna**. Before break-even, the plotted map cost including construction is higher than Raw Corpus; after it, reuse spreads the construction cost across enough queries to make the plotted average lower. [Section 5.2, p. 8; Figure 5, p. 17](https://arxiv.org/pdf/2609.37226v1#page=17)

These values depend on the paper's cost estimates, corpus, model, and query mix. The curve is an amortization model, not a measured service deployment with guaranteed savings. Corpus updates, rebuilding, price changes, storage, and operational labor can change the economic result. The lower per-query figures in Figure 1 should not be quoted as already including the one-time build.

## Maintenance, scaling, and alternative construction

### Incremental updates

The authors order EnterpriseRAG-Bench documents by benchmark timestamps and grow the map over successive corpus prefixes. They reuse the registry and rerender only Entity Pages whose linked documents change. The agent can search the **full raw corpus at every map state**, so new map coverage is tested beyond merely making documents accessible. [Section 5.2, p. 9](https://arxiv.org/pdf/2609.37226v1#page=9)

Figure 3 reports construction-token savings of **34%, 69%, and 71%** for the three updates relative to full rebuilds. On questions whose evidence becomes covered in each update, annotated correctness gains are **+30.4, +40.0, and +40.0 percentage points**. The final incremental map performs comparably to the full rebuild in the plotted quality measures. These are update-specific findings, not a universal savings rate for arbitrary additions, deletions, or changed documents. [Figure 3, p. 8](https://arxiv.org/pdf/2609.37226v1#page=8)

### Scaling with distractors and an open-weight answering model

Figure 4 compares EnterpriseRAG-Bench corpora of roughly **2.8k, 10k, and 20k documents**. Larger versions add distractors while preserving gold evidence. CorpusMap remains ahead of Raw Corpus in the displayed retrieval and answer aggregates while using fewer input tokens, for GPT-5.6 Luna and Qwen3.8-27B in the plotted configurations. This tests increasing distractor volume on one benchmark, rather than evidence distribution changes across new organizations or arbitrary million-document collections. The plot does not provide confidence intervals or exact labels for every quality point; these notes use its directional comparisons rather than invented exact scores. [Figure 4 and Section 5.2, p. 9](https://arxiv.org/pdf/2609.37226v1#page=9)

### What the off-the-shelf experiment actually replaces

The GLinker variant uses open GLiNER models for entity extraction/linking and deterministic rendering from extracted evidence. Section 5.2 explicitly instantiates **Extraction, Resolution, and Rendering** without LLM calls. Figure 4 shows it is comparably effective to the LLM-built map in the plotted GPT setting and benefits Qwen answering as well. [Section 5.2 and Figure 4, p. 9](https://arxiv.org/pdf/2609.37226v1#page=9)

Cataloging is a separate stage: Section 3.3 describes inducing and verifying the entity-type catalog with an LLM. The specified off-the-shelf substitution therefore does not by itself establish a fully specified, end-to-end pipeline in which every construction stage is LLM-free. A zero-LLM claim should identify how the catalog is supplied. [Section 3.3, p. 5](https://arxiv.org/pdf/2609.37226v1#page=5)

## Ablations: relevant starting paths matter

In the GPT-5.5 EnterpriseRAG-Bench candidate analysis, CorpusMap without candidates reaches Quality **69.04**, above Raw Corpus's **65.60**, but uses **496.4k** input tokens versus **206.5k**. The default relevant linked-document candidates reach **76.60** with **88.1k** tokens. Both candidate types reach the highest displayed Quality, **77.43**, at **102.7k** tokens. Relevant Entity Page candidates reach **76.68** at **247.1k** tokens. Thus, the highest-quality candidate configuration and the lowest-token configuration are different. [Table 8, p. 18](https://arxiv.org/pdf/2609.37226v1#page=18)

Random linked-document candidates instead yield **60.76** with **413.5k** tokens. Relevant raw-corpus document candidates yield **66.19** with **107.4k** tokens, a modest quality increase over raw search while approximately halving its input tokens. Together, these comparisons support both the usefulness of a map without candidates and the substantial contribution of relevance-based candidate selection. They do not support crediting all improvements exclusively to graph traversal. [Appendix B.3 and Table 8, p. 18](https://arxiv.org/pdf/2609.37226v1#page=18)

Figure 6 shows a large quality improvement when moving beyond a single candidate Entity Page or linked document, followed by a relatively broad plateau rather than a monotonic increase. The authors explain elevated tokens with one linked document as additional self-directed search, and with many documents as the repeated input cost of a longer candidate list. The plot supports sensitivity analysis in this setting, not a universal optimal candidate count. [Figure 6, p. 18; Appendix B.3 continuation, p. 19](https://arxiv.org/pdf/2609.37226v1#page=18)

## Ablations: direct entity-entity edges add little in this setting

The default map links entities to documents. Appendix B.4 adds direct entity-entity edges, either extracted relations or co-document pairs. In this test, both edge types join entities already connected through a shared document. They shorten existing paths instead of making previously unreachable pages reachable. Text search can also find related Entity Pages. [Appendix B.4, p. 19](https://arxiv.org/pdf/2609.37226v1#page=19)

The reported navigation diagnostics are:

- Without direct edges, **86-90%** of newly opened Entity Pages are found through search.
- When edges exist, the agent follows them on **11-19%** of questions; **71%** of those moves find no new gold document.
- Of gold documents first reached through an edge, **79%** are retrieved for that question without the direct edges as well.
- Recall changes by only **-2.6 to +0.2 points**, while Entity Pages grow by **27-52%** on average and input tokens increase by as much as **28%**.

These diagnostics support the authors' choice of a simpler bipartite map for the examined setting. They do not establish that direct relations are useless when they add information not recoverable through shared documents, when search tools differ, or in every corpus. [Appendix B.4, p. 19](https://arxiv.org/pdf/2609.37226v1#page=19)

## Two case studies: mechanisms, not frequency estimates

**Table 9, direct-edge shortcut.** An incident page links four of five gold documents. A configuration-flag page links the missing meeting transcript. A relation edge can point to that page, but the existing shared source document and text mentions already connect the two pages. The authors show the agent recovering the same five documents through search without direct edges. [Table 9, p. 19](https://arxiv.org/pdf/2609.37226v1#page=19)

**Table 10, resolving a specification change.** A manifest draft and its final v1 specification live in different sources. The displayed Corpus2Skill trajectory misses their cluster. CorpusMap instead moves from a work-item Entity Page to the draft, then uses its terms to find another Entity Page linked to the v1 document. That second document changes the answer from an embedded signature to optional integrity information and a reference URI. The value illustrated is finding the revision that qualifies the first source, rather than answering from the draft alone. [Section 5.1, p. 8; Appendix B.5 and Table 10, p. 20](https://arxiv.org/pdf/2609.37226v1#page=20)

These examples explain how alternate paths and source inspection can help. They are selected demonstrations, not estimates of how often either navigation pattern occurs.
