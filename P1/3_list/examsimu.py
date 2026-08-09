'''
continuar = "SI"
lista_imc = []

def calPromIMC(lista_imc):
    acum_imc = 0
    for i in lista_imc:
        acum_imc += i
    prom = acum_imc / len(lista_imc)
    return prom

def calIMC(peso,altura):
    imc = peso / (altura*altura)
    return imc

while continuar == "SI":   
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))
    imc = calIMC(peso,altura)
    lista_imc.append(imc)
    continuar = input("¿Desea agregar otro resultado?").upper().strip()

prom = calPromIMC(lista_imc)
lista_imc_set = set(lista_imc)
print(f"Promdeio: {prom} \n Conjunto de IMC: {lista_imc_set}")

continuar = "SI"
lista_tempe = []

def obtener_promedio(lista_tempe):
	acum_tempe = 0
	for i in lista_tempe:
		acum_tempe += i
	prom = acum_tempe / len(lista_tempe)
	return prom

while continuar == "SI":
	lista_tempe.append(float(input("Ingrese la Temperatura: ")))
	continuar = input("¿Desea agregar otra temperatura? SI/NO").upper().strip()

prom = obtener_promedio(lista_tempe)

print(f"La temperatura máxima es: {max(lista_tempe)} \n La temperatura mínima es: {min(lista_tempe)} \n El promedio es: {prom}")

lista_cualquiera = []

nombre = "Joaquín"
fichas = 500

jugador = (nombre,fichas)
lista_cualquiera.append(jugador)
print(lista_cualquiera)

for i in lista_cualquiera:
    for r in range(0,1):
        for c in range(0,2):
        	print(lista_cualquiera[r])
'''























continuar = "SI"
lista_areas = []

def calPromArea(lista_areas):
    prom = sum(lista_areas) / len(lista_areas)
    return prom

def calArea(r):
    area = 3.1416 * r * r
    return area

while continuar == "SI":
    radio = float(input("Ingrese el radio: ").strip())
    area = calArea(radio)
    lista_areas.append(area)
    print(f"El área del círculo es: {area:.2f}")
    continuar = input("¿Desea ingresar otro valor? (SI/NO)").strip().upper()

prom = calPromArea(lista_areas)
lista_areas.sort(reverse=True)
lista_areas = tuple(lista_areas)
print(f"El promedio de las áreas es: {prom:.2f} \n Tupla de las áreas: {lista_areas}")
