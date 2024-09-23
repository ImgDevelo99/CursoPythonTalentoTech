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
suma = 0
while True:
    numero = int(input("ingrese un numero( si quiere salir del programa ingrese un numero negativo): "))
    if numero < 0:
        break
    suma += numero
    print("la suma total es: ", suma)

print("usted ingreso un numero negativo fin del programa, total de la suma: ",suma)   
#-------------------------------------------------------------------------------------------------------
#TAREA: Escribe un programa en Python que utilice un bucle while para encontrar y
#  mostrar el primer número divisible por 7 en el rango del 1 al 100.  solicitarle el unmero al usuario
