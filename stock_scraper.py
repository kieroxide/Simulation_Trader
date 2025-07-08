import os
import time
import pandas as pd
import yfinance as yf
from datetime import datetime as dt

def check_tickers(tickers):
    filepath = "stock_data/Stock_List.csv"
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        existing_tickers = df.iloc[:, 0].tolist()
        print(existing_tickers)
        new_tickers = []
        folder = "stock_data"
        for ticker in tickers:
            if ticker not in existing_tickers:
                new_tickers.append(ticker)
        return new_tickers
    return tickers

def download_stock_data(tickers):
    if not tickers:
        print("LOG - No stocks to download")
        return
    done_tickers = []
    folder = "stock_data"

    if not os.path.exists(folder):
        os.makedirs(folder)

    today = dt.today().date()
    for symbol in tickers:
        filename = f"{symbol}.csv"
        path_name = f"{folder}/{filename}"
        if(os.path.exists(path_name)):
            mod_time = os.path.getmtime(path_name)
            mod_date = dt.fromtimestamp(mod_time).date()
            if(mod_date == today):
                continue
            

        print(f"Downloading data for {symbol}...")
        ticker = yf.Ticker(symbol)
        df = ticker.history(start="2010-01-01", end="2025-01-01", interval="1d")

        done_tickers.append(symbol)
        # Save to CSV
        df.to_csv(path_name)

        time.sleep(1)  # to avoid hitting API limits

    done_tickers = pd.DataFrame(done_tickers, columns=['Tickers'])
    done_tickers.to_csv(f"{folder}/Stock_List.csv" , index=False, header=True)