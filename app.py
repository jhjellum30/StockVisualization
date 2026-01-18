# streamlit_yfinance_compare.py
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Streamlit page config
st.set_page_config(page_title="Stock Comparison App", layout="wide")

st.title("📊 Stock Comparison using yFinance")

# Sidebar inputs
st.sidebar.header("Stock Selection")

# Default date range: last 6 months
default_start = datetime.date.today() - datetime.timedelta(days=180)
default_end = datetime.date.today()

ticker1 = st.sidebar.text_input("First Stock Ticker (e.g., AAPL)", "AAPL").upper().strip()
ticker2 = st.sidebar.text_input("Second Stock Ticker (e.g., MSFT)", "MSFT").upper().strip()

start_date = st.sidebar.date_input("Start Date", default_start)
end_date = st.sidebar.date_input("End Date", default_end)

# Validate date range
if start_date >= end_date:
    st.sidebar.error("Start date must be before end date.")

# Fetch data function with error handling
@st.cache_data
def fetch_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None

# Fetch both datasets
if st.sidebar.button("Compare Stocks"):
    data1 = fetch_data(ticker1, start_date, end_date)
    data2 = fetch_data(ticker2, start_date, end_date)

    if data1 is None:
        st.error(f"No data found for {ticker1}")
    if data2 is None:
        st.error(f"No data found for {ticker2}")

    if data1 is not None and data2 is not None:
        # Display summary stats
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"{ticker1} Summary")
            st.write(data1.describe())
        with col2:
            st.subheader(f"{ticker2} Summary")
            st.write(data2.describe())

        # Price comparison chart
        st.subheader("Closing Price Comparison")
        combined = pd.DataFrame({
            ticker1: data1['Close'],
            ticker2: data2['Close']
        })
        st.line_chart(combined)

        # Normalized comparison (percentage change)
        st.subheader("Normalized Performance (Start = 100)")
        normalized = combined / combined.iloc[0] * 100
        st.line_chart(normalized)

        # Volume comparison
        st.subheader("Trading Volume Comparison")
        volume_df = pd.DataFrame({
            f"{ticker1} Volume": data1['Volume'],
            f"{ticker2} Volume": data2['Volume']
        })
        st.line_chart(volume_df)
