import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
ply.style.use('seaborn')

ticker=yf.Ticker('msft')
stockinfo = ticker.info

for key.value in stockinfo.items():
   print(key, ":", value)
