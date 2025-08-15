# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 09:52:35 2025

@author: Wilfredo
"""
nombre = "Wilfredo"
num1 = int(input("Ingrese su primer numero"))
num2 = int(input("Ingrese su segundo numero"))

def suma(a, b):
    return a + b

print(suma(num1, num2))

def resta(a, b):
    return a - b

print(resta(num1, num2))

def multiplicacion(a, b):
    return a * b

print(multiplicacion(num1, num2))

def division(a, b):
    if b != 0:
        return a / b

print(division(num1, num2))

def potencia(a, b):
    return a ** b

print(potencia(num1, num2))


def saludo():
    print("Hola a todos, sean bienvenidos al curso de programacion")
    
def saludo_pred(nombre):
    print(f"hola{nombre}, sea bienvenido al curso de programacion 2 ")