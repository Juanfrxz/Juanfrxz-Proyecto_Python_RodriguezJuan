import random
from Modules.utils import createUser as user
opciones = ['piedra', 'papel', 'tijera']
contador = {
    'rondasGanadasUser' : 0,
    'rondasGanadasCompu' : 0 
}
def juego1v1():
    print("¡Bienvenido al juego The Chachipun!")
    try:
        user.solicitar_informacion()
        while True:
            if contador['rondasGanadasUser'] < 3 and contador['rondasGanadasCompu'] < 3:
                jugador1 = input("Player 1 : Elige piedra, papel o tijera: ").lower()
                jugador2 = input("Player 2: Elige piedra, papel o tijera: ").lower()
                print(f"{user.solicitar_informacion} eligió : {jugador1}")
                print(f"{user.solicitar_informacion} eligió : {jugador2}")
                if jugador1 not in opciones:
                    print("Opción no válida, por favor elige entre piedra, papel o tijera.")
                    return
                elif jugador2 not in opciones:
                    print("Opción no válida, por favor elige entre piedra, papel o tijera.")
                    return
                if jugador1 == jugador2:
                    print("¡Es un empate!")
                elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
                    (jugador1 == 'tijera' and jugador2 == 'papel') or \
                    (jugador1 == 'papel' and jugador2 == 'piedra'):
                    print("¡Ganaste!")
                    contador['rondasGanadasUser'] += 1
                else:
                    print("¡Perdiste!")
                    contador['rondasGanadasCompu'] += 1
                print(f"{user.solicitar_informacion}: {contador['rondasGanadasUser']} | {user.solicitar_informacion}: {contador['rondasGanadasCompu']}")
            else:
                break
    except ValueError:
        print("Ocurrió un error con la entrada del usuario.")