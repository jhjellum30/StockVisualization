import streamlit as st
import yfinance as yf
import pandas as pd
#import matplotlib.pyplot as plt


from datetime import datetime
#plt.style.use('seaborn')

msft=yf.Ticker('msft')
stockinfo = msft.info

# This prints all items
# for key,value in stockinfo.items():
#     print(key, ":", value)

print(msft.symbol)

