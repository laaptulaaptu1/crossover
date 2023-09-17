import os, csv
import talib
import yfinance as yf
import pandas
import datetime as dt

def download_data():
    with open('data/symbols_NIFTY50.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2018-07-01", end=dt.date.today())
            data.to_csv('data/daily_nifty/{}.csv'.format(symbol))

    return {
        "code": "success"
    }

download_data()