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

def types():
    # Scrapeamos 9 generacion y sus tipos

    PATH=("C:\Program Files (x86)\chromedriver.exe")
    driver=webdriver.Chrome(PATH)
    driver.get("https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number#List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number")
    time.sleep(5)
    new_gen = []
    tipo1 = []
    tipo2 = []

    # Looping to get names
    for i in range(2,136):
        try:

            name = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[10]/tbody/tr[{i}]/td[3]/a').text
            new_gen.append(name)
            print(name)
            # Try to save first type
            try:
                t = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[10]/tbody/tr[{i}]/td[4]').text
                tipo1.append(t)
                print(tipo1)
            
            except:
                tipo1.append(None)

        # Try to get second type
            try:
                
                t2 = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[10]/tbody/tr[{i}]/td[5]').text
                tipo2.append(t2)
                print(tipo2)
            
            except:
                tipo2.append(None)
        except:
            driver.close()
    driver.close()
    # Convertimos a DataFrame la info
    p = {"Name":new_gen,"Type_1":tipo1,"Type_2":tipo2}
    scraped = pd.DataFrame(p)
    scraped.tail()

    return new_gen,tipo1,tipo2