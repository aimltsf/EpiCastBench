# This file contains code for evaluating the models in EpiCastBench

from darts.metrics import smape, mae, rmse, mase

def evaluate(pred, test, train):

    metrics = {}

    try:
        metrics["SMAPE"] = smape(test, pred)
    except Exception as e:
        metrics["SMAPE"] = None

    try:
        metrics["MAE"] = mae(test, pred)
    except Exception as e:
        metrics["MAE"] = None

    try:
        metrics["RMSE"] = rmse(test, pred)
    except Exception as e:
        metrics["RMSE"] = None

    try:
        metrics["MASE"] = mase(test, pred, train)
    except Exception as e:
        metrics["MASE"] = None

    return metrics
