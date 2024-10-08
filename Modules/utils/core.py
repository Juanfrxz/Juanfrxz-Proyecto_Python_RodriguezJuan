import json
import os


MY_DATABASE ="data/jugadores.json"

def ReadFile():
    try:
        with open(MY_DATABASE, "r") as rf:
            return json.load(rf)
    except FileNotFoundError:
        return {}
    
def WriteFile(data):
    print(data)
    with open(MY_DATABASE, "w") as wf:
        json.dump(data, wf, indent=4)
        
def signUp_User(diccionarioPrincipal):
    data = ReadFile()
    nombre_completo = input("Introduce el nombre completo del jugador: ")
    nickname = input("Introduce el nickname del jugador: ")
    if nickname in data:
        print("El nickname ya está registrado. Intenta con otro.")
        return None
    nuevo_jugador = {
        'nombre_completo': nombre_completo,
        'nickname': nickname,
        'partidas_jugadas': 0,
        'partidas_ganadas': 0,
        'partidas_perdidas': 0,
        'puntos_totales': 0
    }
    data['jugadores'].append(nuevo_jugador)
    #data['jugadores'][nickname] = nuevo_jugador
    WriteFile(data)
    print(f"Jugador {nickname} ha sido registrado con éxito.")
    return nickname

def login(diccionarioPrincipal):
    data = ReadFile()
    nickname = input("Introduce tu nickname: ")
    if nickname in data:
        print(f"Bienvenido {nickname}.")
        return nickname
    else:
        print("Nickname no encontrado.")
        return None

"""import os
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
"""    