import alpaca_trade_api as tradeapi
from settings import constants


class TradeStock:

    def get_account_details(self):
        api = tradeapi.REST(key_id=constants.ALPACA_API_KEY,
                            secret_key=constants.ALPACA_SECRET_KEY,
                            base_url=constants.BASE_URL,
                            api_version=constants.ALPACA_API_VERSION)
        return api.get_account()