import numpy as np

def generate_signal(model, X):
    prob = model.predict_proba(X)[-1][1]
    if prob > 0.6:
        return 1
    if prob < 0.4:
        return -1
    return 0
