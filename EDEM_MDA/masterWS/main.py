from librerias.funciones.basicas import saludar
from librerias.funciones.peticiones import generar_usuario
import requests
from requests.models import Response

from librerias.funciones.peticiones import num_chistes

URL: str = "https://api.chucknorris.io/jokes/random"

#Realizamos peticion y obtenemos respuesta JSON
respuesta: Response = requests.get(url = URL)

#Comprobamos estado HTTP
estado: int = respuesta.status_code

#Obtenemos datos de la respuesta JSON
datos = respuesta.json()

if estado == 200:
    #obtenemos chiste de la respuesta accediendo a la clave 'value'
    frase_chuck: str = datos['value']
    print(f'El chiste: {frase_chuck}')