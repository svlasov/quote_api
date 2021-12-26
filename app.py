import pprint
from operator import itemgetter

from flask import Flask, request
from flask_api import status
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)
logger = app.logger

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


    return {
        "from_currency_code": from_currency_code,
        "to_currency_code": to_currency_code,
        'exchange_rate': None,
        'currency_code': None,
        'amount': amount,
        'provider_name': ''
    }


if __name__ == '__main__':
    app.run()
