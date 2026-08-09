import peliculas

pelis = []

opc = ""

while opc != "7":
    peliculas.borrarPantalla()
    opc = peliculas.menuPrincipal()
    match opc:
        case "1":
            peliculas.borrarPantalla()
            peliculas.agregarPeliculas(pelis)
        case "2":
            peliculas.borrarPantalla()
            peliculas.borrarPeliculas(pelis)
        case "3":
            peliculas.borrarPantalla()
            peliculas.modificarPeliculas(pelis)
        case "4":
            peliculas.borrarPantalla()
            peliculas.mostrarPeliculas(pelis)
        case "5":
            peliculas.borrarPantalla()
            peliculas.buscarPeliculas(pelis)
        case "6":
            peliculas.borrarPantalla()
            peliculas.limpiarPeliculas()
        case "7":
            peliculas.borrarPantalla()
            peliculas.terminarSistema()
        case _:
            peliculas.opcionInvalida()
