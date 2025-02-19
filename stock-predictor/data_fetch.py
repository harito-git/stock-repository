import yfinance as yf
import pandas as pd

# Fetch stock/ETF data
def get_stock_data(symbol, period="6mo"):
    stock = yf.Ticker(symbol)
    hist = stock.history(period=period)

    if hist.empty:
        return None
    
    df = hist[['Close']].reset_index()
    df.columns = ['Date', 'Close']
    return df
