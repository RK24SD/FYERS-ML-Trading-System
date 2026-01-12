from fyers_api.auth import get_fyers
from fyers_api.data_fetch import fetch_data
from features.feature_engineering import add_features
from model.train_model import train
from backtest.walk_forward import backtest
from evaluation.performance_metrics import metrics

CLIENT_ID = "YOUR_CLIENT_ID"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
SYMBOL = "NSE:RITES-EQ"

fyers = get_fyers(CLIENT_ID, ACCESS_TOKEN)

df = fetch_data(fyers, SYMBOL, "2025-11-01", "2025-12-31")
df = add_features(df)

X = df[["ema5","ema20","rsi","atr"]]
y = df["target"]

model = train(X[:-5], y[:-5])

capital, trades = backtest(df[-10:], model)
print(metrics(trades))
