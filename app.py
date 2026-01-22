from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash('Pink Morsel')

df = pd.read_csv('./single-formatted_data.csv')
df = df.sort_values(by='date')

COLORS = {
    'background': '#1e1e1e',
    'text': '#f5a9bc',
    'card': '#2d2d2d'
}


app.layout = html.Div(
    style={'backgroundColor': COLORS['background'], 'color': COLORS['text'], 'padding': '40px', 'minHeight': '100vh'},
    children=[
    html.H1(
        children='Pink Morsel Visualizer',
        style={'textAlign': 'center', 'fontWeight': 'bold', 'fontSize': '42px'}    
    ),

    html.Div(
        children='Visualising the sales data of Pink Morsel across all regions.',
        style={'textAlign': 'center', 'color': '#ffffff', 'opacity': '0.8'}    
    ),

    html.Div(
        style={
            'backgroundColor': COLORS['card'], 
            'padding': '20px', 
            'borderRadius': '15px', 
            'boxShadow': '0px 4px 15px rgba(0,0,0,0.5)',
            'maxWidth': '600px',
            'margin': '0 auto 30px auto'
        },
        children=[
            html.Label("Filter by Region", style={'fontWeight': 'bold', 'display': 'block', 'marginBottom': '10px', 'textAlign': 'center'}),
            dcc.RadioItems(
                id='region-picker',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all',
                inline=True,
                style={'textAlign': 'center'},
                inputStyle={"margin-left": "20px", "margin-right": "5px"}
            )
        ]
    ),

    html.Div(
        style={'backgroundColor': COLORS['card'], 'borderRadius': '15px', 'padding': '20px'},
        children=[
            dcc.Graph(
                id='sales-line-chart',
            )
        ]
    )
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)

def update_graph(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales Data: {region.capitalize()}", template="plotly_dark")

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales (USD)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color=COLORS['text']
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
