# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 14:47:59 2025

@author: Wilfredo
"""

import time 
import numpy as np

for i in range(3):
    for j in range(3):
        print(f"{i},{j}", end = " ")
        time.sleep(1)
    print( )

for i in range(0,3,1):
    for j in range(0,3):
        print(f"{i},{j}", end = " ")
        time.sleep(1)
    print( )
    
tabla = np.full((11,9), None)

#Encabezado
for fila in range(1):
    for columna in range(9):
        match columna:
            case 0:
                tabla[fila, columna] = "Club"
            case 1:
                tabla[fila, columna] = "Pj"
            case 2:
                tabla[fila, columna] = "G"
            case 3:
                tabla[fila, columna] = "E"
            case 4:
                tabla[fila, columna] = "P"
            case 5:
                tabla[fila, columna] = "GF"
            case 6:
                tabla[fila, columna] = "GC"
            case 7:
                tabla[fila, columna] = "DG"
            case 8:
                tabla[fila, columna] = "Pts"

#%% funciones

import time 
import numpy as np

#funcion crea tabla

def crear_tabla(filas, columnas):
    return np.full((filas, columnas), None)

#Funcion de encabezados

def encabezados (tabla):
    for fila in range(1):
        for columna in range(9):
            match columna:
                case 0:
                    tabla[fila, columna] = "Club"
                case 1:
                    tabla[fila, columna] = "Pj"
                case 2:
                    tabla[fila, columna] = "G"
                case 3:
                    tabla[fila, columna] = "E"
                case 4:
                    tabla[fila, columna] = "P"
                case 5:
                    tabla[fila, columna] = "GF"
                case 6:
                    tabla[fila, columna] = "GC"
                case 7:
                    tabla[fila, columna] = "DG"
                case 8:
                    tabla[fila, columna] = "Pts"
    return tabla

# Funcion de llenar la tabla 


#%% invocacion de funciones

tabla_dimayor = crear_tabla(11, 9)

encabezados(tabla_dimayor)