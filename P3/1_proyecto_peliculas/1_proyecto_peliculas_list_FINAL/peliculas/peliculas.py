import funciones
from peliculas import crud
      
def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    nombre=input("Introducir el nombre de la película: ").upper().strip()
    categoria=input("Introducir la categoría de la película: ").upper().strip()
    clasificacion=input("Introducir la clasificación de la película: ").upper().strip()
    genero=input("Introducir el género de la película: ").upper().strip()
    idioma=input("Introducir el idioma de la película: ").upper().strip()
    respuesta=crud.insertar(nombre,categoria,clasificacion,genero,idioma,conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()    

def mostrarPeliculas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    pelis=crud.consultar(conexionBD)
    if  len(pelis) > 0:
        print(f"\t{'Código':<5}\t\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<10}\t{'Género':<10}\t{'Idioma':<10}\n")
        print("-"*100)
        for i in pelis:
            print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<10}\t{i[4]:<10}\t{i[5]:<10}")
        print("-"*100)
    else:
        input("...¡No hay películas a mostrar!...")
    funciones.espereTecla()
  
def limpiarPeliculas(conexionBD):
    pelis=crud.consultar(conexionBD)
    if len(pelis) > 0:
        opc = input("¿Estás seguro que deseas borrar TODAS las películas? ").upper().strip()
        while opc != "SI" and opc != "NO":
            opc = input("¿Estás seguro que deseas borrar TODAS las películas? ").upper().strip()
        if opc == "SI":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay películas que borrar!...")

    funciones.espereTecla()
        
def buscarPeliculas(conexionBD):
    print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
    nombre=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis=crud.buscar(nombre,conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        print(f"\t{'Código':<5}\t\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<10}\t{'Género':<10}\t{'Idioma':<10}\n")
        print("-"*100)
        for i in pelis:
            print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<10}\t{i[4]:<10}\t{i[5]:<10}")
        print("-"*100)
    else:
        input("...¡No hay películas a buscar!...")
    funciones.espereTecla()

def borrarPeliculas(conexionBD):
    print("\n\t\t...:::: BORRAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis=crud.buscar(peli,conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        print(f"\t{'Código':<5}\t\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<10}\t{'Género':<10}\t{'Idioma':<10}\n")
        print("-"*100)
        for i in pelis:
            print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<10}\t{i[4]:<10}\t{i[5]:<10}")
        print("-"*100)
        opc = ""
        while opc != "SI" and opc != "NO":
            opc = input("¿Estás seguro que deseas borrar la(s) película(s)? (SI/NO)").upper().strip()
        if opc == "SI":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay películas a buscar!...")
    funciones.espereTecla()
        
def modificarPeliculas(conexionBD):
    print("\n\t\t...:::: MODIFICAR PELICULAS ::::...\n")
    nombre_old=input("Escribir el nombre de la pelicula: ").upper().strip()
    nombre=nombre_old
    pelis=crud.buscar(nombre,conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        print(f"\t{'Código':<5}\t\t{'Nombre':<10}\t{'Categoría':<10}\t{'Clasificación':<10}\t{'Género':<10}\t{'Idioma':<10}\n")
        print("-"*100)
        for i in pelis:
            print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<10}\t{i[4]:<10}\t{i[5]:<10}")
        print("-"*100)
        opc = ""
        while opc != "SI" and opc != "NO":
            opc = input("¿Deseas modificar la(s) película(s)? (SI/NO)").upper().strip()
        if opc == "SI":
            nombre=input("Introducir el nuevo nombre de la película: ").upper().strip()
            categoria=input("Introducir la nueva categoría de la película: ").upper().strip()
            clasificacion=input("Introducir la nueva clasificación de la película: ").upper().strip()
            genero=input("Introducir el nuevo género de la película: ").upper().strip()
            idioma=input("Introducir el nuevo idioma de la película: ").upper().strip()
            respuesta=crud.insertar(nombre,categoria,clasificacion,genero,idioma,conexionBD)
            respuesta = crud.actualizar(nombre,categoria,clasificacion,genero,idioma,nombre_old,conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay películas a modificar!...")
    funciones.espereTecla()
    