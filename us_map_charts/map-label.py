import plotly.graph_objects as go

# Sample data
states = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
values = [100, 200, 150, 180, 130]
latitudes = [36.7783, 31.9686, 40.7128, 27.9944, 40.6331]
longitudes = [-119.4179, -99.9018, -74.0060, -81.7603, -89.3985]

# Create the map
fig = go.Figure(go.Scattergeo(
    locationmode = 'USA-states',
    lon = longitudes,
    lat = latitudes,
    text = [f'{state}: {value}' for state, value in zip(states, values)],
    mode = 'markers+text',
    marker = dict(size = 10, color = 'blue'),
    textposition = 'top center'
))

# Update layout for better visualization
fig.update_layout(
    title = 'US Map with Labeled Values',
    geo = dict(
        scope = 'usa',
        projection = dict(type = 'albers usa'),
        showland = True,
    )
)

fig.show()
