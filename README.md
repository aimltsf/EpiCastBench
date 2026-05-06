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
- DLinear [[Zeng et al., 2023]](https://dl.acm.org/doi/10.1609/aaai.v37i9.26317)
- Random Forest [[Breiman, 2001]](https://doi.org/10.1023/A:1010933404324)
- XGBoost [[Chen et al., 2016]](https://doi.org/10.1145/2939672.2939785)
- TSMixer [[Chen et al., 2023]](https://openreview.net/pdf?id=wbpxTuXgm0)
- KAN [[Liu et al., 2025]](https://openreview.net/forum?id=Ozo7qJ5vZi)
- LSTM [[Hochreiter et al., 1997]](https://www.bioinf.jku.at/publications/older/2604.pdf)
- DeepAR [[Salinas et al., 2020]](https://doi.org/10.1016/j.ijforecast.2019.07.001)
- TCN [[Chen et al., 2020]](https://doi.org/10.1016/j.neucom.2020.03.011)
- NBeats [[Oreshkin et al., 2020]](https://openreview.net/forum?id=r1ecqn4YwB)
- NHiTS [[Challu et al., 2023]](https://doi.org/10.1609/aaai.v37i6.25854)
- Transformer [[Vaswani et al., 2017]](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
- TiDE [[Das et al., 2023]](https://openreview.net/forum?id=pCbC3aQB5W)
- Chronos2 [[Ansari et al., 2025]](https://arxiv.org/abs/2510.15821)
- TimesFM [[Das et al., 2024]](https://openreview.net/forum?id=jn2iTJas6h)

All models are implemented in `Code/models.py` and are evaluated under a unified training and testing pipeline defined in `Code/main.py`.

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
