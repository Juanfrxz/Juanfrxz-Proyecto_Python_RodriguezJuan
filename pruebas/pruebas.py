import random
import json
import os

# Opciones de juego
opciones = ['piedra', 'papel', 'tijera']

# Función para cargar o crear un archivo JSON con las estadísticas
def cargar_estadisticas():
    if os.path.exists('estadisticas.json'):
        with open('estadisticas.json', 'r') as archivo:
            return json.load(archivo)
    else:
        return {}

# Función para guardar las estadísticas en un archivo JSON
def guardar_estadisticas(estadisticas):
    with open('estadisticas.json', 'w') as archivo:
        json.dump(estadisticas, archivo, indent=4)

# Registro de jugadores
def registrar_jugador():
    nombre_completo = input("Introduce tu nombre completo: ")
    nickname = input("Introduce tu nickname: ")
    return {'nombre_completo': nombre_completo, 'nickname': nickname, 'partidas_jugadas': 0, 'partidas_ganadas': 0, 'partidas_perdidas': 0, 'puntos_totales': 0}

# Función principal del juego
def juegojvia():
    print("¡Bienvenido al juego The Chachipun!")

    # Registrar jugadores
    jugador1 = registrar_jugador()
    jugador2 = registrar_jugador()

    # Cargar estadísticas
    estadisticas = cargar_estadisticas()

    # Inicializar variables de juego
    contador = {
        'rondasGanadasJugador1': 0,
        'rondasGanadasJugador2': 0
    }
    escudo_jugador1 = False
    escudo_jugador2 = False
    victorias_consecutivas_jugador1 = 0
    victorias_consecutivas_jugador2 = 0

    try:
        while True:
            if contador['rondasGanadasJugador1'] < 3 and contador['rondasGanadasJugador2'] < 3:
                # Turno de los jugadores
                usuario1 = input(f"{jugador1['nickname']}, elige piedra, papel o tijera: ").lower()
                usuario2 = input(f"{jugador2['nickname']}, elige piedra, papel o tijera: ").lower()

                if usuario1 not in opciones or usuario2 not in opciones:
                    print("Opción no válida. Por favor, elijan entre piedra, papel o tijera.")
                    continue

                # Comparar resultados
                if usuario1 == usuario2:
                    print("¡Es un empate!")

                elif (usuario1 == 'piedra' and usuario2 == 'tijera') or \
                     (usuario1 == 'tijera' and usuario2 == 'papel') or \
                     (usuario1 == 'papel' and usuario2 == 'piedra'):
                    print(f"¡{jugador1['nickname']} gana la ronda!")
                    victorias_consecutivas_jugador1 += 1
                    victorias_consecutivas_jugador2 = 0
                    if victorias_consecutivas_jugador1 == 2:
                        escudo_jugador1 = True
                        print(f"¡{jugador1['nickname']} tiene un escudo!")
                    if escudo_jugador2:
                        print(f"¡Escudo de {jugador2['nickname']} bloqueó tu victoria!")
                        escudo_jugador2 = False
                    else:
                        contador['rondasGanadasJugador1'] += 1
                else:
                    print(f"¡{jugador2['nickname']} gana la ronda!")
                    victorias_consecutivas_jugador2 += 1
                    victorias_consecutivas_jugador1 = 0
                    if victorias_consecutivas_jugador2 == 2:
                        escudo_jugador2 = True
                        print(f"¡{jugador2['nickname']} tiene un escudo!")
                    if escudo_jugador1:
                        print(f"¡El escudo de {jugador1['nickname']} bloqueó la derrota!")
                        escudo_jugador1 = False
                    else:
                        contador['rondasGanadasJugador2'] += 1

                # Mostrar marcador actual
                print(f"{jugador1['nickname']}: {contador['rondasGanadasJugador1']} | {jugador2['nickname']}: {contador['rondasGanadasJugador2']}")

            else:
                # Actualizar estadísticas al finalizar la partida
                ganador = jugador1 if contador['rondasGanadasJugador1'] == 3 else jugador2
                perdedor = jugador2 if contador['rondasGanadasJugador1'] == 3 else jugador1

                ganador['partidas_jugadas'] += 1
                ganador['partidas_ganadas'] += 1
                ganador['puntos_totales'] += 3

                perdedor['partidas_jugadas'] += 1
                perdedor['partidas_perdidas'] += 1

                # Guardar estadísticas
                estadisticas[ganador['nickname']] = ganador
                estadisticas[perdedor['nickname']] = perdedor
                guardar_estadisticas(estadisticas)

                print(f"¡{ganador['nickname']} ha ganado la partida!")
                print(f"Estadísticas de {jugador1['nickname']}: {jugador1}")
                print(f"Estadísticas de {jugador2['nickname']}: {jugador2}")
                break

    except ValueError:
        print("Ocurrió un error con la entrada de uno de los jugadores.")

# Ejecutar el juego
juegojvia()

                              
                                                 