import mysql.connector

def accionExitosa():
    input("...¡Acción realizada con éxito!...")

def accionNoExitosa():
    input("...¡Ha habido un problema durante la ejecución de esta acción, verifique!...")

def menuPrincipal():
    print(f"\n\t 1.- Agregar \n\t 2.- Mostrar \n\t 3.- Salir")
    opc = input("Elige una Opción: ").strip()
    return opc

def agradecimiento():
    input("...¡Gracias por utilizar nuestro programa!...")

def limpiarPantalla():
    print("\033c")

def espereTecla():
    input("...¡Oprima cualquier tecla para continuar!...")

def agregarPeliculas(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Introducir el nombre de la pelicula: ").upper().strip()
    categoria = input("Introducir la categoría de la película: ").upper().strip()
    respuesta=insertar(categoria,peli,conexionBD)
    if respuesta:
        accionExitosa()
        menuPrincipal()
    else:
        accionNoExitosa()    

def mostrarPeliculas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    pelis=consultar(conexionBD)
    if  len(pelis) > 0:
        print("\tCodigo\t\tPelicula\n")
        for i in pelis:
            print(f"\t{i[0]}\t\t{i[1]}")
        espereTecla()
    else:
        input("...¡No hay películas a mostrar!...")

def insertar(categoria,peli,conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("insert into películas values (null,%s,%s)",(peli,categoria))
          conexionBD.commit()
          return True
        else:
          return False   
    except Exception as e:
        return False
    
def consultar(conexionBD):
    try:
       if conexionBD!=None:
           cursor=conexionBD.cursor()
           cursor.execute("select * from películas")
           return cursor.fetchall()
       else:
           return []
    except:
        return []
    
def conectar():
    try:
       conexion=mysql.connector.connect(
           host="127.0.0.1",
           user="root",
           password="",
           database="bd_examen_peliculas"
       )
       return conexion
    except Exception as e:
        input("...¡Por el momento no es posible conectar el sistema o aplicacion con la Base de datos, intentalo mas tarde! ...")
        return None

conexionBD = conectar()

opc = menuPrincipal()

while opc != "3":
    
    match opc:
        case "1":
            limpiarPantalla()
            agregarPeliculas(conexionBD)
        case "2":
            limpiarPantalla()
            mostrarPeliculas(conexionBD)
        case "3":
            limpiarPantalla()
            agradecimiento()