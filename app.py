import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.graph_objects as go
import pandas as pd

########### Define your variables ######
df = pd.read_csv('assets/health-facilities-gh.csv')
df.rename(columns={
    'Region' : 'region',
    'District' : 'district',
    'FacilityName' : 'facilityname',
    'Type' : 'type',
    'Town' : 'town',
    'Ownership' : 'ownership',
    'Latitude' : 'latitude',
    'Longitude' : 'longitude',
},inplace=True)

fig = go.Figure(data=go.Scattergeo(
        lon = df['longitude'],
        lat = df['latitude'],
        mode = 'markers',
        dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)')
        )
))


########## Set up the chart

layout = go.update_layout(
            autosize=False,
            width=900,
            height=600,
            title = "Ghana",
            geo_scope='africa')

########### Initiate the app

app = dash.Dash(__name__)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.Graph(
        id='figure-1',
        figure=fig
    )
])

############ Deploy
if __name__ == '__main__':
    app.run_server()
