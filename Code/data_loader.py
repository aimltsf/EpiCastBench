# This is the file for loading datasets for the EpiCastBench codes

import pandas as pd
from pathlib import Path
from darts import TimeSeries

# Base directory for all datasets
DATA_DIR = Path("data")

def load_series(path):
    """
    Loads a time series from EpiCastBench/data/
    """
    filename = DATA_DIR / path
    
    df = pd.read_csv(path)

    try:
        df["time"] = pd.to_datetime(df["time"])
    except:
        df["time"] = pd.to_datetime(df["time"], format="%d/%m/%Y")

    df = df.set_index("time")
    return TimeSeries.from_dataframe(df)

def get_name(path):
    return Path(path).stem
