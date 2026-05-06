# This is the main execution file for EpiCastBench codes

import pandas as pd
from config import *
from utils import set_seed, get_horizon
from data_loader import load_series, get_name
from evaluator import evaluate
from models import get_models

set_seed(RANDOM_STATE)

all_results = []

for file in DATASETS:

    data_name = get_name(file)
    frequency = DATA_FREQUENCY_MAPPING[data_name]
    horizon = get_horizon(frequency, HORIZON_TYPE)

    series = load_series(file)
    train, test = series[:-horizon], series[-horizon:]

    models = get_models(INPUT_CHUNK, OUTPUT_CHUNK, N_EPOCHS, RANDOM_STATE)

    fitted = {}
    forecasts = {}

    # ---------------- TRAIN ----------------
    for name, model in models.items():
        try:
            model.fit(train, verbose=True)
            fitted[name] = model
            print(f"Trained: {name} | {data_name}")
        except Exception as e:
            print(f"Train failed {name}: {e}")

    # ---------------- FORECAST ----------------
    for name, model in fitted.items():
        try:
            pred = model.predict(n = horizon)
            forecasts[name] = pred
            print(f"Forecast complete for: {name}")
        except Exception as e:
            print(f"Forecast failed for {name}: {e}")

    # ---------------- EVAL ----------------
    for name, pred in forecasts.items():
        metrics = evaluate(pred, test, train)
        metrics["Model"] = name
        metrics["Dataset"] = data_name
        all_results.append(metrics)

# ---------------- SAVE ----------------
results_df = pd.DataFrame(all_results)
results_df.to_csv("epicastbench_results.csv", index=False)

print("Done. Results saved.")
