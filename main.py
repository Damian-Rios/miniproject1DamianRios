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

my_tickers = ["MSFT", "AAPL", "GOOG", "TSLA", "NTDOY"]

for ticker in my_tickers:
    closing_prices = get_closing(ticker)
    print(f"Ticker: {ticker} \tClosing Price: {closing_prices}")