# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 10:34:02 2025

@author: Wilfredo
"""

import Scrip_1 as s1

name = input("ingrese su nombre: ")

var1 = int(input("ingrese su primer numero:  "))
var2 = int(input("ingrese su segundo numero: "))

s1.saludo()
s1.saludo_pred(name)

print("la operacion de la potencia es: ")
print(s1.potencia(var1,var2))

print("La operacion de la multiplicacion es: ")
print(s1.multiplicacion(var1, var2))

#%%

