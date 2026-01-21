# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash('Pink Morsel')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('./single-formatted_data.csv')

fig = px.bar(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales (USD)",
)

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales',
        style={'textAlign': 'center'}    
    ),

    html.Div(
        children='Visualising the sales data of Pink Morsel across all regions.',
        style={'textAlign': 'center', 'marginBottom': '20px'}    
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
