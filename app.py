import plotly.graph_objects as go
import pandas as pd

# Example OHLC data
data = {
    'Date': pd.date_range(start='2025-01-01', periods=5, freq='D'),
    'Open': [100, 102, 101, 105, 107],
    'High': [105, 106, 103, 108, 110],
    'Low': [99, 101, 100, 104, 106],
    'Close': [104, 103, 102, 107, 109]
}
df = pd.DataFrame(data)

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])

# Customize layout
fig.update_layout(
    title='Candlestick Chart Example',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False
)

fig.show()
