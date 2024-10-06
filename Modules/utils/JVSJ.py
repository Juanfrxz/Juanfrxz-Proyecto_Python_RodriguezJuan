import random
opciones = ['piedra', 'papel', 'tijera']
def juego1v1():
    print("¡Bienvenido al juego The Chachipun!")
    try: 
        jugador1 = input("Player 1 : Elige piedra, papel o tijera: ").lower()
        jugador2 = input("Player 2: Elige piedra, papel o tijera: ").lower()
        print(f"Player 1 eligió: {jugador1}")
        print(f"Player 2 eligió: {jugador2}")
        if jugador1 == jugador2:
            print("¡Es un empate!")
        elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
            (jugador1 == 'tijera' and jugador2 == 'papel') or \
            (jugador1 == 'papel' and jugador2 == 'piedra'):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    except ValueError:
        if jugador1 not in opciones:
            print("Opción no válida, por favor elige entre piedra, papel o tijera.")
            return
        if jugador2 not in opciones:
            print("Opción no válida, por favor elige entre piedra, papel o tijera.")
            return