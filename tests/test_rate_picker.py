import pytest

from quotes_api.rate_picker import RatePicker


@pytest.fixture()
def rates_single_available():
     return {
         'p1': 1.0,
         'p2': None
     }

@pytest.fixture(scope='function')
def rates_two_different():
    return {
        'p1': 1.1,
        'p2': 1.0
    }

@pytest.fixture(scope='function')
def rates_two_same():
    return {
        'p1': 1.0,
        'p2': 1.0
    }

@pytest.fixture(scope='function')
def rate_picker():
    rp = RatePicker()
    return rp

#####################################################

def test_rate_picker_returns_available_rate(rate_picker, rates_single_available):

    p, r = rate_picker.pick_rate(rates_single_available)

    assert p
    assert r

def test_rate_picker_returns_minimal_rate(rate_picker, rates_two_different):
    p, r = rate_picker.pick_rate(rates_two_different)

    assert p
    assert r
    assert not [v for v in rates_two_different.values()
                if v < r]

def test_rate_picker_returns_least_common_provider(rate_picker, rates_two_different, rates_two_same):

    most_common = None

    # make a provider common one
    for i in range(3):
        p, r = rate_picker.pick_rate(rates_two_different)
        most_common = p

    # expect to get another one
    p, r = rate_picker.pick_rate(rates_two_same)
    assert p != most_common

def test_rate_picker_returns_any_min_rate_provider(rate_picker, rates_two_same):
    p, r = rate_picker.pick_rate(rates_two_same)
    assert p
    assert r