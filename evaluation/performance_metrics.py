import numpy as np

def metrics(trades):
    return {
        "net_pnl": sum(trades),
        "win_rate": np.mean([1 if t > 0 else 0 for t in trades])
    }
