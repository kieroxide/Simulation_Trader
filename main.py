from Portfolio import Portfolio
from Stock_Scraper import *
from Simulator import *
import yfinance as yf


tradeTime = 12

tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "BRK-B", "UNH", "JNJ",
    "XOM", "JPM", "PG", "V", "MA", "HD", "AVGO", "LLY", "PEP", "KO",
    "MRK", "ABBV", "COST", "ADBE", "WMT", "BAC", "CRM", "DIS", "PFE", "CVX",
    "INTC", "CSCO", "ABT", "T", "CMCSA", "QCOM", "TMO", "AMGN", "NKE", "ORCL",
    "MCD", "TXN", "DHR", "WFC", "UPS", "LOW", "NEE", "MS", "HON", "UNP",
    "LIN", "PM", "IBM", "AMD", "RTX", "SBUX", "INTU", "MDT", "CAT", "AMAT",
    "GE", "GS", "PLD", "NOW", "ELV", "ISRG", "BKNG", "LMT", "SPGI", "BLK",
    "AXP", "ADP", "ZTS", "CB", "TGT", "SYK", "DE", "C", "CI", "PGR",
    "USB", "MMC", "ADI", "MO", "BSX", "MDLZ", "REGN", "VRTX", "EQIX", "FDX",
    "APD", "CL", "GM", "HCA", "EW", "F", "ROST", "GILD", "HUM", "ETN"
]

tickers = check_tickers(tickers) #filters already downloaded tickers
download_stock_data(tickers)

sim = Simulator()
sim.simulate()

