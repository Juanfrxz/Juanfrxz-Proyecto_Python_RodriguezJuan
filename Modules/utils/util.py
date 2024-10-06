import os
import json

def load_json(filename, default_value):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return default_value

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
def validateData(message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que usted ingreso no esta permitida.......')
            validateData()
        elif (accion== 'N'): 
            flagFunction = True
        elif  (accion == 'S'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateData(message)
def validateResponse(message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que usted ingreso no esta permitida.......')
            validateData()
        elif (accion== 'S'): 
            flagFunction = True
        elif  (accion == 'N'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateResponse(message)
