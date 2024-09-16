# nombre = input("ingrese su nombre para saludarlo: ")
# edad = int(input("ingrese su edad: "))

# print(f"Bienvenido {nombre}, estamos en el curso de python y su edad es: {edad}")

# num1 = float(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero numero: "))

# suma = num1 + num2
# print("la suma es: ",suma)

#crear un programa donde calcule las 3 notas ingresadas por el usuario y sacar el promedio
# nota1 = float(input("ingrese la primera nota: "))
# nota2 = float(input("ingrese la segunda nota: "))
# nota3 = float(input("ingrese la tercera nota: "))

# notaFinal = (nota1 + nota2 + nota3)/3

# print(f"el promedio de su calificacion segun las notas es: {notaFinal}")

#------------------------------------------------------------------
# lado = int(input("ingrese la medida del lado del cuadrado: "))

# area = lado * lado

# print("el area del cuadrado es: ",area)

"""
Escribe un programa en Python que convierta una temperatura 
dada en grados Celsius a grados Fahrenheit. La fórmula de conversión es: F = C * 9/5 + 32.
"""

# celsius = float(input("ingrese la temperatura en grados Celsius: "))

# fahrenheit = celsius * 9/5 + 32

# print("la temperatura en grados fahrenheit es: ", fahrenheit)

#-----------------------------------------------------------------------------
"""
scribe un programa en Python que tome una cadena de texto como entrada 
y la convierta en tres formatos diferentes: todo en mayúsculas, todo en minúsculas
y en formato título (donde cada palabra empieza con mayúscula).
"""
# texto = input("ingrese el mensaje")

# mayuscula = texto.upper()
# minuscula = texto.lower()
# titulo = texto.title()

# print(f"el texto en mayuscula es: {mayuscula},\nel texto en minuscula es: {minuscula},\n el texto en formmato titulo es: {titulo}")

#------------------------------------operadores aritmeticos----------------------------------------------------
"""
+  suma     12+3 = 15
-  resta    5-2  = 3
*  multip   2*5  = 10
/  div      10/2  = 5 
%  modulo   16%3  = 1
** potenciacion 12**3 = 1728
"""
#------------------------------------operadores relacionales----------------------------------------------------
"""
> mayor que    12 > 3 True
< menor que    12 < 3 False
== igualdad    12 == 3 False
>= mayor o igual que 12 >= 12 True
<= menor o igual que 12 <= 3  false
!= distinto     12 != 3 True
"""
#------------------------------------operadores logicos----------------------------------------------------
"""
and  devuelve true si ambos opereradores son true
or   devuelve true si alguno de los dos operadores es true
not  devuelve true si alguno de los dos operadores es false

v and v  = true
v or f   = true
f or v   = true
v not f  = true
f not v  = true

"""
# edad = 20
# ciudadanoColombiano = True

# puedeVotar =  edad != 18 and ciudadanoColombiano

# if puedeVotar:
#     print("TRUE")
# else:
#     print("FALSE")

# print(puedeVotar)

#---------------------------Operadores de asignacion-------------------------------------------------
"""
=           var = "hola"
+=          x+=2 =7                 x=x+2 =7    5=5+2 =7           // x = 5
-=          x-=2                    x=x-2
*=          x*=2                    x=x*2 
/=          x/=2                    x=x/2
%=          x%=2                    x=x%2
**=         x**2                    x=x**2    
"""

# var = 3
# print(var)

# x = 5
# print(x)
# x+=3           # x=x+1   5=5+1 = 6
# print(x)

y = 10
y%=3
print(y)

div = 30
div/= 10
print(div)
