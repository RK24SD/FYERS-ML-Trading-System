def place_order(fyers, symbol, qty, side):
    order = {
        "symbol": symbol,
        "qty": qty,
        "type": 2,
        "side": side,
        "productType": "INTRADAY",
        "limitPrice": 0,
        "stopPrice": 0,
        "validity": "DAY",
        "disclosedQty": 0,
        "offlineOrder": False
    }
    return fyers.place_order(order)
