# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
modulos.funcion1()

nom = "Daniel"
ape = "Carreon"

name,lastname = modulos.funcion4(nom,ape)
print(f"Nombre: {name} \n Apellidos: {lastname}")

#2da forma de utilizar modulos

from modulos import borrarPantalla,funcion1,funcion4
#from modulos import * (Importa todas las funciones)

borrarPantalla()
funcion1()

nom = "Daniel"
ape = "Carreon"

name,lastname = funcion4(nom,ape)
print(f"Nombre: {name} \n Apellidos: {lastname}")