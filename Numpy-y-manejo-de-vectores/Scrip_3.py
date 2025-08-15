# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 12:43:44 2025

@author: Wilfredo
"""

import numpy as np 

print(np.pi)
print (np.e)

vector1 = {5, 6, 8}
vector2 = np.array([5, 6, 8])
vector3 = np.array([[5, 7, 8, 4],
                    [3, 2, 1, 0]])

print(f"CantidaD de Dimensiones: {vector2.ndim}")
print(f"Dimension: {vector2.shape}")

print(vector3)

iteracion = 0

for fila in vector3:
    iteracion +- 1
    print(f"{iteracion}:{fila}")

for fila in vector3:
    for elemento in fila:
        print(elemento)

for fila in vector3:
    for elemento in fila:
        print(elemento, end=" ")
    print()
    
vector4 = np.array([[5, 7, 8.3, 4],[3, 2, 1, 0]])
for fila in vector4:
    for elemento in fila:
        print(elemento, end = " ")
    print()

type(vector3[1][2])
type(vector4[1][2])

vector5 = np.zeros((3,3))
vector6 = np.ones((3,3))
vector7 = np.eye(5)
vector8 = np.full((3,2),5)
vector9 = np.full_like(2,7)
vector10 = np.random.rand(4,3)
vector11 = np.random.randint(0, 11, (8,3))
vector12 = np.identity(5)

vector13 = np.arange(1,11,3)
vector14 = np.linspace(1,11,20)

