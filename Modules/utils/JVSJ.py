import main
import json
import main as mn
from Modules.utils import core as user

opciones = ['piedra', 'papel', 'tijera']
contador = {
    'rondasGanadasUser1': 0,
    'rondasGanadasUser2': 0
}

jugador=True
escudo_usuario1 = False
escudo_usuario2 = False
victorias_consecutivas_usuario1 = 0
victorias_consecutivas_usuario2 = 0

MY_DATABASE = 'data/jugadores.json'

def WriteFile(data):
    with open(MY_DATABASE, "w") as wf:
        json.dump(data, wf, indent=4)

def ReadFile():
    with open(MY_DATABASE, 'r') as rf:
        return json.load(rf)

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
        input('Error al registrar el jugador. Enter para regresar al menú.')
        mn.men()
        
def gamePermission2(diccionarioPrincipal):
    gamer2 = user.signUp_User2(diccionarioPrincipal)
    if isinstance(gamer2, str):
        print(f"El jugador {gamer2} ha sido registrado con éxito.")
    else:
        input('Error al registrar el jugador. Enter para regresar al menú principal.')
        main.menuPrincipal()
        
def startGame(diccionarioPrincipal):
    while True:
        print("Inicio de sesión para el Jugador 1")
        jugador1 = user.login(diccionarioPrincipal)
        if not isinstance(jugador1, str):
            input('El jugador 1 no pudo ser validado. Enter para regresar al menú principal.')
            return

        print("Inicio de sesión para el Jugador 2")
        jugador2 = user.login(diccionarioPrincipal)
        if not isinstance(jugador2, str):
            input('El jugador 2 no pudo ser validado. Enter para regresar al menú principal.')
            return
    
        print(f"¡Bienvenidos {jugador1} y {jugador2}! Empecemos a jugar.")
        jvs2p(jugador1, jugador2)
        
        jugar_otra = input("¿Quieren jugar otra partida? (s/n): ").lower()
        if jugar_otra != 's':
            break

def jvs2p(jugador1, jugador2):
    global victorias_consecutivas_usuario1
    global victorias_consecutivas_usuario2
    global escudo_usuario1
    global escudo_usuario2
    global contador
    
    # Reiniciar contadores para una nueva partida
    contador['rondasGanadasUser1'] = 0
    contador['rondasGanadasUser2'] = 0
    victorias_consecutivas_usuario1 = 0
    victorias_consecutivas_usuario2 = 0
    escudo_usuario1 = False
    escudo_usuario2 = False
    
    try: 
        while True:
            if contador['rondasGanadasUser1'] < 3 and contador['rondasGanadasUser2'] < 3:
                print(f"\nTurno de {jugador1}")
                jugador1_choice = input(f"{jugador1}, elige piedra, papel o tijera: ").lower()

                print(f"\nTurno de {jugador2}")
                jugador2_choice = input(f"{jugador2}, elige piedra, papel o tijera: ").lower()

                if jugador1_choice not in opciones or jugador2_choice not in opciones:
                    print("Opción no válida, por favor ambos jugadores elijan entre piedra, papel o tijera.")
                    continue

                if jugador1_choice == jugador2_choice:
                    print("¡Es un empate!")

                elif (jugador1_choice == 'piedra' and jugador2_choice == 'tijera') or \
                     (jugador1_choice == 'tijera' and jugador2_choice == 'papel') or \
                     (jugador1_choice == 'papel' and jugador2_choice == 'piedra'):
                    print(f"¡{jugador1} gana la ronda!")
                    victorias_consecutivas_usuario1 += 1
                    victorias_consecutivas_usuario2 = 0  
                    if victorias_consecutivas_usuario1 == 2:
                        escudo_usuario1 = True
                        print(f"¡{jugador1} tiene un escudo!")
                    if escudo_usuario2:
                        print(f"¡El escudo de {jugador2} bloqueó tu victoria!")
                        escudo_usuario2 = False  
                    else:
                        contador['rondasGanadasUser1'] += 1
                else:
                    print(f"¡{jugador2} gana la ronda!")
                    victorias_consecutivas_usuario2 += 1
                    victorias_consecutivas_usuario1 = 0  
                    if victorias_consecutivas_usuario2 == 2:
                        escudo_usuario2 = True
                        print(f"¡{jugador2} tiene un escudo!")
                    if escudo_usuario1:
                        print(f"¡El escudo de {jugador1} te salvó de perder la ronda!")
                        escudo_usuario1 = False  
                    else:
                        contador['rondasGanadasUser2'] += 1

                print(f"{jugador1}: {contador['rondasGanadasUser1']} | {jugador2}: {contador['rondasGanadasUser2']}")

            else:
                if contador['rondasGanadasUser1'] == 3:
                    print(f"¡{jugador1} ha ganado la partida!")
                    actualizar_estadisticas(jugador1, True)
                    actualizar_estadisticas(jugador2, False)
                else:
                    print(f"¡{jugador2} ha ganado la partida!")
                    actualizar_estadisticas(jugador2, True)
                    actualizar_estadisticas(jugador1, False)
                break

    except ValueError:
        print("Ocurrió un error con la entrada.")

