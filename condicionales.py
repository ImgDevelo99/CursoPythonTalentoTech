"""
if(condicion):
    ejecutese el bloque de codigo
else:
    ejecutese otro bloque de codigo  
    > mayor que    12 > 3 True  
"""
# num1 = 880
# num2 = 88
# if num1 >= num2 :
#     print("es mayor TRUE")
# else:
#     print("no es mayor FALSE")

#-------------------------------------------------    
"""
crearun programa para indicarle al usuario si es mayor de edad podra conducir, soliciar por
consola la edad
"""
# edad = int(input("ingrse su edad para saber si puede conducir"))
# nacionalidad = True

# if edad >= 18 or nacionalidad == True:
#     print("si puede conducir")
# else:
#     print("no puede conducir") 

# print("Felicitaciones")
#------------------------------------------------------------------------
"""
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
# password = "Admin123*"

# passInput = input("Ingrese su contraseña: ")

# if password.lower() == passInput.lower():
#     print("contraseña correcta Bienvenido! ")
# else:
#     print("contraseña incorrecta por favor verifique!") 

#-----------------------------------------------------------------------------
# //Elaborar un algoritmo que permita ingresar el 
# 	//nombre del trabajador, su sueldo básico y el 
# 	//número de hijos, se deberá mostrar su 
# 	//bonificación y el sueldo final. Tenga en cuenta 
# 	//que la empresa está dando una bonificación 
# 	//del 7% del sueldo básico sólo en el caso el 
# 	//trabajador tuviese hijos

# nombre = input("ingrese el nombre del trabajador: ")
# sueldoBasico = float(input("el sueldo del trabajador: "))
# numeroHijos = int(input("Ingre el numero de hijos: "))

# if numeroHijos > 0:
#     bonificacion = sueldoBasico * 0.07
# else:
#     bonificacion = 0
#     print("---------no tiene bonificacion--------------")
    
# sueldoFinal = sueldoBasico + bonificacion

# print("nombre del trabajador: ",nombre)
# print("su sueldo basico es: ",sueldoBasico)
# print("su bonificacion es: ",bonificacion )
# print("su sueldo final con bonificacion es: ",sueldoFinal)

#-----------------------------------------------------------------
# //La entrada a un circo vale  x pesos por persona, 
# 	//sin embargo, si la edad de la persona es menor 
# 	//de 10 años se le da un descuento del 25% en el 
# 	//valor del boleto. Escribir el código que 
# 	//calcule y muestre lo que pagará por la entrada 
# 	//al circo según la edad.

# precioBoleto = float(input("Ingrese el valor del boleto por persona: "))
# edad = int(input("ingrese la edad de la persona: "))

# if edad < 10:
#     descuento = precioBoleto * 0.25
#     print(f"el precio a pagar de su boleto con descuento del 25% es: { precioBoleto - descuento} pesos")   
# else:
#     print("No tiene descuento, valor a pagar: ",precioBoleto)

#------------------------------------------------------------------------
# //Digite el nombre del cliente y su importe de 
# 	//compra, en caso que su importe sea 150 o más, 
# 	//se le descontará el 12%. Mostrar el descuento 
# 	//otorgado y el importe de compra final.

#----------condicional anidado---------------------------------------------------------

#escribir u programa donde al usuario ingrese la calificacion de 0 a 10, el programa debe clasificar
#calificacion :
#mayor o igual a 9 = excelente
#7 y 8.9 = notable
#5 y 6.9 = aprobado
#menos de 4.9 =insuficiente

calificacion = float(input("Ingrese su calificacion entre 0 y 10 : "))

if calificacion >= 9:
    print("Felicitaciones  su nota es Excelente")
elif calificacion >=7:
    print("Su nota es notable")
elif calificacion >= 5:
    print("su calificacion es Aprobado")    
else:
    print("Su calificacion es insuficiente")    

#------------------------------------------------------------
#solicitarle al usuario que ingrese un numero del 1 al 7, e indicar que dia de la semana es
