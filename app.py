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
data = [go.Scattermapbox(
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

layout = go.Layout(autosize=False,
                   mapbox= dict(accesstoken="pk.eyJ1IjoiYWtpbnRvbGEiLCJhIjoiY2swazZ1ODR6MGllcDNjcXM1ZzJqdDFrNiJ9.qMY4G68kqD_5BLa0tqq9bw",
                                bearing=10,
                                pitch=60,
                                zoom=5,
                                center= dict(lat=7.9465,
                                             lon=1.0232),
                                style=shaz13_custom_style),
                    width=900,
                    height=600,
                    title = "Ghana")

fig = dict(data=data, layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1)
    dcc.Graph(
        id='ghana_graph',
        figure=fig
    )
])

############ Deploy
if __name__ == '__main__':
    app.run_server()
