# rate-tracker
Liteweight loan rate tracking application on open source data.


## Dependencies
We use various `Free tiered` API's in order to gather this data locally. We cache the data within `~/cache` to then reference locally for our api. The caches are initialized by running `daily.py`


### FRED
Within this application we use [Frederal Reserve Bank of St Louis API.](https://fred.stlouisfed.org/docs/api/fred/series_observations.html#frequency) In order to run this you must register for an api key [here](https://fred.stlouisfed.org/docs/api/api_key.html) and add your api key within `.env` of variable `FRED_API_KEY`.

### ALPHA VANTAGE
Within this application we use [Alpha Vantage.](https://www.alphavantage.co/documentation/) In order to run this you must register for an api key [here](https://www.alphavantage.co/support/#api-keyl) and add your api key within `.env` of variable `ALPHA_VANTAGE_API_KEY`.


## Run locally

### Docker
Install docker

There is a `build.sh` script that simplifies docker commands so you don't have to type everything.

```shell
# To run the script you will run ./build.sh <command> <dockerfile_name>
# Commands:
# build - build the docker image
# run - run the docker image
# stop - stop the docker image
# remove - remove the docker image
# exec - terminal into the docker container
# logs - show the logs of the docker image
```
*Note you can provide a `<dockerfile_name>` as the second parameter to the command, if not provided the dockerfile_name will be defaulted to `rate-tracker`.

