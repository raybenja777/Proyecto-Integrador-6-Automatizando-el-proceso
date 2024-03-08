import sys
import requests
import pandas as pd


def descargar_y_procesar(url):
    # Descargar el archivo CSV desde la URL proporcionada
    try:
        response = requests.get(url)
        # Verificar si la descarga fue exitosa
        if response.status_code == 200:
           with open ('datos_descargados.csv', 'w') as file:
               file.write(response.text)
           print("Se ha descargado el archivo")
           # Procesar el archivo CSV descargado
           df = pd.read_csv('datos_descargados.csv')
           preprocesar_datos(df) # Llamar a la función para preprocesar los datos
        else:
            print("No se ha podido descargar el archivo: ", response.status_code)
    except Exception as e:
        print("Error: ", e)

def preprocesar_datos(df):
    # Realizar el preprocesamiento de datos, como categorización, limpieza, etc.
    df.to_csv('datos_preprocesados.csv', index=False)  # Guardar el DataFrame preprocesado en un archivo CSV
    print(df)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Por favor, proporcione la URL del archivo CSV como argumento.")
    else:
        url = sys.argv[1] # Obtener la URL del archivo CSV de los argumentos de la línea de comandos
        descargar_y_procesar(url) # Llamar a la función principal para descargar y procesar los datos