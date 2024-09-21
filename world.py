import plotly.express as px
import pandas as pd

# Sample data
df = px.data.gapminder().query("year == 2007")

# Create a scatter geo map
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     projection="natural earth")

# Show the map
fig.show()

