# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
prediction = 0
column1 = dbc.Col(
    [
        html.H1('Enter some information about your home'),
        html.Br(),
        html.H4('Latitude'),
        dcc.Slider(id='latitude',
            min=19.5,
            max=64.85,
            step=0.25,
            value=42.5,
            marks={19.5: {'label': '19.5°'},
            64.85: {'label': '64.85°'}}),

        html.H4('Longitude'),
        dcc.Slider(id='longitude',
            min=-161.75,
            max=-68,
            step=0.25,
            value=-114,
            marks={-161.75: {'label': '-161.75°'},
            -68: {'label': '-68°'}}),
        
        html.Div(
            [html.H3('Enter the area (in sq. feet) of each face of the roof'),
            html.Br(),
            dcc.Input(id='north', type='number', value=0),
            html.H4('North'),
            dcc.Input(id='east', type='number', value=0),
            html.H4('East'),
            dcc.Input(id='south', type='number', value=0),
            html.H4('South'),
            dcc.Input(id='west', type='number', value=0),
            html.H4('West')],
            id='roof_div'
            ),
        html.Br(),
        html.Div(
            [
            dcc.Checklist(id='flat_yn',
                options=[{'label':'My roof is flat', 'value':1}],
                labelStyle= {
                'font-weight': 'bold',
                'display': 'block',
                'position': 'relative',
                'margin-bottom': 12,
                'font-size': 22},
         inputStyle= {
            'height': 20,
            'width' : 20
            })
            ],
            id='check_div'
        ),

        html.Div(
            [
                html.H4('Enter the area of your roof'),
                dcc.Input(id='flat_area', type='number', value=0)
            ],
            hidden=True,
            id='flat_div'
        )
    ],
    md=6,
)



column2 = dbc.Col(
    [
        html.H2('If you install the maximum number of solar panels on your roof, you could produce approximately'),
        html.Br(),
        html.Br(),
        html.H1('0', style={'padding-left':240}),
        html.Br(),
        html.Br(),
        html.H2('kWh of electricity per year')
    ]
)

layout = dbc.Row([column1, column2])

sunlight_pred = pickle.load(open('Models/sunlight_total.pkl', 'rb'))