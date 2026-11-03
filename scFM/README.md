# Single-cell foundation models and related representation methods

[← Back to PerTogether](../README.md)

This page covers general single-cell representation learning, RNA-to-protein translation, spatial context, and patient-level embeddings. These methods are not all perturbation-specific predictors. Task-specific annotation, integration, and multi-omics models from the original list are retained in a separate section rather than labeled as foundation models.

**Last checked: 3 November 2026.** Years use first online publication for journal articles, proceedings publication year for conference papers, and posting year for preprints. Meeting and proceedings years can differ. Workshop papers and preprints are labeled explicitly.

Model names link to papers or official proceedings. The Code column links to the official code repository; — means no public repository was found. The feature column distinguishes the main training objective from downstream applications; a perturbation demonstration does not mean the model was pretrained to predict perturbation responses. Full titles appear in the expandable reference list.

The **model structure** column links short architecture/type labels to archived diagrams in [model_figures](../model_figures/). Detailed architecture figures are preferred; otherwise Figure 1 / a method overview is used. Unavailable figures are marked explicitly. Toolkits and statistical methods retain their own type labels.

## Pretrained models and foundation-derived representations

| Model | Year | Publication / status | Features and scope | model structure | Code |
| :--- | :---: | :--- | :--- | :--- | :---: |
| [scBERT](https://www.nature.com/articles/s42256-022-00534-z) | 2022 | Nature Machine Intelligence | Masked-expression pretraining with gene and binned-expression embeddings; fine-tuned for cell-type annotation. | [Transformer (Performer)](../model_figures/scBERT_Figure1.png) | [GitHub](https://github.com/TencentAILabHealthcare/scBERT) |
| [CellLM](https://arxiv.org/pdf/2306.04371.pdf) | 2023 | arXiv preprint | Divide-and-conquer contrastive pretraining learns cell representations for annotation and drug-sensitivity tasks. | [Transformer](../model_figures/CellLM_Figure1.png) | [GitHub](https://github.com/PharMolix/OpenBioMed) |
| [Geneformer](https://www.nature.com/articles/s41586-023-06139-9) | 2023 | Nature | Rank-encoded transcriptome pretraining enables transfer learning and in silico gene perturbation; not trained primarily on Perturb-seq responses. | [Transformer](../model_figures/Geneformer_Figure1.jpg) | [Hugging Face](https://huggingface.co/ctheodoris/Geneformer) |
| [tGPT](https://www.cell.com/iscience/pdf/S2589-0042(23)00613-2.pdf) | 2023 | iScience | Autoregressive pretraining models gene-expression rankings to learn reusable transcriptome representations. | [Autoregressive transformer](../model_figures/tGPT_Figure1.jpg) | [GitHub](https://github.com/deeplearningplus/tGPT) |
| [Cell2Sentence](https://proceedings.mlr.press/v235/levine24a.html) | 2024 | ICML | Converts expression-ranked genes into text-like cell sentences to adapt language models for cell representation and generation. | [Autoregressive language model](../model_figures/Cell2Sentence_Figure1.png) | [GitHub](https://github.com/vandijklab/cell2sentence) |
| [CellPLM](https://openreview.net/forum?id=BKXvPDekud) | 2024 | ICLR | Pretrained cell-language model explicitly captures inter-cell relationships through cell-level representations. | [Cell-level transformer](../model_figures/CellPLM_Architecture_Figure2.png) | [GitHub](https://github.com/OmicsML/CellPLM) |
| [GenePT](https://www.nature.com/articles/s41551-024-01284-6) | 2024 | Nature Biomedical Engineering | Builds gene embeddings from text descriptions using a general language model; no large transcriptome-pretraining stage is required. | [Text-embedding model](../model_figures/GenePT_Figure1.png) | [GitHub](https://github.com/yiqunchen/GenePT) |
| [scFoundation](https://www.nature.com/articles/s41592-024-02305-7) | 2024 | Nature Methods | Read-depth-aware transcriptome pretraining learns gene/cell representations for multiple downstream tasks, including perturbation prediction. | [Asymmetric transformer](../model_figures/scFoundation_Figure1.png) | [GitHub](https://github.com/biomap-research/scFoundation) |
| [scGPT](https://www.nature.com/articles/s41592-024-02201-0) | 2024 | Nature Methods | Generative transcriptome pretraining supports multi-omics representations and task-specific fine-tuning, including perturbation prediction. | [Transformer](../model_figures/scGPT_Figure1.png) | [GitHub](https://github.com/bowang-lab/scGPT) |
| [SCimilarity](https://www.nature.com/articles/s41586-024-08411-y) | 2024 | Nature | Metric learning with cell-type supervision creates a shared space for scalable cell-state similarity search. | [Autoencoder + metric learning](../model_figures/SCimilarity_Figure1.png) | [GitHub](https://github.com/Genentech/scimilarity) |
| [scMulan](https://link.springer.com/chapter/10.1007/978-1-0716-3989-4_57) | 2024 | RECOMB 2024 | Multitask generative pretraining combines expression and metadata for annotation, metadata prediction, and conditional cell generation. | [Autoregressive transformer](../model_figures/scMulan_Figure1.png) | [GitHub](https://github.com/SuperBianC/scMulan) |
| [mcBERT](https://openreview.net/pdf/7c26dfa4dc9e49fb033965e77ec0050a7b7644a6.pdf) | 2025 | ICLR 2025 LMRL Workshop | Self-supervised and contrastive learning aggregate cells into patient-level representations; focuses on disease-cohort comparisons. | [Transformer + pooling](../model_figures/mcBERT_Figure1.png) | [GitHub](https://github.com/COMSYS/mcBERT) |
| [Nicheformer](https://www.nature.com/articles/s41592-025-02814-z) | 2025 | Nature Methods | Pretrained on dissociated and spatial transcriptomes to learn cell representations informed by tissue context. | [Transformer](../model_figures/Nicheformer_Figure1.png) | [GitHub](https://github.com/theislab/nicheformer) |
| [scTranslator](https://www.nature.com/articles/s41551-025-01528-z) | 2025 | Nature Biomedical Engineering | Pretrained RNA-to-protein translation; perturbation prediction is a downstream application, not the core pretraining task. | [Transformer encoder–decoder](../model_figures/scTranslator_Figure1.png) | [GitHub](https://github.com/TencentAILabHealthcare/scTranslator) |
| [PaSCient](https://doi.org/10.1016/j.cels.2026.101570) | 2026 | Cell Systems | Multi-level representation learning aggregates single-cell profiles into patient embeddings for disease-state characterization. | [DeepSets + attention pooling](../model_figures/PaSCient_Figure1.jpg) | [GitHub](https://github.com/Genentech/pascient) |
| [UCE](https://www.nature.com/articles/s41586-026-10689-z) | 2026 | Nature | Protein-language-model gene embeddings support self-supervised, cross-species cell representations and zero-shot embedding. | [Transformer](../model_figures/UCE_Figure1.png) | [GitHub](https://github.com/snap-stanford/UCE) |

GenePT derives representations from a general-purpose language model rather than a dedicated transcriptome-pretraining stage. mcBERT and PaSCient represent patient samples; they are not interchangeable with per-cell encoders.

## Related task-specific methods

| Model | Year | Publication / status | Features and scope | model structure | Code |
| :--- | :---: | :--- | :--- | :--- | :---: |
| [scMVP](https://link.springer.com/article/10.1186/s13059-021-02595-6) | 2022 | Genome Biology | Multi-view VAE jointly represents RNA and chromatin accessibility for integration and imputation; task-specific multi-omics model. | [Multi-view VAE](../model_figures/scMVP_Figure1.png) | [GitHub](https://github.com/bm2-lab/scMVP) |
| [TransCluster](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.1038919/full) | 2022 | Frontiers in Genetics | Task-specific transformer for supervised cell-type identification; not presented here as a broadly pretrained foundation model. | [Transformer](../model_figures/TransCluster_Figure1.jpg) | [GitHub](https://github.com/Danica123/TransCluster) |
| [CIForm](https://academic.oup.com/bib/article/24/4/bbad195/7169137) | 2023 | Briefings in Bioinformatics | Splits expression vectors into patches for transformer-based cell-type annotation; a task-specific classifier. | [Transformer](../model_figures/CIForm_Figure1.jpg) | [GitHub](https://github.com/zhanglab-wbgcas/CIForm) |
| [DeepMAPS](https://www.nature.com/articles/s41467-023-36559-0) | 2023 | Nature Communications | Heterogeneous cell–gene graph transformer infers cell-type-specific biological networks from multi-omics data; task-specific inference. | [Heterogeneous graph transformer](../model_figures/DeepMAPS_Figure1.png) | [GitHub](https://github.com/OSU-BMBL/deepmaps) |
| [scMoFormer](https://dl.acm.org/doi/pdf/10.1145/3583780.3615061) | 2023 | CIKM 2023 | Combines multimodal graphs and transformers to predict surface-protein abundance from RNA; task-specific cross-modal prediction. | [Graph transformers](../model_figures/scMoFormer_Figure1.png) | [GitHub](https://github.com/OmicsML/scMoFormer) |
| [scTransSort](https://www.mdpi.com/2218-273X/13/4/611) | 2023 | Biomolecules | Gene-expression embeddings and transformer features support cell-type annotation; a task-specific classifier. | [Transformer](../model_figures/scTransSort_Figure1.jpg) | [GitHub](https://github.com/jiaojiao-123/scTransSort) |
| [TOSICA](https://www.nature.com/articles/s41467-023-35923-4) | 2023 | Nature Communications | Supervised pathway/regulon-token transformer for interpretable cell-type annotation; not a general pretraining framework. | [Pathway-informed transformer](../model_figures/TOSICA_Figure1.png) | [GitHub](https://github.com/JackieHanLab/TOSICA) |

<details>
<summary>Full paper titles and sources</summary>

| Entry | Paper title |
| :--- | :--- |
| Cell2Sentence | [Cell2Sentence: Teaching Large Language Models the Language of Biology](https://proceedings.mlr.press/v235/levine24a.html) |
| CellLM | [Large-Scale Cell Representation Learning via Divide-and-Conquer Contrastive Learning](https://arxiv.org/pdf/2306.04371.pdf) |
| CellPLM | [CellPLM: Pre-training of Cell Language Model Beyond Single Cells](https://openreview.net/forum?id=BKXvPDekud) |
| CIForm | [CIForm as a Transformer-based model for cell-type annotation of large-scale single-cell RNA-seq data](https://academic.oup.com/bib/article/24/4/bbad195/7169137) |
| DeepMAPS | [Single-cell biological network inference using a heterogeneous graph transformer](https://www.nature.com/articles/s41467-023-36559-0) |
| Geneformer | [Transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9) |
| GenePT | [Simple and effective embedding model for single-cell biology built from ChatGPT](https://www.nature.com/articles/s41551-024-01284-6) |
| mcBERT | [Transformer-Based Integrative Patient Representations from Single-Cell RNA Data](https://openreview.net/pdf/7c26dfa4dc9e49fb033965e77ec0050a7b7644a6.pdf) |
| Nicheformer | [Nicheformer: a foundation model for single-cell and spatial omics](https://www.nature.com/articles/s41592-025-02814-z) |
| PaSCient | [Learning multi-cellular representations of single-cell transcriptomics data enables characterization of patient-level disease states](https://doi.org/10.1016/j.cels.2026.101570) |
| scBERT | [scBERT as a large-scale pretrained deep language model for cell type annotation of single-cell RNA-seq data](https://www.nature.com/articles/s42256-022-00534-z) |
| scFoundation | [Large-scale foundation model on single-cell transcriptomics](https://www.nature.com/articles/s41592-024-02305-7) |
| scGPT | [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0) |
| SCimilarity | [A cell atlas foundation model for scalable search of similar human cells](https://www.nature.com/articles/s41586-024-08411-y) |
| scMoFormer | [Single-Cell Multimodal Prediction via Transformers](https://dl.acm.org/doi/pdf/10.1145/3583780.3615061) |
| scMulan | [scMulan: a multitask generative pre-trained language model for single-cell analysis.](https://link.springer.com/chapter/10.1007/978-1-0716-3989-4_57) |
| scMVP | [A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data](https://link.springer.com/article/10.1186/s13059-021-02595-6) |
| scTranslator | [A pre-trained large generative model for translating single-cell transcriptomes to proteomes](https://www.nature.com/articles/s41551-025-01528-z) |
| scTransSort | [scTransSort: Transformers for Intelligent Annotation of Cell Types by Gene Embeddings](https://www.mdpi.com/2218-273X/13/4/611) |
| tGPT | [Generative pretraining from large-scale transcriptomes for single-cell deciphering](https://www.cell.com/iscience/pdf/S2589-0042(23)00613-2.pdf) |
| TOSICA | [Transformer for one stop interpretable cell type annotation](https://www.nature.com/articles/s41467-023-35923-4) |
| TransCluster | [TransCluster: A Cell-Type Identification Method for single-cell RNA-Seq data using deep learning based on transformer.](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.1038919/full) |
| UCE | [Universal cell embedding provides a foundation model for cell biology](https://www.nature.com/articles/s41586-026-10689-z) |

</details>
