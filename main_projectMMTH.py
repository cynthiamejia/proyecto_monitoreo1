# Main Project - Humidity, Temperatura and CO2
# Version 3.0. JAGR.
# 28/05/2024
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
sensorth_18_22_Mar = "./Datasetth/18_22_Mar24.csv"
sensorth_22_26_Mar = "./Datasetth/22_26_Mar24.csv"
sensorth_26_30_Mar = "./Datasetth/26_30_Mar24.csv"
sensorth_30_3_Abr = "./Datasetth/30_3_Abr24.csv"
sensorth_3_7_Abr = "./Datasetth/3_7_Abr24.csv"
sensorth_26_30_Abr = "./Datasetth/26_30_Abr24.csv"
sensorth_30_4_May = "./Datasetth/30_4_May24.csv"
sensorth_4_8_May = "./Datasetth/4_8_May24.csv"
sensorth_8_23_May = "./Datasetth/8_23_May24.csv"
sensorth_23_27_May = "./Datasetth/23_27_May24.csv"
sensorth_27_30_May = "./Datasetth/27_30_May24.csv"


# NOTE1: Add HERE for more TH data. 

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
sensormm_18_22_Mar = "./Datasetmm/18_22_Mar24.csv"
sensormm_22_26_Mar = "./Datasetmm/22_26_Mar24.csv"
sensormm_26_30_Mar = "./Datasetmm/26_30_Mar24.csv"
sensormm_30_3_Abr = "./Datasetmm/30_3_Abr24.csv"
sensormm_3_7_Abr = "./Datasetmm/3_7_Abr24.csv"
sensormm_26_30_Abr = "./Datasetmm/26_30_Abr24.csv"
sensormm_30_4_May = "./Datasetmm/30_4_May24.csv"
sensormm_4_8_May = "./Datasetmm/4_8_May24.csv"


# NOTE2: Add HERE for more MM data. 

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
datamm_11 = setup_sensormm(sensormm_18_22_Mar)
datamm_12 = setup_sensormm(sensormm_22_26_Mar)
datamm_13 = setup_sensormm(sensormm_26_30_Mar)
datamm_14 = setup_sensormm(sensormm_30_3_Abr)
datamm_15 = setup_sensormm(sensormm_3_7_Abr)
datamm_16 = setup_sensormm(sensormm_26_30_Abr)
datamm_17 = setup_sensormm(sensormm_30_4_May)
datamm_18 = setup_sensormm(sensormm_4_8_May)


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
datath_11 = setup_sensorth(sensorth_18_22_Mar)
datath_12 = setup_sensorth(sensorth_22_26_Mar)
datath_13 = setup_sensorth(sensorth_26_30_Mar)
datath_14 = setup_sensorth(sensorth_30_3_Abr)
datath_15 = setup_sensorth(sensorth_3_7_Abr)
datath_16 = setup_sensorth(sensorth_26_30_Abr)
datath_17 = setup_sensorth(sensorth_30_4_May)
datath_18 = setup_sensorth(sensorth_4_8_May)
datath_19 = setup_sensorth(sensorth_8_23_May)
datath_20 = setup_sensorth(sensorth_23_27_May)
datath_21 = setup_sensorth(sensorth_27_30_May)


data_combined_mm = pd.concat([datamm_1, datamm_2, datamm_3, datamm_4, datamm_5, datamm_6, datamm_7, datamm_8, datamm_9, datamm_10, datamm_11, datamm_12, datamm_13, datamm_14, datamm_15, datamm_16, datamm_17, datamm_18])
data_combined_th = pd.concat([datath_1, datath_2, datath_3, datath_4, datath_5, datath_6, datath_7, datath_8, datath_9, datath_10, datath_11, datath_12, datath_13, datath_14, datath_15, datath_16, datath_17, datath_18, datath_19, datath_20, datath_21])
# NOTE3: Add data name files. 


data_combined_th['created_at'] = pd.to_datetime(data_combined_th['created_at'])- pd.Timedelta(hours=6)
data_combined_th['created_at'] = data_combined_th['created_at'].dt.strftime('%Y-%m-%d %H:%M')
data_combined_th = data_combined_th.sort_values(by='created_at')
data_combined_th = data_combined_th.drop_duplicates(subset='created_at')
data_combined_th.dropna(inplace=True)

data_combined_mm['created_at'] = pd.to_datetime(data_combined_mm['created_at'])- pd.Timedelta(hours=6)
data_combined_mm['created_at'] = data_combined_mm['created_at'].dt.strftime('%Y-%m-%d %H:%M')
data_combined_mm = data_combined_mm.sort_values(by='created_at')
data_combined_mm = data_combined_mm.drop_duplicates(subset='created_at')
data_combined_mm.dropna(inplace=True)


# NOTE4: Select Sample Minutes
sample_minutes = 7
data_combined_th=data_combined_th[::sample_minutes]
data_combined_mm=data_combined_mm[::sample_minutes]

######### APLICATION ################
#### Version 3.0 #################### 28/05/2024
app = dash.Dash()
server = app.server

font_style = {'fontFamily': 'Segoe UI, Arial, sans-serif','fontSize': '45px'}

app.layout = html.Div([
     html.Div([
          html.Img(src='https://upload.wikimedia.org/wikipedia/commons/d/d4/Logo-TecNM-2017.png',
                 style={'height': '200px', 'width': '300px', 'verticalAlign': 'middle', 'marginRight': '80px'}),
          html.H1(children='Monitoreo de variables ambientales', style=font_style),
          ], style={'display': 'flex', 'alignItems': 'center','marginBottom': '30px'}),
          html.P(children='Instituto Tecnológico de Ciudad Guzmán', style={'fontSize': '25px', 'fontWeight': 'bold'}),
     html.Br(),  
     html.Div([
         html.Div([
             html.Label('Selección variable canal 1', style={'display': 'inline-block','fontSize': '25px','marginBottom': '20px'}),
             dcc.Dropdown(
                 id='selec_variable1',
                 options=[ {'label': 'Humedad', 'value': 'Humedad'}, #la propiedad value es la utilizada internamente en el script
                           {'label': 'Temperatura', 'value': 'Temperatura'},
                           {'label': 'CO2', 'value': 'CO2'}],
                value='Humedad'
            ),
         ], style={'display': 'inline-block', 'marginRight': '125px'}), 

         html.Div([
             html.Label('Rango fecha canal 1', style={'display': 'inline-block','fontSize': '25px','marginRight': '25px'}),
             dcc.DatePickerRange(
                 id='selector_fecha1', 
                 start_date=data_combined_th['created_at'].min(), 
                 end_date=data_combined_th['created_at'].max()
                 ) 
        ], style={'display': 'inline-block'}),
        ], style={'display': 'inline-block','width': '90%', 'margin':'auto', 'marginBottom': '2px'}
        ),
     
     dcc.Graph(id='grafico_var1'),
     
     
     html.Div([
         html.Div([
             html.Label('Selección variable canal 2', style={'display': 'inline-block','fontSize': '25px','marginBottom': '20px'}),
             dcc.Dropdown(
                 id='selec_variable2',
                 options=[ {'label': 'Metano', 'value': 'Metano'},
                          {'label': 'Monóxido', 'value': 'Monóxido'}],
                 value='Metano'
            ), 
     ], style={'display': 'inline-block', 'marginRight': '125px'}), 
         
         html.Div([
             html.Label('Rango fecha canal 2', style={'display': 'inline-block','fontSize': '25px','marginRight': '25px'}),
             dcc.DatePickerRange(
                 id='selector_fecha2', 
                 start_date=data_combined_mm['created_at'].min(), 
                 end_date=data_combined_mm['created_at'].max()
                 ), 
     ], style={'display': 'inline-block'}) 
     ], style={'display': 'inline-block','width': '90%', 'margin':'auto', 'marginBottom': '2px'}
     ),

     dcc.Graph(id='grafico_var3'),
     
     dcc.Graph(id='grafico_var2'),

     dcc.Graph(id='grafico_var4')
     
],style={'padding':20})

axis_labels1 = {
    'Humedad': 'Humedad (%)',
    'Temperatura': 'Temperatura (°C)',
    'CO2': 'CO2 (ppm)'
}

@app.callback(
    Output('grafico_var1', 'figure'),
    [Input('selector_fecha1', 'start_date'), Input('selector_fecha1', 'end_date'), Input('selec_variable1', 'value')])

def update_graph1(fecha_min, fecha_max, nombre_variable):
    filt_data_combined_th = data_combined_th[(data_combined_th["created_at"]>=fecha_min) & (data_combined_th["created_at"]<=fecha_max)]
    y_axis_label = axis_labels1.get(nombre_variable, nombre_variable)
    
    if nombre_variable == "Humedad":
        return {
            'data': [go.Scatter(x=filt_data_combined_th["created_at"],
                                y=filt_data_combined_th[nombre_variable],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label ))
                } 
    
    if nombre_variable == "Temperatura":
        return {
            'data': [go.Scatter(x=filt_data_combined_th["created_at"],
                                y=filt_data_combined_th[nombre_variable],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label ))
                }
    
    if nombre_variable == "CO2":
        return {
            'data': [go.Scatter(x=filt_data_combined_th["created_at"],
                                y=filt_data_combined_th[nombre_variable],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label ))
                }
    
    else:
        return {
            'data': [go.Scatter(x=data_combined_th["created_at"],
                                y=data_combined_th[nombre_variable],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label ))
        }

@app.callback(
    Output('grafico_var2', 'figure'),
    [Input('selec_variable1', 'value')])

def update_graph2(nombre_variable):
    df = data_combined_th
    fig = px.histogram(df, x=nombre_variable, marginal="box", title=f"Distribución de datos de {nombre_variable}", hover_data=df.columns)
    data2 = fig.to_dict()['data']
    layout2 = fig.to_dict()['layout']
    layout2['title']['x'] = 0.5
    layout2['yaxis']['title'] = f"Conteo de datos de {nombre_variable}"
    layout2['xaxis']['title'] = f"{nombre_variable}"
    for trace in data2:
        trace['marker']['color'] = 'blue'
    return {'data': data2, 'layout': layout2}

axis_labels2 = {
    'Monóxido': 'Monóxido',
    'Metano': 'Metano'
}

@app.callback(
    Output('grafico_var3', 'figure'),
    [Input('selector_fecha2', 'start_date'), Input('selector_fecha2', 'end_date'), Input('selec_variable2', 'value')])

def update_graph21(fecha_min2, fecha_max2, nombre_variable2):
    filt_data_combined_mm = data_combined_mm[(data_combined_mm["created_at"]>=fecha_min2) & (data_combined_mm["created_at"]<=fecha_max2)]
    y_axis_label2 = axis_labels2.get(nombre_variable2, nombre_variable2)
    
    if nombre_variable2 == "Monóxido":
        return {
            'data': [go.Scatter(x=filt_data_combined_mm["created_at"],
                                y=filt_data_combined_mm[nombre_variable2],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable2}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label2))
                } 
    
    if nombre_variable2 == "Metano":
        return {
            'data': [go.Scatter(x=filt_data_combined_mm["created_at"],
                                y=filt_data_combined_mm[nombre_variable2],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable2}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label2))
                }
    
      
    else:
        return {
            'data': [go.Scatter(x=data_combined_mm["created_at"],
                                y=data_combined_mm[nombre_variable2],
                                line = dict(color='green', width=2),
                                mode="lines+markers",
                                )],
            'layout': go.Layout(title = f"Medición de {nombre_variable2}",
                                xaxis = dict(title = "Fecha"),
                                yaxis = dict(title = y_axis_label2))
        }
                
@app.callback(
    Output('grafico_var4', 'figure'),
    [Input('selec_variable2', 'value')])

def update_graph22(nombre_variable2):
    df = data_combined_mm
    fig = px.histogram(df, x=nombre_variable2, marginal="box", title=f"Distribución de Datos de {nombre_variable2}", hover_data=df.columns)
    data2 = fig.to_dict()['data']
    layout2 = fig.to_dict()['layout']
    layout2['title']['x'] = 0.5
    layout2['yaxis']['title'] = f"Conteo de datos de {nombre_variable2}"
    layout2['xaxis']['title'] = f"{nombre_variable2}"
    for trace in data2:
        trace['marker']['color'] = 'blue'
    return {'data': data2, 'layout': layout2}

if __name__ == '__main__':
    app.run_server(port=1507)

