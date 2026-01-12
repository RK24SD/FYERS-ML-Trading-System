import pandas as pd
from datetime import datetime

def fetch_data(fyers, symbol, start, end):
    data = {
        "symbol": symbol,
        "resolution": "D",
        "date_format": "1",
        "range_from": start,
        "range_to": end,
        "cont_flag": "1"
    }
    res = fyers.history(data)
    df = pd.DataFrame(res["candles"],
        columns=["time","open","high","low","close","volume"])
    df["date"] = pd.to_datetime(df["time"], unit="s")
    return df.drop(columns="time")
