# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 07:21:24 2025

@author: Wilfredo
"""


import numpy as np

def crear_tabla(filas, columnas):

    tabla = np.zeros((filas, columnas))

    for i in range(filas):
        for j in range(columnas):
            tabla[i, j] = (i + j) % 2
    return tabla


filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

tabla = crear_tabla(filas, columnas)
print(tabla)