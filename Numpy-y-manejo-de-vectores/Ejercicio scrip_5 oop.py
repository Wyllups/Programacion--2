# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:32:46 2025

@author: Wilfredo
"""


""" 

Clase Estudiante:
    Atributos - Nombre, Edad, calificacion
    Metodos - Constructor(), Calificacion(Notas), Resumen final > 3> Aprobo, 3< No aprobo

"""

class Estudiante:
    def __init__(self):
        self.__nombre = ""
        self.__edad = None
        self.__identificacion = None
        self.__calificacion = None
        print("Estudiante Creado")
    
    def datos(self, nombre, edad, identificacion):
        self.__nombre = nombre
        self.__edad = edad
        self.__identificacion = identificacion
    
    def calificacion_final(self, notas):
        contador = 0
        for nota in notas :
            contador += nota
        self.__calificacion = contador/len(notas)
        return self.__calificacion
        
    
    def resumen(self):
        if self.__calificacion >= 3:
            return f"{self.__nombre} ha aprobado con {self.__calificacion}."
        else:
            return f"{self.__nombre} no aprobó. Nota: {self.__calificacion}."

est1 = Estudiante()
est1.datos("Wilfredo", 21, 1087)
est1.calificacion_final([4.5, 4.7, 3.0])
print(est1.resumen())

est2 = Estudiante()
est2.datos("Juan Felipe", 19, 4567)
est2.calificacion_final([2.6, 4.6, 2.1])
print(est2.resumen())

est3 = Estudiante()
est3.datos("Miller Q", 19, 4567)
est3.calificacion_final([2.6, 1.6, 2.1])
print(est3.resumen())
