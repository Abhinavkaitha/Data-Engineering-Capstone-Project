import dash
import plotly.graph_objs as go
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from sqlalchemy import create_engine
from dash.dependencies import Input, Output
import pandas_datareader.data as web
from datetime import datetime

app = dash.Dash()

db = 'abkaitha'
user = 'abkaitha'
host = 'tone-of-the-nation.c8ubsnm2laco.us-west-2.rds.amazonaws.com'
password = 'abkaitha'
port = '5432'

url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, db)

con = create_engine(url)

features = ['Coca-Cola', 'Pepsi']
hours = list(range(1, 25))
days = ['Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
        'Sun']

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='company',
            options=[{'label': i, 'value': i} for i in features],
            value='Coca-Cola'
        )
    ], style={'width': '28%', 'display': 'inline-block'}),

    html.Div([
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2018, 5, 2),
            max_date_allowed=datetime(2018, 10, 31),
            start_date=datetime(2018, 5, 2),
            end_date=datetime(2018, 5, 3)
        )
    ], style={'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='hour',
            options=[{'label': i, 'value': i} for i in hours],
            value=14
        )
    ], style={'width': '18%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='day',
            options=[{'label': i, 'value': i} for i in days],
            value='Thu'
        )
    ], style={'width': '18%', 'display': 'inline-block'}),

        dcc.Graph(style={'height': '700px'},id='feature-graphic'),
    html.H3(children = '0 --> Negative  1--> Positive',style={'textAlign':'right'})
    ], style={'padding': 10})

@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('company', 'value'),
     Input('hour', 'value'),
    Input('my_date_picker','start_date'),
     Input('my_date_picker','end_date'),
     Input('day','value')])
def update_graph(company_name, hour_of_the_day, start_date, end_date, day):

    states = pd.read_sql("SELECT * FROM tone1 WHERE tone1.date BETWEEN '{}' AND '{}' AND tone1.company = '{}' AND tone1.hour={} AND tone1.day='{}'".format(start_date, end_date, company_name, hour_of_the_day, day), con)
    mean_df = states.groupby('location').mean()
    mean_tone = mean_df['tone']
    valid_states = list(mean_df.index)
    return {
        'data':[go.Choropleth(
    locations = valid_states,
    z = mean_tone,
    locationmode = 'USA-states',
    colorscale = 'Blues',
    colorbar_title = 'Sentiment')
                                 ],
    'layout': go.Layout(
    title_text = 'Tone of the Nation',
    geo_scope = 'usa')
    }


if __name__ == '__main__':
    app.run_server(port=80,host='0.0.0.0')
