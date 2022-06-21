# main app for visualisation

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output, callback
from pages import info, patient1, patient2, patient3, patient4, patient5, patient6, patient7, patient8, patient9, patient10

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/info':
        return info.layout
    elif pathname == '/patient1':
        return patient1.layout
    elif pathname == '/patient2':
        return patient2.layout
    elif pathname == '/patient3':
        return patient3.layout
    elif pathname == '/patient4':
        return patient4.layout
    elif pathname == '/patient5':
        return patient5.layout
    elif pathname == '/patient6':
        return patient6.layout
    elif pathname == '/patient7':
        return patient7.layout
    elif pathname == '/patient8':
        return patient8.layout
    elif pathname == '/patient9':
        return patient9.layout
    elif pathname == '/patient10':
        return patient10.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)