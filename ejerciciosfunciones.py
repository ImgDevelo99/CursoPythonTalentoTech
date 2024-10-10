# Enunciado: Gestión de inventario de una tienda
# Escribe un programa que gestione el inventario de una tienda. La función principal debe permitir agregar nuevos productos al inventario,
# actualizar la cantidad de un producto existente, y calcular el valor total del inventario. 
# La función de cálculo de valor total se debe reutilizar en varias partes del programa, como después de agregar o actualizar un producto.

# Requisitos:
# Crear una función para agregar nuevos productos al inventario.
# Crear una función para actualizar la cantidad de un producto existente.
# Crear una función para calcular el valor total del inventario (reutilizada en otras partes del programa).
# El programa debe permitir agregar o actualizar productos varias veces, y mostrar el valor total del inventario después de cada acción.

#agregar productos
def agregarProducto(inventario):
    nombre = input("ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("ingrese el precio del producto: "))
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto {nombre} agregado al inventario")

#actualizar   
def actualizarProducto(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        nuevaCantidad = int(input(f"ingrese la nueva cantidad para el producto {nombre}"))
        inventario[nombre]["cantidad"] = nuevaCantidad
        print(f"Producto {nombre} actualizado a {nuevaCantidad} unidades") 
    else:
        print(f"el producto {nombre} no existe")

#calcular
def calcularTotal(inventario):
    total = 0 
    for producto in inventario :
        total += inventario[producto]["cantidad"] * inventario[producto]["precio"]
        return total
    
def gestionInventario():
    inventario = {}    

    while True:
        print("\n--GESTION DE INVENTARIO--")
        print("1. Agregar producto")
        print("2. Actualizar cantidad del producto")
        print("3. Ver total del inventario")
        print("4. Salir")

        opcion = input(" Seleccione una opcion: ")

        if opcion == "1":
            agregarProducto(inventario)

        elif opcion == "2":
            actualizarProducto(inventario)

        elif opcion == "3":            
            valorTotal = calcularTotal(inventario)
            print(f" el valor total del inventario es: {valorTotal}")

        elif opcion == "4":
            print("Saliendo del pprograma...")
            break
        else:
            print("Opcion incorrecta por favor verificar.")    

gestionInventario()
        
