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

symbol1 = st.sidebar.text_input("Stock Symbol (e.g., AAPL, MSFT, TSLA)", default_symbol).upper()
symbol2 = "TRU"
start_date = st.sidebar.date_input("Start Date", default_start)
end_date = st.sidebar.date_input("End Date", default_end)

# Validate date range
if start_date > end_date:
    st.sidebar.error("Start date must be before end date.")

# Fetch data button
if st.sidebar.button("Fetch Data"):
    try:
        # Download stock data
        stock1 = yf.Ticker(symbol1)
        stock2 = yf.Ticker(symbol2)
        df1 = stock1.history(start=start_date, end=end_date)
        df2 = stock2.history(start=start_date, end=end_date)
        
        if df1.empty:
            st.error(f"No data found for symbol1 '{symbol1}'. Please check the symbol1 and date range.")
        else:
            #st.subheader(f"Stock Data for {symbol1}")
            #st.dataframe(df)

            # Price chart
            st.subheader("Closing Price Over Time1")
            st.line_chart(df1["Close"], color="#ffaa00")
            st.subheader("Closing Price Over Time TRU")
            st.line_chart(df2["Close"], color="#ff0000")

            combined = pd.DataFrame({
                df1['Close'],
                df2['Close']
            })
            st.line_chart(combined)


            # Volume chart
            #st.subheader("Trading Volume Over Time")
            #st.bar_chart(df["Volume"])

            # Basic statistics
            #st.subheader("Summary Statistics")
            #st.write(df.describe())

    except Exception as e:
        st.error(f"An error occurred: {e}")
