# Main Project - Metan and Monoxide
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff 
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px

def setup_sensormm(url):
    df = pd.read_csv(url)
    df.drop(columns=['entry_id', 'field1', 'field4', 'field5', 'field6'], inplace=True)
    df.rename(columns={'field2': 'Metano', 'field3': 'Monóxido'}, inplace=True)
    return df

sensormm_8_12_Feb = "./Datasetmm/8_12_Feb24.csv"
sensormm_12_16_Feb = "./Datasetmm/12_16_Feb24.csv"
sensormm_16_20_Feb = "./Datasetmm/16_20_Feb24.csv"
sensormm_20_24_Feb = "./Datasetmm/20_24_Feb24.csv"
sensormm_24_28_Feb = "./Datasetmm/24_28_Feb24.csv"
sensormm_28_2_Mar = "./Datasetmm/28_2_Mar24.csv"
sensormm_2_6_Mar = "./Datasetmm/2_6_Mar24.csv"
sensormm_6_10_Mar = "./Datasetmm/6_10_Mar24.csv"
sensormm_10_14_Mar = "./Datasetmm/10_14_Mar24.csv"
sensormm_14_18_Mar = "./Datasetmm/14_18_Mar24.csv"

datamm_1 = setup_sensormm(sensormm_8_12_Feb)
datamm_2 = setup_sensormm(sensormm_12_16_Feb)
datamm_3 = setup_sensormm(sensormm_16_20_Feb)
datamm_4 = setup_sensormm(sensormm_20_24_Feb)
datamm_5 = setup_sensormm(sensormm_24_28_Feb)
datamm_6 = setup_sensormm(sensormm_28_2_Mar)
datamm_7 = setup_sensormm(sensormm_2_6_Mar)
datamm_8 = setup_sensormm(sensormm_6_10_Mar)
datamm_9 = setup_sensormm(sensormm_10_14_Mar)
datamm_10 = setup_sensormm(sensormm_14_18_Mar)

data_combined_mm = pd.concat([datamm_1, datamm_2, datamm_3, datamm_4, datamm_5, datamm_6, datamm_7, datamm_8, datamm_9, datamm_10])

data_combined_mm['created_at'] = pd.to_datetime(data_combined_mm['created_at'])- pd.Timedelta(hours=6)
data_combined_mm['created_at'] = data_combined_mm['created_at'].dt.strftime('%Y-%m-%d %H:%M')

data_combined_mm = data_combined_mm.sort_values(by='created_at')

#print("Número de filas SIN ACONDICIONAMIENTO en data_combined_mm:")
#print(len(data_combined_mm))

data_combined_mm = data_combined_mm.drop_duplicates(subset='created_at')
data_combined_mm.dropna(inplace=True)

print("Número de filas ACONDICIONADAS en data_combined_mm:")
#print(len(data_combined_mm))

app = dash.Dash()
#server = app.server

font_style = {'fontFamily': 'Segoe UI, Arial, sans-serif'}

app.layout = html.Div([
     html.Div([
          html.Img(src='https://upload.wikimedia.org/wikipedia/commons/d/d4/Logo-TecNM-2017.png',
                 style={'height': '200px', 'width': '300px', 'verticalAlign': 'middle', 'marginRight': '30px'}),
          html.H1(children='Visualización de variables para SIMAR', style=font_style),
          ], style={'display': 'flex', 'alignItems': 'center','marginBottom': '20px'}),
          html.P(children='Instituto Tecnológico de Ciudad Guzmán'),
     
     html.Div([
            dcc.Dropdown(
                id='selec_variable',
                options=[ {'label': 'Metano', 'value': 'Metano'}, #la propiedad value es la utilizada internamente en el script
                          {'label': 'Monóxido', 'value': 'Monóxido'}],
                          #{'label': 'Temperatura', 'value': 'T3'},
                          #{'label': 'Humedad', 'value': 'H4'},
                          #{'label': 'CO2', 'value': 'C5'}],
                value='Metano'
            )
        ], style={'width': '25%', 'display': 'inline-block'}),
     
     dcc.Graph(id='grafico_var'),
     dcc.Graph(id='grafico_var2') 
],style={'padding':20})

@app.callback(
    Output('grafico_var', 'figure'),
    [Input('selec_variable', 'value')])

def update_graph1(nombre_variable):
    return {
        'data': [go.Scatter(x=data_combined_mm["created_at"],
                   y= data_combined_mm[nombre_variable],
                   name = 'Metano en SIMAR',
                   line = dict(color='green', width=2),
                   mode="lines+markers",
                   )],
        'layout': go.Layout(title = f"Medición de {nombre_variable}",
                    xaxis = dict(title = "Fecha"),
                    yaxis = dict(title = f'{nombre_variable} (ppm)' ))
            } 


@app.callback(
    Output('grafico_var2', 'figure'),
    [Input('selec_variable', 'value')])

def update_graph2(nombre_variable):
    df = data_combined_mm
    fig = px.histogram(df, x=nombre_variable, marginal="box", title=f"Distribución de Datos de {nombre_variable}", hover_data=df.columns)
    data2 = fig.to_dict()['data']
    layout2 = fig.to_dict()['layout']
    layout2['title']['x'] = 0.5
    layout2['yaxis']['title'] = f"Conteo de datos de {nombre_variable}"
    layout2['xaxis']['title'] = f"{nombre_variable} (ppm)"
    for trace in data2:
        trace['marker']['color'] = 'blue'
    return {'data': data2, 'layout': layout2}

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=7000)
