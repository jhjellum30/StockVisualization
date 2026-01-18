import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Streamlit page configuration
st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Stock Dashboard with yFinance")

# Sidebar inputs
st.sidebar.header("Stock Parameters")

# Default values
default_symbol = "AAPL"
default_start = datetime.today() - timedelta(days=365)
default_end = datetime.today()

symbol = st.sidebar.text_input("Stock Symbol (e.g., AAPL, MSFT, TSLA)", default_symbol).upper()
start_date = st.sidebar.date_input("Start Date", default_start)
end_date = st.sidebar.date_input("End Date", default_end)

# Validate date range
if start_date > end_date:
    st.sidebar.error("Start date must be before end date.")

# Fetch data button
if st.sidebar.button("Fetch Data"):
    try:
        # Download stock data
        stock = yf.Ticker(symbol)
        df = stock.history(start=start_date, end=end_date)

        if df.empty:
            st.error(f"No data found for symbol '{symbol}'. Please check the symbol and date range.")
        else:
            #st.subheader(f"Stock Data for {symbol}")
            #st.dataframe(df)

            # Price chart
            st.subheader("Closing Price Over Time")
            st.line_chart(df["Close"])

            # Volume chart
            #st.subheader("Trading Volume Over Time")
            #st.bar_chart(df["Volume"])

            # Basic statistics
            #st.subheader("Summary Statistics")
            #st.write(df.describe())

    except Exception as e:
        st.error(f"An error occurred: {e}")
