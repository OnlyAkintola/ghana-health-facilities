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

shaz13_custom_style = "mapbox://styles/mapbox/streets-v11"
data = [go.Scattergeo(
            lat= df['latitude'] ,
            lon= df['longitude'],
            text = df['facilityname'],
            mode='markers',
            marker=go.scattermapbox.Marker(
            size=10

            ),
)]
myheading1 = 'Ghana Health Facilities'
tabtitle = 'Ghana'

########## Set up the chart

layout = go.Layout(
            autosize=False,
            width=900,
            height=600,
            title = "Ghana",
            geo_scope='africa')

fig = dict(data=data, layout=layout)

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
