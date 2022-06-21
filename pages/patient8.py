import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash import Input, Output, callback
#import globals

#data_parser = globals.data_parser

from dash import Input, Output, callback
import plotly.express as px
import pandas as pd

# kaikki annetut lääkkeet
medcsv = pd.read_csv('mimicData/P8/inputText28093007.csv')
# uniikit lääkenimet valintaa varten
medoptions = sorted(medcsv["label"].unique())
# charted event taulukko
charcsv = pd.read_csv('mimicData/P8/Responce28093007.csv')
# respitatory, vital ym labels
charoptions = sorted(charcsv["label"].unique())
# respitatory, vital ym category
#charcategory = charcsv["category"].unique()
# diagnoosit taulukko
diagcsv = pd.read_csv('mimicData/P8/patient28093007_descDiag.csv')

layout = html.Div([
    html.H1(children='Interactive visualization for data science thesis'),
    dcc.Link('Info', href='/info', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 1', href='/patient1', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 2', href='/patient2', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 3', href='/patient3', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 4', href='/patient4', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 5', href='/patient5', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 6', href='/patient6', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 7', href='/patient7', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 8', href='/patient8', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 9', href='/patient9', style={'display': 'inline-block','padding': '10px'}),
    dcc.Link('Patient 10', href='/patient10', style={'display': 'inline-block','padding': '10px'}),
    html.H2(children='Patient 8'),
    html.H3(children='Medication'),

    dcc.Checklist(
         id="medChecklist8",
        options=[{"label": x, "value": x} for x in medoptions],
        value=medoptions[0:6],
         labelStyle={'display': 'inline-block'}
    ),
    html.H3(children='Medication'),
    dcc.Graph(
        id='medication8',
        config={'displayModeBar': True}
    ),
    html.H3(children='Patient Responce'),
    dcc.Graph(
        id='chartedevents8',
        config={'displayModeBar': True}
    ),
    dcc.Checklist(
        id="charChecklist8",
        options=[{"label": x, "value": x} for x in charoptions],
        value=charoptions[0:6],
        labelStyle={'display': 'inline-block'}
    ),
    dash_table.DataTable(
        id='table8',
        columns=[{"name": i, "id": i} 
                 for i in diagcsv.loc[:,['seq_num','icd_code','icd_version_x', 'long_title']]],
        data=diagcsv.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
    )
])

# Medication graph
@callback(
    Output("medication8", "figure"),
    [Input("medChecklist8", "value")])
def update_med_chart(medList):
    mask = medcsv['label'].isin(medList)
    medfig = px.scatter(
        medcsv[mask], 
        y="label", 
        x="starttime", 
        color="label", 
        hover_data=['rate', 'unitname'])
    medfig.update_xaxes(
        rangeslider_visible=True,
    )
    return medfig
    
# Charted events ("responce") graph
@callback(
    Output("chartedevents8", "figure"),
    [Input("charChecklist8", "value")])
def update_med_chart(charList):
    mask = charcsv['label'].isin(charList)
    charfig = px.line(
        charcsv[mask], 
        y="valuen", 
        x="charttime", 
        color="label", 
        hover_data=['label', 'unitname'],
    )
    charfig.update_xaxes(
        rangeslider_visible=True,)
    charfig.update_traces(mode='lines+markers')
    return charfig