from django_plotly_dash import DjangoDash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

from dashboard.models import VendaMensal, VendaCategoria, ClienteRegiao

# Dashboard 1
app1 = DjangoDash('Dashboard1')
dados1 = VendaMensal.objects.all().values()
df1 = pd.DataFrame(dados1)
fig1 = px.line(df1, x="mes", y="valor", title="Evolução de Vendas")
app1.layout = html.Div([dcc.Graph(figure=fig1)])


# Dashboard 2
app2 = DjangoDash('Dashboard2')
dados2 = VendaCategoria.objects.all().values()
df2 = pd.DataFrame(dados2)
fig2 = px.bar(df2, x="categoria", y="valor", title="Vendas por Categoria")
app2.layout = html.Div([dcc.Graph(figure=fig2)])


# Dashboard 3
app3 = DjangoDash('Dashboard3')
dados3 = ClienteRegiao.objects.all().values()
df3 = pd.DataFrame(dados3)
fig3 = px.pie(df3, names="regiao", values="quantidade", title="Distribuição de Clientes")
app3.layout = html.Div([dcc.Graph(figure=fig3)])


# Dashboard 4 continua com dados do plotly
from plotly.data import iris
df4 = iris()

app4 = DjangoDash('Dashboard4')
app4.layout = html.Div([
    html.Label("Selecione uma espécie:"),
    dcc.Dropdown(
        id="dropdown-species",
        options=[{"label": i, "value": i} for i in df4["species"].unique()],
        value="setosa"
    ),
    dcc.Graph(id="scatter-plot")
])

@app4.callback(
    Output("scatter-plot", "figure"),
    [Input("dropdown-species", "value")]
)
def update_graph(selected_species):
    filtered_df = df4[df4["species"] == selected_species]
    fig = px.scatter(filtered_df, x="sepal_width", y="sepal_length", color="species",
                     title=f"Espécie: {selected_species}")
    return fig
