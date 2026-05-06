# EpiCastBench: A Benchmark for Multivariate Epidemic Forecasting (Code)

This repository contains the codebase for EpiCastBench, a benchmark designed to evaluate multivariate epidemic forecasting models across diverse real-world datasets.

## Overview

EpiCastBench provides a standardized framework for training, evaluating, and comparing forecasting models under heterogeneous epidemic settings.

The benchmark is designed to assess model performance across:

* Multiple diseases
* Diverse geographic regions
* Varying temporal resolutions
* Complex statistical properties

## Dataset Access

The datasets used in this benchmark are hosted separately to ensure modularity and reproducibility.

👉 Dataset available via anonymous link on [Kaggle](https://www.kaggle.com/datasets/aimltsf/epicastbench)

After downloading, place the dataset in:

EpiCastBench/data/

## Setup

```bash
git clone <repo_url>
cd EpiCastBench
pip install -r requirements.txt
```

## Running the Code

```
python Code/main.py
```

## Repository Structure

```
EpiCastBench/
│
├── code/
│   ├── config.py        # experiment and model configuration
│   ├── data_loader.py   # dataset loading and preprocessing
│   ├── evaluator.py     # evaluation metrics and benchmarking
│   ├── main.py          # main training and evaluation entry point
│   ├── models.py        # forecasting model implementations
│   └── utils.py         # utility functions
│
├── data/                # place downloaded datasets here
├── requirements.txt     # Python dependencies
└── README.md
```

## Models Implemented

EpiCastBench includes a diverse set of forecasting baselines and modern deep learning models to ensure comprehensive benchmarking.

- Naive
- Random Forest
- XGBoost
- LSTM
- TCN
- Transformer
- N-BEATS
- N-HiTS
- DeepAR
- DLinear
- TSMixer
- TiDE
- KAN
- Chronos2
- TimesFM

All models are implemented in `code/models.py` and are evaluated under a unified training and testing pipeline defined in `code/main.py`.

## Reproducibility

All experiments are designed to be reproducible using:

* Fixed random seeds
* Standardized data splits
* Unified evaluation metrics

## License

This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Anonymity Notice

This repository is released for anonymous peer review.
Identifying information (e.g., authors, affiliations, and repository ownership) has been removed and will be restored after the review process.
