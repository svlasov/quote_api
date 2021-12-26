# Quotes API

## How to run

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


