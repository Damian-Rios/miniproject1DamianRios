### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 1
import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "GOOG", "TSLA", "NTDOY"]

mydata = {}

mytickers.sort()

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dayHigh': result.info['dayHigh']
                      }
    #print(f"Ticker: {ticker} \tDaily High: {result.info['dayHigh']}")

pprint.pprint(mydata)
