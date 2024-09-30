
import plotly.express as px
import pandas as pd

# The number of electoral votes for each state
data = {
    'state': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'electoral_votes': [9, 3, 11, 6, 54, 10, 7, 3, 3, 30, 16, 4, 4, 19, 11, 6, 6, 8, 8, 4, 10, 11, 15, 10, 6, 10, 4, 5, 6, 4, 14, 5, 28, 16, 3, 17, 7, 8, 19, 4, 9, 3, 11, 40, 6, 3, 13, 12, 4, 10, 3]
}

df = pd.DataFrame(data)

# Create a choropleth map
fig = px.choropleth(df, 
                    locations='state', 
                    locationmode='USA-states', 
                    scope='usa',
                    color='electoral_votes', 
                    color_continuous_scale='purpor',
                    labels={'electoral_votes':'Electoral Votes', 'state':'State'},
                    title='Election 2024: The number of electoral votes for each state')

fig.add_scattergeo(
    locations=df['state'],
    locationmode="USA-states",
    text=df['electoral_votes'],
    mode='text',
    textfont=dict(
        family="helvetica",
        size=18,
        color="red"
    )
)

# Show the map
fig.show()
