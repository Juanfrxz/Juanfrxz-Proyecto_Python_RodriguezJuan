import os
import json

MY_DATABASE = 'data/usuarios.json'

def LeerFile():
    if os.path.isfile(MY_DATABASE):
        with open (MY_DATABASE) as al:
            return json.load(al)
    else:
        return {}
    
def NewFile(data):
    with open(MY_DATABASE, "w") as md:
        json.dump(data,md,indent=4)
        
    
def checkFile(initialDta):
    if not os.path.isfile(MY_DATABASE):
        NewFile(initialDta)

def login_User(nombre, nickname):
    data = LeerFile()
    gamers = data.get('gamers', {})
    nombres = input('Por favor ingrese su nombre completo : ')
    nicknames = input('Por favor ingrese su nickname : ')
    if nickname in gamers:
        print("El nickname ya esta ocupado, utiliza otro por favor😊")
    else:
        dato = {
            "gamers" : nombres,
            "nickname" : nicknames,
            "pointsTotal" : 0,
            "gameWins" : 0,
            "gameJugados" : 0,
            "gameLoss" : 0,
        }
        checkFile(dato)
        gamers[nickname] = dato
        dato["gamers"] = gamers
        NewFile(dato)
        print(f'Jugador {nickname} registrado con exito.')

