import funciones
from peliculas import crud
      
def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Introducir el nombre de la pelicula: ").upper().strip()
    respuesta=crud.insertar(peli,conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()    

def mostrarPeliculas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    pelis=crud.consultar(conexionBD)
    if  len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        for i in pelis:
            print(f"\t{i[0]}\t\t{i[1]}")
        funciones.espereTecla()
    else:
        input("...¡No hay películas a mostrar!...")
        
    
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

    funciones.accionNoExitosa()
        
def buscarPeliculas(conexionBD):
    print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis=crud.buscar(peli,conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        for i in pelis:
            print(f"\t{i[0]}\t\t{i[1]}")
    else:
        input("...¡No hay películas a buscar!...")
    funciones.espereTecla()

def borrarPeliculas(conexionBD):
    print("\n\t\t...:::: BORRAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis=crud.buscar(peli,conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        for i in pelis:
            print(f"\t{i[0]}\t\t{i[1]}")
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
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis=crud.buscar(peli,conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        for i in pelis:
            print(f"\t{i[0]}\t\t{i[1]}")
            opc = ""
        while opc != "SI" and opc != "NO":
            opc = input("¿Deseas modificar la(s) película(s)? (SI/NO)").upper().strip()
        if opc == "SI":
            peli2=input("Escribir el nombre de la nueva pelicula: ").upper().strip()
            respuesta = crud.actualizar(peli,peli2,conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay películas a modificar!...")
    funciones.espereTecla()
    