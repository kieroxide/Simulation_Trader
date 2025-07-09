import os
import time
import pandas as pd
import yfinance as yf
from datetime import datetime as dt, timedelta as td
from decimal import Decimal


def check_tickers(tickers):
    filepath = "stock_data/Stock_List.csv"
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        existing_tickers = df.iloc[:, 0].tolist()

        new_tickers = []
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

def read_current_stock_price(date, symbol):
    if not date:
        print("Invalid date to read stock price")
        return
    if not symbol:
        print("Invalid ticker to read stock price")
        return
    
    csv_path = f"stock_data/{symbol}.csv"
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'], utc=True)

    if df['Date'].isnull().any():
        print("Warning: some dates failed to convert and will be NaT")
    
    date = pd.to_datetime(date)
    date = date.normalize()
    filtered = df[df['Date'].dt.date == date.date()]

    if filtered.empty:
        price = read_current_stock_price(date - td(days=1), symbol)
    else:
        price = filtered['Open'].iloc[0]
    return price