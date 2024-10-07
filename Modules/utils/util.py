import os
import json

MY_DATABASE = 'data/usuarios.json'

def NewFile(data):
    with open(MY_DATABASE, "r+") as md:
        json.dump(data,md,indent=4)
        
def LeerFile():
    if os.path.isfile(MY_DATABASE):
        with open (MY_DATABASE) as al:
            return json.load(al)
    else:
        return {}
    
def checkFile(initialDta):
    if not os.path.isfile(MY_DATABASE):
        NewFile(initialDta)

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
