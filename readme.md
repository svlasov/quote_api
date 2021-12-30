# Quotes API

## How to use

Given the service is running on the `localhost` (see the next "How to run" section) you can issue a GET request in the following format:

```
curl http://localhost:5000/api/quote?from_currency_code=USD&amount=100&to_currency_code=EUR
```

If your host IP and/or port differ then substitute accordingly


## How to run

### With Docker

```shell
 docker build . -t svlasov/quotes_api:latest
 docker run -it -p 5000:5000 svlasov/quotes_api:latest
```
Then go to this link: http://127.0.0.1:5000/api/quote?from_currency_code=USD&to_currency_code=EUR&amount=100

### With Python
Install prerequisites
Python 3.8 (probably should work with other 3+ versions)

Install requirements:
```shell
pip install -r requirements.txt
```

Run Flask app with default settings:
```shell
python -m flask run
```

Run Flask app in development + debug mode on port 8000
```shell
FLASK_ENV=development FLASK_DEBUG=1 python -m flask run --port=8000
```

### Design decision motivations

#### Rates data feed 

Several dilemmas I had to resolve are around data feed polling strategy.

I took into considerations the following options:
 - sequentially poll all (both) providers in the web request thread
 - run a thread per provider and join them
 - run a scheduler which will poll providers and fill a storage (in-memory cache etc.) where latest values would be available on demand

For the sake of the exercise I've chosen a compromise variant: join on threads

#### Business Logic

While the task states there are only 2 providers I tried to get it to work with any amount of providers


