import streamlit as st
import yfinance as yf
import pandas as pd
#import matplotlib.pyplot as plt


from datetime import datetime
#plt.style.use('seaborn')

ticker=yf.Ticker('msft')
stockinfo = ticker.info

# This prints all items
#for key,value in stockinfo.items():
#   print(key, ":", value)

print(ticker.dayHigh)
print(ticker.dayLow)
