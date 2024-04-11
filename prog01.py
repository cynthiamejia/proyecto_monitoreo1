import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Función para cargar y acondicionar los datos
def cargar_y_limpiar(url, drop_cols, rename_cols):
    df = pd.read_csv(url)
    df.drop(columns=drop_cols, inplace=True)
    df.rename(columns=rename_cols, inplace=True)
    df['created_at'] = pd.to_datetime(df['created_at'])  
    return df

ch4co8_url = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-08offset=UTC-06:00&end=2024-02-12offset=UTC-06:00"
temphum8_url = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-08offset=UTC-06:00&end=2024-02-12offset=UTC-06:00"
ch4co8 = cargar_y_limpiar(ch4co8_url, ['entry_id', 'field1', 'field4', 'field5', 'field6'], {'field2': 'Metano', 'field3': 'Monoxido'})
temphum8 = cargar_y_limpiar(temphum8_url, ['entry_id', 'field4', 'field5', 'field6'], {'field1': 'Humedad', 'field2': 'Temperatura', 'field3': 'CO2'})

# Descripción de los datos.
print("La descripción detallada de las variables metano y monóxido es: \n\n", round(ch4co8.describe()))
print('\r \r')
print("La descripción detallada de las variables humedad, temperatura y CO2: \n\n", round(temphum8.describe()))

# Gráficas de Distribución de los datos. VERSIÓN 1. 
sns.set_style("whitegrid")

def plot_distribution(data, column, binwidth, color, title, xlabel):
    g = sns.displot(data=data, x=column, binwidth=binwidth, kde=True, color=color, height=3, aspect=2)
    g.set_axis_labels(xlabel, "Conteo de datos (mediciones tomadas)")
    g.figure.suptitle(title, y=1.03)
    plt.legend(['Densidad de datos'])
    plt.show()
    g.savefig(f"{column}_distribucion.png", dpi=300) #En caso de desear guardar las imagenes.

plot_distribution(ch4co8, "Metano", 100, 'skyblue', 'Distribución de datos de Metano', "Metano (ppm)")
plot_distribution(ch4co8, "Monoxido", 2.5, 'seagreen', 'Distribución de datos de Monóxido', "Monóxido (ppm)")
plot_distribution(temphum8, "Humedad", 5, 'royalblue', 'Distribución de datos de Humedad', "Humedad (%)")
plot_distribution(temphum8, "Temperatura", 5, 'coral', 'Distribución de datos de Temperatura', "Temperatura (°C)")
plot_distribution(temphum8, "CO2", 100, 'limegreen', 'Distribución de datos de CO2', "CO2 (ppm)")