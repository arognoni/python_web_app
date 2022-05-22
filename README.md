# Web applications with Python and Flask

This repository contains the material for the "Python web applications" course.
You can download it (as a .zip folder) by clicking the "code" button at the top-right corner of the window.

## Directory structure
```
python_web_app
│   README.md
│   crypto_data.csv  
│   environment.yml
│   
└───static
│      uniupo_logo.svg
│      mystyle.css
│   
└───templates
       .gitignore (ignore this file)
```

## Creating the Conda environment
For these lectures, we will need the following libraries:
- flask
- pandas
- matplotlib
- requests

You can create a conda environment named `web_app_env` that contains all these libraries through the `environment.yml` file located in the root folder.
You only need to type:

`$ conda env create -f environment.yml`

The environment can then be activated by running the following command:

`$ conda activate web_app_env`

## Executing a Flask app

To execute a Flaks app, you need to set two environment variables.
Suppose that the file containing the app is named `app.py`. On the command prompt run:

```
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

On Linux, you must use `export` instead of `set`:


```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

Once the variables are defined, you can simply execute the app through:

`$ flask run`

## The Binance API

To get real-time cryptocurrency prices, we will use the Binance API. The documentation can be found [here](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md).

In particular, we will make a GET request to:

`https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]`

The data we will receive is a JSON having this shape:
```
[
    {
        "symbol":"BTCUSDT",
        "price":"29316.60000000"
    },
    {
        "symbol":"ETHUSDT",
        "price":"1969.81000000"
    },
    {
        "symbol":"DOGEUSDT",
        "price":"0.08400000"
    }
]
```

where `symbol` corresponds to the cryptocurrency and `price` is the value in USD(T). Notice that:
- The symbols do not correspond to the column labels of our dataframe
- Prices are provided as strings.
