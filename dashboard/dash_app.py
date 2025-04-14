import dash
from dash import html
from django_plotly_dash import DjangoDash

# Cria um app Dash chamado "SimpleExample"
app = DjangoDash("SimpleExample")

# Layout do Dash
app.layout = html.Div(children=[
    html.H1("Gráfico Simples com Dash"),
    html.P("Aqui vai seu conteúdo Plotly + Dash dentro do Django 🎉")
])
