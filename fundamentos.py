#print("bienvenidos a python")
# en esta liena hay una cadena de caracteres q es igual a un string

#print("hola mundo")

"""
me sirve para
comentar 
varias lines 
al mismo tiempo
"""
#print("mostrar en pantalla")
#para limpiar la consola utilizo cls

#----------------TIPOS DE DATOS-------------
# print(type("es un tipo de dato string")) #tipo de dato str
# print(type(56)) #tipo de dato entero int
# print(type(3.14))# tipo de dato decimal float
# print(type(True))# tipo de dato boolenao bool
# print(type('y'))

#para comentar muchas lineas utilizo las teclas CTRL K C y para descomentar muchas lineas utilizo CTRL K U

#--------------Variables---------------------
# texto = "hola mundo"
# print(texto)
# texto = "bienvenidoa a py"
# print(texto)

# numero = "hola a todos"
# print(numero)
# saludo = "hola a todos"
# edad = 20
# precio = 35.600
# pregunta = True
#----------errores al declarar las variables----------
# bool = "verdad" #no essta bien
# 2edad = 33 
# $edad = 20
# mi variable # no dejar espacios
# def = 34543

#--- variables correctamente----------

# saludo = "    HOLA mundo"
# precioUnitario = 234.334
# miEdad = 33
# valor_unitario = 44.55
# mi_edad = 20

# cantidadCaracter = len(saludo)#len devuelve la longitud de la cadena(numero de caracteres)

# print(saludo)
# print(cantidadCaracter)

# saludoMayuscula = saludo.upper()#upper me convierte le texto en MAYUSCULA
# print(saludoMayuscula)

# saludoMinuscula = saludo.lower()# para convertir el texto en minuscula
# print(saludoMinuscula)

# capitalized = saludo.capitalize()# convertir la primera latra del texto en mayuscula
# print(capitalized)

# titulo = saludo.title()# convierte el primer caracter de cada palabra en mayuscula
# print(titulo)

# nuevoTexto = saludo.replace("mundo", "pyton")#remplazar texto de la variable por otro
# print(nuevoTexto)
# print(saludo)

# eliminaEspacios = saludo.strip()# elimina los espacios en balnco al principio
# print(eliminaEspacios)

#---------------------------------Metodos para int-------------------------------------------------------------

# num = -10
# print(num)
# valorDevuelto =  abs(num) #devolver el mismo valor pero positivo
# print(valorDevuelto)

# precio = 3.4
# redondeado = round(precio)# nos aproxima el valor de la variable
# print(redondeado)


#--------------------------------metodos para float-----------------------------------------------------------
# import math

# calcularRaiz = math.sqrt(1654)
# print(calcularRaiz)

# maximo = max(2,4.5,1.2,56,1,90)
# minimo = min(2,4.5,1.2,56,1,90)
# print("el numero mayor es: ", maximo)
# print("el numero menor de la variable:" , minimo)

# num1 = 10
# num2 = 20
# num3 = 50

# total = num1 + num2 + num3
# print("la suma de los 3 numeros es: ", total )

# palabra1 = "hola"
# palabra2 = "mundo"
# palabra3 = "python"

# frase = palabra1 + " " + palabra2 + " " +palabra3
# print(frase)

# nombre = "Diego"
# ciudad = "Medellin"
# telefono = "224234"

# print(f"hola mi nombre es: {nombre}\n y vivo en la ciudad de: {ciudad}\n y mi numero telefonico es: {telefono} ")
# # print("hola mi nombre es:", nombre , "vivo en la ciudad de: ", ciudad , "y mi telefono es: ",telefono)


# #---------------------------impor fecha---------------------------------------------------------------
#import datetime

# fechaActual = datetime.datetime.now()#imprimir fecha actual
# print(fechaActual)

# formatoFecha = fechaActual.strftime("%d/%m/%Y %H:%M:%S")# me permite dar formato
# print("la fecha y la hora actual con formato: ",formatoFecha)

#------------------------------impor random-------------------------------------------------------
# import random
# numeroAleatorio = random.randint(1,100)

# print("el numero aleatorio generado por el sistema es:", numeroAleatorio)