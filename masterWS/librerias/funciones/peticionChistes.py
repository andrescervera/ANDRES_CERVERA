import requests
from requests.models import Response


URL: str = "https://api.chucknorris.io/jokes/random"

def num_chistes ():
        print(f'¿Cuántos chistes quieres imprimir?')
        numero = input('')
        numero = int(numero)
        if numero <= 5:
            for i in range(1, numero + 1):
                respuesta: requests.Response = requests.get(url = URL)
                estado: int = respuesta.status_code
                datos = respuesta.json()
                if estado == 200:
                    frase_chuck: str = datos['value']
                    print(f'El chiste {i} es: {frase_chuck}')
        else:
            print(f"Máximo 5!!! Solicita otro número")
            num_chistes()

num_chistes()


"""print(f'¿Cuántos chistes quieres imprimir?')
numero = input('')
numero = int(numero)
if numero <= 5:
    num_chistes(numero)
else:
    print(f"Máximo 5!!! Solicita otro número")"""