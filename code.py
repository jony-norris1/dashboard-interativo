import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Dados fictícios de vendas online
data = {'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
        'price': [100, 200, 120, 300, 220],
        'location': ['Brazil', 'USA', 'Brazil', 'USA', 'USA']}

df = pd.DataFrame(data)

# Adicione coluna de receita
df['revenue'] = df['price']

# Supondo que você tenha dados fictícios de latitude e longitude
df['latitude'] = [-23.5505, 37.7749, -23.5505, 37.7749, 37.7749]
df['longitude'] = [-46.6333, -122.4194, -46.6333, -122.4194, -122.4194]

# Gráfico de barras de produtos mais vendidos
fig1 = px.bar(df, x='product', y='revenue', color='location',
              title='Vendas por Produto',
              labels={'product': 'Produto',
                      'revenue': 'Receita',
                      'location': 'Localização'})

# Gráfico de linhas de vendas ao longo do tempo
fig2 = px.line(df, x='date', y='revenue', color='location',
               title='Vendas ao Longo do Tempo',
               labels={'date': 'Data',
                       'revenue': 'Receita',
                       'location': 'Localização'})

# Crie um mapa interativo
fig3 = go.Figure(go.Scattermapbox(
    lat=df['latitude'],
    lon=df['longitude'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=10
    ),
    text=df['location'],
))

fig3.update_layout(
    mapbox=go.layout.Mapbox(
        center=go.layout.mapbox.Center(
            lat=df['latitude'].mean(),
            lon=df['longitude'].mean(),
        ),
        zoom=1.5,
        style="open-street-map",
    ),
    title='Distribuição Geográfica das Vendas'
)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph1', figure=fig1),
    dcc.Graph(id='graph2', figure=fig2),
    dcc.Graph(id='graph3', figure=fig3),
])

if __name__ == '__main__':
    app.run_server(debug=True)
