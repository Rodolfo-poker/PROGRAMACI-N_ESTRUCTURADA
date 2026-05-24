'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

#print("\033c")

#num_tabla = int(input("Ingrese un número para mostrar en pantalla la tabla de multiplicar: "))

#num = 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

#multi = num_tabla * num
#print(f"{num_tabla} X {num} = {multi}")
#num += 1

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control con for con decrementos de 10
  2.- Sin funciones

'''

#print("\033c")

#num_tabla = int(input("Ingrese un número para mostrar en pantalla la tabla de multiplicar: "))

#num = 1

#for bucle in range(100,0,-10):
    #multi = num_tabla * num
    #print(f"{num_tabla} X {num} = {multi}")
    #num +=1
    
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control con while con decrementos de 10
  2.- Sin funciones

'''

#print("\033c")

#num_tabla = int(input("Ingrese un número para mostrar en pantalla la tabla de multiplicar: "))

#num = 1
#bucle = 100

#while bucle > 0:
    #multi = num_tabla * num
    #print(f"{num_tabla} X {num} = {multi}")
    #num += 1
    #bucle -= 10

#PAL HACKATON

#for num in range(1,11):
    #multi = num_tabla * num
    #print(f"{num_tabla} X {num} = {multi}")

#num = 1
#while num <= 10:
    #multi = num_tabla * num
    #print(f"{num_tabla} X {num} = {multi}")
    #num += 1

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Con funciones

'''

print("\033c")

def tabla(num_tabla,n):
    mul = num_tabla * n
    print(f"{num_tabla} X {n} = {mul}")
    n += 1
    return n

num_tabla = int(input("Ingrese un número para mostrar la tabla de multiplicar: "))

num = 1

for i in range(1,11):
  num = tabla(num_tabla,num)