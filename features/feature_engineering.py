import pandas as pd
import numpy as np

def add_features(df):
    df["ret"] = df["close"].pct_change()
    df["ema5"] = df["close"].ewm(span=5).mean()
    df["ema20"] = df["close"].ewm(span=20).mean()
    df["rsi"] = 100 - (100 / (1 + df["ret"].rolling(14).mean()))
    df["atr"] = (df["high"] - df["low"]).rolling(14).mean()
    df["target"] = (df["ret"].shift(-1) > 0).astype(int)
    return df.dropna()
