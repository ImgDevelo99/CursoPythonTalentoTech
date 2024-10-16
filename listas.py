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
# calificaiones = []

# calif1 = float(input("ingrese su calificacion"))
# calificaiones.append(calif1)

# calif2 = float(input("ingrese su calificacion"))
# calificaiones.append(calif2)

# calif3 = float(input("ingrese su calificacion"))
# calificaiones.append(calif3)

# print("la calificacion mas alta es: ",max(calificaiones))
# print("la calificacion minima es: ",min(calificaiones))

#------------------------------------------------------------------------------------------------------
## Escribe un programa en Python que permita al usuario crear una lista de compras. 
# El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno 
# y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, 
# el programa debe imprimir la lista completa de compras en orden.
# Requisitos:
# El programa debe permitir al usuario ingresar productos hasta que decida detenerse.
# Después de ingresar cada producto, el usuario debe ser preguntado si desea agregar otro producto.
# Si el usuario decide que no quiere agregar más productos, el programa debe mostrar la lista completa de compras.

# listaCompras = []# arroz,  papaas, leche

# while True:
#     producto = input(" ingrese el nombre del producto a la lista: ")
#     listaCompras.append(producto)

#     continuar = input("¿Desea agregar otro producto? (si/no): ").lower()
#     if continuar == "no":
#         break

# print("\nLista completa de compra")

# for i in listaCompras:
#     print(i)
#-----------------------------------------------------------------------------------------
# Escribe un programa en Python que solicite al usuario ingresar una lista de números enteros.
# Luego, el programa debe calcular e imprimir la suma de todos los números ingresados. 
# El programa debe continuar solicitando números hasta que el usuario decida dejar de ingresar más.
# Requisitos:
# El programa debe permitir al usuario ingresar números uno por uno.
# Después de ingresar cada número, el usuario debe ser preguntado si desea agregar otro número.
# Si el usuario decide que no quiere agregar más números, el programa debe calcular y mostrar 
# la suma total de los números ingresados.

# listaNumeros = []

# while True:
#     numero = int(input(" Ingrese el numero entero : "))
#     listaNumeros.append(numero)

#     continuar = input("¿Desea agregar otro numero? (si/no): ").lower()
#     if continuar == "no":
#         break

# sumaTotal = sum(listaNumeros)
# print("la suma total de todos los numeros que agrego es: ",sumaTotal)

#------------------------------------------------------------------------------------------
# Escribe un programa en Python para gestionar una lista de contactos. 
# El programa debe permitir al usuario realizar las siguientes operaciones:

# Agregar un contacto a la lista, incluyendo un nombre y un número de teléfono.
# Eliminar un contacto de la lista especificando el nombre del contacto.
# Mostrar todos los contactos en la lista, con el formato "Nombre: Número de teléfono".
# El programa debe mostrar un menú con las opciones disponibles y seguir funcionando hasta 
# que el usuario elija salir. Asegúrate de manejar situaciones en las que el usuario intente
# eliminar un contacto que no está en la lista y que el programa informe adecuadamente al usuario.

# Requisitos:
# El programa debe permitir al usuario ingresar contactos con un nombre y un número de teléfono.
# Debe ser posible eliminar un contacto buscando por el nombre.
# Debe mostrar todos los contactos en la lista en un formato claro.
# El programa debe seguir ejecutándose hasta que el usuario decida salir.

contactos = []#[nombre:diego, telefono : "3333", nombre: "maria", telefono: 3333, nombre: 2juan",]

# print("-------AGENDA TELEFONICA-------------")
# while True:
#     print("\n1. Agregar contacto")
#     print("\n2. Eliminar contacto")
#     print("\n3. Mostrar contacto")
#     print("\n4. Salir")

#     opcion = input("Elige una opcion: ")

#     #agregar un contacto
#     if opcion == "1":
#         nombre = input("Nombre de contacto: ")
#         telefono = input("Numero telefonico: ")
#         contactos.append([nombre, telefono])

#     #eliminar un contacto
#     elif opcion == "2":
#         nombre = input("nombre del contactp a eliminar: ")
#         for i in contactos:
#             if i[0] == nombre:
#                 contactos.remove(i)
#                 print("Contacto eliminado exitosamente")
#                 break
#         else:
#             print("no hay contactos")    

#     #mostrar contactos
#     elif opcion == "3":
#        # if contactos: #lista
#         for i in range(0, len(contactos),2): #bucle
#             print(f"Nombre:{contactos[i][0]}, Telefono: {contactos[i][1]}")  
#         else:    
#             print("no hay contactos")   

#     #salir
#     elif opcion == "4":
#         print( "Gracias")
#         break        

#----------------------------------------------------------------------------------
# #Escribe un programa en Python que permita al usuario crear una lista de sus películas favoritas.
# El programa debe permitir al usuario realizar las siguientes acciones:

# Agregar una película a la lista.
# Eliminar una película especificando su nombre.
# Mostrar todas las películas en la lista.
# Buscar si una película específica está en la lista.
# El programa debe ofrecer estas opciones en un menú y continuar funcionando hasta que el usuario decida salir.

#--------------------------------------------------------------------------------
"""Escribe un programa en Python para gestionar una lista de tareas pendientes. El programa debe implementar un CRUD 
(Crear, Leer, Actualizar, Eliminar) para las tareas y permitir al usuario realizar las siguientes acciones:

Crear una nueva tarea: Añadir una tarea a la lista con una descripción y una fecha de vencimiento.
Leer todas las tareas: Mostrar todas las tareas actuales, incluyendo su descripción y fecha de vencimiento.
Actualizar una tarea: Modificar la descripción y/o la fecha de vencimiento de una tarea existente especificando 
su número de identificación.
Eliminar una tarea: Eliminar una tarea de la lista especificando su número de identificación.
El programa debe ofrecer un menú de opciones y seguir funcionando hasta que el usuario decida salir. Asegúrate 
de manejar situaciones en las que el usuario intente realizar acciones sobre tareas que no existen y proporciona
mensajes adecuados.

Requisitos:
El programa debe permitir al usuario ingresar una descripción y una fecha de vencimiento para cada nueva tarea.
Cada tarea debe tener un identificador único que se utiliza para actualizar o eliminar la tarea.
El programa debe mostrar todas las tareas en un formato claro.
El usuario debe poder actualizar la descripción y/o la fecha de vencimiento de una tarea.
El usuario debe poder eliminar una tarea especificando su identificador."""

tareas = []
id_tarea = 1

while True:
    print("-----------\nMEnu de tareas-------------")
    print("1. Nueva tarea")
    print("2. Leer todas las tareas")
    print("3. Actualizar las tareas")
    print("4. eliminar una tarea")
    print("5. Salir")

    opcion = input("Elige la opcion: ")
    
    #crear nueva tarea
    if opcion == "1":
        descripcion = input("Descripcion de la tarea: ")
        fechaVencimiento = input("Fecha de vencimiento (dd/mm/aaaa): ")

        tareas.append({"id": id_tarea, "descripcion":descripcion, "fechaVencimiento":fechaVencimiento})
        print(f"Tarea {id_tarea} creada con exito\n")
        id_tarea += 1

        #leer todas las tareas
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            print("---------------lista de tares pendientes-------------")
            for i in tareas:
                print(f"ID: {i["id"]} descripcion: {i["descripcion"]} Fecha de vencimiento {i["fechaVencimiento"]}")
            print()    

        #Editar tarea
    elif opcion == "3" :
        idActualizar = int(input("Ingrese el id de la tarea a editar: "))
        tareaEncontrada = False
        for i in tareas :
            if i ["id"] == idActualizar:
                nuevaDescripcion = input("Escriba la nueva descripcion (dejar en blanco si on quiere editar): ")
                nuevaFecha = input("ingrese nueva fecha de vencimiento (dejar en blanco si on quiere editar): ")
                if nuevaDescripcion:
                    i["descripcion"] = nuevaDescripcion
                if nuevaFecha:
                    i["fechaVencimiento"] = nuevaFecha
                print(f"Tarea {idActualizar} actualizado con exito\n")
                tareaEncontrada = True
                break
        if not tareaEncontrada:
            print(f"NO se encontro la tarea con el ID: {idActualizar}\n")    

        #Eliminar tarea#
    elif opcion == "4" :
        idEliminar = int(input("ingrese el id de la tarea a eliminar: "))
        tareaEncontrada = False
        for i in tareas :
            if i ["id"] == idEliminar:
                tareas.remove(i) 
                print(f"tarea {idEliminar} eliminada con exito\n")
                tareaEncontrada = True
                break
        if not tareaEncontrada:
                print(f"no se encontro la tarea con ID {idEliminar}")

    #Salir del programa
    elif opcion == "5" :
        print("Salir del programa")
        break
    else:
        print("opcion invalida, por favor verifique: ")            












