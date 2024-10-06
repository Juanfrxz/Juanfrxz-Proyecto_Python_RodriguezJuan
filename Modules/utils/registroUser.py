import os
from Modules.utils import menus as men
from Modules.utils import mensajes as msg
from Modules.utils import util as utl
from Modules.utils import createUser as cru

def menuPrincipal():
    thechapipun = []
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            os.system('cls')
            print(msg.tituloPrincipal)
            print(men.menuRegistro)
            opMenu = int(input('づ￣ 3￣)づ⮞ '))
            match opMenu:
                case 1:
                    isGame = True
                    opMenuGame = 0
                    while (isGame):
                        try:
                            os.system('cls')
                            print(msg.tituloJugar)
                            print(men.menuJugar)
                            opMenu = int(input('づ￣ 3￣)づ⮞ '))
                        except ValueError:
                            print('Error en el dato ingresado...')
                            os.system('pause')
                            continue
                        else:
                            match opMenuGame:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    pass
                case 2:
                    isAddRsg = True
                    opMenuRegis = 0
                    while (isAddRsg):
                        try:
                            os.system('cls')
                            cru.solicitar_informacion()
                            isActive = utl.vali(msg.msgRegister)
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