import random

opciones = ['piedra', 'papel', 'tijera']

def juegojvia():
    print("¡Bienvenido al juego The Chachipun!")
    try: 
        usuario = input("Elige piedra, papel o tijera: ").lower()
        computadora = random.choice(opciones)
        print(f"Computadora eligió: {computadora}")
        if usuario == computadora:
            print("¡Es un empate!")
        elif (usuario == 'piedra' and computadora == 'tijera') or \
            (usuario == 'tijera' and computadora == 'papel') or \
            (usuario == 'papel' and computadora == 'piedra'):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    except ValueError:
        if usuario not in opciones:
            print("Opción no válida, por favor elige entre piedra, papel o tijera.")
            return
    
