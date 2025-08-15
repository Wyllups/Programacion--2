# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 10:15:26 2025

@author: Wilfredo
"""

class Animal:
    # Atributos
    tipo_animal = " "
    color = " "
    raza = " "
    collar = False

    #Metodos
    def sonido():
        return "Emite ruido"

    def corre():
        return "Corre"
    
    def caminar():
        return "Camina"

    def vuela():
        return "Vuela"

    def nadar():
        return "Nada en el agua"

#%%
#Instanciar un objeto

perro = Animal()
perro.nombre = "Franco"
perro.tipo_animal = "canino"
perro.color = "Cafe"
perro.raza = "Mestizo"
perro.collar = "Collar"

print(f"Mi primer objeto es un {perro.nombre}, .\
      de tipo, {perro.tipo_animal}, con color {perro.color}, .\
          de raza {perro.raza}.\
Mi perro {perro.sonido()},")

#%%

gato = Animal()

gallo = Animal()

culebra = Animal()

pez = Animal()

#%%

perro.tipo_animal = "canino"

perro.color = "cafe"

perro.raza = "retriever"

perro.collar = True

#%%

print(f"Animal: {perro.tipo_animal}")

print(f"Color del animal: {perro.color}")

print(f"Raza del animall: {perro.raza}")

print(f"El perro tiene collar: {perro.collar}")

#%% AUTOMOVIL

class Automovil:
    
    def __init__(self):
        self.__largo_chasis = 2.50
        self.__ancho_chasis = 1.20
        self.__ruedas = 4
        self.__en_marcha = False
        print('iniciando las variables')
    #Metodos
    def arrancar(self, arranca):
        self.__en_marcha = arranca
        
        if(self.__en_marcha == True):
            return "El automovil se encuentra en movimiento"
        else:
            return "El automovil esta detenido"
    
    def estado(self):
        print(f"El automovil tiene un largo de chasis .\
        {self.__largo_chasis} m, con un ancho de chasis .\
        {self.__ancho_chasis} m, y tiene {self.__ruedas} ruedas")

#%%AUTOMOVIL 1

automovil1 = Automovil()
print(automovil1.arrancar(False))
automovil1.estado()

print("----------------Objeto 2 --------------")
#AUTOMOVIL 2
mustang = Automovil()
mustang.en_marcha = True
print(mustang.arrancar(True))
mustang.estado()

#%%
#Encapsular metodos
#CODIGO ACTUALIZADO 

class Automovil:
    # Atributos iniciarlos 
    def __init__(self):
        self.__largo_chasis = 2.50
        self.__ancho_chasis = 1.20
        self.__ruedas = 4
        self.__en_marcha = False
        print('iniciando las variables')
    #Metodos
    def arrancar(self, arranca):
        self.__en_marcha = arranca
        
        if (self.__en_marcha):
            chequeo = self.__chequeointerno()
        
        if(self.__en_marcha) and (chequeo):
            return "El automovil se encuentra en movimiento"
        
        elif (self.__en_marcha) and (chequeo == False):
            return "Algo salio mal, EL VEICULO NO PUEDE ARRANCAR"
        
        else:
            return "El automovil esta detenido"
    
    def estado(self):
        print(f"El automovil tiene un largo de chasis .\
        {self.__largo_chasis} m, con un ancho de chasis .\
        {self.__ancho_chasis} m, y tiene {self.__ruedas} ruedas")
    
    def __chequeointerno(self):
        print("Realizando chequeo...")
        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.temperatura = "Ok"
        self.puertas = "abiertas"
        if(self.gasolina == "Ok") and (self.aceite == "Ok") and (self.temperatura == "Ok") and (self.puertas == "cerradas"):
            return True
        else:
            return False

#%%

#Automovil 1 

automovil1 = Automovil()
print(automovil1.arrancar(False))
automovil1.estado()

print("----------------Objeto 2 --------------")
#AUTOMOVIL 2
mustang = Automovil()
print(mustang.arrancar(True))
mustang.estado()


