import requests

token = "wIzTUSDJ65bAcZdyV1zljQWKfNOyhD3P"

base_url = "http://www.mapquestapi.com/directions/v2/route"

def calcular_duracion(origen, destino):
    params = {
        "key": token,
        "from": origen,
        "to": destino,
        "unit": "k"  
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    duracion = data["route"]["formattedTime"]
    distancia = data["route"]["distance"]

    narrativa = data["route"]["legs"][0]["maneuvers"]

    horas, minutos, segundos = map(int, duracion.split(':'))

    print(f"Duración del viaje: {horas:02d}:{minutos:02d}:{segundos:02d}")
    print(f"Distancia: {distancia:.2f} kilómetros")

    print("Narrativa del viaje:")
    for i, paso in enumerate(narrativa, start=1):
        print(f"{i}. {paso['narrative']}")

while True:
    
    origen = input("Ciudad de Origen (q para salir): ")
    if origen.lower() == "q":
        break

    destino = input("Ciudad de Destino (q para salir): ")
    if destino.lower() == "q":
        break

    calcular_duracion(origen, destino)

    print()  

print("¡Hasta luego!")
