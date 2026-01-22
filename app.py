import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Streamlit page configuration
st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Stock Comparison Dashboard v6")

# Sidebar inputs
st.sidebar.header("Stock Parameters")

# Default values
default_symbol = "CVX"
default_symbol2 = "XOM"
default_symbol3 = "PSX"
default_start = datetime.today() - timedelta(days=365)
default_end = datetime.today()

symbol1 = st.sidebar.text_input("Stock Symbol #1 (e.g., AAPL, MSFT, TSLA)", default_symbol).upper()
symbol2 = st.sidebar.text_input("Stock Symbol #2 (e.g., AAPL, MSFT, TSLA)", default_symbol2).upper()
symbol3 = st.sidebar.text_input("Stock Symbol #3 (e.g., AAPL, MSFT, TSLA)", default_symbol3).upper()
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
        stock3 = yf.Ticker(symbol3)
        df1 = stock1.history(start=start_date, end=end_date)
        df2 = stock2.history(start=start_date, end=end_date)
        df3 = stock3.history(start=start_date, end=end_date)
        
        if df1.empty:
            st.error(f"No data found for symbol1 '{symbol1}'. Please check the symbol1 and date range.")
        if df2.empty:
            st.error(f"No data found for symbol2 '{symbol2}'. Please check the symbol2 and date range.")
        if df3.empty:
            st.error(f"No data found for symbol3 '{symbol3}'. Please check the symbol3 and date range.")
        else:

            combined = pd.DataFrame({
                stock1: df1['Close'],
                stock2: df2['Close'],
                stock3: df3['Close'],
            })
            st.line_chart(combined)

            # Volume chart
            st.subheader("Trading Volume Over Time '{symbol1}'")
            #variable_output = symbol1
            #font_size_px = 30 # Can be a variable or user input (e.g., st.slider)
            #st.markdown(f'<p style="font-size: {font_size_px}px;">{variable_output}</p>', unsafe_allow_html=True)
            #st.write(symbol1)
            st.bar_chart(df1["Volume"])
            
            st.subheader("Trading Volume Over Time '{symbol2}'")
            st.bar_chart(df2["Volume"])

            st.subheader("Trading Volume Over Time '{symbol3}'")
            st.bar_chart(df3["Volume"])
            

            # Basic statistics
            st.subheader("Summary Statistics")
            st.write(symbol1)
            st.write(df1.describe())

            st.write(symbol2)
            st.write(df2.describe())
            
            st.write(symbol3)
            st.write(df3.describe())

    except Exception as e:
        st.error(f"An error occurred: {e}")

