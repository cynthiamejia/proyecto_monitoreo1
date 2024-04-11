# Main Project - Humidity, Temperatura and CO2
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

def setup_sensorth(url):
    df = pd.read_csv(url)
    df.drop(columns=['entry_id', 'field4', 'field5', 'field6'], inplace=True)
    df.rename(columns={'field1': 'Humedad', 'field2': 'Temperatura', 'field3':'CO2'}, inplace=True)
    return df

sensorth_8_12_Feb = "./Datasetth/8_12_Feb24.csv"
sensorth_12_16_Feb = "./Datasetth/12_16_Feb24.csv"
sensorth_16_20_Feb = "./Datasetth/16_20_Feb24.csv"
sensorth_20_24_Feb = "./Datasetth/20_24_Feb24.csv"
sensorth_24_28_Feb = "./Datasetth/24_28_Feb24.csv"
sensorth_28_2_Mar = "./Datasetth/28_2_Mar24.csv"
sensorth_2_6_Mar = "./Datasetth/2_6_Mar24.csv"
sensorth_6_10_Mar = "./Datasetth/6_10_Mar24.csv"
sensorth_10_14_Mar = "./Datasetth/10_14_Mar24.csv"
sensorth_14_18_Mar = "./Datasetth/14_18_Mar24.csv"

datath_1 = setup_sensorth(sensorth_8_12_Feb)
datath_2 = setup_sensorth(sensorth_12_16_Feb)
datath_3 = setup_sensorth(sensorth_16_20_Feb)
datath_4 = setup_sensorth(sensorth_20_24_Feb)
datath_5 = setup_sensorth(sensorth_24_28_Feb)
datath_6 = setup_sensorth(sensorth_28_2_Mar)
datath_7 = setup_sensorth(sensorth_2_6_Mar)
datath_8 = setup_sensorth(sensorth_6_10_Mar)
datath_9 = setup_sensorth(sensorth_10_14_Mar)
datath_10 = setup_sensorth(sensorth_14_18_Mar)

data_combined_th = pd.concat([datath_1, datath_2, datath_3, datath_4, datath_5, datath_6, datath_7, datath_8, datath_9, datath_10])

data_combined_th['created_at'] = pd.to_datetime(data_combined_th['created_at'])- pd.Timedelta(hours=6)
data_combined_th['created_at'] = data_combined_th['created_at'].dt.strftime('%Y-%m-%d %H:%M')

data_combined_th = data_combined_th.sort_values(by='created_at')

#print("Número de filas SIN ACONDICIONAMIENTO en data_combined_mm:")
#print(len(data_combined_th))

data_combined_th = data_combined_th.drop_duplicates(subset='created_at')
data_combined_th.dropna(inplace=True)
#print("Número de filas ACONDICIONADAS en data_combined_th:")
#print(len(data_combined_th))

app = dash.Dash()
server = app.server

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
                options=[ {'label': 'Humedad', 'value': 'Humedad'}, #la propiedad value es la utilizada internamente en el script
                          {'label': 'Temperatura', 'value': 'Temperatura'},
                          {'label': 'CO2', 'value': 'CO2'}],
                          #{'label': 'Humedad', 'value': 'H4'},
                          #{'label': 'CO2', 'value': 'C5'}],
                value='Humedad'
            )
        ], style={'width': '25%', 'display': 'inline-block'}),
     
     dcc.Graph(id='grafico_var'),
     dcc.Graph(id='grafico_var2') 
],style={'padding':20})


axis_labels = {
    'Humedad': 'Humedad (%)',
    'Temperatura': 'Temperatura (°C)',
    'CO2': 'CO2 (ppm)'
}

@app.callback(
    Output('grafico_var', 'figure'),
    [Input('selec_variable', 'value')])

def update_graph1(nombre_variable):
    y_axis_label = axis_labels.get(nombre_variable, nombre_variable)
    return {
        'data': [go.Scatter(x=data_combined_th["created_at"],
                   y= data_combined_th[nombre_variable],
                   name = 'Metano en SIMAR',
                   line = dict(color='green', width=2),
                   mode="lines+markers",
                   )],
        'layout': go.Layout(title = f"Medición de {nombre_variable}",
                    xaxis = dict(title = "Fecha"),
                    yaxis = dict(title = y_axis_label ))
            } 


@app.callback(
    Output('grafico_var2', 'figure'),
    [Input('selec_variable', 'value')])

def update_graph2(nombre_variable):
    df = data_combined_th
    fig = px.histogram(df, x=nombre_variable, marginal="box", title=f"Distribución de Datos de {nombre_variable}", hover_data=df.columns)
    data2 = fig.to_dict()['data']
    layout2 = fig.to_dict()['layout']
    layout2['title']['x'] = 0.5
    layout2['yaxis']['title'] = f"Conteo de datos de {nombre_variable}"
    layout2['xaxis']['title'] = f"{nombre_variable}"
    for trace in data2:
        trace['marker']['color'] = 'blue'
    return {'data': data2, 'layout': layout2}

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=8005)

