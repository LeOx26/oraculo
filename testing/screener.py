from gettext import install
import yfinance as yf
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

nasdaq_tickers = pd.read_csv('nasdaq_screener.csv')

fig = px.histogram(nasdaq_tickers)

app.layout = html.Div(children=[html.H1(children='Screener'),
    dcc.Graph(
        id='Screener nasdaq',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)