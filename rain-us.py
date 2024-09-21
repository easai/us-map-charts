import plotly.express as px
import pandas as pd

# Sample data: Average annual precipitation (in mm) for US states
data = {
    'state': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'precipitation': [1420, 460, 330, 1240, 580, 430, 1200, 1150, 1350, 1270, 1700, 460, 990, 1040, 910, 790, 1200, 1600, 1100, 1100, 1200, 820, 750, 1400, 1100, 380, 610, 240, 1100, 1200, 360, 1050, 1200, 510, 1000, 960, 1000, 760, 1100, 1200, 1100, 510, 1300, 790, 940, 1100, 970, 1100, 860, 310]
}

df = pd.DataFrame(data)

# Create a choropleth map
fig = px.choropleth(df, 
                    locations='state', 
                    locationmode='USA-states', 
                    scope='usa',
                    color='precipitation', 
                    color_continuous_scale='Blues',
                    labels={'precipitation': 'Annual Precipitation (mm)'},
                    title='Annual Precipitation of US States')

# Show the map
fig.show()
