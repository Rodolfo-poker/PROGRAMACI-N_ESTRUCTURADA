from diccionario_en import main as ingles
from diccionario_fr import main as frances

OPCION_SALIR = "3"
TITULO = "DicciPro"
SUBTITULO = "Tu diccionario personal en Inglés y Francés"
ANCHO_TITULO = 48

COLOR_RESET = "\033[0m"
COLOR_NEGRITA = "\033[1m"
COLOR_AMARILLO = "\033[93m"
COLOR_CIAN = "\033[96m"


def borrarPantalla():
    print("\033c")


def opcionInvalida():
    input(f"\n\t{COLOR_AMARILLO}⚠️  ¡Opción invalida, por favor verifique!...{COLOR_RESET}")


def terminarSistema():
    input(f"\n\t\t{COLOR_CIAN}...::: 👋 GRACIAS POR UTILIZAR NUESTRO SISTEMA :::...{COLOR_RESET}\n")


def imprimirTitulo():
    print()
    print(COLOR_CIAN + "╔" + "═" * ANCHO_TITULO + "╗" + COLOR_RESET)
    linea_titulo = TITULO.center(ANCHO_TITULO)
    print(COLOR_CIAN + "║" + COLOR_RESET + COLOR_AMARILLO + COLOR_NEGRITA + linea_titulo + COLOR_RESET + COLOR_CIAN + "║" + COLOR_RESET)
    linea_subtitulo = SUBTITULO.center(ANCHO_TITULO)
    print(COLOR_CIAN + "║" + COLOR_RESET + linea_subtitulo + COLOR_CIAN + "║" + COLOR_RESET)
    print(COLOR_CIAN + "╚" + "═" * ANCHO_TITULO + "╝" + COLOR_RESET)


def menuTablas():
    imprimirTitulo()
    opcion = input(
        "\n\t1.- 📘 Diccionario Inglés \n\t2.- 📙 Diccionario Francés \n\t3.- 🚪 Salir \n\t Escribe una opción: "
    ).strip()
    return opcion


opc = ""
while opc != OPCION_SALIR:
    borrarPantalla()
    opc = menuTablas()

    match opc:
        case "1":
            borrarPantalla()
            ingles.menuDiccionario()
        case "2":
            borrarPantalla()
            frances.menuDiccionario()
        case "3":
            borrarPantalla()
            terminarSistema()
        case _:
            opcionInvalida()
