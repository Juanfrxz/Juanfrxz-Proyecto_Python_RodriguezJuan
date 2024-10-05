import os
import Modules.utils.ui as menu
import Modules.utils.mensajes as msg

def menuPrincipal():
    thechapipun = []
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            os.system('cls')
            print(msg.tituloPrincipal)
            print(menu.menuRegistro)
            opMenu = int(input('づ￣ 3￣)づ⮞ '))
            match opMenu:
                case 1:
                    isGame = True
                    opMenuGame = 0
                    while (isGame):
                        try:
                            os.system('cls')
                            print(msg.tituloJugar)
                            print(menu.menuJugar)
                            opMenu = int(input('づ￣ 3￣)づ⮞ '))
                        except ValueError:
                            print('Error en el dato ingresado...')
                            os.system('pause')
                            continue
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
                    pass
                case 3:
                    pass
                case 4:
                    pass
        except ValueError:
            print('La opcion ingresa no es valida')
            os.system('pause')
            continue