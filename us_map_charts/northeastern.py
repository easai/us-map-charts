import plotly.express as px
import pandas as pd

# Sample DataFrame for northeastern states
data = {
    'state': ['NY', 'NJ', 'PA', 'CT', 'MA', 'RI', 'VT', 'NH', 'ME', 'DC','MD','DE'],
    'electoral_votes': [28, 14, 19, 7, 11, 4, 3, 4, 4, 3, 10, 3]
}
df_northeast = pd.DataFrame(data)

# Create the choropleth map
fig = px.choropleth(df_northeast,
                    locations='state',
                    locationmode='USA-states',
                    color='electoral_votes',
                    color_continuous_scale='purpor',
                    range_color=(0, 54),
                    scope='usa')

# Update the layout to focus on the northeastern region
fig.update_geos(
    visible=False,
    resolution=50,
    scope='usa',
    projection=dict(type='albers usa'),
    center=dict(lat=41, lon=-74),
    lataxis_range=[36, 46], lonaxis_range=[-82, -66]
)

fig.add_scattergeo(
    locations=df_northeast['state'],
    locationmode="USA-states",
    text=df_northeast['electoral_votes'],
    mode='text',
    textfont=dict(
        family="helvetica",
        size=18,
        color="red"
    )
)

fig.show()
