import os
import re
import random
import mysql.connector

TABLA = "diccionario_fr"
HOST = "127.0.0.1"
PUERTO = 3307
USUARIO = "root"
PASSWORD = ""
BASE_DATOS = "bd_diccionario"
ARCHIVO_SALIDA = f"{TABLA}_reporte.txt"
PATRON_TEXTO = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")
PATRON_TEXTO_EXTENDIDO = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ,.]+$")
ANCHO_PANTALLA = 60
UMBRAL_BIEN = 60
UMBRAL_EXCELENTE = 85


COLOR_RESET = "\033[0m"
COLOR_NEGRITA = "\033[1m"
COLOR_VERDE = "\033[92m"
COLOR_ROJO = "\033[91m"
COLOR_AMARILLO = "\033[93m"
COLOR_AZUL = "\033[94m"
COLOR_CIAN = "\033[96m"


def colorear(texto, color):
    """Envuelve un texto entre un color ANSI y el color de reset."""
    return f"{color}{texto}{COLOR_RESET}"


def imprimirEncabezado(texto):
    """Imprime el título de una sección de pantalla, con color."""
    print(colorear(f"\n\t\t...::: {texto} :::...\n", COLOR_CIAN + COLOR_NEGRITA))


def borrarPantalla():
    print("\033c")


def espereTecla():
    input("\n\t...¡Oprima cualquier tecla para continuar!...")


def opcionInvalida():
    input(colorear("\n\t⚠️  ¡Opción invalida, por favor verifique!...", COLOR_AMARILLO))


def accionExitosa():
    input(colorear("\n\t✅ ¡Acción realizada con éxito!...", COLOR_VERDE))


def accionNoExitosa():
    input(colorear("\n\t❌ ¡No fue posible realizar esta acción, inténtelo más tarde!...", COLOR_ROJO))


def terminarSistema():
    input(colorear("\n\t\t...::: 👋 GRACIAS POR UTILIZAR NUESTRO SISTEMA :::...\n", COLOR_CIAN))


def mostrarTabla(dicc):
    encabezado = f"\t{'Código':<5}\t{'Palabra':<10}\t{'Traducción':<10}\t{'Significado':<10}"
    print(colorear(encabezado, COLOR_AZUL + COLOR_NEGRITA))
    print(colorear("-" * 100, COLOR_AZUL))
    for i in dicc:
        print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<10}\t{i[3]:<10}")
    print(colorear("-" * 100, COLOR_AZUL))


def leerTexto(mensaje, permitir_puntuacion=False):
    patron = PATRON_TEXTO_EXTENDIDO if permitir_puntuacion else PATRON_TEXTO
    texto = input(mensaje).strip()
    while texto == "" or not patron.match(texto):
        print(colorear("...⚠️  Entrada inválida, inténtalo de nuevo!...", COLOR_AMARILLO))
        texto = input(mensaje).strip()
    return texto.upper()


def confirmar(mensaje):
    opc = ""
    while opc not in ("SI", "NO"):
        opc = input(mensaje).upper().strip()
    return opc == "SI"


def conectar():
    try:
        conexion = mysql.connector.connect(
            host=HOST, port=PUERTO, user=USUARIO, password=PASSWORD, database=BASE_DATOS
        )
        return conexion
    except Exception:
        input(colorear(
            "...❌ Por el momento no es posible conectar el sistema con la Base de Datos, inténtelo más tarde!...",
            COLOR_ROJO
        ))
        return None


def insertar(palabra, traduccion, significado, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                f"insert into {TABLA} (palabra, traduccion, significado) values (%s,%s,%s)",
                (palabra, traduccion, significado)
            )
            conexionBD.commit()
            return True
        return False
    except Exception:
        return False


def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(f"select * from {TABLA}")
            return cursor.fetchall()
        return []
    except Exception:
        return []


def buscar(palabra, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(f"select * from {TABLA} where palabra=%s or traduccion=%s", (palabra, palabra))
            return cursor.fetchall()
        return []
    except Exception:
        return []


def borrar(palabra, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(f"delete from {TABLA} where palabra=%s or traduccion=%s", (palabra, palabra))
            conexionBD.commit()
            return True
        return False
    except Exception:
        return False


def actualizar(palabra_actual, palabra, traduccion, significado, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                f"update {TABLA} set palabra=%s, traduccion=%s, significado=%s where palabra=%s or traduccion=%s",
                (palabra, traduccion, significado, palabra_actual, palabra_actual)
            )
            conexionBD.commit()
            return True
        return False
    except Exception:
        return False


def vaciar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(f"truncate {TABLA}")
            conexionBD.commit()
            return True
        return False
    except Exception:
        return False


def exportarArchivo(conexionBD):
    registros = consultar(conexionBD)
    if len(registros) == 0:
        return None
    try:
        with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as archivo:
            archivo.write(f"--- REPORTE DE DICCIONARIO ({TABLA.upper()}) ---\n\n")
            archivo.write(f"{'ID':<5}\t{'PALABRA':<15}\t{'TRADUCCIÓN':<15}\t{'SIGNIFICADO'}\n")
            archivo.write("-" * 70 + "\n")
            for fila in registros:
                archivo.write(f"{fila[0]:<5}\t{fila[1]:<15}\t{fila[2]:<15}\t{fila[3]}\n")
        return os.path.abspath(ARCHIVO_SALIDA)
    except Exception:
        return None


def estadisticas(conexionBD):
    registros = consultar(conexionBD)
    if len(registros) == 0:
        return None

    longitudes = []
    letras_iniciales = {}
    contador = 0
    suma_longitudes = 0

    for fila in registros:
        palabra = fila[1]
        longitud = len(palabra)
        longitudes.append(longitud)
        suma_longitudes = suma_longitudes + longitud
        contador = contador + 1
        letra = palabra[0]
        letras_iniciales[letra] = letras_iniciales.get(letra, 0) + 1

    promedio = suma_longitudes / contador if contador > 0 else 0

    resultado = {
        "total": contador,
        "suma_longitudes": suma_longitudes,
        "promedio": promedio,
        "mas_larga": max(longitudes),
        "mas_corta": min(longitudes),
        "letras_iniciales": letras_iniciales,
    }
    return resultado


def obtenerPalabrasParaEstudiar(conexionBD):
    registros = consultar(conexionBD)
    lista = list(registros)
    random.shuffle(lista)
    return lista


def calificarEstudio(aciertos, total):
    if total == 0:
        return 0, ""
    porcentaje = (aciertos / total) * 100
    if porcentaje >= UMBRAL_EXCELENTE:
        mensaje = "Excelente"
    elif porcentaje >= UMBRAL_BIEN:
        mensaje = "Bien hecho"
    else:
        mensaje = "Sigue esforzándote"
    return porcentaje, mensaje
