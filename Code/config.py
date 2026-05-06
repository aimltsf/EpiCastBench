# -----------------------------
# Dataset Configuration
# -----------------------------
# List of all epidemic time-series datasets used in EpiCastBench.
# Each dataset corresponds to a disease-region pair.

DATASETS = [
    "chickenpox_hungary.csv", "covid_india.csv", "dengue_malaysia.csv", "chikungunya_brazil.csv", "covid_ireland.csv",
    "dengue_panama.csv", "chikungunya_colombia.csv", "covid_italy.csv", "dengue_peru.csv", "covid_australia.csv",
    "covid_japan.csv", "dengue_philippines.csv", "covid_belgium.csv", "covid_mexico.csv", "dengue_taiwan.csv",
    "covid_brazil.csv", "covid_netherlands.csv", "influenza_us2.csv", "covid_canada2.csv", "covid_spain.csv",
    "influenza_us.csv", "covid_canada.csv", "covid_switzerland.csv", "measles_us.csv", "covid_chile.csv",
    "covid_uk.csv", "covid_china.csv", "covid_us.csv", "tuberculosis_china.csv", "covid_colombia.csv",
    "dengue_argentina.csv", "tuberculosis_japan.csv", "covid_czech.csv", "dengue_brazil.csv", "zika_colombia.csv",
    "covid_eu.csv", "dengue_colombia.csv", "zika_mexico.csv", "covid_germany.csv", "dengue_malaysia2.csv"
]

# -----------------------------
# Forecasting Horizon Settings
# -----------------------------
# The forecasting horizon defines how far into the future the model predicts.
#
# Available options:
#   - "short"  : short-term forecasting
#   - "medium" : medium-term forecasting
#   - "long"   : long-term forecasting (default setting)
#
# You can change this value to evaluate model performance under different forecasting regimes.

HORIZON_TYPE = "long" # Choose between "long", "medium", "short"

# -----------------------------
# Window Configuration
# -----------------------------
# INPUT_CHUNK: number of past timesteps used as model input
# OUTPUT_CHUNK: number of future timesteps to predict, multistep forecasts are made iteratively
# These define the sliding window for supervised learning.

INPUT_CHUNK = 24
OUTPUT_CHUNK = 12
N_EPOCHS = 50
RANDOM_STATE = 42

# Mapping from dataset name to sampling frequency.
# Used to correctly interpret temporal resolution across heterogeneous datasets.

DATA_FREQUENCY_MAPPING = {
    "chickenpox_hungary": "weekly",
    "chikungunya_brazil": "monthly",
    "chikungunya_colombia": "weekly",
    "covid_australia": "daily",
    "covid_belgium": "daily",
    "covid_brazil": "daily",
    "covid_canada": "daily",
    "covid_canada2": "weekly",
    "covid_chile": "daily",
    "covid_china": "daily",
    "covid_colombia": "daily",
    "covid_czech": "daily",
    "covid_eu": "daily",
    "covid_germany": "daily",
    "covid_india": "daily",
    "covid_ireland": "daily",
    "covid_italy": "daily",
    "covid_japan": "daily",
    "covid_mexico": "daily",
    "covid_netherlands": "daily",
    "covid_spain": "daily",
    "covid_switzerland": "weekly",
    "covid_uk": "daily",
    "covid_us": "daily",
    "dengue_argentina": "weekly",
    "dengue_brazil": "monthly",
    "dengue_colombia": "weekly",
    "dengue_malaysia": "weekly",
    "dengue_malaysia2": "weekly",
    "dengue_panama": "weekly",
    "dengue_peru": "weekly",
    "dengue_philippines": "monthly",
    "dengue_taiwan": "weekly",
    "influenza_us": "weekly",
    "influenza_us2": "weekly",
    "measles_us": "weekly",
    "tuberculosis_china": "monthly",
    "tuberculosis_japan": "monthly",
    "zika_colombia": "weekly",
    "zika_mexico": "weekly",
}

# -----------------------------
# Model Benchmarking Suite
# -----------------------------
# List of models evaluated in EpiCastBench experiments.

MODELS_TO_RUN = [
    "Naive", "DLinear", "RandomForest", "XGBoost", "TSMixer", "KAN", "LSTM", "DeepAR",
    "TCN", "NBEATS", "NHITS", "Transformer", "TiDE", "Chronos2", "TimesFM"
]
