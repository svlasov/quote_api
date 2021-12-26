import pprint

import requests

class ProviderClient(object):
    def __init__(self, provider_name, api_url_template):
        self.provider_name = provider_name
        self.api_url_template = api_url_template

    def get_latest_rate(self, from_currency_code, to_currency_code):

        url = self.api_url_template.format(from_currency_code)
        rates_resp = requests.get(url)
        rates_json = rates_resp.json()
        rates = rates_json['rates']
        rate = rates.get(to_currency_code)

        return rate



class RatesFeed(object):
    def __init__(self, provider_clients):
        self._clients = provider_clients

    def get_rates(self, from_currency_code, to_currency_code):

        def get_rate(provider_client, code_from, code_to):
            return provider_client.get_latest_rate(from_currency_code=code_from,
                                                                                  to_currency_code=code_to)

        rates = {}

        for client in self._clients:
            provider_name = client.provider_name
            provider_rate = get_rate(provider_client=client,
                                     code_from=from_currency_code,
                                     code_to=to_currency_code)

            rates[provider_name] = provider_rate

        return rates


if __name__ == '__main__':

    xchr = ProviderClient(provider_name="exchangerate-api.com",
                          api_url_template="https://api.exchangerate-api.com/v4/latest/{}")


    fran = ProviderClient(provider_name="frankfurter.app",
                          api_url_template='https://api.frankfurter.app/latest?from={}')

    code_from = "USD"
    code_to = "RUB"

    feed = RatesFeed(provider_clients=[xchr, fran])
    rates = feed.get_rates(from_currency_code=code_from, to_currency_code=code_to)

    pprint.pprint(rates)

    # https://api.exchangerate-api.com/v4/latest/USD
    # url = 'https://api.exchangerate-api.com/v4/latest/USD'
    # resp = requests.get(url)
    # pjson = pprint.pformat(resp.json())
    # print(pjson)
    #
    # # https://api.frankfurter.app/latest?from=USD
    # url = 'https://api.frankfurter.app/latest?from=USD'
    # resp = requests.get(url)
    # pjson = pprint.pformat(resp.json())
    # print(pjson)
