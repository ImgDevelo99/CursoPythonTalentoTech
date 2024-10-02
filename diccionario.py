"""que es un diccionario?
es una estructura de datos que almacena pares de clave y valor, cada clave esta asociado a un valor,
los diccionarios son mutables, nos permite almacenar cualquier tipo de dato,
Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value.
Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. 
En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.
"""
# lista = [2,4,5,6,66,]

# diccionario = {
#     "clave ": "valor",
#     "clave ": "valor",
#     "clave ": "valor",
#     "clave ": "valor"
# }

# informacionPersonal ={
#     "nombre" : "juan", # nombre = "juan"
#     "telefono": 565555,
#     "profesion": "desarrollador"
# }
# #print(informacionPersonal)

# nombres = {"nombre": "carlos", "edad": "30", "cursos":["py","js","Nodejs",".net"]}
# print(nombres)
# print(nombres["nombre"])
# print(nombres["cursos"])
# print(nombres["cursos"][1])

# notaEsrudiantes = {
#     "juan" : [2 , 3 ,3.6 , 4],
#     "maria" : [4 , 5 ,3.6 , 2],
#     "pedro" : [2.7 ,4.7 ,3.6 , 5]
# }
# print(notaEsrudiantes["maria"])

#---------------------AGREGAR DATOS A LA LISTA--------------
miDiccionario = {
    "nombre": "Sara",
    "edad" : 30 
}

miDiccionario["profesion"] = "Abogada"
print(miDiccionario)

#-------------------EDITAR-------------------------
miDiccionario["edad"] = 32
print(miDiccionario)

#---------------------ELIMINAR----------------------
del miDiccionario["profesion"]
print(miDiccionario)

#.pop = elimina la clave y devuelve su valor
texto = miDiccionario.pop("nombre")
print(miDiccionario)
print(texto)

#----------------Agregar multiples valores------------------
nuevosDatos = {
    "ciudad " : "Bogota",
    "profesion": "secretaria",
    "telefono ": 222333
}
for clave, valor in nuevosDatos.items() :
    miDiccionario[clave] = valor

print(miDiccionario)    

#--------------------------update-----------------------------------
agregarDatos  = {
    "direccion": " carera 20 89 -90",
    "fecha_nacimiento": "12/05/2000"
}
miDiccionario.update(agregarDatos)
print(miDiccionario)

#----------------------Eliminar multiples valores----------
claveEliminar = ["direccion","fecha_nacimiento"]

for clave in claveEliminar :
    if clave in miDiccionario :
        del miDiccionario[clave]

print(miDiccionario)    

#----------------Comprension de Diccionarios---------------
#se utiliza para crear un nuevo diccionario con solo las claves que deseo mantener
clave_a_eliminar = {"edad","profesion"}#a eliminar

miDiccionarioFiltrado = {
    clave: valor
    for clave, valor in miDiccionario.items()
    if clave not in clave_a_eliminar}

print(miDiccionarioFiltrado)