import requests
from peticionChistes import URL

def generar_usuario(url: str):
    respuesta = requests.get(url)
    if(respuesta.status_code == 200):
        print("Correcto")
    else:
        print("Algo ha ido mal, Error: {respuesta.status_code}")
        

def num_chistes (numero: int):
      for i in range(1, numero + 1):
          respuesta: requests.Response = requests.get(url = URL)
          estado: int = respuesta.status_code
          datos = respuesta.json()
          if estado == 200:
        #obtenemos chiste de la respuesta accediendo a la clave 'value'
            frase_chuck: str = datos['value']
            print(f'El chiste {i} es: {frase_chuck}')