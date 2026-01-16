import yfinance as yf
import pandas as pd

def load_portfolio(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    return pd.read_excel(file)

def portfolio_value(portfolio):
    total = 0
    details = []
    for _, row in portfolio.iterrows():
        stock = yf.Ticker(row['Ticker'])
        price = stock.history(period="1d")['Close'][0]
        value = price * row['Shares']
        total += value
        details.append((row['Ticker'], price, value))
    return total, details
