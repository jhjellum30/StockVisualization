import pandas as pd
import numpy as np

def moving_average(df, window=20):
    return df['Close'].rolling(window).mean()

def rsi(df, period=14):
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = -delta.where(delta < 0, 0).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def bollinger_bands(df, window=20):
    ma = df['Close'].rolling(window).mean()
    std = df['Close'].rolling(window).std()
    return ma + 2*std, ma - 2*std
