import os
from Modules.utils import menus as men 
from Modules.utils import mensajes as msg
from Modules.utils import util as utl
from Modules.utils import JvsIA as ia
from Modules.utils import JVSJ as jvj
 
def menuPrincipal():
    thechapipun = {}
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            os.system('cls')
            print(msg.tituloPrincipal)
            print(men.menuJugar)
            opMenu = int(input('づ￣ 3￣)づ⮞ '))
            match opMenu:
                case 1:
                    isAddRsg = True
                    opMenuRegis = 0
                    while (isAddRsg):
                        try:
                            os.system('cls')                           
                            print(msg.titulo1VS1)
                            isActive = jvj.juego1v1()
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
                            os.system('cls')
                            print(msg.tituloJVSIA)
                            isActive = ia.juegojvia()
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
                    print('Opcion ingresa no esta permitida')
                    os.system ('pause')
        except ValueError:
            print('La opcion ingresa no es valida')
            os.system('pause')
            continue