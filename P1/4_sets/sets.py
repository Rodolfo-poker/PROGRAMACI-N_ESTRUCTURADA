"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

set1 = {"hola","123","123","Mexico","Holanda",123,3.1416}
print(set1)

set1.add("Ganador")
print(set1)

set1.pop()
print(set1)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
correos_alumnos = []
continuar = "SI"

while continuar == "SI":
  correos_alumnos.append(input("Ingrese un email: ").lower().strip())
  continuar = input("¿Desea agregar otro correo?(SI/NO)").upper().strip()

print(f"Lista original: {correos_alumnos}")

correos_alumnos_sin_duplicados = []
for correo in correos_alumnos:
  if correo not in correos_alumnos_sin_duplicados:
    correos_alumnos_sin_duplicados.append(correo)

print(f"Lista sin duplicados: {correos_alumnos_sin_duplicados}")

#Solucion 2
correos_alumnos = []
continuar = "SI"

while continuar == "SI":
  correos_alumnos.append(input("Ingrese un email: ").lower().strip())
  continuar = input("¿Desea agregar otro correo?(SI/NO)").upper().strip()

print(f"Lista original: {correos_alumnos}")

correos_alumnos_sin_duplicados_set = list(set(correos_alumnos))

print(f"Lista sin duplicados: {correos_alumnos_sin_duplicados_set}")