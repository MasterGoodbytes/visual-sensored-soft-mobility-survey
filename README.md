![Laboratory banner](./figures/les2banner.png)

# Visual Observation of Soft Mobility

Understanding the aspects of soft mobility is important for assisting, protecting, and planning for pedestrians, cyclists, and scooter users. Advances in learning-based visual sensing are expanding the use of these technologies to observe and monitor soft-mobility users and their environments.

This repository contains the data-processing and analysis workflow for a survey of visual monitoring of soft mobility over the last decade. The study examines trends in the bibliography through semantic analysis and classifies the included literature by vision methodologies, reported monitoring setups, observed areas, and whether or how privacy is considered. It also discusses key challenges and aims to support informed research and development in urban mobility.

The analysis workflow combines bibliographic data processing, LLM-assisted screening with a manually labeled hold-out set, corpus descriptives, term-based analysis, and structured research-question extraction.

## Analysis workflow

The current notebooks in `notebooks/` are intended to be run in this order:

1. `01-Scopus_Data_Extraction.ipynb` — retrieve bibliographic records from Scopus.
2. `02-Extract_Scopus_Data.ipynb` — clean and structure the retrieved records.
3. `03-Extract_Intro_and_Contribution.ipynb` — add introduction and contribution text where available.
4. `04_LLM_Screening.ipynb` — screen records against the visual-monitoring eligibility criteria, validate against the manually labeled hold-out, and produce the screened corpus.
5. `05_Corpus_Descriptives.ipynb` — summarize the screened corpus, including publication, keyword, and geographic distributions.
6. `06_Term_Metrics.ipynb` — calculate and review term-based metrics for the screened corpus.
7. `07_RQ_Extraction.ipynb` — extract structured information for the review research questions and create records for manual review.

Some notebooks require access credentials for Scopus or an LLM provider. Configure credentials locally, using environment variables or a local configuration file, and never commit API keys, passwords, or other secrets.

## Getting started

1. Install Python and Jupyter Notebook or JupyterLab.
2. Install the dependencies listed in `notebooks/requirements.txt` from the repository root.
3. Configure any required API credentials locally.
4. Open the notebooks and run them in workflow order. Many notebooks use paths relative to `notebooks/`, so run them from that directory or keep the configured working directory consistent.

The LLM screening notebook can reuse saved inference results when available. For a new corpus or changed prompt, verify the input paths and screening configuration before running it. The hold-out labels are for evaluation; do not use test-set results to tune prompts or screening rules if reporting them as final test metrics.

## Repository structure

- `data/` — bibliographic inputs, processed records, screening outputs, caches, and analysis results.
- `figures/` — project figures and generated visualizations.
- `model/` — model experiments, training materials, and labeled datasets used during development.
- `notebooks/` — the current analysis workflow, supporting files, and archived notebooks.
- `results/` — exported analysis tables.

Some files are intermediate outputs, local caches, or historical experiments rather than required inputs for every workflow. Check each notebook's configuration and output paths before reusing or removing data.

## Article

**TODO:** Add the final article title, author list, publication status, citation, and DOI or URL when available.

## Data and access

Bibliographic metadata and analysis outputs are provided for research and reproducibility. Access to source databases, full-text articles, and third-party datasets may be subject to their own terms and copyright restrictions. Verify the applicable permissions before sharing or redistributing those materials.
