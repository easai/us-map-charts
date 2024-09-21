import plotly.express as px
import pandas as pd

# Sample data: Average annual temperature (in Celsius) for US states
data = {
    'state': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'temperature': [18.3, -3.0, 15.6, 16.1, 15.0, 7.2, 10.6, 12.2, 21.1, 18.3, 23.3, 6.1, 10.6, 11.1, 9.4, 12.2, 13.3, 19.4, 6.1, 12.8, 10.0, 8.9, 5.6, 18.3, 12.8, 5.0, 9.4, 11.1, 9.4, 12.8, 13.3, 9.4, 15.6, 4.4, 10.6, 15.0, 10.0, 10.6, 9.4, 10.6, 11.1, 16.1, 19.4, 11.1, 6.1, 13.3, 10.0, 11.1, 11.1, 5.6]
}

print(f"{len(data['state'])=} {len(data['temperature'])}")

df = pd.DataFrame(data)

# Create a choropleth map
fig = px.choropleth(df, 
                    locations='state', 
                    locationmode='USA-states', 
                    scope='usa',
                    color='temperature', 
                    color_continuous_scale='RdYlBu_r',
                    labels={'temperature': 'Average Annual Temperature (°C)'},
                    title='Average Annual Temperature of US States')

# Show the map
fig.show()
