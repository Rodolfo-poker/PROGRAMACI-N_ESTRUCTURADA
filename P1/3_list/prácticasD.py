#continuar = "SI"
#conta = 0
#acum_rendi = 0
#prom_rendi = 0

#def calcuRendi(kilo_reco,lit_cons):
#	rendimiento = kilo_reco / lit_cons
#	return rendimiento

#while continuar == "SI":
#	kilo_reco = float(input("Ingrese los kilómetros recorridos: "))
#	lit_cons = float(input("Ingrese los litros consumidos: "))
#	rendimiento = calcuRendi(kilo_reco,lit_cons)
#	acum_rendi += rendimiento
#	conta += 1
#	print(f"Rendimiento: {rendimiento}")
#	continuar = input("¿Desea realizar otra vez el proceso? SI/NO").upper().strip()

#prom_rendi = acum_rendi / conta
#print(f"El promedio es: {prom_rendi}")

#continuar = "SI"
#conta = 0
#acum_dol = 0
#prom = 0

#def conveDol(dolares,tipo_cambio):
#	pesos = dolares * tipo_cambio
#	return pesos

#while continuar == "SI":
#	dolares = float(input("¿Cuántos dólares son en total?"))
#	tipo_cambio = float(input("¿A cuánto está el dólar actualmente?"))
#	pesos = conveDol(dolares,tipo_cambio)
#	acum_dol += pesos
#	conta += 1
#	print(f"Total en pesos: {pesos}")
#	continuar = input("¿Desea realizar nuevamente el proceso?").upper().strip()

#prom = acum_dol / conta
#print(f"Promedio: {prom}")

registro_temperaturas = [68.5, 76.2, 72.1, 79.8, 81.0, 74.5, 77.3, 70.0]
acum_reg_tem = 0
conta = 0

def evaluar_temperatura(temp):
    return temp > 75 

for temp in registro_temperaturas:
    if evaluar_temperatura(temp):
        acum_reg_tem += temp
        conta += 1

if conta > 0:
    prom_reg_tem = acum_reg_tem / conta
    print(f"Promedio de temperaturas críticas: {prom_reg_tem:.2f}°C")
else:
    print("No hubo alertas críticas.")