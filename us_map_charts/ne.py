import plotly.graph_objects as go

# Define the northeastern states
northeastern_states = ['ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA']

# Create a map figure
fig = go.Figure()

# Add the states to the map
for state in northeastern_states:
    fig.add_trace(go.Choropleth(
        locations=[state],
        locationmode='USA-states',
        z=[1],  # Dummy value for color scale
        colorscale='Blues',
        showscale=False,
        geo='geo'
    ))

# Update the layout of the map
fig.update_layout(
    title_text='Northeastern States of the USA',
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'
    )
)

fig.update_geos(fitbounds="locations")

# Show the map
fig.show()
