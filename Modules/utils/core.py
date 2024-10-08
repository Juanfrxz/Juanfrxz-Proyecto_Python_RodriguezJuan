import os
import json

MY_DATABASE = None

def NewFile(param):
    with open(MY_DATABASE, "w") as wf:
        json.dump(param[0], wf, indent=4)

def ReadFile():
    with open(MY_DATABASE, "r") as rf:
        return json.load(rf)

def checkFile(param):
    data = list(param)
    if os.path.isfile(MY_DATABASE):
        if len(param):
            data[0].update(ReadFile())
    else:
        if len(param):
            NewFile(data[0])

def signUp_User(mainDictionary):
    data = ReadFile()
    gamers = data.get('gamers', {})
    nombres = input('Por favor ingrese su nombre completo : ')
    nicknames = input('Por favor ingrese su nickname : ')
    if nicknames in gamers:
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
        gamers[nicknames] = dato
        dato["gamers"] = gamers
        mainDictionary.update({len(mainDictionary)+1:dato})
        NewFile(dato)
        print(f'Jugador {nicknames} registrado con exito.')

def login(mainDictionary):
    nombreUsuario= str(input("Por favor, ingrese su nombre completo."))
    nicknameUsuario= str(input("Por favor, ingrese su nickname para validarlo."))
    userValidated = False
    
    for k,v in mainDictionary.items():
        if v.get("gamers")== nombreUsuario:
            if v.get("nickname")== nicknameUsuario:
                userValidated= nicknameUsuario

    return nicknameUsuario