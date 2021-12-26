import pprint
from decimal import Decimal
from operator import itemgetter

from flask import Flask, request
from flask_api import status
from werkzeug.exceptions import BadRequestKeyError

from quotes_api.rate_picker import RatePicker
from quotes_api.rates_feed import RatesFeed, ProviderClient

app = Flask(__name__)
logger = app.logger

xchr = ProviderClient(provider_name="exchangerate-api.com",
                          api_url_template="https://api.exchangerate-api.com/v4/latest/{}")


fran = ProviderClient(provider_name="frankfurter.app",
                      api_url_template='https://api.frankfurter.app/latest?from={}')

feed = RatesFeed(provider_clients=[xchr, fran])

picker = RatePicker()

# Method: GET; Request URL: <BASE_URL>/api/quote
@app.route('/api/quote', methods=['GET'])
def quote():
    logger.debug(pprint.pformat(request.args))

    param_names = "from_currency_code", "amount", "to_currency_code"

    extract_quote_params = itemgetter(*param_names)

    try:
        from_currency_code, amount, to_currency_code = extract_quote_params(request.args)
    except BadRequestKeyError as ex:
        # return Bad Request response but don't show the stack trace
        return f"Expected to get params: {param_names}", status.HTTP_400_BAD_REQUEST

    provider_rates = feed.get_rates(from_currency_code, to_currency_code)
    """
    rates data structure
    {
        <provider_name>: <provider_exchange_rate>,
        ...
    }
    """

    provider_name, exchange_rate = picker.pick_rate(provider_rates)
    amount_dec = Decimal(amount)
    exchange_rate_dec = Decimal(exchange_rate)
    total = float(amount_dec * exchange_rate_dec)

    return {
        'exchange_rate': exchange_rate,
        'currency_code': to_currency_code,
        'amount': total,
        'provider_name': provider_name,
    }


if __name__ == '__main__':
    app.run()
