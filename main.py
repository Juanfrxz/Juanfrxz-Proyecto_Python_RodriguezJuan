import os
from Modules.utils import menus as men 
from Modules.utils import mensajes as msg
from Modules.utils import util as utl
from Modules.utils import JvsIA as ia
from Modules.utils import JVSJ as jvj
from Modules.utils import core as cr
from Modules.utils import custom as cs

def menuPrincipal():
    juego = {
        'palyers':{},
        'maquina':{
            'gamesPerdidos':0,
            'gamesGanados':0,
            'gamesJugados':0
        }
    }
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            cs.borrar_pantalla()
            print(msg.tituloPrincipal)
            print(men.menuJugar)
            opMenu = int(input('づ￣ 3￣)づ⮞ '))
            match opMenu:
                case 1:
                    isAddRsg = True
                    opMenuRegis = 0
                    while (isAddRsg):
                        try:
                            cs.borrar_pantalla()
                            print(msg.titulo1VS1)
                            jvj.gamePermission(juego)
                            jvj.gamePermission2(juego)
                            cs.borrar_pantalla()
                            print(msg.titulo1VS1)
                            jvj.startGame(juego)
                            break
                        except ValueError:
                            print('Error en el dato ingresado...')
                            os.system('pause')
                            continue
                case 2:
                    isAddRsg = True
                    opMenuRegis = 0
                    while (isAddRsg):
                        try:
                            cs.borrar_pantalla()
                            print(msg.tituloJVSIA)
                            ia.gamePermission(juego)
                            ia.startGame(juego)
                            break
                        except ValueError:
                            print('Error en el dato ingresado...')
                            os.system('pause')
                            continue
                case 3:
                    pass
                case 4:
                    isActive = utl.validateData(msg.msgInfoEquipo)
                case _:
                    print('Opcion ingresada no esta permitida')
                    cs.pausar_pantalla()
        except ValueError:
            print('La opcion ingresa no es valida')
            cs.pausar_pantalla()
            continue
if __name__ == '__main__':
    menuPrincipal()