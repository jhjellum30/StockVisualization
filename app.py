import pandas as pd
import plotly.graph_objects as go

# Example: Create a sample DataFrame (replace with your own data)
data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "Close": [150, 152, 148, 155, 157, 160, 158, 162, 165, 163]
}
df = pd.DataFrame(data)

# Ensure Date is datetime type
df["Date"] = pd.to_datetime(df["Date"])

# Create the scatter plot
fig = go.Figure(
    data=go.Scatter(
        x=df["Date"],          # X-axis: Dates
        y=df["Close"],         # Y-axis: Close prices
        mode="lines+markers",  # Show both lines and points
        name="Close Price",    # Legend label
        line=dict(color="blue", width=2),
        marker=dict(size=6)
    )
)

# Customize layout
fig.update_layout(
    title="Close Price Over Time",
    xaxis_title="Date",
    yaxis_title="Close Price",
    template="plotly_white"
)

# Show the plot
fig.show()
