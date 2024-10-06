import json
# Función para cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)  
    except FileNotFoundError:
        print("Archivo 'usuarios.json' no encontrado, se creará uno nuevo.")
        return {} 
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {} 

def guardar_usuarios(usuarios):
    try:
        with open('usuarios.json', 'w') as archivo:
            json.dump(usuarios, archivo, indent=4)  
    except Exception as e:
        print(f"Error al guardar los usuarios: {e}")

def solicitar_informacion():
    usuarios = cargar_usuarios()  
    nombre_completo = input("Ingrese su nombre completo: ")  
    
    while True:
        nickname = input("Ingrese su nickname: ")  
        if nickname in usuarios:
            print("Nickname ocupado, ingrese otro.")  
        else:
            agregar_otro = input("¿Deseas agregar otro? (sí/no): ").lower()
            usuarios[nickname] = nombre_completo  
            guardar_usuarios(usuarios)  
            print(f"¡Registro completado! Bienvenido/a, {nombre_completo} con el nickname {nickname}")
            break 

