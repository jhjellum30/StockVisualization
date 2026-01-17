import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from utils.indicators import moving_average, rsi, bollinger_bands
from utils.portfolio import load_portfolio, portfolio_value
from utils.storage import save_config, load_config

st.set_page_config("Stock Market Visualizer", layout="wide")
st.title("📈 Stock Market Visualizer v5")

# Sidebar Controls
ticker = st.sidebar.text_input("Stock Ticker", "TU")
start = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("today"))

ma_window = st.sidebar.slider("Moving Average Window", 5, 200, 20)
show_rsi = st.sidebar.checkbox("Show RSI", True)
show_bb = st.sidebar.checkbox("Show Bollinger Bands", True)

# Fetch Data
df = yf.download(ticker, start=start, end=end)
df.dropna(inplace=True)

# Indicators
df['MA'] = moving_average(df, ma_window)
df['RSI'] = rsi(df)
df['BB_upper'], df['BB_lower'] = bollinger_bands(df)

# Candlestick Chart
fig = go.Figure()
fig.add_candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name="Price"
)

fig.add_trace(go.Scatter(x=df.index, y=df['MA'], name="MA"))

if show_bb:
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_upper'], name="BB Upper", line=dict(dash='dot')))
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_lower'], name="BB Lower", line=dict(dash='dot')))

fig.update_layout(height=600, xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

# RSI Chart
if show_rsi:
    st.subheader("RSI Indicator")
    rsi_fig = go.Figure()
    rsi_fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], name="RSI"))
    rsi_fig.add_hline(y=70, line_dash="dash")
    rsi_fig.add_hline(y=30, line_dash="dash")
    st.plotly_chart(rsi_fig, use_container_width=True)

# Export
st.download_button(
    "📥 Export Chart (HTML)",
    fig.to_html(),
    file_name=f"{ticker}_chart.html"
)

# Portfolio Tracking
st.subheader("💼 Portfolio Tracker")
uploaded = st.file_uploader("Upload Portfolio (CSV / Excel)", type=["csv", "xlsx"])

if uploaded:
    portfolio = load_portfolio(uploaded)
    total, details = portfolio_value(portfolio)
    st.write("### Portfolio Breakdown")
    st.table(pd.DataFrame(details, columns=["Ticker", "Price", "Value"]))
    st.success(f"💰 Total Portfolio Value: ${total:,.2f}")

# Correlation Analysis
st.subheader("📊 Stock Correlation")
tickers = st.multiselect("Select stocks", ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",])
if tickers:
    prices = yf.download(tickers, start=start, end=end)['Close']
    corr = prices.corr()
    #st.dataframe(corr.style.background_gradient(cmap="coolwarm"))

# Save Config
if st.button("💾 Save Settings"):
    save_config({
        "ticker": ticker,
        "ma_window": ma_window,
        "show_rsi": show_rsi,
        "show_bb": show_bb
    })
    st.success("Configuration Saved!")
