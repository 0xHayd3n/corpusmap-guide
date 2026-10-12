# Limitations and questions worth testing

[Home](../README.md) · [Evaluation](evaluation.md) · [Results](results.md) · [Reproduction](reproduction.md)

This note separates **cautions stated or directly demonstrated by the paper** from **questions raised by the companion**. The latter are interpretation and future work, not findings attributed to the authors. Source: [arXiv:2609.37226v1](https://arxiv.org/abs/2609.37226v1).

## Cautions grounded in the paper

**Permissions and privacy.** Aggregating scattered facts about a person or project can concentrate sensitive information. Entity Pages can also reveal documents a user may not be permitted to access. The ethics statement calls for construction and serving that respect corpus access permissions, with privacy and content safeguards. A link or page should not be treated as permission to expose its sources. [Ethics statement, p. 10.](https://arxiv.org/pdf/2609.37226v1#page=10)

**Bias and harmful content.** The paper acknowledges that maps and answers may reflect harmful or biased corpus/model content. Source attribution helps inspection; it does not remove that risk. [Ethics statement, p. 10.](https://arxiv.org/pdf/2609.37226v1#page=10)

**Efficiency depends on the query interface.** Table 8's no-candidate map setting has higher quality but substantially more tokens than Raw Corpus. Relevant linked-document candidates are important to the reported efficiency. Random candidates perform worse and consume more tokens than the relevant default. Do not describe savings as the automatic effect of merely adding a graph. [B.3, pp. 18–19.](https://arxiv.org/pdf/2609.37226v1#page=18)

**Averages conceal exceptions.** Main Relative Tokens combines three benchmark ratios geometrically; it does not promise every benchmark uses fewer tokens. Table 2's MAI experiment improves quality while using more tokens than Raw Corpus. The seven tested model count spans multiple analyses and does not mean seven models were evaluated on every benchmark. [§4–5, pp. 6–9; Appendix A, p. 16.](https://arxiv.org/pdf/2609.37226v1#page=7)

**Offline work must be paid for.** Construction has a separate cost, recovered only after enough reuse in Figure 5's model. Figure 1 is an inference-cost comparison. Builder reuse and incremental additions reduce some costs, but one-time construction, refresh, storage, and query volume all matter. [§5.2, pp. 8–9; Fig. 5, p. 17.](https://arxiv.org/pdf/2609.37226v1#page=17)

**Source navigation is not factual proof.** The rendering prompt explicitly treats registry fields and extraction evidence as navigation metadata and requires factual page statements to come from raw documents. Resolution permits uncertainty, and unresolved observations create no links. These design choices acknowledge that identity and factual grounding require more than a matching name. [§3.3, p. 5; Figs. 12–13, pp. 28–29.](https://arxiv.org/pdf/2609.37226v1#page=29)

## Scope of the evidence

The main experiment selects 80 EnterpriseRAG-Bench, 79 WixQA, and 238 HERB questions. Corpora are fixed and methods share the same corpus in each comparison. HERB's corpus is evidence artifacts for the selected questions plus metadata; EnterpriseRAG-Bench's base corpus contains gold and one-hop distractor documents. This makes the task definition concrete but differs from an arbitrary live organizational corpus. Scaling adds distractors while preserving gold documents, reaching about 20k documents in Figure 4. [§4, p. 6; Appendix A, p. 16; Fig. 4, p. 9.](https://arxiv.org/pdf/2609.37226v1#page=16)

Judged metrics depend on model evaluators and benchmark reference answers. Re-judging GPT-5.5 answers with DeepSeek is useful evidence that the ranking is not unique to the main judge; it is not a human audit across all models or an estimate of every kind of factual error. Three-run standard deviations and paired-bootstrap intervals describe variability in the reported evaluation, not uncertainty about future deployments. [Table 1, p. 7; B.1–B.2, pp. 17–18.](https://arxiv.org/pdf/2609.37226v1#page=17)

## Companion analysis: unresolved questions

| Question | Why it matters | Useful future test |
| --- | --- | --- |
| How often do identity mistakes merge distinct subjects or split one subject? | False merges can route to unrelated evidence; false splits remove useful paths | Independently labeled mention clusters, per-type precision/recall, and downstream error attribution |
| What happens when useful subjects are singletons or absent from the catalog? | Retained entities require at least two linked documents; the corpus remains searchable, but the map cannot help every document equally | Compare covered/uncovered question classes and catalog changes |
| How are deletions, corrected documents, and identity changes propagated? | The reported update experiment adds chronological prefixes and rerenders changed neighborhoods | Delete/revoke/rename/revise sources and verify removal of stale facts and links |
| How is a page safely assembled for users with overlapping permissions? | A summary can reveal a fact even when direct source access is blocked | Permission-aware construction and serving tests, including aggregate facts and path disclosure |
| How does document order affect an initially empty registry? | Resolution updates a shared registry sequentially | Repeat builds under varied order; measure cluster and answer stability |
| What if a document contains hostile instructions or misleading identity evidence? | The rendering prompt asks the model to treat source text as data, but the paper does not quantify adversarial robustness | Controlled hostile-document and conflicting-source evaluation |
| Are savings maintained with current prices, latency, output tokens, and frequent rebuilds? | Input tokens and modeled query costs are only part of operational economics | Complete cost and latency accounting with realistic query/update volumes |
| Does the effect hold for broader corpora and tasks? | The evaluated datasets and scale define a bounded test | Different languages/domains, much larger corpora, negative/ambiguous questions, and authorization-sensitive tasks |

These tests are proposals from this reading companion. None was run here. The paper's map design offers navigational structure; it does not by itself certify production access control, identity accuracy, or robust factual reasoning.
