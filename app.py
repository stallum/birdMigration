import dash
from dash import html, dcc
from charts import createFigures
import pandas as pd
from utils import loadData

# Carrega os dados
df = loadData()

# Gera os gráficos
fig1, fig2, fig3, fig4, fig5 = createFigures(df)

# Inicializa o app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Migração de Aves", style={'textAlign': 'center'}),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5),
])

if __name__ == "__main__":
    app.run(debug=True)