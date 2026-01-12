def position_size(capital, atr):
    risk = capital * 0.01
    return int(risk / atr)
