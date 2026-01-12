# FYERS-ML-Trading-System

This repository implements a fully automated, machine learning–based trading system integrated with the FYERS trading ecosystem.
The system covers the complete pipeline:

Market Data → Feature Engineering → ML Model → Trade Signals → Risk Management → Backtesting → Performance Evaluation

The project is designed in alignment with industry-standard quantitative trading practices and competition requirements.

🎯 Objective

Predict next-day price direction for a selected NSE-listed equity

Convert predictions into systematic trading signals

Execute trades programmatically using FYERS API

Evaluate strategy using walk-forward backtesting

Focus on risk-adjusted performance, not raw profits

🏗 Repository Structure
fyers-ml-trading-system/
│
├── data/                # Raw and processed data
├── features/            # Feature engineering pipeline
├── model/               # Model training and persistence
├── strategy/            # Signal generation & trading rules
├── backtest/            # Walk-forward backtesting logic
├── evaluation/          # Performance metrics
├── fyers_api/           # FYERS authentication & execution
│
├── main.py              # End-to-end pipeline runner
├── requirements.txt
└── README.md

📊 Data Source

Source: FYERS Market Data API

Frequency: Daily

Data Type: OHLCV

Universe: NSE-listed equity (single stock)

Time Window: Last 2 calendar months

⚠️ No external or third-party datasets are used.

⚙️ Feature Engineering

Raw prices are transformed into market-relevant signals representing trend, momentum, and volatility.

Key Features

Returns: Daily percentage change

Trend: EMA (5, 20)

Momentum: RSI (14)

Volatility: ATR (14)

Price Action: High–Low range

These features are intentionally limited to ensure:

Interpretability

Stability

Reduced overfitting

🤖 Model Details

Model: Random Forest Classifier

Target:

target = 1  → Next-day return > 0
target = 0  → Next-day return ≤ 0

Why This Model?

Performs well on small financial datasets

Captures non-linear market behavior

Widely used in systematic trading research

🔔 Signal Generation Logic

Model outputs are converted into actionable signals:

BUY  → High probability of upward movement
SELL → High probability of downward movement
HOLD → Otherwise


Only one position is allowed at any time to control exposure.

💰 Position Sizing & Risk Management

Risk management is embedded at the strategy level.

Position Sizing Formula
Risk per trade = 1% of total capital
Position Size = (Capital × 0.01) / ATR

Risk Controls

Stop-Loss: 1 × ATR

Take-Profit: 2 × ATR

Risk–Reward Ratio: ≥ 1:2

Capital preservation is prioritized over aggressive returns.

🔁 Backtesting Methodology

A chronological walk-forward backtest is used:

Train model on past data

Predict next trading day

Simulate trade execution

Move window forward

Why Walk-Forward?

Prevents data leakage

Closely replicates live trading conditions

Accepted industry standard for time-series evaluation

📈 Performance Metrics

The strategy is evaluated using risk-adjusted metrics:

Net Profit & Loss

Win Rate

Directional Accuracy

Capital Curve Progression

(Sharpe and drawdown can be added easily if required.)

📌 Assumptions

The system operates under the following standard quantitative trading assumptions:

FYERS-provided OHLCV data is accurate and complete

Market liquidity is sufficient for execution at quoted prices

Transaction costs and slippage are minimal and constant

No major corporate actions distort price behavior

Trades are executed at the next market open using end-of-day signals

No manual intervention occurs at any stage

🚀 How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Add FYERS Credentials

Update in main.py:

CLIENT_ID = "YOUR_CLIENT_ID"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

3️⃣ Execute Pipeline
python main.py

✅ Compliance Checklist

✔ Uses FYERS API only
✔ Fully automated pipeline
✔ No manual trading
✔ Reproducible results
✔ Industry-aligned methodology

📌 Limitations

Short historical window limits exposure to different market regimes

Strategy is stock-specific

Performance may vary under extreme volatility or news-driven events

🏁 Conclusion

This project demonstrates a disciplined, ML-driven trading system built using professional quantitative finance principles and fully integrated with the FYERS trading ecosystem.
The emphasis is on signal quality, risk control, and methodological rigor, rather than speculative profit maximization.


