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
# def calcularDesceunto(porcentaje):
#     precio = float(input("ingrese el precio del producto: "))
#     descuento = (precio * porcentaje) /100
#     precioFinal = precio - descuento

#     return precioFinal

# precioDescuento = calcularDesceunto(10)
# print("el precio final del producto con descuento es: ", precioDescuento)

# precioDescuento = calcularDesceunto(20)
# print("el precio final del producto con descuento es: ", precioDescuento)
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

# def calcularSalario(porcentajeImpuestos):
#     salarioBruto = float(input("Ingrese su salario bruto :"))
#     impuestos = (salarioBruto * porcentajeImpuestos) / 100
#     salarioNeto = salarioBruto -impuestos
#     return salarioNeto

# salarioNeto = calcularSalario(10)
# print(salarioNeto)
#------------------------------------------------------------------------------------------------------
# Enunciado: Cálculo del costo total de una compra con múltiples productos y descuentos
# Escribe un programa que calcule el costo total de una compra con varios productos. 
# El programa debe solicitar al usuario la cantidad de productos a comprar, y por cada producto,
# debe pedir el precio y la cantidad. Además, la función debe recibir como parámetro un porcentaje 
# de descuento que se aplicará al total de la compra si el usuario supera una cantidad mínima (por ejemplo, 1000 unidades monetarias). 
# El programa debe devolver el costo total después del descuento (si corresponde).

# Requisitos:
# Solicitar al usuario la cantidad de productos que va a comprar.
# Para cada producto, solicitar el precio y la cantidad.
# Recibir como parámetro el porcentaje de descuento y el monto mínimo para aplicar el descuento.
# Calcular el costo total de la compra antes y después del descuento.
# Si el costo total es mayor o igual al monto mínimo, aplicar el descuento y devolver el costo final.

#-----------------------------------------------------------------------------------------------------------

# Enunciado: Cálculo del salario neto de empleados con bonificaciones y deducciones
# Escribe un programa que calcule el salario neto de un grupo de empleados. El programa debe recibir el número de empleados como argumento y,
# para cada empleado, solicitar el salario bruto, el porcentaje de bonificación, y el porcentaje de deducción. 
# La función debe recibir estos datos como parámetros, calcular el salario neto y devolver una lista con los
# salarios netos de todos los empleados.

# Requisitos:
# El programa debe recibir el número de empleados como argumento.
# Para cada empleado, solicitar el salario bruto, el porcentaje de bonificación, y el porcentaje de deducción.
# Calcular el salario neto aplicando las bonificaciones y deducciones al salario bruto.
# Devolver una lista con los salarios netos de todos los empleados.
# Mostrar el salario neto de cada empleado en pantalla.

#-----------------------------------------------------------------------------------------------------------
# Enunciado: Gestión de inventario de una tienda
# Escribe un programa que gestione el inventario de una tienda. La función principal debe permitir agregar nuevos productos al inventario,
# actualizar la cantidad de un producto existente, y calcular el valor total del inventario. 
# La función de cálculo de valor total se debe reutilizar en varias partes del programa, como después de agregar o actualizar un producto.

# Requisitos:
# Crear una función para agregar nuevos productos al inventario.
# Crear una función para actualizar la cantidad de un producto existente.
# Crear una función para calcular el valor total del inventario (reutilizada en otras partes del programa).
# El programa debe permitir agregar o actualizar productos varias veces, y mostrar el valor total del inventario después de cada acción.

# funcion agregar productos-----
def agregarProductos(inventario, nombreProducto, cantidad, precio):
    if nombreProducto not in inventario:
        inventario[nombreProducto] = {"cantidad": cantidad, "precio": precio  }
        print(f"producto agregado: {nombreProducto}")
    else:
        print(f"el producto {nombreProducto} ya existe en el inventario")
    return inventario

#funcion  actualizar cantidad de productos------
def actualizarProducto(inventario, nombreProducto, nuevaCantidad):
    if nombreProducto in inventario:
        inventario[nombreProducto]["cantidad"] = nuevaCantidad
        print(f"el producto {nombreProducto} fue actualizado")
    else:
        print(f"el producto {nombreProducto} no esta en el inventario")
    return inventario

#funcion calcular total inventario
def calcularInventario(inventario):
    valorTotal = 0
    for producto, detalle  in inventario.items():
        valorTotal += detalle["cantidad"] * detalle["precio"]
    return valorTotal

#iniciamos el inventario vacio
inventario = {}

# #agregar producto
# inventario = agregarProductos(inventario, "portatil", 5 , 100000 )
# valorInventario = calcularInventario(inventario)
# print(f"el valor total del inventario es: {valorInventario}\n")

# inventario = agregarProductos(inventario, "celular", 15 , 150000 )
# valorInventario = calcularInventario(inventario)
# print(f"el valor total del inventario es: {valorInventario}\n")

# inventario = agregarProductos(inventario, "monitor", 50 , 550000 )
# valorInventario = calcularInventario(inventario)
# print(f"el valor total del inventario es: {valorInventario}\n")

# #Editar  la cantidad
# inventario = actualizarProducto(inventario, "portatil", 100 )
# valorInventario = calcularInventario(inventario)
# print(f"el valor total del inventario es: {valorInventario}\n")

while True:

    print("opciones: ")
    print("1. agregar un producto: ")
    print("2. aeditar un producto existente: ")
    print("3. exit ")

    opcion = input("seleccione una opcion")

    if opcion == "3":
        break 

    nombreProducto = input("ingrese el nombre del producto o ( exit para terminar ):")

    if opcion == "1":

        
        precio = float(input(f"introduzca el precio unitario de {nombreProducto}: "))

        inventario = agregarProductos(inventario, nombreProducto, cantidad, precio)
        
    elif opcion  == "2":

        if nombreProducto in inventario :
            nuevaCantidad = int(input(f"ingrese la nueva cantidad del producto {nombreProducto}"))
    
            inventario = actualizarProducto(inventario, nombreProducto, nuevaCantidad)
        else:
            print(f"el producto {nombreProducto} no existe")

    else:
        print("opcion no valida, porfavor verifique")

    
    valorInventario = calcularInventario(inventario)
    print(f"el valor total del inventario es: {valorInventario}\n")

print("fin del programa")    

