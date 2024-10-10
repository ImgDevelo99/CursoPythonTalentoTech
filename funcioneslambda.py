"""
es una funcion anonima o sin nombre en python, se utiliza para crear funciones pequeñas y faciles de manejar, se escriben en una sola linea
q utiliza para operaciones sencillas.

"""
#lambda argumento: expresion

#lambda : la palabra que define la funcion anonima
#argumento : son los parametros que recibe la funcion lambda,
#expresion : es unua unica expresion que la funcion evalua, no van multiples lineas

f = lambda: 5
print(f())
#-------------------------------
suma = lambda a,b : a + b
print(suma(5,2))

#map
numeros = [1,2,3,4,5]
cuadrado = list(map(lambda x: x ** 2, numeros ))
print(cuadrado)

#----------------------------------
estudiantes = [("juan", 85),("ana",92),("luis",78)]

estudiantesOrdenados = sorted(estudiantes, key = lambda estudiante : estudiante[1])
print(estudiantesOrdenados)


