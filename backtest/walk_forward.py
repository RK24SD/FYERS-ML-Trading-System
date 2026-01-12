import pandas as pd

def backtest(df, model):
    capital = 100000
    trades = []

    for i in range(len(df)-1):
        X = df.iloc[:i+1][["ema5","ema20","rsi","atr"]]
        signal = model.predict(X.tail(1))[0]
        if signal == 1:
            pnl = df.iloc[i+1]["ret"] * capital
            capital += pnl
            trades.append(pnl)

    return capital, trades
