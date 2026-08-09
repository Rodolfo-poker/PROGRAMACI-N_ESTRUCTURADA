import funciones

#pelis = {
#    "nombre" : "Toy Story 5",
#    "duracion" : "120 min",
#    "idioma" : "español",
#    "clasificacion" : "A",
#    "genero" : "animada"
#       }
      
def menuPrincial():
    print("\n\t\t...:::: M E N U   P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: A G R E G A R   C A R A C T E R Í S T I C A S   D E   U N A   P E L Í C U L A ::::...\n")
    caracteristica=input("Introducir el nombre de la característica: ").lower().strip()
    valor = input("Introducir el valor de la característica: ").lower().strip()
    pelis[caracteristica] = valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR   C A R A C T E R Í S T I C A S   D E   L A   P E L Í C U L A ::::...\n")
    
    if len(pelis) > 0:
        print("\tCaracterística\t\tValor\n")
        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("\n\t ...¡No hay características a mostrar, verifique!...")
    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS las características (Si/No)? ").lower().strip()
        if opc == "si":
            pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay características que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: B U S C A R   U N A   C A R A C T E R Í S T I C A   D E   L A   P E L Í C U L A ::::...\n")
    caracteristica=input("Escribir el nombre de la característica: ").lower().strip()
    
    no_encontro = False
    
    for i in pelis:
        if caracteristica==i:
            print("\tCaracterística\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            no_encontro = True
        funciones.espereTecla()
    if not(no_encontro):
        input("...¡No existe la característica que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: B O R R A R   U N A   C A R A C T E R Í S T I C   D E   L A    P E L I C U L A ::::...\n")
    caracteristica=input("Escribir el nombre de la característica: ").upper().strip()
    no_encontro = True
    if i in pelis:
        for i in pelis:
            if caracteristica==i:
                opc=""
                print("\tCaracterística\t\tValor\n")
                print(f"{i}\t\t{pelis[i]}")
                while opc!="si" and opc!="no":
                  opc=input("¿Deseas borrar la característica (Si/No)? ").lower().strip()
                if opc=="si":
                  pelis.pop(caracteristica)
                  funciones.accionExitosa()
                  no_encontro = False
    if no_encontro:
        input("...¡No existe la característica a borrar, verifique!...")
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: M O D I F I C A R   E L   V A L O R   D E   L A   C A R A C T E R Í S T I C A ::::...\n")
    caracteristica=input("Escribir el valor: ").upper().strip()
    no_encontro = True
    for i in pelis:
        if caracteristica==i:
            opc=""
            print("\tCaracterística\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            while opc!="si" and opc!="no":
                opc=input("¿Deseas modificar el valor de la característica de la película (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[caracteristica] = input("Escribe el nuevo valor de la característica: ").upper().strip() 
                no_encontro = False
                funciones.accionExitosa()
    if no_encontro:       
        input("...¡No existe el valor a modificar, verifique!...")