# Quotes API

## How to run

### With Python

### With Docker

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


