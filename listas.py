"""
listas son tipos de datos que nos permiten almacenar cualquier tipo de datos multiples
-son ordenadas
-pueden ser indexadas
-se pueden anidar
-son mutable (se pueden modificar)
-son dinamicas(CRUD editar, agregar, eliminar, mostrar)

"""
# # lista = list(1,3,4,5,7,8,5) # lista
# datos = [1, 4, 3, 6, "hola", 5, 7, "python", True, 4,6]

# informacion = [ 4, 6 ,34, "hola",[3, 4, "py"]]
numeros = [1,6,3,2,5,8,7]

# print(numeros)
# print(numeros[0])

frutas = ["manzana", "pera", "uvas", "Naranja","Naranja"]
print(frutas)
print(frutas[1])

#--------------------------METEDOS DE LAS LISTAS--------------------------------
#metdo append(elemto) : agrega un elemento al final de la lista
frutas.append("piña")
print(frutas)

#extend(iterable): agrega otra lista al final de la lista existente
frutas.extend(numeros)
print(frutas)

#insert(posicion,elemento): inserta un elemento en una posisicon especifica de la lista
frutas.insert(1,"banano")
print(frutas)

#remove(elemento):elimina el elemento de la lista  on el parametro del elemento
frutas.remove("pera")
print(frutas)

#pop : elimina y devuelve el elemento en la posision dada(si no se indica la posision el indice sera el ultimo)
elemento = frutas.pop(1)
print(elemento)
print(frutas)

#-------------------------------
# print(frutas[:3]) #imprime los primeros 3 elementos de la lista
# print(frutas[0],frutas[3],frutas[5])

#count(elemento):cuenta cuantas veces aparece el elemento en la lista
contador = frutas.count("Naranja")
print(contador)

#sort: ordena la lista(modo original)
numeros.sort()
print(numeros)

#reverse: invierte el orden de los elementos de la lista
numeros.reverse()
print(numeros)

#copy o [:] :crea una copia superficial de la lista
copiar = numeros.copy()
print(copiar)

copy = numeros[:]
print(copy)

#len : longitud de la lista
print(len(frutas))
print(len(numeros))
#-------------------------------------------------------------------------------------------------------
# solicitar al usuario que ingrese 3 nombres y se almacenen en una lista y luego imprimir

# nombres = []

# nombre1 = input("ingrese el primer nombre: ")
# nombres.append(nombre1)

# nombre2 = input("ingrese el primer nombre: ")
# nombres.append(nombre2)

# nombre3 = input("ingrese el primer nombre: ")
# nombres.append(nombre3)

# print("los nombres que usted agrego a la lista son: ",nombres)
# print(nombres)

#-----------------------------------------------------------------
# Pide al usuario que ingrese el precio de tres productos y almacénalos en una lista.
# Luego, muestra la lista y el precio total sumado.
# precio = []

# precio1 = float(input("ingrese el precio del producto: "))
# precio.append(precio1)

# precio2 = float(input("ingrese el precio del producto: "))
# precio.append(precio2)

# precio3 = float(input("ingrese el precio del producto: "))
# precio.append(precio3)

# precio.sort()
# print("lista de precios :",precio)

# print(" la suma total es: ",sum(precio))

#-------------------------------------------------------------------
# Pide al usuario que ingrese tres calificaciones de exámenes, sacar el promedio, si es mayor a 3 aprobo el curso
# si es menor o igual a 3 desaprobo, ordenar la calificaciones,
# guárdalas en una lista y muestra la calificación más alta.
calificaiones = []

calif1 = float(input("ingrese su calificacion"))
calificaiones.append(calif1)

calif2 = float(input("ingrese su calificacion"))
calificaiones.append(calif2)

calif3 = float(input("ingrese su calificacion"))
calificaiones.append(calif3)

print("la calificacion mas alta es: ",max(calificaiones))
print("la calificacion minima es: ",min(calificaiones))
