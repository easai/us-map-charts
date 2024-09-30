import plotly.graph_objects as go

fig = go.Figure(go.Choropleth(
    locations=['USA', 'CAN', 'MEX'],
    z=[1, 2, 3],
    text=['United States', 'Canada', 'Mexico'],  # Use 'text' instead of 'texttemplate'
    hoverinfo='location+z+text'
))

fig.show()
