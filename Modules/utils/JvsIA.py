import random
import main as mn
import json
from Modules.utils import core as user
from Modules.utils import menus as mn

opciones = ['piedra', 'papel', 'tijera']
contador = {
    'rondasGanadasUser': 0,
    'rondasGanadasCompu': 0
}

MY_DATABASE = 'data/jugadores.json'

def WriteFile(data):
    with open(MY_DATABASE, "w") as wf:
        json.dump(data, wf, indent=4)

def ReadFile():
    try:
        with open(MY_DATABASE, 'r') as rf:
            return json.load(rf)
    except FileNotFoundError:
        return {}

def actualizar_estadisticas(jugador, ganada):
    data = ReadFile()
    if jugador in data:
        data[jugador]['partidas_jugadas'] += 1
        if ganada:
            data[jugador]['partidas_ganadas'] += 1
        else:
            data[jugador]['partidas_perdidas'] += 1
    else:
        data[jugador] = {
            'partidas_jugadas': 1,
            'partidas_ganadas': 1 if ganada else 0,
            'partidas_perdidas': 0 if ganada else 1
        }
    WriteFile(data)

def gamePermission(diccionarioPrincipal):
    gamer = user.signUp_User(diccionarioPrincipal)
    if isinstance(gamer, str):
        print(f"El jugador {gamer} ha sido registrado con éxito.")
    else:
        input('Error al registrar el jugador. Enter para regresar al menú principal.')
               
def startGame(diccionarioPrincipal):
    while True:
        jugador = user.login(diccionarioPrincipal)
        if isinstance(jugador, str):
            print(f"¡Bienvenido {jugador}! Empecemos a jugar.")
            jvsia(jugador)
            jugar_otra = input("¿Quieres jugar otra partida? (s/n): ").lower()
            if jugar_otra != 's':
                break
        else:
            input('El usuario no pudo ser validado. Enter para regresar al menú principal.')
            break

def jvsia(jugador):
    global contador
    victorias_consecutivas_usuario = 0
    victorias_consecutivas_computadora = 0
    escudo_usuario = False
    escudo_computadora = False
    contador['rondasGanadasUser'] = 0
    contador['rondasGanadasCompu'] = 0

    try: 
        while True:
            if contador['rondasGanadasUser'] < 3 and contador['rondasGanadasCompu'] < 3:
                usuario = input("Elige piedra, papel o tijera: ").lower()
                computadora = random.choice(opciones)
                print(f"Computadora eligió: {computadora}")

                if usuario not in opciones:
                    print("Opción no válida, por favor elige entre piedra, papel o tijera.")
                    continue

                elif usuario == computadora:
                    print("¡Es un empate!")

                elif (usuario == 'piedra' and computadora == 'tijera') or \
                     (usuario == 'tijera' and computadora == 'papel') or \
                     (usuario == 'papel' and computadora == 'piedra'):
                    print("¡Ganaste!")
                    victorias_consecutivas_usuario += 1
                    victorias_consecutivas_computadora = 0  
                    if victorias_consecutivas_usuario == 2:
                        escudo_usuario = True
                        print("¡Tienes un escudo!")
                    if escudo_computadora:
                        print("¡Escudo de la computadora bloqueó tu victoria!")
                        escudo_computadora = False  
                    else:
                        contador['rondasGanadasUser'] += 1
                else:
                    print("¡Perdiste!")
                    victorias_consecutivas_computadora += 1
                    victorias_consecutivas_usuario = 0  
                    if victorias_consecutivas_computadora == 2:
                        escudo_computadora = True
                        print("¡La computadora tiene un escudo!")
                    if escudo_usuario:
                        print("¡Tu escudo te salvó de perder la ronda!")
                        escudo_usuario = False  
                    else:
                        contador['rondasGanadasCompu'] += 1
                print(f"Usuario: {contador['rondasGanadasUser']} | Computadora: {contador['rondasGanadasCompu']}")      
            else:
                if contador['rondasGanadasUser'] == 3:
                    print(f"¡{jugador} ha ganado la partida!")
                    actualizar_estadisticas(jugador, True)
                else:
                    print("¡La computadora ha ganado la partida!")
                    actualizar_estadisticas(jugador, False)
                break
    except ValueError:
        print("Ocurrió un error con la entrada del usuario.")
