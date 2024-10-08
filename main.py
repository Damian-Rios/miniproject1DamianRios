### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# function to get closing prices of last 10 days
def get_closing(ticker):
    stock = yf.Ticker(ticker)
    # have to use 1-month period
    hist = stock.history(period="1mo")

    closing_list = []

    # -10 to get last 10 days of the month
    for price in hist['Close'][-10:]:
        closing_list.append(round(price, 2))

    return closing_list

# function to get dates of last 10 days
def get_dates(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")

    closing_dates = []

    # -10 gets last 10 days of month
    for date in hist.index[-10:]:
        # formatting dates
        closing_dates.append(date.strftime('%m-%d'))

    return closing_dates

try:
    # Create our charts folder
    Path("charts").mkdir()
except FileExistsError:
    pass

my_tickers = ["MSFT", "AAPL", "GOOG", "TSLA", "NTDOY"]

# loop to print data and make plots from data
for ticker in my_tickers:
    closing_dates = get_dates(ticker)
    closing_prices = np.array(get_closing(ticker))

    print(f"Ticker: {ticker}")
    print("Dates(2024):\tClosing Prices:")

    for i in range(len(closing_dates)):
        print(f"{closing_dates[i]}\t\t\t{closing_prices[i]}")

    print()

    # Get our min and max for y
    low_price = closing_prices.min() - (closing_prices.min()*0.05)
    high_price = closing_prices.max() + (closing_prices.max()*0.05)

    # set our yaxis min and max
    plt.ylim(low_price, high_price)

    # set our labels for the graph
    plt.xlabel("Date (2024)")
    plt.ylabel("Closing Price")
    plt.title(f"Closing Prices for {ticker}")

    # plots the graph
    plt.plot(closing_dates, closing_prices)

    # Save plots as png
    save_file = "charts/" + ticker + ".png"
    plt.savefig(save_file)

    # Display the graph
    plt.show()
