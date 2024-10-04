"""
Supongamos que tienes un grupo de estudiantes y quieres almacenar sus calificaciones
en un diccionario. Luego, puedes agregar nuevas calificaciones, actualizar las notas existentes
y eliminar estudiantes del registro.
"""
# calificaciones = {
#     "juan": [3, 5, 2],
#     "maria":[4.6 , 3 , 2.4],
#     "carlos":[4 , 2.2 , 3.6]
# }
# #agregar
# calificaciones["juan"].append(1)
# print(calificaciones)

# #actualizar
# calificaciones["maria"] = [5 , 4.5 , 3]
# print(calificaciones)

# calificaciones["maria"][2] = 5
# print(calificaciones)

# #eliminar
# del calificaciones["carlos"]
# print(calificaciones)

# for estudiantes, notas in calificaciones.items():
#     print(f"{estudiantes}: {notas}")

"""
Ejemplo Práctico: CRUD para un Directorio de Contactos
Vamos a implementar las operaciones básicas de un CRUD:

Crear: Agregar un nuevo contacto.
Leer: Mostrar los contactos existentes.
Actualizar: Modificar el número de teléfono de un contacto existente.
Eliminar: Borrar un contacto del directorio.
"""
# diccionarioContacto ={

#     "juan": "34444",
#     "Maria": "44444",
#     "Carlos": "12334",
#     "Dario": 889998
# }
# #craer contacto-----------
# diccionarioContacto["Diana"] = "555333"
# print(f"{diccionarioContacto}")
# print(f"contacto agregado: Diana - {diccionarioContacto["Diana"]}")

# #leer contacto
# print("\nDIRECTORIO DE CONTACTOS")
# for nombre, telefono in diccionarioContacto.items():
#     print(f"{nombre} : {telefono}")

# #Editar
# diccionarioContacto["Dario"] = 232323
# print(f"\nnumero actualizado para Dario {diccionarioContacto["Dario"]}")

# #eliminar
# del diccionarioContacto["juan"]
# print("\nContacto eliminado.")
# print(diccionarioContacto)

# print("\n-----DIRECTORIO DE CONTACTOS---------")
# for nombre, telefono in diccionarioContacto.items():
#     print(f"{nombre} : {telefono}")

"""
Ejercicio: Gestión de Inventario de Productos
El usuario podrá:

Agregar un nuevo producto o actualizar la cantidad de un producto existente.
Eliminar un producto del inventario.
Mostrar el inventario actual.
"""
# inventario = {}
# continuar = True

# while continuar:
#     print("\n Opciones")
#     print("1. agregar o actualizar un producto")
#     print("2. eliminar un producto")
#     print("3. mostrar el inventario")
#     print("4. salir")

#     opcion = input("ingrese una opcion entre 1 y 4: ")

#     if opcion == "1" :
#         #agregar o actualizar
#         producto = input("Nombre del producto a ingresar: ").lower()
#         cantidad = int(input(f"cantidad de {producto}: "))

#         if producto in inventario :
#             inventario[producto] += cantidad
#             print(f"se a agregado {cantidad} unidades de {producto}. total : {inventario[producto]} unidades")
#         else:
#             inventario[producto] = cantidad
#             print(f"{producto.capitalize()} añadido al inventario con {cantidad} unidades")    

#     elif opcion == "2":
#         #eliminar
#         producto = input("Nombre del producto a eliminar: ").lower()

#         if producto in inventario:
#             del inventario[producto]
#             print(f"{producto.capitalize()} eliminado del inventario.")
#         else:
#             print(f"{producto.capitalize()} no se encontro en el inventario.")

#     elif opcion == "3":
#         #mostrar inventario
#         print("\n--INVENTARIO ACTUAL--")
#         if inventario:
#             for producto, cantidad in inventario.items():
#                 print(f"{producto.capitalize()}: {cantidad} unidades")
#         else:
#             print("inventario esta vacio")

#     elif opcion == "4":
#         #salir
#         continuar = False  
#         print("gracias por preferirnos.........")

#     else:
#         print("opcion incorrecta por favor verifique nuevamente")
#------------------------------------------------------------------------------   
"""
simular un sistema de administración de una biblioteca. El sistema gestionará información sobre libros y usuarios. 
Los libros tendrán atributos como título, autor y cantidad disponible, mientras que los usuarios podrán tomar
prestados o devolver libros.

Ejercicio: Sistema de Gestión de Biblioteca
Este programa permitirá:

Agregar libros a la biblioteca. diccionarios
Agregar usuarios a la biblioteca. diccionarios
Prestar libros a los usuarios.
Devolver libros a la biblioteca.
Mostrar el estado de los libros y los usuarios.
"""    
biblioteca = {}
usuario = {}
continuar = True

while continuar :
    print("\n---Opciones---")
    print("1. Agregar un libro a la bibliioteca")
    print("2. Agregar un usuario a la biblioteca")
    print("3. prestar un libro a un usuario")
    print("4. devolver un libro a la biblioteca")
    print("5. mostrar estado del libro y de los usuarios")
    print("6. Salir ")

    opcion = input("Ingrese una opcion (1-6): ")

    if opcion == "1" : # id: 1 , nombre : don quijote 
        idLibro = input("Ingrese el ID del libro : ")

        if idLibro in biblioteca:
            print()
            print(f"el libro con el ID {idLibro} ya existe")
        else:
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("ingrese ek autor del libro: ")
            cantidad = int(input("Ingrese la cantidad de copias disponibles: ")) # 10

            #agregar un libro
            biblioteca[idLibro] = { #biblioteca = {idLibro: [titulo: don quijote, autor: miguel, cantidad: 10]}
                "titulo": titulo,
                "autor": autor,
                "cantidad": cantidad
            }
            print()
            print(f"libro {titulo} añadido a la biblioteca.")

            #-----------------------------------------------------------------------------------------
    elif opcion == "2":
        idUsuario = input("Ingrese el ID del usuario")

        if idUsuario in usuario:
            print(f"el usuario con ID {idUsuario} ya existe.")

        else:
            nombreUsuario = input("Ingrese el nombre del usuario: ")
            usuario[idUsuario] = {
                "nombre": nombreUsuario,
                "prestamo": []
            }
            print(f"usuario {nombreUsuario} añadido a la biblioteca.")   

                #-----------------------------------------------------------------------------------
    elif opcion == "3":
        idUsuario = input("Ingrese el ID del usuario: ")
        if idUsuario not in usuario:
            print(f"No se encontro el usuario con el ID {idUsuario}")

        else:
            idLibro = input("ingrese el ID del libro: ")
            if idLibro not in biblioteca:
                print(f"No se encontro el usuario con el ID {idLibro}")
            elif biblioteca[idLibro]["cantidad"] <= 0 :
                print(f"no hay copias disponibles del libro {biblioteca[idLibro]["titulo"]}.")

            else:#prestamo libro
                usuario[idUsuario]["prestamo"].append(idLibro) 
                biblioteca[idLibro]["cantidad"]-=1
                print(f"El libro {biblioteca[idLibro]["titulo"]} ha sido prestado a {usuario[idUsuario]["nombre"]}.")

            #-----------------------------------------------------------------------------------------------
    elif opcion == "4":
        idUsuario = input("ingrese el ID del usuario: ")
        if idUsuario not in usuario:
            print(f"no se encontro el usuario con ID {idUsuario}")
        else:
            idLibro = input("Ingrese el Id del libro a devolver: ")
            if idLibro not in biblioteca:
                print(f"no se encontro el usuario con ID {idLibro}")

            else:
                usuario[idUsuario]["prestamo"].remove(idLibro)
                biblioteca[idLibro]["cantidad"] += 1
                print(f"el libro {biblioteca[idLibro]["titulo"]} ha sido devuelto por {usuario[idUsuario]["nombre"]}." )        

                #----------------------------------------------------------------------------------------
    elif opcion == "5":
        print("\nEstado de la biblioteca-----------")
        if biblioteca:
            for idLibro, inf in biblioteca.items():
                print(f"ID : {idLibro} Titulo: {inf["titulo"]} Autor: {inf["autor"]} copias disponibles: {inf["cantidad"]}")
        else:
            print("No hay libros en la biblioteca")

        print("\nEstado de los usuario----")
        if usuario:
                for idUsuario, inf in usuario.items():                           
                    print(f"ID usuario: {idUsuario} Nombre: {inf["nombre"]} libros prestados: {", ".join(inf["prestamo"]) if inf["prestamo"] else  "ninguno" }")
        else:
            print("no hay usuarios registrados")



                




