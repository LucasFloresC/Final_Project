# import libraries 
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import seaborn as sns
import random
import os
pd.set_option('display.max_columns', None)
import math
from pandas import json_normalize
import matplotlib.pyplot as plt
import time
import streamlit as st

# Load dataset and delete index
pokemon_data = pd.read_csv('dataset/pokemon_final.csv')
pokemon_data.drop(columns='Unnamed: 0',inplace=True)
# Modify fight to have it equal to the column against
pokemon_data['Base_type'].replace('Fighting','Fight',inplace=True)
pokemon_data['Secondary_type'].replace('Fighting','Fight',inplace=True)


# Creating the class pokemon
class my_pokemon():

    #Defining attributes
    def __init__(self, pokedex_number,name,evolution,base_type,secondary_type,legendary,attack,defense,hp,sp_attack,sp_defense,speed,experience_growth):
        
        #Variable Attributes
        self.defense = defense
        self.hp = hp
        self.alive = True
        self.experience_growth = experience_growth
        self.armor = True
        
        #Static Attributes
        self.pokedex_number = pokedex_number
        self.name = name
        self.base_type = base_type
        self.secondary_type = secondary_type
        self.legendary = legendary
        self.attack = attack
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.evolution = evolution

    # Creating a dictionary with the against types
    def types_relation(self,row):

        llaves = [i.split('_')[1] for i in row.keys() if 'Against' in i]

        self.against_dict = {llave.capitalize(): row[f"Against_{llave}"] for llave in llaves}
       
        

    #Defining status of the pokemons
    def status(self):

        if self.secondary_type == '-':

            print(f'You selected: {self.name}! from {self.base_type} type.')
            print('')
        else:
            print(f'You selected: {self.name}! from {self.base_type} primary type and {self.secondary_type} secondary type.')
            print('')

        print('Check your stats before the battle starts!')
        print('')
        print(f'HP (Health Points): {self.hp}')
        print(f'Attack: {self.attack}')
        print(f'Defense: {self.defense}')
        print(f'Speed: {self.speed}')
        print(f'Special Attack: {self.sp_attack}')
        print(f'Special Defense: {self.sp_defense}')
        print(f'Alive: {self.alive}')
        print('') 
        
   #Defining if the pokemon is hitting or missing
    def hitting(self,missing_chance = 0.4):
        tirada = random.random()
        if tirada > missing_chance:

            print(f'{self.name} hitted!')
            print('')

            return [self.attack,self.base_type]
        else:
            print(f'{self.name} missed!')
            print('')
            return []
    #Defining hoy the damage is done during the battle          
    def receiving_hit(self,lista):
        while len(lista) != 0:
            #Damage is done by the attack per the multiplier of the type defined in the against columns. 
            # First we calculate the effectivity and then we calculate the real damage done
            efectividad = self.against_dict[lista[1]]
            damage =  efectividad*lista[0]
            damage = int(damage)       
            #Define an armor to add complexity to the battle
            if self.armor == False:
                
                if damage >= self.hp or self.hp <= 0:

                    self.alive = False
                    print(f'Critical hit, {self.name} took {damage} damage and died!☠️',flush=True)
                    break 
                
                else:
                    
                    self.hp -= damage
                    print(f'{self.name} took {damage} damage and remaining HP is: {self.hp}',flush=True)
                    break
                
            else:
                
                if damage <= self.defense:

                    self.defense -= damage
                    print(f"{self.name} didn't took damage, remaining HP is: {self.hp}",flush=True)
                    print(f'{self.name} Defense has drooped to: {self.defense}',flush=True)
                    print('')
                    break
                else:
                    self.armor=False
                    print(f'The armor of {self.name} has fallen! {self.name} has no defense!',flush=True)
                    print('')    
                    break

                       
#Creating a list with all pokemon objects
pokemon_list = []

for index, row in pokemon_data.iterrows():
    pokemon_obj = my_pokemon(pokedex_number=row["Pokedex_number"], 
                             name=row["Name"], 
                             attack=row["Attack"], 
                             defense=row["Defense"], 
                             experience_growth=row["Experience_growth"], 
                             hp=row["Hp"], 
                             sp_attack=row["Sp_attack"], 
                             sp_defense=row["Sp_defense"], 
                             speed=row["Speed"], 
                             base_type=row["Base_type"], 
                             secondary_type=row["Secondary_type"], 
                             legendary=row["Legendary"],
                             evolution=row['Evolution'])
    pokemon_obj.types_relation(row)
    pokemon_list.append(pokemon_obj)

# Define who is starting
def starter(poke_1,poke_2):

    if poke_1.speed > poke_2.speed:
        print(f'{poke_1.name} was faster!')
        return poke_1, poke_2
    
    elif poke_1.speed <= poke_2.speed:
        print(f'{poke_2.name} was faster!')
        return poke_2, poke_1

        
# Simulate the fight between each pokemon, will always be 1 vs 1
def fight_simulation(pokemon_1,pokemon_2):
    ronda = 1

    while True:

        if pokemon_1.alive == False or pokemon_2.alive == False:
            if pokemon_1.alive:
                print(f'{pokemon_1.name} wins!',flush=True)
            else:
                print(f'{pokemon_2.name} wins!',flush=True)

            break

        else:
                print(f'Round {ronda}!')
                print('')
                attacker, defender = starter(pokemon_1,pokemon_2)
                primero = attacker.hitting()
                if len(primero) != 0:
                    defender.receiving_hit(primero)

                    if defender.alive:
                        segundo = defender.hitting()
                        
                        if len(segundo) != 0:
                            attacker.receiving_hit(segundo)

                    ronda+=1
                else:
                    segundo = defender.hitting()
                    if len(segundo) != 0:
                        attacker.receiving_hit(segundo)
                    
                    ronda+=1
# Choosing our teams. The enemy team will be a random choice between all pokemons except those we tried
def teams():

    mi_equipo = [] 
    tu_equipo = []

    while len(mi_equipo) < 5:

        seleccion = ((input('Select one Pokemon: ')).lower()).capitalize()
        for i in pokemon_list:
            if i.name == seleccion:
                mi_equipo.append(i)
                print(f'You selected {i.name}',flush=True)

    random.shuffle(pokemon_list)
    for i in pokemon_list: 
        if i not in mi_equipo and len(tu_equipo)<5:
            tu_equipo.append(i)

    return mi_equipo, tu_equipo

# Define the trainers function to add more options to the battle simulator
def trainers():

    a = ['Pikachu','Pidgeot','Charizard','Blastoise','Gengar']
    ash_team = []
    r = ['Arbok','Meowth','Koffing','Wobbuffet','Cacnea']
    team_rocket = []
    m = ['Goldeen','Staryu','Starmie','Horsea','Psyduck']
    misty_team = []

    for i in pokemon_list:
        if i.name in a:
            ash_team.append(i)
        elif i.name in r:
            team_rocket.append(i)
        elif i.name in m:
            misty_team.append(i)

    return ash_team, team_rocket, misty_team

# Function that simulate the battle
def multi_battle():

    combatientes = []

    print('Welcome to the Pokemon Battle Simulator!',flush=True)
    print('Choose your Pokemon team!',flush=True)
    team_1, team_2 = teams()
    adversary = input('Choose your adversary: (1) Random Pokemon Trainer, (2) Random Battle, (3) Choose Enemy Team')

    #Convert the string to int 
    try:
        adversary = int(adversary)

    except:

        adversary = input('Please choose your adversary: (1) Random Pokemon Trainer, (2) Random Battle, (3) Choose Enemy Team...only integers please 😎')
    

    # Choosing against trainer
    if adversary == 1:
        #Load the trainers
        ash, rocket, misty = trainers()
        entrenador = random.choice([ash,rocket,misty])

        if entrenador == ash:
            print(f'You are going to fight Ash!',flush=True) 
        elif entrenador == rocket:
            print('You are going to fight Team Rocket!',flush=True)
        else:
            print('You are going to fight Misty!')  

        #Adding one of our pokemons to the list that will be passed to the fight simulation
        if len(combatientes) < 2:
                #Choosing our firt pokemon to fight
                combatiente_1 = ((input('Elige a tu primer pokemon!')).lower()).capitalize()

                while True:

                    for i in team_1:
                        # if  the pokemon is alive and it is in our list
                        if (i.name == combatiente_1) and (i.alive == True):

                            combatientes.append(i)
                            
                            break
                    
                    if len(combatientes) > 0:
                        break
                    #Check if the pokemon is not found
                    input(f'Pokemon no encontrado, elige uno de tu equipo: {[poke.name for poke in team_1 if poke.alive == True]}')

        while (sum([poke.alive for poke in team_1]) > 0) and (sum([poke.alive for poke in entrenador]) > 0):  
            
            if len(combatientes) < 2:
                # Choosing random alive pokemon from the enemy list
                combatiente_2 = random.choice([poke for poke in entrenador if poke.alive == True ])    
                combatientes.append(combatiente_2)
                
            #Simulate the fight
            fight_simulation(combatientes[0],combatientes[1])

            # Where is combatiente 1? Get index. If it's dead we delete from the combatientes list in order to add a new pokemon form our team
            index_in_mylist = [i.name for i in team_1].index(combatiente_1)
            team_1_position = team_1[index_in_mylist]
            combatiente_1_index = combatientes.index(team_1_position)    
            
            if combatientes[combatiente_1_index].alive == False:

                del combatientes[combatiente_1_index]
                
                if sum([poke.alive for poke in team_1]) == 0:
                    break
                else:
                    
                    combatiente_1 = ((input('Elige a tu siguiente pokemon!')).lower()).capitalize()
                    while len(combatientes) < 2:

                        for i in team_1:

                            if i.name == combatiente_1 and i.alive == True:
                                
                                combatientes.append(i)
                                
                                break
                
            #Where is pokemon 2 located? Get index. If it's dead we delete from the combatientes list in order to add a new pokemon from enemy team
            second_index_pokemon = entrenador.index(combatiente_2)
            team_2_position = entrenador[second_index_pokemon]
            combatiente_2_index = combatientes.index(team_2_position)

            if combatientes[combatiente_2_index].alive == False:

                del combatientes[combatiente_2_index]
                
                if sum([poke.alive for poke in entrenador]) == 0:
                    break
                else:
                    combatiente_2 = random.choice([poke for poke in entrenador if poke.alive == True])

                while len(combatientes) < 2:
                    
                    combatientes.append(combatiente_2)
                    
                    break

        if sum([poke.alive for poke in team_1]) > 0:
            print('Our team wins the battle!🔥')
        else:
            print('Enemy teams wins the battle!😒')        
    # Battle against pc
    elif adversary == 2:
       
        # Adding one of our pokemons to the list that will be passed to the fight simulation
        if len(combatientes) < 2:
                #Choosing our first pokemon
                combatiente_1 = ((input('Elige a tu primer pokemon!')).lower()).capitalize()

                while True:

                    for i in team_1:
                        # if  the pokemon is alive and it is in our list
                        if (i.name == combatiente_1) and (i.alive == True):

                            combatientes.append(i)
                            
                            break
                   
                    if len(combatientes) > 0:
                        break
                    #Check if the pokemon is not found
                    input(f'Pokemon no encontrado, elige uno de tu equipo: {[poke.name for poke in team_1 if poke.alive == True]}')

        while (sum([poke.alive for poke in team_1]) > 0) and (sum([poke.alive for poke in team_2]) > 0):  
            
            if len(combatientes) < 2:
                # Choosing random alive pokemon from the enemy list
                combatiente_2 = random.choice([poke for poke in team_2 if poke.alive == True ])    
                combatientes.append(combatiente_2)
                
            #Simulate the fight
            fight_simulation(combatientes[0],combatientes[1])

            # Where is combatiente 1? Get index. If it's dead we delete from the combatientes list in order to add a new pokemon form our team
            index_in_mylist = [i.name for i in team_1].index(combatiente_1)
            team_1_position = team_1[index_in_mylist]
            combatiente_1_index = combatientes.index(team_1_position)    
            
            if combatientes[combatiente_1_index].alive == False:
 
                del combatientes[combatiente_1_index]
                
                if sum([poke.alive for poke in team_1]) == 0:
                    break
                else:
                    
                    combatiente_1 = ((input('Elige a tu siguiente pokemon!')).lower()).capitalize()
                    while len(combatientes) < 2:

                        for i in team_1:

                            if i.name == combatiente_1 and i.alive == True:
                                
                                combatientes.append(i)
                                
                                break
                
            #Where is pokemon 2 located? Get index. If it's dead we delete from the combatientes list in order to add a new pokemon from enemy team
            second_index_pokemon = team_2.index(combatiente_2)
            team_2_position = team_2[second_index_pokemon]
            combatiente_2_index = combatientes.index(team_2_position)
        
            if combatientes[combatiente_2_index].alive == False:

                del combatientes[combatiente_2_index]
                
                if sum([poke.alive for poke in team_2]) == 0:
                    break
                else:
                    combatiente_2 = random.choice([poke for poke in team_2 if poke.alive == True])

                while len(combatientes) < 2:
                    
                    combatientes.append(combatiente_2)
                    
                    break 

        if sum([poke.alive for poke in team_1]) > 0:
            print('Our team wins the battle!🔥')
        else:
            print('Enemy teams wins the battle!😒')

    # Choose all pokemons for the battle                    
    elif adversary == 3:

        enemy_team = []
        #Choosing enemy's team
        while len(enemy_team) < 5:

            enemy_selection = ((input('Choose enemy pokemon:')).lower()).capitalize()

            for z in pokemon_list:
                if z.name == enemy_selection:
                    enemy_team.append(z)
                    print(f'Enemy selected {z.name}!')

        if len(combatientes) < 2:
                
                combatiente_1 = ((input('Elige a tu primer pokemon!')).lower()).capitalize()

                while True:

                    for i in team_1:
                        
                        if (i.name == combatiente_1) and (i.alive == True):

                            combatientes.append(i)
                            
                            break
                    
                    if len(combatientes) > 0:
                        break
                    
                    input(f'Pokemon no encontrado, elige uno de tu equipo: {[poke.name for poke in team_1 if poke.alive == True]}')

        while (sum([poke.alive for poke in team_1]) > 0) and (sum([poke.alive for poke in enemy_team]) > 0):  
            
            if len(combatientes) < 2:
                
                combatiente_2 = random.choice([poke for poke in enemy_team if poke.alive == True ])    
                combatientes.append(combatiente_2)
                
            fight_simulation(combatientes[0],combatientes[1])

            # Where is combatiente 1? Get index. If it's dead we delete from the combatientes list in order to add a new pokemon form our team
            index_in_mylist = [i.name for i in team_1].index(combatiente_1)
            team_1_position = team_1[index_in_mylist]
            combatiente_1_index = combatientes.index(team_1_position)    
            
            if combatientes[combatiente_1_index].alive == False:
 
                del combatientes[combatiente_1_index]
                
                if sum([poke.alive for poke in team_1]) == 0:
                    break
                else:
                    
                    combatiente_1 = ((input('Elige a tu siguiente pokemon!')).lower()).capitalize()
                    while len(combatientes) < 2:

                        for i in team_1:

                            if i.name == combatiente_1 and i.alive == True:
                                
                                combatientes.append(i)
                                
                                break
                
            #Where is pokemon 2 located? Get index. If it's dead we delete from the combatientes list in order to add a new pokemon from enemy team
            second_index_pokemon = enemy_team.index(combatiente_2)
            team_2_position = enemy_team[second_index_pokemon]
            combatiente_2_index = combatientes.index(team_2_position)
        
            if combatientes[combatiente_2_index].alive == False:

                del combatientes[combatiente_2_index]
                
                if sum([poke.alive for poke in enemy_team]) == 0:
                    break
                else:
                    combatiente_2 = random.choice([poke for poke in enemy_team if poke.alive == True])

                while len(combatientes) < 2:
                    
                    combatientes.append(combatiente_2)
                    
                    break 


        if sum([poke.alive for poke in team_1]) > 0:
            print('Our team wins the battle!🔥')
        else:
            print('Enemy teams wins the battle!😒')
    
multi_battle()

        