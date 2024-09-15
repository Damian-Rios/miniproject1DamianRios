### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 1

import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def get_closing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    closing_list = []

    for price in hist['Close']:
        closing_list.append(round(price, 2))

    return closing_list

def get_dates(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    closing_dates = []

    for date in hist.index:
        closing_dates.append(date.strftime('%Y-%m-%d'))

    return closing_dates

my_tickers = ["MSFT", "AAPL", "GOOG", "TSLA", "NTDOY"]

for ticker in my_tickers:
    closing_dates = get_dates(ticker)
    closing_prices = np.array(get_closing(ticker))

    print(f"Ticker: {ticker}")
    print("Dates:\t\tClosing Prices:")

    for i in range(len(closing_dates)):
        print(f"{closing_dates[i]}\t{closing_prices[i]}")

    print()

    plt.figure()

    # plots the graph
    plt.plot(closing_dates, closing_prices)

    # Get our min and max for y
    low_price = min(closing_prices)
    high_price = max(closing_prices)

    # set our yaxis min and max
    plt.ylim(low_price, high_price)

    # set our labels for the graph
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"Closing Prices for {ticker}")

    # Display the graph
    plt.show()