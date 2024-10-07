import random
from Modules.utils import createUser as user
opciones = ['piedra', 'papel', 'tijera']
contador = {
    'rondasGanadasUser' : 0,
    'rondasGanadasCompu' : 0 
}

def juegojvia():
    print("¡Bienvenido al juego The Chachipun!")
    nombre = input("Imgrese su nombre por favor : ")
    nickname = input("Imgrese su nickname por favor : ")
    user.loginUser(nombre, nickname)
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
                    contador['rondasGanadasUser'] += 1
                else:
                    print("¡Perdiste!")
                    contador['rondasGanadasCompu'] += 1
                print(f"Usuario: {contador['rondasGanadasUser']} | Computadora: {contador['rondasGanadasCompu']}")
            else:
                break
    except ValueError:
        print("Ocurrió un error con la entrada del usuario.")

