def evolutions():
# Scraping evoluions from API 
  # import libraries
  import warnings
  warnings.filterwarnings('ignore')
  import pandas as pd
  import numpy as np
  import seaborn as sns
  from pandas import json_normalize
  import requests


  api_poke = []
  poke_evol = []
  conteo = 1
  attempts = 0

  # while true because sometimes we get 400 error 
  while True:
      
      url = f"https://pokeapi.co/api/v2/evolution-chain/{conteo}"
      response = requests.get(url)
      if response.status_code != 200:
        attempts +=1
      else:
        #Saving pokemon name
          api_poke.append(response.json()["chain"]['species']["name"])

        # Save the pokemon evolution name if it has, if don't it will append the following message
          try:
            poke_evol.append(response.json()["chain"]["evolves_to"][0]["species"]["name"])
            print("Pokemon:", response.json()["chain"]['species']["name"])
          except:
              poke_evol.append("No hay")

      conteo +=1
            
      if attempts >= 15:
            
        break

  return api_poke,poke_evol 