'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Utilizar o implementar BD relacional con MySQL para guardar la información

'''
import funciones

#def menuPrincipal():
#    print("\n\t\t ...:::: M E N Ú   P R I N C I P A L ::::... \n")
#    opcion = input ("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n\t Elige una opción: ").strip()
#    return opcion

#def agregarPeliculas(pelis):
#    print("\n\t\t ...:::: A G R E G A R   P E L Í C U L A S ::::... \n")
#    peli = input("\n\t Introduce el nombre de la película: ").strip().upper()
#    pelis.append(peli)
#    accionExitosa()
#    return pelis

#def mostrarPeliculas(pelis):
#    print("\n\t\t ...:::: M O S T R A R   P E L I C U L A S ::::... \n")
#    print("\t Código \t\t Película")
#    for i in range(0,len(pelis)):
#        print(f"\t{i + 1} \t\t\t {pelis[i]}")
#    espereTecla()

#def limpiarPeliculas(pelis):
#    if len(pelis) > 0:
#        pelis = pelis.clear()
#        accionExitosa()
#    else:
#        input("\n\t ...¡No hay películas que borrar!...")

#def buscarPeliculas(pelis):
#    print("\n\t\t ...:::: B U S C A R   P E L I C U L A S ::::... \n")
#    peli = input("Escribir el nombre de la pelicula: ").upper().strip()
#    if peli in pelis:
#        print("\t Código \t\t Película")
#        for i in range(0,len(pelis)):
#            if peli == pelis[i]:
#                print(f"\t{i + 1} \t\t\t {pelis[i]}")
#                espereTecla()
#    else:
#        input("...¡No existe la película que estas buscando, verifique!...")

#def borrarPeliculas(pelis):
#    posiciones = []
#    print("\n\t\t ...:::: B O R R A R   P E L I C U L A S ::::... \n")
#    peli = input("Escribir el nombre de la pelicula: ").upper().strip()
#    if peli in pelis:
#        for i in range(0,len(pelis)):
#            if peli == pelis[i]:
#                posiciones.append(i)
#        if len(posiciones) > 0:
#            for i in range(0,len(posiciones)):
#                pelis.remove(peli)
#            accionExitosa()
#    else:
#        input("...¡No existe la película que estas buscando, verifique!...")

#def modificarPeliculas(pelis):
#    posiciones = []
#    print("\n\t\t ...:::: M O D I F I C A R   P E L I C U L A S ::::... \n")
#    peli = input("Escribir el nombre de la pelicula: ").upper().strip()
#    if peli in pelis:
#        for i in range(0,len(pelis)):
#            if peli == pelis[i]:
#                posiciones.append(i)
#        if len(posiciones) > 0:
#            for i in range(0,len(posiciones)):
#                pelis.remove(peli)
#            accionExitosa()
#    else:
#        input("...¡No existe la película que estas buscando, verifique!...")