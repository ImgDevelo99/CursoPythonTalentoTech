"""
len :me cuenta la cantidad de caracteres en una cadena
funciones: es un bloque de codigo diseñada para realizar tareas especificas en la cual se puede invocar(llamar)
desde cualquier parte del programa. nos permite origanizar el codigo por ploques mas pequeños y reutilizable.
para que sirve: 
-codigo reutilizable: evita la repeticion de codigo.
-modular: nos permite dividir un problema grande en tareas mas pequeñas.
-abstraccion: esconder los detalles de implementacion yen focarse en las tareas que realiza la funcion.

"""
#sintaxis de la funcion
def nombreFuncion(parametros):
    return valorRetorno #cuerpo

"""
def: la palabra cñave en py que me indica q estoy definiendo una funcion.
nombreFuncion : identifiador que se utiliza para llamar la funcion.
parametros : opcional. lista de variables que la funcion puede recibir como entrada.
return : opcional, palabra clave indica que valor devueve la funcion

"""
# #sin parametros
# def saludar() :
#     print("Hola, Bienvenidos a la funcion en py") 

# saludar() ##invoco la funcion
# #------------------------------------------------------------------------
# def texto(nombre) :
#     print(f"hola {nombre}, usted esta aprendiendo py")

# texto("juan")
# texto("maria") 
# texto("carlos") 
# texto("doris") 
# texto("pablo")  

#-------------------------------------------------------------
# def sumar(num1, num2) :
#     resultado =  num1 + num2
#     return resultado

# total= sumar(5,7)
# print(total)

#-------------------------------------------------------------
# def saludar(nombre, saludo):
#     mensaje = {saludo}, {nombre}
#     return mensaje

# #llamar a la funcion utilizando argumentos
# resultado = saludar("carlos" , "hola")
# print(resultado)

#-------------------------------------------------------------

# from  datetime  import datetime

# def fechaActual():
#     fecha = datetime.now()
#     print(f"la fecha actual es: {fecha} ")

# fechaActual()    
# #------------------------------------------------------------

# def imprimirNumeros():
#     for i in range(1,11):
#         print(i)

# imprimirNumeros()    

# #-----------------------------------------------------------

# def areaTriangulo():
#     base = float(input("ingrese la base del triangulo: "))
#     altura = float(input("ingrese la altura del triangulo :"))

#     area = (base * altura) / 2
#     print("el area del triangulo es: ", area)

# areaTriangulo()    

# #-------------------------------------------------------------------------
# def calcularIMC ():
#     peso = float(input("ingrese su peso en kg: "))
#     altura = float(input("ingrese su altura en metros: "))
#     imc = peso / (altura ** 2)
#     return imc

# resultado = calcularIMC()
# print(resultado)

#------------------------------------------------------------------------------
"""
Ejemplo: Cálculo de descuento sobre un producto
En este ejercicio, la función pide al usuario el precio original de un producto, pero recibe el porcentaje
de descuento como parámetro. Luego, calcula el precio final con el descuento aplicado y lo devuelve.
"""
def calcularDesceunto(porcentaje):
    precio = float(input("ingrese el precio del producto: "))
    descuento = (precio * porcentaje) /100
    precioFinal = precio - descuento

    return precioFinal

precioDescuento = calcularDesceunto(10)
print("el precio final del producto con descuento es: ", precioDescuento)

precioDescuento = calcularDesceunto(20)
print("el precio final del producto con descuento es: ", precioDescuento)
#-------------------------------------------------------------------------------------
# 1. Ejercicio: Cálculo del tiempo total de un viaje
# En este ejercicio, la función solicita al usuario la distancia a recorrer, pero recibe la velocidad promedio como parámetro. 
# Luego, calcula el tiempo total del viaje y lo devuelve.

# 1. nunciado: Cálculo del salario neto de un empleado

# Escribe un programa que calcule el salario neto de un empleado. La función debe solicitar al usuario el salario bruto (antes de impuestos).
# La función también debe recibir como parámetro el porcentaje de impuestos que se le debe aplicar. Luego, debe devolver el salario neto 
# después de deducir los impuestos.

# Requisitos:
# Solicitar al usuario el salario bruto (antes de impuestos).
# La función debe recibir como parámetro el porcentaje de impuestos.
# Calcular el salario neto restando los impuestos al salario bruto.
# Devolver el salario neto y mostrarlo por pantalla.