from . import funciones


def menuPrincipal():
    funciones.imprimirEncabezado("MENU PRINCIPAL - DICCIONARIO INGLÉS")
    opcion = input(
        "\n\t1.- ➕ Agregar\n\t2.- 🗑️  Borrar\n\t3.- ✏️  Modificar\n\t4.- 📖 Mostrar\n\t5.- 🔍 Buscar"
        "\n\t6.- 🧹 Limpiar\n\t7.- 📊 Estadísticas\n\t8.- 📤 Exportar\n\t9.- 📚 Repasar/Estudiar"
        "\n\t10.- 🚪 Salir\n\tEscribe una opción: "
    ).strip()
    return opcion


def agregarPalabras(conexionBD):
    funciones.imprimirEncabezado("➕ AGREGAR PALABRAS")
    palabra = funciones.leerTexto("Introduce una palabra: ")
    traduccion = funciones.leerTexto("Introduce la traducción de la palabra: ")
    significado = funciones.leerTexto("Introduce el significado de la palabra: ", permitir_puntuacion=True)
    respuesta = funciones.insertar(palabra, traduccion, significado, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarPalabras(conexionBD):
    funciones.imprimirEncabezado("📖 MOSTRAR PALABRAS")
    dicc = funciones.consultar(conexionBD)
    if len(dicc) > 0:
        funciones.mostrarTabla(dicc)
    else:
        print(funciones.colorear("...¡No hay palabras a mostrar!...", funciones.COLOR_AMARILLO))
    funciones.espereTecla()


def buscarPalabras(conexionBD):
    funciones.imprimirEncabezado("🔍 BUSCAR PALABRAS")
    palabra = funciones.leerTexto("Escribir la palabra a buscar: ")
    dicc = funciones.buscar(palabra, conexionBD)
    if len(dicc) > 0:
        funciones.mostrarTabla(dicc)
    else:
        print(funciones.colorear("...¡No se encontraron palabras!...", funciones.COLOR_AMARILLO))
    funciones.espereTecla()


def borrarPalabras(conexionBD):
    funciones.imprimirEncabezado("🗑️  BORRAR PALABRAS")
    palabra = funciones.leerTexto("Escribir la palabra a borrar: ")
    dicc = funciones.buscar(palabra, conexionBD)
    if len(dicc) == 0:
        input(funciones.colorear("...¡No se encontraron palabras a borrar!...", funciones.COLOR_AMARILLO))
        return
    funciones.mostrarTabla(dicc)
    if funciones.confirmar("¿Estás seguro que deseas borrar la(s) palabra(s)? (SI/NO)   "):
        respuesta = funciones.borrar(palabra, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()


def modificarPalabras(conexionBD):
    funciones.imprimirEncabezado("✏️  MODIFICAR PALABRAS")
    palabra_actual = funciones.leerTexto("Escribir la palabra a modificar: ")
    dicc = funciones.buscar(palabra_actual, conexionBD)
    if len(dicc) == 0:
        input(funciones.colorear("...¡No se encontraron palabras a modificar!...", funciones.COLOR_AMARILLO))
        return
    funciones.mostrarTabla(dicc)
    if funciones.confirmar("¿Deseas modificar la(s) palabra(s)? (SI/NO) "):
        palabra = funciones.leerTexto("Introducir la nueva palabra: ")
        traduccion = funciones.leerTexto("Introducir la nueva traducción: ")
        significado = funciones.leerTexto("Introducir el nuevo significado: ", permitir_puntuacion=True)
        respuesta = funciones.actualizar(palabra_actual, palabra, traduccion, significado, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()


def limpiarPalabras(conexionBD):
    funciones.imprimirEncabezado("🧹 LIMPIAR DICCIONARIO")
    dicc = funciones.consultar(conexionBD)
    if len(dicc) == 0:
        input(funciones.colorear("...¡No hay palabras a borrar!...", funciones.COLOR_AMARILLO))
        return
    if funciones.confirmar("¿Estás seguro que deseas borrar TODAS las palabras del diccionario? (SI/NO) "):
        respuesta = funciones.vaciar(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()


def exportarPalabras(conexionBD):
    funciones.imprimirEncabezado("📤 EXPORTAR DICCIONARIO")
    ruta = funciones.exportarArchivo(conexionBD)
    if ruta:
        print(funciones.colorear("\t✅ ¡Archivo generado con éxito!...", funciones.COLOR_VERDE))
        print(funciones.colorear(f"\t📁 Ubicación: {ruta}", funciones.COLOR_CIAN))
        funciones.espereTecla()
    else:
        funciones.accionNoExitosa()


def mostrarEstadisticas(conexionBD):
    funciones.imprimirEncabezado("📊 ESTADÍSTICAS DEL DICCIONARIO")
    resultado = funciones.estadisticas(conexionBD)
    if resultado is None:
        input(funciones.colorear("...¡No hay palabras para generar estadísticas!...", funciones.COLOR_AMARILLO))
        return
    print(f"\tTotal de palabras: {resultado['total']}")
    print(f"\tSuma de longitudes: {resultado['suma_longitudes']}")
    print(f"\tPromedio de longitud: {resultado['promedio']:.2f}")
    print(f"\tPalabra más larga: {resultado['mas_larga']} letras")
    print(f"\tPalabra más corta: {resultado['mas_corta']} letras")
    print("\n\tPalabras por letra inicial:")
    for letra in sorted(resultado["letras_iniciales"]):
        cantidad = resultado["letras_iniciales"][letra]
        porcentaje = (cantidad / resultado["total"]) * 100
        print(f"\t{letra}: {cantidad} palabra(s) ({porcentaje:.1f}%)")
    funciones.espereTecla()


def estudiarPalabras(conexionBD):
    funciones.imprimirEncabezado("📚 REPASAR / ESTUDIAR")
    palabras = funciones.obtenerPalabrasParaEstudiar(conexionBD)
    total = len(palabras)
    if total == 0:
        input(funciones.colorear("...¡No hay palabras agregadas para repasar!...", funciones.COLOR_AMARILLO))
        return

    aciertos = 0
    for indice, fila in enumerate(palabras):
        palabra_correcta = fila[1]
        traduccion = fila[2]

        funciones.borrarPantalla()
        print(funciones.colorear(f"\n\t\t...::: REPASO ({indice + 1}/{total}) :::...", funciones.COLOR_CIAN))
        print("\n" * 3)
        texto_centrado = traduccion.center(funciones.ANCHO_PANTALLA)
        print(funciones.colorear(texto_centrado, funciones.COLOR_AMARILLO + funciones.COLOR_NEGRITA))
        print("\n" * 3)

        respuesta = input("Escribe la palabra en inglés: ").strip().upper()
        if respuesta == palabra_correcta.upper():
            print(funciones.colorear("\n\t✅ ¡Correcto!...", funciones.COLOR_VERDE))
            aciertos = aciertos + 1
        else:
            print(funciones.colorear(
                f"\n\t❌ ¡Incorrecto! La palabra correcta era: {palabra_correcta}...", funciones.COLOR_ROJO
            ))
        funciones.espereTecla()

    porcentaje, mensaje = funciones.calificarEstudio(aciertos, total)
    funciones.borrarPantalla()
    funciones.imprimirEncabezado("🎯 RESULTADO DEL REPASO")
    print(f"\tAciertos: {aciertos} de {total}")
    print(f"\tPorcentaje: {porcentaje:.1f}%")

    if mensaje == "Excelente":
        color_resultado, emoji_resultado = funciones.COLOR_VERDE, "🏆"
    elif mensaje == "Bien hecho":
        color_resultado, emoji_resultado = funciones.COLOR_AMARILLO, "👍"
    else:
        color_resultado, emoji_resultado = funciones.COLOR_ROJO, "💪"

    print(funciones.colorear(
        f"\n\t{emoji_resultado} ¡{mensaje}! {emoji_resultado}\n", color_resultado + funciones.COLOR_NEGRITA
    ))
    funciones.espereTecla()


def menuDiccionario():
    conexionBD = funciones.conectar()
    opc = ""
    while opc != "10":
        funciones.borrarPantalla()
        opc = menuPrincipal()

        match opc:
            case "1":
                funciones.borrarPantalla()
                agregarPalabras(conexionBD)
            case "2":
                funciones.borrarPantalla()
                borrarPalabras(conexionBD)
            case "3":
                funciones.borrarPantalla()
                modificarPalabras(conexionBD)
            case "4":
                funciones.borrarPantalla()
                mostrarPalabras(conexionBD)
            case "5":
                funciones.borrarPantalla()
                buscarPalabras(conexionBD)
            case "6":
                funciones.borrarPantalla()
                limpiarPalabras(conexionBD)
            case "7":
                funciones.borrarPantalla()
                mostrarEstadisticas(conexionBD)
            case "8":
                funciones.borrarPantalla()
                exportarPalabras(conexionBD)
            case "9":
                funciones.borrarPantalla()
                estudiarPalabras(conexionBD)
            case "10":
                funciones.borrarPantalla()
            case _:
                funciones.opcionInvalida()
