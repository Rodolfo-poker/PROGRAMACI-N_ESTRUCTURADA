def borrarPantalla():
    print("\033c")

def ventaAutos(continuar,autos,acum_pv):
    #Entrada
    borrarPantalla()
    while continuar == "SI":
        marca = input("Marca: ").strip().upper()
        origen = input("Origen: ").strip().upper()
        costo = float(input("Costo: "))

        #Proceso
        impuesto = 0
        if origen=="ALEMANIA":
           impuesto = 0.2
        elif origen == "JAPON":
           impuesto = 0.3
        elif origen == "ITALIA":
            impuesto = 0.15
        elif origen == "USA":
            impuesto = 0.08
    
        impuesto_pesos = costo * impuesto
        pv = impuesto_pesos + costo
        acum_pv += pv
        autos+= 1
    
        #Salida
        print (f"El impuesto pagar es: ${impuesto_pesos}")
        print (f"El precio de venta es: ${pv}")

        continuar = input("¿Desea continuar? Si/No").upper().strip()
    return autos,acum_pv

ACUM_PV = 0
AUTOS = 0
CONTINUAR = "SI"
    
autos,acum_pv=ventaAutos(CONTINUAR,AUTOS,ACUM_PV)

print (f"El total de los vehículos ingresados es: {autos} \n Y el monto total de los precios de venta es: ${acum_pv}")