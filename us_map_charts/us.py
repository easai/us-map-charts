import plotly.express as px
import pandas as pd

# Sample data: Population of US states with state abbreviations
data = {
    'state': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'population': [4903185, 731545, 7278717, 3017804, 39512223, 5758736, 3565287, 973764, 21477737, 10617423, 1415872, 1787065, 12671821, 6732219, 3155070, 2913314, 4467673, 4648794, 1344212, 6045680, 6892503, 9986857, 5639632, 2976149, 6137428, 1068778, 1934408, 3080156, 1359711, 8882190, 2096829, 19453561, 10488084, 762062, 11689100, 3956971, 4217737, 12801989, 1059361, 5148714, 884659, 6833174, 28995881, 3205958, 623989, 8535519, 7614893, 1792147, 5822434, 578759]
}

df = pd.DataFrame(data)

# Create a choropleth map
fig = px.choropleth(df, 
                    locations='state', 
                    locationmode='USA-states', 
                    scope='usa',
                    color='population', 
                    color_continuous_scale='Viridis_r',
                    labels={'population': 'Population'},
                    title='Population of US States')

# Show the map
fig.show()
