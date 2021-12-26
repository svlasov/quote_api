from collections import defaultdict, Counter


class RatePicker(object):

    quote_counter = Counter()

    def pick_rate(self, provider_rates):

        # invert the map
        rates_providers = defaultdict(list)

        for p, r in provider_rates.items():
            rates_providers[r].append(p)

        # filter out unavailable rates
        available_rates = [v for v in provider_rates.values()
                           if v is not None]

        # if remains a single rate then return it
        if len(available_rates) == 1:
            r = available_rates[0]
            p = rates_providers[r][0]
        else:

            # find out minimal rate
            r = min(available_rates)

            providers_of_min_rate = rates_providers[r]

            p = providers_of_min_rate[0]

            if len(providers_of_min_rate) > 1:

                # get the least common provider
                try:
                    p, _ = self.quote_counter.most_common()[-1]
                except IndexError as err:
                    # could fail on a fresh counter
                    # it's okay, just return any provider with the min rate
                    pass

        # update usage counter
        self.quote_counter.update(p)
        # return result
        return p, r