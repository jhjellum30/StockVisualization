import plotly.graph_objects as go

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 14]

# Create a Figure object
fig = go.Figure()

# Add a line trace
fig.add_trace(
    go.Scatter(
        x=x_values,
        y=y_values,
        mode='lines+markers',  # Show both lines and markers
        name='Sample Data',
        line=dict(color='royalblue', width=2),
        marker=dict(size=8, color='orange', symbol='circle')
    )
)

# Customize layout
fig.update_layout(
    title="Line Chart Example with plotly.graph_objects",
    xaxis_title="X Axis Label",
    yaxis_title="Y Axis Label",
    template="plotly_white",  # Clean background
    hovermode="x unified"     # Single hover label for all traces
)

# Show the interactive plot
fig.show()
