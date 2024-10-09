import json

MY_DATABASE ="data/jugadores.json"

def ReadFile():
    try:
        with open(MY_DATABASE, "r") as rf:
            return json.load(rf)
    except FileNotFoundError:
        return {}
    
def WriteFile(data):
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
    data[nickname] = nuevo_jugador
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
    
def signUp_User2(diccionarioPrincipal):
    data = ReadFile()
    nombre_completo = input("Introduce el nombre completo del jugador2: ")
    nickname = input("Introduce el nickname del jugador2: ")
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
    data[nickname] = nuevo_jugador
    WriteFile(data)
    print(f"Jugador {nickname} ha sido registrado con éxito.")
    return nickname


