# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 15:39:59 2025

@author: Wilfredo
"""

import numpy as np

# Crear tabla vacía
def crear_tabla(filas, columnas):
    return np.full((filas, columnas), None)

def encabezados(tabla):
    encabezado = ["Club", "Pj", "G", "E", "P", "GF", "GC", "DG", "Pts"]
    for i in range(len(encabezado)):
        tabla[0, i] = encabezado[i]
    return tabla

def llenar_equipo(tabla, fila, nombre, g, e, p, gf, gc):
    pj = g + e + p  
    dg = gf - gc    
    pts = g * 3 + e 
    datos = [nombre, pj, g, e, p, gf, gc, dg, pts]
    
    for col in range(len(datos)):
        tabla[fila, col] = datos[col]
    return tabla

def ordenar_tabla(tabla):
    datos = tabla[1:]
    # Convertimos Pts y DG a enteros para ordenarlos correctamente
    datos_ordenados = sorted(
        datos, 
        key=lambda fila: (int(fila[8]), int(fila[7])), 
        reverse=True # El reverse lo use para odenar de mayor a menor cuendo es true 
    )                  #y de menos a mayor cuando es false 
    return np.vstack([tabla[0], datos_ordenados])

#Esta parte la adicione para darle formato a la tabla
def mostrar_tabla(tabla):
    for fila in tabla:
        print("{:<15} {:<3} {:<3} {:<3} {:<3} {:<4} {:<4} {:<4} {:<4}".format(*fila))

# ========================

# ========================
num_equipos = int(input("¿Cuántos equipos vas a ingresar? "))
tabla = crear_tabla(num_equipos + 1, 9)
encabezados(tabla)

for i in range(1, num_equipos + 1):
    print(f"\n== Ingresando datos del equipo #{i} ==")
    nombre = input("Nombre del equipo: ")
    g = int(input("Partidos ganados: "))
    e = int(input("Partidos empatados: "))
    p = int(input("Partidos perdidos: "))
    gf = int(input("Goles a favor: "))
    gc = int(input("Goles en contra: "))
    
    llenar_equipo(tabla, i, nombre, g, e, p, gf, gc)

tabla_ordenada = ordenar_tabla(tabla)

print("\n===== TABLA DE POSICIONES =====")
mostrar_tabla(tabla_ordenada)