# Notation and glossary

[Repository overview](../README.md) · [Method walkthrough](method.md)

This glossary explains the notation and terminology used by **Soyeong Jeong, Sujay Kumar Jauhar, Sung Ju Hwang, and Andrew Joohun Nam** in *Follow the Entities: A Corpus Map for Agentic Search*, **arXiv:2609.37226v1**. It is an unofficial reading aid, not the paper's code or a reproduction. References use printed v1 pages: [PDF](https://arxiv.org/pdf/2609.37226v1) · [HTML](https://arxiv.org/html/2609.37226v1).

## Mathematical objects

The paper's formal task and graph definition appear in [§§3.1-3.2, p. 4](https://arxiv.org/pdf/2609.37226v1#page=4); construction variables appear in [Algorithm 1, p. 5](https://arxiv.org/pdf/2609.37226v1#page=5).

| Symbol | Meaning | Reading qualification |
| --- | --- | --- |
| $\mathcal{D}$ | The document corpus. | Documents remain accessible even when they have no retained entity neighbor. |
| $d$ | One document in $\mathcal{D}$. | It can participate in several entity neighborhoods. |
| $q$ | A question requiring evidence from multiple documents. | The map is constructed without knowing this particular question. |
| $\hat a_q$ | The answer produced for $q$. | This is a generated answer, not a gold reference. |
| $\hat{\mathcal{D}}_q \subseteq \mathcal{D}$ | The agent's selected supporting document set for $q$. | Accessed content and the explicitly selected supporting set need not be the same object. |
| $\mathrm{Agent}(q,\mathcal{D})$ | Raw-corpus agentic question answering. | The formal output contains both the answer and supporting set. |
| $\mathrm{Agent}(q,\mathcal{D};\mathcal{G})$ | Question answering with the reusable corpus map available. | $\mathcal{G}$ augments access to the original corpus. |
| $\mathcal{G}$ | The entity-document map. | The default is a bipartite graph, not a graph of direct entity relations. |
| $\mathcal{E}$ | The retained cross-document entities in the rendered map. | Each is linked to at least two distinct documents; $\mathcal{E}$ is not every extracted mention or every registry entry. |
| $e$ | One retained entity in $\mathcal{E}$. | It represents a resolved subject, not merely a word or a type label. |
| $\mathcal{N}(e) \subseteq \mathcal{D}$ | Documents whose mentions were resolved to $e$ during construction. | This is the stored neighborhood; it need not be every document in the world that concerns the subject. |
| $\mathcal{L}$ | The set of entity-document edges. | An edge records a resolved reference, not a semantic relation such as “owns” or “causes.” |
| $\mathcal{C}$ | The induced, fixed entity-type catalog. | Describes kinds of subjects and their identity criteria; it is distinct from the instance registry. |
| $\mathcal{E}^d_{\mathrm{local}}$ | Document-local entities extracted from document $d$. | Mentions of one subject are grouped locally before cross-document resolution. |
| $z$ | One document-local entity considered by the resolver. | The same spelling can still refer to different subjects across documents. |
| $\mathcal{R}$ | The shared entity registry, initially empty. | May contain entries that never satisfy the final cross-document retention rule. |
| $\delta$ | A resolution decision. | Algorithm 1 allows linking, addition, or recording an unresolved observation. |
| $p_e$ | The rendered Entity Page for retained entity $e$. | It exposes source-grounded summary information and its document neighborhood. |

## The graph equation in words

The paper defines

$$
\mathcal{G}=(\mathcal{E}\cup\mathcal{D},\mathcal{L}),\qquad
\mathcal{L}=\{(e,d)\mid e\in\mathcal{E},\ d\in\mathcal{N}(e)\}.
$$

The union contains two different node kinds. For each retained entity, include one edge to each document in its neighborhood. A document need not be assigned to one exclusive cluster. Its several entity links can offer several routes to other evidence. [Equation (1), §3.2, p. 4](https://arxiv.org/pdf/2609.37226v1#page=4)

If two entities have a common document, their neighborhoods intersect: $\mathcal{N}(e)\cap\mathcal{N}(e')$ is nonempty. The default map already permits a path from the first entity through that document to the second. Appendix B.4 studies direct edges that shorten this kind of path. The path expresses navigability; it does not by itself assert a factual relationship between the entities. [Appendix B.4, p. 19](https://arxiv.org/pdf/2609.37226v1#page=19)

## Terms that should stay distinct

| Term | Working definition | Do not conflate it with |
| --- | --- | --- |
| Entity type | A kind of identifiable subject with coherent identification and distinction rules. | A topical category or a particular subject instance. |
| Identity criteria | Evidence used to recognize instances, distinguish confusable subjects, and choose a canonical form. | A name-similarity score alone. |
| Catalog example | An observed subject string used to ground and explain a proposed type. | An already registered entity instance. |
| Surface form | Exact source text by which a document refers to a subject. | An inferred alias absent from the document. |
| Local entity | One subject observation within one document, potentially grouping several surface forms. | A fully resolved cross-document identity. |
| Registry entity | An instance established by the resolution process and stored in $\mathcal{R}$. | A rendered Entity Page; retention is a later step. |
| Canonical name | The name used for a registry entity. The new-entity prompt chooses it from a local surface form. | Proof that another similar string denotes the same subject. |
| Entity Page | A file representing a retained entity, with its summary, grounded facts, observed names, and source-document links. | An independent factual authority or the complete original documents. |
| Candidate registry entry | A plausible existing identity retrieved for construction-time comparison. | A query-time candidate document. |
| Query-time candidate | An initial file suggestion relevant to the current question. The default uses entity-linked document paths. | A fixed context that limits all further search. |
| Unresolved observation | A mention whose type or cross-document identity cannot be defensibly chosen. | A new entity or an existing-entity link. |
| Raw corpus | The original document collection exposed to the agent. | Documents omitted from the map; all original documents remain available. |
| Navigation layer | A persistent organization that helps the agent find sources across questions. | The answer-generation model or its search policy. |

Sources: [§3, pp. 4-6](https://arxiv.org/pdf/2609.37226v1#page=4), [Appendix B.3, p. 18](https://arxiv.org/pdf/2609.37226v1#page=18), and [Appendix C, Figures 7 and 11-13, pp. 21 and 27-29](https://arxiv.org/pdf/2609.37226v1#page=27).

## Resolution outcomes

| Algorithm label | Registry operation | Edge effect |
| --- | --- | --- |
| LINK | Update an existing entry with the grounded local observation. | Add the corresponding entity-document link. |
| ADD | Introduce a new entry for the observed subject. | Add its first entity-document link; it may still be a singleton until later observations arrive. |
| UNRESOLVED | Record the undecided observation. | Add no entity-document link for that observation. |

These uppercase labels are the paper's conceptual cases, not repository commands. The final graph filters links to keep only retained cross-document entities. “Added to the registry” and “published as an Entity Page” are therefore different events. [Algorithm 1 and §3.3, p. 5](https://arxiv.org/pdf/2609.37226v1#page=5)

## Evaluation vocabulary

The method formalizes three complementary axes: answer quality, retrieval quality, and context consumption. Their numerical metrics vary by benchmark. Read result tables with those distinctions intact. [§3.1, p. 4; Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16)

| Term | Meaning in this paper |
| --- | --- |
| Gold documents | Benchmark-annotated supporting documents, used as an evaluation reference. |
| Document recall | On EnterpriseRAG-Bench, the percentage of gold documents in the agent's selected supporting set; computed without an LLM judge. |
| Context recall | On WixQA, the judged presence of ground-truth information in gathered context, including tool outputs and any supplied candidate list. |
| Correctness | EnterpriseRAG-Bench's binary judgment of broad alignment with the reference answer and the core question. |
| Completeness | EnterpriseRAG-Bench's judged coverage of the reference answer's atomic facts. |
| Factuality | WixQA's official judged measure of essential ground-truth information in the answer. |
| Content | HERB's official judged score for factual accuracy, completeness, and relevance against a reference answer. |
| Overall Quality | Table 1's mean across benchmarks of each benchmark's mean quality metrics. It combines answer and retrieval measures; it is not a pure accuracy percentage. |
| Input tokens | Tokens accumulated across all LLM calls in one question's agent trajectory, rather than only the final prompt. |
| Relative tokens / Rel. Tok. | The geometric mean across benchmarks of a method's input-token ratio to the raw-corpus baseline. |
| Construction cost | The one-time cost of producing a reusable map; separate from the answering trajectory's token usage. |
| Amortized cost | Per-query cost after distributing construction cost across a specified number of queries served by the map. |
| Oracle | An idealized reference where the answering model receives only the gold documents. |

The definitions above follow [§4, p. 6 and Appendix A, p. 16](https://arxiv.org/pdf/2609.37226v1#page=16); cost separation follows [§5.2, pp. 8-9](https://arxiv.org/pdf/2609.37226v1#page=8). Metrics called “quality” should not be treated as interchangeable across benchmarks or as independent human-verified measurements.

[Back to repository overview](../README.md) · [Return to method walkthrough](method.md)
