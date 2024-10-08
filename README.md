# Juanfrxz-Proyecto_Python_RodriguezJuan
Proyecto: Juego de Piedra, Papel o Tijera
Este proyecto implementa el clásico juego de Piedra, Papel o Tijera en Python, con modos de juego contra la computadora y entre dos jugadores. El juego incluye características adicionales como escudos y un sistema de registro de jugadores.
Estructura del Proyecto
El proyecto está compuesto por los siguientes archivos principales:

main.py

Este archivo contiene la función principal menuPrincipal() que inicia el juego y maneja el menú principal. Permite a los usuarios elegir entre diferentes modos de juego y opciones.

Características principales:

- Menú de selección para jugar 1vs1 o contra la IA
- Manejo de errores para entradas inválidas
- Integración con otros módulos del juego

core.py

Gestiona la interacción con la base de datos de jugadores (un archivo JSON) y proporciona funciones para el registro y inicio de sesión de usuarios.
Funciones principales:

- ReadFile(): Lee los datos de los jugadores desde el archivo JSON
- WriteFile(data): Escribe los datos de los jugadores en el archivo JSON
- signUp_User(diccionarioPrincipal): Registra un nuevo jugador
- login(diccionarioPrincipal): Inicia sesión de un jugador existente

JvsIA.py

Implementa el modo de juego contra la computadora (Jugador vs IA).
Características:

- Lógica del juego Piedra, Papel o Tijera
- Sistema de escudos después de dos victorias consecutivas
- Actualización de estadísticas de jugadores

JVSJ.py

Implementa el modo de juego entre dos jugadores humanos.
Características:

- Manejo de turnos entre dos jugadores
- Sistema de escudos después de dos victorias consecutivas
- Actualización de estadísticas para ambos jugadores

util.py

Contiene funciones de utilidad para validar entradas del usuario.
Funciones principales:

- validateData(message:str): Valida respuestas de tipo Sí/No
- validateResponse(message:str): Similar a validateData(), pero con lógica inversa

custom.py

Proporciona funciones para mejorar la experiencia del usuario en diferentes sistemas operativos.

Funciones principales:

- borrar_pantalla(): Limpia la pantalla de la consola en Windows, Linux o macOS
- pausar_pantalla(): Pausa la ejecución hasta que el usuario presione una tecla

mensajes.py

Contiene constantes de cadenas de texto para los diferentes títulos y mensajes utilizados en el juego.

Elementos principales:

- Títulos ASCII para el menú principal, registro, modos de juego, etc.
- Mensajes para confirmaciones y salidas

menus.py

Define las opciones de menú para diferentes partes del juego.

Elementos principales:

- menuRegistro: Opciones para registrarse, iniciar sesión, jugar o salir
- menuJugar: Opciones para elegir modo de juego, ver estadísticas o salir
- selectPiedra: Opciones para elegir piedra, papel o tijera

Cómo jugar

- Ejecute main.py para iniciar el juego.
![Captura de pantalla 2024-10-08 231716](https://github.com/user-attachments/assets/55a7aca0-958c-4751-8b97-0ab4656a937d)
- Elija entre jugar contra otro jugador o contra la computadora.
![image](https://github.com/user-attachments/assets/179c1b9a-185d-4b12-a7af-fbc2e2cea4b8)
- Si es un nuevo jugador, regístrese. Si ya está registrado, inicie sesión.
![image](https://github.com/user-attachments/assets/5498650e-dc14-417f-a4b9-69d590f385b0)
![image](https://github.com/user-attachments/assets/8c1a30e6-145f-4fd5-a9e1-8dffecf41a0c)
- Siga las instrucciones en pantalla para jugar.
![image](https://github.com/user-attachments/assets/f7c13fb7-9c10-4d12-ac03-d28ca3c04b20)
![image](https://github.com/user-attachments/assets/a83cbcc4-4137-43c9-81e4-bdbaff86a7e4)
![image](https://github.com/user-attachments/assets/ea32a0ad-fa9d-4c58-86e8-5d75ab4c4aa6)
- Disfrute del juego y ¡que gane el mejor!

Características especiales

- Escudos: Después de ganar dos rondas consecutivas, un jugador obtiene un escudo que lo protege de perder la siguiente ronda.
![image](https://github.com/user-attachments/assets/d9150982-bab0-47b9-a9d1-b92f4e37eddc)
- Modos de juego: Elija entre jugar contra la computadora o contra otro jugador.
![image](https://github.com/user-attachments/assets/c3bd8aa0-c6bd-465c-b266-9af271ad08a7)

Requisitos

- Python 3.x
- No se requieren bibliotecas externas

Notas adicionales
Este proyecto es una excelente demostración de programación orientada a objetos en Python, manejo de archivos JSON para persistencia de datos, y lógica de juegos simple pero efectiva. Es ideal para principiantes que quieran entender cómo se estructuran proyectos más grandes en Python.
