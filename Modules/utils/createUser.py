from Modules.utils.util import LeerFile, NewFile

def loginUser(nombre, nickname):
    data = LeerFile()
    gamers = data.get('gamers', {})
    if nickname in gamers:
        print("El nickname ya esta ocupado, utiliza otro por favor😊")
    else:
        dato = {
            "gamers" : nombre,
            "nickname" : nickname,
            "pointsTotal" : 0,
            "gameWins" : 0,
            "gameJugados" : 0,
            "gameLoss" : 0,
        }
        gamers[nickname] = dato
        dato["gamers"] = gamers
        NewFile(dato)
        print(f'Jugador {nickname} registrado con exito')

