import requests

token = "wIzTUSDJ65bAcZdyV1zljQWKfNOyhD3P"

base_url = "http://www.mapquestapi.com/directions/v2/route"

santiago_coords = "-33.4489,-70.6693"
ovalle_coords = "-30.5986,-71.2006"

params = {
    "key": token,
    "from": santiago_coords,
    "to": ovalle_coords,
    "unit": "k"  
}

response = requests.get(base_url, params=params)
data = response.json()

distance = data["route"]["distance"]

print(f"La distancia entre Santiago y Ovalle es de {distance} kilómetros.")
