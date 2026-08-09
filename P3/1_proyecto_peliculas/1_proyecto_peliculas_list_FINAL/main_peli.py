'''
Crear un proyecto que permita gestionar (administrar) diccionario. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de diccionario.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de diccionario
3.- Utilizar o implementar BD relacional con MySQL para guardar la información

'''
from diccionario import diccionario
import funciones

#Conexión con la base de datos:
conexionBD = funciones.conectar()

opc=""

while opc!="7":
    funciones.borrarPantalla()
    opc=diccionario.menuPrincial()

    match opc:
        case "1":
            funciones.borrarPantalla()
            diccionario.agregardiccionario(conexionBD)
        case "2":
            funciones.borrarPantalla()
            diccionario.borrardiccionario(conexionBD)
        case "3":
            funciones.borrarPantalla()
            diccionario.modificardiccionario(conexionBD)
        case "4":
            funciones.borrarPantalla()
            diccionario.mostrardiccionario(conexionBD)
        case "5":
            funciones.borrarPantalla()
            diccionario.buscardiccionario(conexionBD)
        case "6":
            funciones.borrarPantalla()
            diccionario.limpiardiccionario(conexionBD)
        case "7":
            funciones.borrarPantalla()
            funciones.terminarSistema()
        case _:
            funciones.opcionInvalida()
