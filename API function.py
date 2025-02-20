# import de todas las librerias que usaremos
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import seaborn as sns
from pandas import json_normalize
import requests


def evolutions():
# Scrap de evoluciones de la API 

# Sacamos info adicional de la API de Pokemon
api_poke = []
poke_evol = []
conteo = 1
attempts = 0

# Usamos un while true para que hago mas intentos ya que hay casos en los que el status code era 400 y entonces paraba
while True:
    
    url = f"https://pokeapi.co/api/v2/evolution-chain/{conteo}"
    response = requests.get(url)
    if response.status_code != 200:
      attempts +=1
    else:
      # Guardamos el nombre del pokemon
        api_poke.append(response.json()["chain"]['species']["name"])

      # Guardaremos la evolucion de ese pokemon si tiene, si no, pondra que no tiene
        try:
          poke_evol.append(response.json()["chain"]["evolves_to"][0]["species"]["name"])
          print("Pokemon:", response.json()["chain"]['species']["name"])
        except:
            poke_evol.append("No hay")

    conteo +=1
          
    if attempts >= 15:
          
      break

return api_poke,poke_evol 