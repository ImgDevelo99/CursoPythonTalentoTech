"""
el uso del WHILE nos permite ejecutar un seccion de codigo repetidas veces MIENTRAS la condicion
se cumpla TRUE
"""
# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1 #contador = contador + 1

# print("fin del bucle")

#-----------------------------------------------------------------------------
# contador = 1
# while contador <= 100:
#     contador += 1
#     print(contador)
#     if contador == 50:
#         break

# print("fin")

#------------------------------------------------------------------------------
#Escribe un programa en Python que use un bucle while para sumar números ingresados por el usuario hasta
#  que se ingrese un número negativo. Luego, muestra la suma total.
# suma = 0
# while True:
#     numero = int(input("ingrese un numero( si quiere salir del programa ingrese un numero negativo): "))
#     if numero < 0:
#         break
#     suma += numero
#     print("la suma total es: ", suma)

# print("usted ingreso un numero negativo fin del programa, total de la suma: ",suma)   
#-------------------------------------------------------------------------------------------------------
#TAREA: Escribe un programa en Python que utilice un bucle while para encontrar y
#  mostrar el primer número divisible por 7 en el rango del 1 al 100.  solicitarle el unmero al usuario

# rango = int(input("ingrese el numero maximo del rango: "))

# numero = 1

# while numero <= rango:
#     if numero % 7 == 0:
#         print("El  primer numero divisible por 7 en el rango es: ",numero)
#         break
#     numero += 1
# else:
#     print("no se encontro ningun numero divisible por 7 en el rango de 1 a ",rango)    

#--------------------------------------------------------------------------------------------
# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.

# notaMayor = 0
# notaMenor = 0
# i = 1

# while i <= 10 :
#     nota = float(input(f"ingrese la nota {i} :"))
#     if nota >= 7 :
#         notaMayor += 1
#     else :
#         notaMenor += 1  
#     i += 1
    
# print(" cantidad de notas del estudiante mayor a 7 son: ",notaMayor)
# print(" cantidad de notas del estudiante menores a 7 son: ",notaMenor)

#----------------------------------------------------------------
#crear un programa donde cuente de forma desendentes 10 segundos para que explote una bomba

# segundos = 10

# while 10 > 0 :
#     print(f"la bomba explotara en {segundos}, segundos ")
#     segundos -= 1

# print("¡¡¡¡¡¡¡¡¡¡¡¡!BOMMMMMMMMMM!!!!!!!!!")    


#CONCATENAR
# num1 =" hola a todos"
# num2 = "bienvenidos a python "

# print(f"las dos variables que tengo en este momento son {num1}, {num2}")
# print(num1, num2)

#------------------------------------------------------------------------
# Árbol de navidad en Python. Imprime un árbol de navidad formado con * haciendo uso del while
# y de la multiplicación deun entero por una cadena, cuyo resultado en Python es replicar la cadena.
# z = 7
# y = 1

# while z  > 0 :
#     print(" "* z + "*" * y + "" * z )
#     y +=2
#     z -=1

# print("      "  "**" )
# print("      "  "**" )
# print("      "  "**" )
