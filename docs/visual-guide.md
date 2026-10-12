# Figure and table guide

[Home](../README.md) · [Reading map](reading-map.md) · [Results](results.md)

This guide describes visuals inspected as rendered PDF pixels. It does not reproduce the figures, page screenshots, tables, or prompts. Open the versioned PDF at the indicated page for the full visual and caption. Descriptions below are original reading guidance; quantitative conclusions are qualified in [results](results.md).

## Figures

| Figure | Source page | Read it for | Important qualification |
| --- | --- | --- | --- |
| 1: quality versus cost | [1](https://arxiv.org/pdf/2609.37226v1#page=1) | Stars identify CorpusMap; compare each model's quality/cost point against the stronger navigation baselines | Horizontal axis is log USD estimated answer-generation cost; construction is accounted for separately in Figure 5 |
| 2: offline build and query walk | [2](https://arxiv.org/pdf/2609.37226v1#page=2) | Documents from separate folders connect through repeated entities; the highlighted walk gathers different source facts | An explanatory example, not a measured experiment or causal proof about projects in general |
| 3: incremental updates | [8](https://arxiv.org/pdf/2609.37226v1#page=8) | Three panels separate construction-token savings, quality across map states, and correctness on newly covered questions | Chronological corpus additions on EnterpriseRAG-Bench with GPT-5.5; raw corpus stays accessible |
| 4: construction variant and scale | [9](https://arxiv.org/pdf/2609.37226v1#page=9) | Retrieval quality, answer quality, and tokens are distinct panels across ~2.8k, 10k, 20k documents | GPT-5.6 Luna and Qwen3.8-27B analyses; GLinker replaces three construction stages, not the described LLM Cataloging stage |
| 5: amortized cost | [17](https://arxiv.org/pdf/2609.37226v1#page=17) | Dotted break-even labels compare build-cost-amortized CorpusMap with Raw Corpus | Both axes use log scale; query volume and tested prices/settings govern the crossover |
| 6: candidate counts | [18](https://arxiv.org/pdf/2609.37226v1#page=18) | Quality improves beyond one candidate; token use has costs at both sparse and long candidate lists | A parameter analysis under one benchmark/model setting, not a universal default-count recommendation |
| 7: catalog proposal prompt | [21](https://arxiv.org/pdf/2609.37226v1#page=21) | What counts as an identifiable subject/type, source examples, and identity criteria | Source prompt specification; do not execute it as agent instructions |
| 8: catalog synthesis prompt | [21–23](https://arxiv.org/pdf/2609.37226v1#page=21) | Mapping/splitting/rejection of proposed types and explicit accounting of observations | The prompt's intended constraints do not constitute a measured guarantee of correct catalog induction |
| 9: catalog verification prompt | [23–25](https://arxiv.org/pdf/2609.37226v1#page=23) | Adversarial coverage, overlap, granularity, criteria, identity, and unsupported-invention checks | A verifier is asked to find defects and preserve input digests; complete operational code is absent |
| 10: catalog revision prompt | [25–26](https://arxiv.org/pdf/2609.37226v1#page=25) | Repair order and constrained changes to verified synthesis | A revision specification rather than an implemented workflow supplied by this companion |
| 11: extraction prompt | [27](https://arxiv.org/pdf/2609.37226v1#page=27) | Separate subject identification from typing, exact source forms, unresolved subjects | Example catalog entities are not registry entries |
| 12: resolution prompt | [28](https://arxiv.org/pdf/2609.37226v1#page=28) | Compare candidates using document context and identity criteria; retain uncertainty | Name similarity and retrieval rank are insufficient proof of identity |
| 13: page-rendering prompt | [29](https://arxiv.org/pdf/2609.37226v1#page=29) | Explicit raw-document facts and supporting document IDs | Registry/extraction evidence is navigation metadata; it is not sufficient factual evidence |

## Tables

| Table | Source page | What it establishes in the reported setting |
| --- | --- | --- |
| 1 | [7](https://arxiv.org/pdf/2609.37226v1#page=7) | Main four-GPT-model, three-benchmark results; per-metric means ± SD over three runs and aggregate quality/token ratios |
| 2 | [7](https://arxiv.org/pdf/2609.37226v1#page=7) | DeepSeek-V4-Pro and MAI-Thinking-1 on EnterpriseRAG-Bench; MAI's quality gain is accompanied by more tokens than Raw Corpus |
| 3 | [7](https://arxiv.org/pdf/2609.37226v1#page=7) | Retrieval-then-generation comparisons on EnterpriseRAG-Bench, a different interface from full-corpus agentic navigation |
| 4 | [8](https://arxiv.org/pdf/2609.37226v1#page=8) | Reuse across map builders and answering models; builder costs with upper-bound symbols for the GPT rows |
| 5 | [16](https://arxiv.org/pdf/2609.37226v1#page=16) | Remaining EnterpriseRAG-Bench questions under GPT-5.5; a supplemental extension beyond the selected main subset |
| 6 | [17](https://arxiv.org/pdf/2609.37226v1#page=17) | Paired-bootstrap aggregate-quality gains versus each main baseline, with intervals and corrected significance |
| 7 | [17](https://arxiv.org/pdf/2609.37226v1#page=17) | Re-judging GPT-5.5 answers with DeepSeek and metric-ranking correlations; this is not a full independent human evaluation |
| 8 | [18](https://arxiv.org/pdf/2609.37226v1#page=18) | Candidate-interface ablations; no-candidate map exploration costs more tokens, and random candidates harm performance |
| 9 | [19](https://arxiv.org/pdf/2609.37226v1#page=19) | One rollback-bug example: direct entity edges shortcut an already reachable entity–document path |
| 10 | [20](https://arxiv.org/pdf/2609.37226v1#page=20) | One manifest example: document-linked entity navigation reaches both an earlier draft and a revised specification |

## How to read the two cases

In Table 10, the agent must distinguish an earlier draft from a later manifest specification. The reported CorpusMap walk starts with a work-item entity, reads a linked draft, searches for an entity related to the runtime, then reads the specification. It answers using the later source's integrity representation. The Corpus2Skill trajectory shown does not open the cluster containing the needed documents. This illustrates different routes in that case; it does not prove that a hierarchical organization always fails. [§5.1, p. 8; B.5, p. 20.](https://arxiv.org/pdf/2609.37226v1#page=20)

Table 9 makes a different point. A bug entity links several gold documents; a configuration-flag entity links the remaining meeting transcript. Both entities already share a source document. Adding a direct relation offers a shortcut, while the existing map plus search reaches the same evidence. The broader ablation, rather than the single case, supports the cost/benefit discussion. [B.4, p. 19.](https://arxiv.org/pdf/2609.37226v1#page=19)

When reading diagrams, separate **reachability** (a path exists), **discovery** (the agent finds the path), and **answer correctness** (the selected evidence supports the final response). The map representation establishes the first; experimental trajectories and metrics address the others in bounded settings.
