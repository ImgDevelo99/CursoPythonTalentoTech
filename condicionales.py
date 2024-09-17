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

edad = int(input("ingrse su edad para saber si puede conducir"))
nacionalidad = True

if edad >= 18 or nacionalidad == True:
    print("si puede conducir")
else:
    print("no puede conducir") 

print("Felicitaciones")


#------------------------------------------------------------------------
"""
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
