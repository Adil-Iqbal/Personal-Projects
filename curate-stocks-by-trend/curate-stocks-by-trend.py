# Copyright 2017 by Adil Iqbal.  All rights reserved.

"""Analyze set of stocks and print a out sorted table based on performance.

Though this script analyzes a limited sample of stocks, it can
be extended to run over all publicly traded stocks.
"""

import os
from datetime import date, timedelta

import quandl
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

from warnings import warn
from requests.exceptions import ConnectionError
from quandl.errors.quandl_error import ForbiddenError, LimitExceededError

plt.style.use("seaborn-dark")

# My API key is hidden.
# You can get your own key or run the script as is.
try:
    import api_keys
    key = api_keys.get["quandl"]
except ImportError:
    key = None

# List of stocks whose price database is included in the EOI free sample.
stocks = ["V", "UNH", "PG", "KO", "GS", "WMT", "MRK", "VZ", "UTX", "TRV",
          "DIS", "BA", "HD", "DD", "MMM", "PFE", "NKE", "MCD", "JPM", "INTC",
          "GE", "CSCO", "CVX", "CAT", "AXP", "JNJ", "MSFT", "IBM", "AAPL"]


def get_data(query):
    """Return data."""
    try:
        global key
        three_months_ago = str(date.today() - timedelta(weeks=12))
        return quandl.get(query, authtoken=key, start_date=three_months_ago)
    except (ConnectionError, ForbiddenError, LimitExceededError):
        warn("There was an issue with the query. Using back-up data...")
        file_path = os.path.join(os.getcwd(), "data", query[4:] + ".csv")
        return pd.DataFrame.from_csv(path=file_path)

def analyze(name, show=False):
    """Return the name, trend, and the current price of the stock."""
    # Query the Quandl API for stock data.
    query = "EOD/" + name
    df = get_data(query)
    # Define x and y based on stock prices.
    y = df["Adj_Open"].tolist()
    x = [i + 1 for i, price in enumerate(y)]
    # Find slope of the best fit line.
    m, b = linregress(x, y)[0:2]
    if show:
        best_fit_x = [x[0], x[-1]] # Best fit line, end-point's x-coordinates.
        best_fit_y = [m * i + b for i in best_fit_x] # Best fit line, end-point's y-coordinates.
        plt.plot(x, y, label="Stock Prices") # Plot the stock prices.
        plt.plot(best_fit_x, best_fit_y, label="Trend") # Plot the stock's trend.
        # Show the graph after a bit of formatting.
        plt.title(name + "'s Stock Price Over Last " + str(x[-1]) + " Days.")
        plt.xlabel("Business Days")
        plt.ylabel("Stock Price (dollars per share)")
        plt.legend()
        plt.show()
    else:
        return name, m, y[-1]

# Construct a list of all of the stocks' name, trend, and price.
curated_stocks = []
for i, stock in enumerate(stocks):
    name, trend, price = analyze(name=stock)
    curated_stocks.append((name, trend, price))

# Construct a pandas data frame from the list above.
labels = ["Stock", "Trend", "Price"]
stock_table = pd.DataFrame.from_records(curated_stocks, columns=labels)
stock_table = stock_table.sort_values(by="Trend", ascending=0)

# Print out the result from best to worst performing.
print(stock_table.set_index("Stock"))

# Print graph of the top performer.
analyze(name=stock_table["Stock"].iloc[0], show=True)
