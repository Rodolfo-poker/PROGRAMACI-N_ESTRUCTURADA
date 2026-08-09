"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""

print("\033c")

paises1 = ("México", "Canadá", "EUA")
paises2 = {"México", "Canadá", "EUA"}
paises3 = ["México", "Canadá", "EUA"]

paises3[1] = "Brazil"

print(paises1)
print(paises2)
print(paises3)


for i in paises1:
  print(i)

for i in paises2:
  print(i)

paises1 = ("México", "Canadá", "EUA")
varios = ("Hola",True,33,3.1416)

print(paises1)
print(varios)

for i in varios:
  print(i)

for i in range(0,len(paises1)):
  print(paises1[i])

i = 0

while i < len(paises1):
  print(paises1[i])
  i += 1

print(f"El pais que inagura la Copa del Mundo 2026 es: ")
print(paises1[0])

edades = (23,24,18,20,20,23,24,19,24)

cuantos = edades.count(24)
print(cuantos)

for i in range(0,len(edades)):
  num = int(input("Dame el número a buscar: ").strip())
  posicion = edades.index(num)
  print(f"El número {num} se encontró en la posición: {posicion}")

#Utilizando Lista:

num = int(input("Dame el número a buscar: ").strip())
posiciones = []

for i in range(0,len(edades)):
  if edades [i]==num:
    posiciones.append(i)

for i in posiciones:
  print(f"El número {num} se encontró en la posición {i}")

#Utilizando Tupla:

num = int(input("Dame el número a buscar: ").strip())
posiciones = []

for i in range(0,len(edades)):
  if edades [i]==num:
    posiciones.append(i)

posiciones_tupla = tuple(posiciones)

for i in posiciones_tupla:
  print(f"El número {num} se encontró en la posición {i}")

#Utilizando Set:

num = int(input("Dame el número a buscar: ").strip())
posiciones = {""}
posiciones.clear()

for i in range(0,len(edades)):
  if edades [i]==num:
    posiciones.add(i)

posiciones_tupla = tuple(posiciones)

for i in posiciones_tupla:
  print(f"El número {num} se encontró en la posición {i}")
