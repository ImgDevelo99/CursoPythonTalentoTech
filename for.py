"""
el bucle for en py se utiliza para iterar sobre una secuencia ( listas, tuplas, diccionario, conjunto de cadena)
"""
# for variable in secuencia
#variable :tomara el valor de la cade na de elementos de la secuencia en cada iteracion
#secuencia :seciencia de elementos que se van a recorrer ( listas)

# for i in range(1,50):
#     print(i)

# nombres = ["ana", "maria", "carlos", "juan","diago"]
# for i in nombres:  
#     print(f"bienvenidos, {i}")  

# nombres = ["ana", "maria", "carlos", "juan","diago"]
# for i in nombres:
#     if i == "carlos":
#         print(f"bienvenidos, {i}")
#         break   

# numeros = [2,4,7,8,9]
# suma = 0
# for i in numeros:
#     suma += i
#     print(i)

# print(f"la suma total de los elementos es: {suma}")

# #-----------------------------------------------------------
# #encontrar los numeros pares de una lista
# numeros = [3,6,5,12,8,9,30,41,7]
# for i in numeros:
#     if i % 2 == 0:
#         print(f"{i} es par")
# #-----------------------------------------------------------
# # programa que me recorra una cadena de texto    
# cadena = "programacion en python A ó"
# vocales = "aeiouAEIOUó"   
# contador = 0

# for letra in cadena:
#     if letra in vocales:
#         contador += 1

# print(f"el numero de vocales en la cadena es: {contador}")

#-----------------------------------------------------------------------------
# numero = int(input("ingrese el numero de la tabla que quiere mostrar (tabla del 1 al 10): "))
# for i in range(1,11):
#     print(f"{numero} X {i} = {numero * i}")

#-------------------------------------------------------------------------
#escribir un programa en py que me muestre las tablas de multiplicar del 1 al 10
# for i in range(1,11):
#     for x in range(1,11):
#         print(f"{i} x {x} = {i * x}")
#         # print( i,"x", x, " = ",i * x   ) #forma de concatenar
#         # print(str(i), "x" , str(x), "=", str(i * x)) #otra forma de concatenar
#     print("-" * 30)    

#---------------------------------------------------
#escribir un programa que dibuje un triangulo con * solicitando al usuario la cantidad de filas

fila = int(input("ingrese el numero filas: "))
for i in range(1, fila, +1):
    for z in range(i):
        print("*", end= "")
    print()#crear una nueva linea    


