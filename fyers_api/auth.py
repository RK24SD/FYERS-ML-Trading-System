from fyers_apiv3 import fyersModel
import webbrowser

def get_fyers(client_id, access_token):
    return fyersModel.FyersModel(
        client_id=client_id,
        token=access_token,
        log_path=""
    )
