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
default_symbol = "AAPL"
default_symbol2 = "GOOG"
default_symbol3 = "NVDA"
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
        else:
            #st.subheader(f"Stock Data for {symbol1}")
            #st.dataframe(df)

            # Price chart
            #st.subheader("Closing Price Over Time1")
            #st.line_chart(df1["Close"], color="#ffaa00")
            #st.subheader("Closing Price Over Time TRU")
            #st.line_chart(df2["Close"], color="#ff0000")

            combined = pd.DataFrame({
                stock1: df1['Close'],
                stock2: df2['Close'],
                stock3: df3['Close'],
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

# New stuff below
ticker_symbol = "AAPL"

if ticker_symbol:
    try:
        # Fetch the ticker data
        ticker_data = yf.Ticker(ticker_symbol)
        
        # Get quarterly earnings data
        # This returns a DataFrame with 'Quarter' as index and 'Earnings' column
        quarterly_earnings = ticker_data.quarterly_earnings

        if not quarterly_earnings.empty:
            # Prepare data for plotting
            # Convert index to a column for Plotly
            quarterly_earnings = quarterly_earnings.reset_index()
            
            # Ensure 'Quarter' is treated as a string for correct x-axis labels
            quarterly_earnings['Quarter'] = quarterly_earnings['Quarter'].astype(str)

            # Create an interactive bar chart using 

            fig = px.bar(
                quarterly_earnings,
                x="Quarter",
                y="Earnings",
                title=f"{ticker_symbol} Quarterly Earnings",
                labels={"Earnings": "Earnings (Millions USD)"},
                color="Quarter", # Differentiate bars by quarter
            )
            
            # Display the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
            
            # Optionally display the raw data table
            st.write(f"Raw quarterly earnings data for {ticker_symbol}:")
            st.dataframe(quarterly_earnings)

        else:
            st.warning(f"No quarterly earnings data found for {ticker_symbol}.")

    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
