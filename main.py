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
    closing_dates = []

    for date in hist.index:
        closing_dates.append(date.strftime('%Y-%m-%d'))

    for price in hist['Close']:
        closing_list.append(round(price, 2))

    return closing_dates, closing_list

my_tickers = ["MSFT", "AAPL", "GOOG", "TSLA", "NTDOY"]

for ticker in my_tickers:
    closing_dates, closing_prices = get_closing(ticker)

    print(f"Ticker: {ticker}")
    print("Dates:\t\tClosing Prices:")

    for i in range(len(closing_dates)):
        print(f"{closing_dates[i]}\t{closing_prices[i]}")

    print()

my_tickers = np.array(my_tickers)

plt.plot(my_tickers)
plt.xlabel("Ticker")
plt.ylabel("Closing Price")
plt.show()