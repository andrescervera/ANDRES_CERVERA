#reto intermedio 1 : discos de música
import datetime

discoPop = {
  "Nombre": 'Viva el Pop',
  "Artista": 'Taylor Swift',
  "Anyo": 2012,
  "Precio": 42,
  "Genero": 'Pop'
}

discoElectro = {
  "Nombre": 'Viva el Electro',
  "Artista": 'Martin Garrix',
  "Anyo": 2015,
  "Precio": 56,
  "Genero": 'Electro'
}

discoRegueaton = {
  "Nombre": 'Viva el Regueaton',
  "Artista": 'Bad Bunny',
  "Anyo": 2019,
  "Precio": 67,
  "Genero": 'Regueaton'
}

importeTotal = 0
dineroAhorrado = 0
fechaCompra  = datetime.datetime.now()

print(f'Los discos disponibles actualmente son:\n' 
      f'Disco 1: {discoPop}\n' 
      f'Disco 2: {discoElectro}\n' 
      f'Disco 3: {discoRegueaton}\n' 
      f'Escribe el número del disco que desees comprar o 0 si deseas finalizar la compra')

def finalizarCompra ():  
  print(f'¿Desea comprar otro disco?. Pulse 1 para confirmar, 0 para finalizar compra')
  numero2 = input('')
  numero2 = int(numero2) 
  if (numero2 == 0):
      print(f'Total de la compra:\n' 
            f'Importe total: {importeTotal}\n'
            f'Dinero Ahorrado: {dineroAhorrado}\n' 
            f'Fecha de compra: {fechaCompra}')
  else:
      print(f'Elige otro disco para comprar')
      compraDisco()
    
def compraDisco ():
  
    global importeTotal, dineroAhorrado
  
    numero = input('')
    numero = int(numero)
    
    if (numero == 1):
        importeTotal += discoPop["Precio"]
        finalizarCompra()
    
    elif (numero == 2): 
        importeTotal += discoElectro["Precio"] * 0.7
        dineroAhorrado += discoElectro["Precio"] * 0.3
        finalizarCompra()
    
    elif (numero == 3):  
        importeTotal = importeTotal + discoRegueaton["Precio"]
        finalizarCompra()
    
    elif (numero == 0):
        finalizarCompra()
        
    else:
        print(f'El disco solicitado no existe, escoge otro')
        compraDisco()

compraDisco()