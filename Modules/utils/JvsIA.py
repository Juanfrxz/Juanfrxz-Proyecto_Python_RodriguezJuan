import random
import os
from Modules.utils import core as user

opciones = ['piedra', 'papel', 'tijera']

contador = {
    'rondasGanadasUser': 0,
    'rondasGanadasCompu': 0
}
escudo_usuario = False
escudo_computadora = False
victorias_consecutivas_usuario = 0
victorias_consecutivas_computadora = 0

def jvsia():
    global victorias_consecutivas_computadora
    global victorias_consecutivas_usuario
    global escudo_computadora
    global escudo_usuario
    global contador
    print("¡Bienvenido al juego The Chachipun!")
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
                break
    except ValueError:
        print("Ocurrió un error con la entrada del usuario.")


