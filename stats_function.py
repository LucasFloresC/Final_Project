# import libraries
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from pandas import json_normalize
import requests


def stats():
    # Scraping all pokedex index in order to can do the merge later, also some more missing stats

    PATH=("C:\Program Files (x86)\chromedriver.exe")
    driver=webdriver.Chrome(PATH)
    driver.get("https://pokemondb.net/pokedex/all")
    time.sleep(2)
    p = []
    name = []
    hp = []
    attack = []
    defense= []
    spa =[]
    spd =[]
    speed = []
    bt = []
    # Looping to get pokedex number + stats
    for i in range(1,1216):
        #index
        dex = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[1]/span').text
        p.append(dex)
        print(dex)
        #name
        nombre = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[2]/a').text
        name.append(nombre)
        print(nombre)
        #Base total of the pokemon
        total = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[4]').text
        bt.append(total)
        print(total)
        #Health points
        vida = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[5]').text
        hp.append(vida)
        print(vida)
        #Attack
        ataque = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[6]').text
        attack.append(ataque)
        print(ataque)
        #Defense
        defensa = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[7]').text
        defense.append(defensa)
        print(defensa)
        #Special Attack
        spat = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[8]').text
        spa.append(spat)
        print(spat)
        #Special Defense        
        sped = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[9]').text
        spd.append(sped)
        print(sped)
        #Speed    
        velocidad = driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[10]').text
        speed.append(velocidad)
        print(velocidad)
            
    driver.close()

    return p,name,hp,attack,defense,spa,spd,speed,bt