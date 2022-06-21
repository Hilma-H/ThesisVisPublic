from dash import Dash, dcc, html

layout = html.Div([
    html.H3(children='Interactive visualization for data science thesis'),
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
    html.Div(
        style={'padding': '20px'},
        children=[
            dcc.Markdown('''
                ## Yleistä:
                Tämä visualisaation on osa gradu-projektia.

                Tässä visualisaatiossa on esillä kymmenen eri potilasta kukin omalla sivullaan.

                Visualisaation latautuminen saattaa kestää hetken, odota rauhassa.

            ''')
        ]
    )
])