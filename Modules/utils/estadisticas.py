import json
import os

def cargar_estadisticas(archivo='estadisticas.json'):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    else:
        return {}

def guardar_estadisticas(estadisticas, archivo='estadisticas.json'):
    with open(archivo, 'w') as f:
        json.dump(estadisticas, f, indent=4)

def actualizar_estadisticas(jugador, resultado, estadisticas):
    nombre = jugador['nickname']
    
    if nombre not in estadisticas:
        estadisticas[nombre] = {
            'nombre_completo': jugador['nombre_completo'],
            'partidas_jugadas': 0,
            'partidas_ganadas': 0,
            'partidas_perdidas': 0,
            'puntos_totales': 0
        }

    estadisticas[nombre]['partidas_jugadas'] += 1
    if resultado == 'ganado':
        estadisticas[nombre]['partidas_ganadas'] += 1
        estadisticas[nombre]['puntos_totales'] += 3
    elif resultado == 'perdido':
        estadisticas[nombre]['partidas_perdidas'] += 1

    return estadisticas
