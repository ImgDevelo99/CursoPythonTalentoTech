"""
#Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra 
# por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que 
# saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
# pedido y calcule el peso total del paquete que será enviado.
# """
# pesoPayaso = 112
# pesomuneca = 75

# numPayasos = int(input("ingrese el numero de payasos"))
# numMuneca = int(input("ingrese el numero de muñecas"))

# print(f"el peso final del pauqete es:{(pesoPayaso * numPayasos) + (pesomuneca * numMuneca)} g ")

#---------------------------------------------------------------------------------------------------

# //Un estacionamiento requiere determinar el cobro 
# 	//que debe aplicar a las personas que lo utilizan. 
# 	//Considere que el cobro es con base en las horas 
# 	//que lo disponen y que las fracciones de hora se 
# 	//toman como completas. realice el
# 	//código py que representen el algoritmo
# 	//que permita determinar el cobro.

# import math

# tarifaHora = 1000

# horas = float(input("ingrese el numero de horas que utilizo en el parqueadero: "))

# costoTotal = math.ceil(horas)

# totaaPagar = costoTotal * tarifaHora

# print("el valor total a pagar es", totaaPagar)

#------------------------------------------------------------------------------------------
"""
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero
#  depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular
#  y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
#  cada cantidad a dos decimales.
"""
# tasa_interes = 0.04

# depositoInicial = float(input("Ingrese la cantidad de dinero a depositar: "))

# ahorroPrimerAño = round(depositoInicial * ( 1 +tasa_interes),2) # completar y tarea
# ahorroSegundoAño = ahorroPrimerAño * (1 + tasa_interes)
# ahorroTercerAño = ahorroSegundoAño * (1 + tasa_interes)

# print(f"ahorro total del primer año: {ahorroPrimerAño}")
# print(f"ahorro total del segundo año: {ahorroSegundoAño:.2f} ")
# print(f"ahorro total del tercer año: {ahorroTercerAño:.2f} ")

#--------------------------------------------------------------------------------------------
"""
solicitar dos datos al usuario y calcular el area de rectangulo, triangulo, poligono regular
formula del poligono regular es: a = perimetro * apotema / 2
"""
dato1 = float(input("ingrese el primer valor(base o lado)"))
dato2 = float(input("ingrese el segundo valor(altura o apotema)"))
#numLados = float(input("ingrese el numero de lados (para el poligono)"))

areaRectangulo = dato1 * dato2
areaTriangulo = (dato1 * dato2)/2
areaPoligono = (dato1 * dato2)/2

print(areaRectangulo)
print(areaTriangulo)
print(areaPoligono)






