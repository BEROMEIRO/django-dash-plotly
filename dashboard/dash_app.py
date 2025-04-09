import dash
from dash import html
from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')

app.layout = html.Div([
    html.H1("Meu primeiro Dash em Django!"),
    html.P("Legal demais!"),
])
