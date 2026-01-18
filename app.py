import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

ticker = "TRU"
start = "2025-01-01"
end = "2026-01-01"
data = yf.download(ticker, start=start, end=end, progress=False)

#print("Working on - TRU")

st.set_page_config("Stock Market Visualizer", layout="wide")
st.title("📈 Stock Market Visualizer v5")

# Create the scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data.index,
    y=data["Close"],
    mode='lines',
    name=f"{ticker} Close Price",
    line=dict(color='blue', width=2)
))

# Customize layout
fig.update_layout(
    title=f"{ticker} Close Price ({start} to {end})",
    xaxis_title="Date",
    yaxis_title="Close Price (USD)",
    template="plotly_white"
)

fig.update_layout(height=600, xaxis_rangeslider_visible=False)
st.plotly_chart(fig, width=True)

#fig.show()
