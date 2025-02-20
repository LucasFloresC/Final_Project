# import de todas las librerias que usaremos
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

def caracteristicas():

    # Scrapeamos las habilidades y otros stats de la generacion 9

    PATH=("C:\Program Files (x86)\chromedriver.exe")
    driver=webdriver.Chrome(PATH)
    driver.get("https://pokemondb.net/pokedex/all")
    time.sleep(2)
    numero = []
    nombre = []
    abilities = []
    altura = []
    peso = []
    egg_step = []
    capture = []
    # Lo incializamos con este valor porque ahi empieza lo que nos interesa
    contador = 899
    # Generamos otro contador para ir haciendo append en la lista de listas para las habilidades
    counter = 0
    # Looping to get pokedex number + stats
    for i in range(1070,1216):

        
        driver.find_element(By.XPATH, f'//*[@id="pokedex"]/tbody/tr[{i}]/td[2]/a').click()
        time.sleep(2)
        n = driver.find_element(By.XPATH, f'//*[@id="main"]/h1').text
        nombre.append(n)
        print(n)
        numero.append(i)
        abilities.append(i)
        print(i)

        # SI existe un pokemon con el mismo numero entonces scrapeamos primero el inicial y luego el siguiente:
        try:       
            # SI solo tiene una habilidad
            try:
                # Intentamos coger las habilidades segun el numero que tengan
                try:
                    for z in range(1,3):    
                        ab = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/span[{z}]/a').text
                        abilities.append(ab)
                        print(ab)
                    
                                    
                    ab2 = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/small/a').text
                    abilities.append(ab2)
                    print(ab2)  

                except:

                    ab = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/span/a').text
                    abilities.append(ab)
                    print(ab)
                    ab2 = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/small/a').text
                    abilities.append(ab2)
                    print(ab2)
            except:

                ab = driver.find_element(By.XPATH, f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/span/a').text
                abilities.append(ab)
                print(ab)
                
                
            alt = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[4]/td').text
            altura.append(alt)
            print(alt)

            ps = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[5]/td').text
            peso.append(ps)
            print(ps)

            try:    
                eg = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[3]/div/div[2]/table/tbody/tr[3]/td/small').text
                egg_step.append(eg)
                print(eg)
            except:

                eg = driver.find_element(By.XPATH, f'//*[@id="tab-basic-{contador}"]/div[1]/div[3]/div/div[2]/table/tbody/tr[3]/td').text

            cap = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[3]/div/div[1]/table/tbody/tr[2]/td').text
            capture.append(cap)
            print(cap)
            
            contador+=1
        # SI existe un pokemon con el mismo numero entonces scrapeamos primero el inicial y luego el siguiente:
        except:
            contador-=1
            try:
            # Intentamos coger las habilidades segun el numero que tengan
                try:
                    for z in range(1,3):    
                        ab = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/span[{z}]/a').text
                        abilities.append(ab)
                        print(ab)
                        
                        
                    ab2 = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/small/a').text
                    abilities.append(ab2)
                    print(ab2)  

                except:

                    ab = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/span/a').text
                    abilities.append(ab)
                    print(ab)
                    ab2 = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/small/a').text
                    abilities.append(ab2)
                    print(ab2)
            except:

                ab = driver.find_element(By.XPATH, f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[6]/td/span/a').text
                abilities.append(ab)
                print(ab)

            alt = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[4]/td').text
            altura.append(alt)
            print(alt)

            ps = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[2]/table/tbody/tr[5]/td').text
            peso.append(ps)
            print(ps)

            try:    
                eg = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[3]/div/div[2]/table/tbody/tr[3]/td/small').text
                egg_step.append(eg)
                print(eg)
            except:

                eg = driver.find_element(By.XPATH, f'//*[@id="tab-basic-{contador}"]/div[1]/div[3]/div/div[2]/table/tbody/tr[3]/td').text

            cap = driver.find_element(By.XPATH,f'//*[@id="tab-basic-{contador}"]/div[1]/div[3]/div/div[1]/table/tbody/tr[2]/td').text
            capture.append(cap)
            print(cap)

            
            contador+=1
    
            
        driver.back()
        time.sleep(1)

    driver.close()
    return numero,nombre,abilities,altura,peso,egg_step,capture