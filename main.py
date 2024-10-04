import Modules.utils.mensajes as msg
import Modules.utils.ui as iu




if __name__ == '__main__':
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            print(msg.tituloPrincipal)
            print(iu.registro)
            opMenu = int(input('づ￣ 3￣)づ⮞ '))
            match opMenu:
                case 1:
                    opMenuSelect = 0
                    
                    
        except ValueError:
            print('La opcion ingresada no es valida')
            continue
    pass