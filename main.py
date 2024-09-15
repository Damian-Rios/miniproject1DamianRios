### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def get_closing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")

    closing_list = []

    for price in hist['Close'][-10:]:
        closing_list.append(round(price, 2))

    return closing_list

def get_dates(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")

    closing_dates = []

    for date in hist.index[-10:]:
        closing_dates.append(date.strftime('%m-%d'))

    return closing_dates

my_tickers = ["MSFT", "AAPL", "GOOG", "TSLA", "NTDOY"]

for ticker in my_tickers:
    closing_dates = get_dates(ticker)
    closing_prices = np.array(get_closing(ticker))

    print(f"Ticker: {ticker}")
    print("Dates(2024):\tClosing Prices:")

    for i in range(len(closing_dates)):
        print(f"{closing_dates[i]}\t\t\t{closing_prices[i]}")

    print()

    # plots the graph
    plt.plot(closing_dates, closing_prices)

    # Get our min and max for y
    low_price = min(closing_prices)
    high_price = max(closing_prices)

    # set our yaxis min and max
    plt.ylim(low_price, high_price)

    # set our labels for the graph
    plt.xlabel("Date (2024)")
    plt.ylabel("Closing Price")
    plt.title(f"Closing Prices for {ticker}")

    # Rotate x-axis labels for better readability
    #plt.xticks(rotation=45)

    # Save plots as png
    save_file = "charts/" + ticker + ".png"
    plt.savefig(save_file)

    # Display the graph
    plt.show()