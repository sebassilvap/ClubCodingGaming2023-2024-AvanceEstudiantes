# ==========================================================
# Listas

# - es el tipo más fundamental de las colecciones de datos
# - el tema colecciones lo vemos a profundidad más adelante
# - pero con lo que sabemos podemos ya entender las bases
# - no son más que una lista de valores separados con coma
# - y van entre corchetes
# - pueden almacenar varios tipos de datos
# ==========================================================


#? 1) Creación de una lista
print('\n1) Creación de una lista')

letras = ['a','b','c','d','e'] # ['a', 'b', 'c', 'd', 'e'] <class 'list'>
numeros = [10,20,30,40,50,60] # [10, 20, 30, 40, 50, 60] <class 'list'>
info_persona = ['Diego', 'Salas', 25, True, 17.5] # ['Diego', 'Salas', 25, True, 17.5] <class 'list'>

print( letras, type(letras) )
print( numeros, type(numeros) )
print( info_persona, type(info_persona) )



#? 2) Index y Slicing
print('\n2) Index y Slicing')
# - al igual que los string
# - son elementos iterables / de secuencia
# - podemos acceder a sus elementos por medio de los índices
# - y a un subgrupo de sus valores por medio del Slicing
# - RECORDAR: que el índice inicia en 0
# - RECORDAR: el último elemento tiene índice -1


# -------------------------------
# => aplicando index
print('\n2.1) Index en Listas')
# -------------------------------

print( letras[0], numeros[-1] )

nombre = info_persona[0]
apellido = info_persona[1]
edad = info_persona[2]
es_estudiante = info_persona[3]
nota_final = info_persona[4]

print( nombre, apellido, edad, es_estudiante, nota_final )
print(nombre, type(nombre)) # Diego <class 'str'>
print(apellido, type(apellido)) # Salas <class 'str'>
print(edad, type(edad)) # 25 <class 'int'>
print(es_estudiante, type(es_estudiante)) # True <class 'bool'>
print(nota_final, type(nota_final)) # 17.5 <class 'float'>


# -----------------------------------
# => aplicando slicing
print('\n2.2) Slicing en Listas')
# -----------------------------------
# RECORDAR: [start , end , step]
# - start => inclusivo
# - end   => exclusivo
# - step  => salto

letras_lista = ['a','b','c','d','e']
letras_string = 'abcde'

print( letras_lista[0:2] )
print( letras_string[0:2] )

print()
print( letras_lista[-3:] )
print( letras_string[-3:] )

print()
print( letras_lista[::2] )
print( letras_string[::2] )


#? 3) Concatenación en Listas
print('\n3) Concatenación en Listas')

numeros_1 = [1,2,3]
numeros_2 = [10,20,30]

resultado_1 = numeros_1 + numeros_2
resultado_2 = numeros_2 + numeros_1

print(numeros_1)
print(numeros_2)
print(resultado_1)
print(resultado_2)

# similar a la concatenación de strings
string_1 = ' 1 2 3 '
string_2 = ' 10 20 30 '

concat_1 = string_1 + string_2
concat_2 = string_2 + string_1

print(concat_1)
print(concat_2)



#? 4) función len()
print('\n4) función len()')
# - función len se aplica a algunos elementos
# - como vimos en los string nos devuelve el tamaño del mismo
# - en listas devuelve el número de elementos de la lista

palabra = 'hola'
print(palabra, len(palabra), type(len(palabra)))

lista = ['X', 'Y', 10, 20, True, False, -100.5]
print(lista, len(lista))



#? 5) Las listas son MUTABLES
print('\n5) Las listas son MUTABLES')
# - RECORDAR: string (cadenas de texto) => INMUTABLES
# - Pero las listas si son MUTABLES
# - es decir, podemos reasignar sus elementos

# => Inmutabilidad del String
string = 'xyz'
#(+)      012

print(string)
print(string[0])
print(string[1])
print(string[2])

#string[0] = '2'
#! TypeError: 'str' object does not support item assignment
#! INMUTABILIDAD


# => Mutabilidad de Listas
lista = ['x', 'y', 'z']
print( hex(id(lista)) )

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

lista[0] = 'A'
print(lista)
print( hex(id(lista)) )

lista[0] = 222333
print(lista)
print( hex(id(lista)) ) #! avanzado funciones id / hex

# ----------------------------------------------------
# * RECORDAR siempre => str inmutable / list mutable
# ----------------------------------------------------



#? 6) Podemos definirlas en varias líneas de código
print('\n6) Podemos definirlas en varias líneas de código')

# => ej: lista de estudiantes
lista_estudiantes = ['Carlos', 'Andrea', 'Marcelo']
print(lista_estudiantes)

lista_estudiantes = [
    'Andrea',
    'Sebastián',
    'Diego',
    'Marcelo',
    'Ana',
    'Xavier'
]

print(lista_estudiantes)

# => no error al poner coma al final
lista_estudiantes = [
    'Andrea',
    'Sebastián',
    'Diego',
    'Marcelo',
    'Ana',
    'Xavier',
]

print(lista_estudiantes)


#? 7) .append() => añadir un elemento al final de la lista
print('\n7) .append() => añadir un elemento al final de la lista')
# - uno de los elementos más importantes de las listas
# - veremos a profundidad luego el tema de colecciones y listas

lista_estudiantes = [
    'Andrea',
    'Sebastián',
    'Diego',
    'Marcelo',
    'Ana',
    'Xavier',
]

print(lista_estudiantes, len(lista_estudiantes))

lista_estudiantes.append('Orlando')

print(lista_estudiantes, len(lista_estudiantes))

lista_estudiantes.append('Belén')

print(lista_estudiantes, len(lista_estudiantes))


#? 8) Reasignación con Slicing
print('\n8) Reasignación con Slicing')

lista = [1,2,3,4,5,6]
#        0 1 2 3
print(lista, len(lista))

print( lista[0:3] )
lista[0:3] = ['X', 'Y', 'Z']
print(lista, len(lista))



# => ¿qué pasa si mandamos MENOS elementos?
lista = [1,2,3,4,5,6]
lista[0:3] = ['A', 'B'] 
print(lista) # ['A', 'B', 4, 5, 6]

# => ¿qué pasa si mandamos MÁS elementos?
lista = [1,2,3,4,5,6]
lista[0:3] = ['A', 'B', 'C', 'D', 'E']
print(lista) # ['A', 'B', 'C', 'D', 'E', 4, 5, 6]

# => ¿si lo hacemos con el index?
lista = [1,2,3,4,5,6]
#        0 1 2 3 4 5

lista[3] = 1000
print(lista)

lista[3] = ['A', 'B', 'C']
print(lista, len(lista))



#? 9) Listas Anidadas
print('\n9) Listas Anidadas')
# - como vimos anteriormente podemos almacenar listas dentro de listas

# => Creación de una lista anidada
lista_anidada_1 = [
    [100,200,300],
    [400,500,600],
    [700,800,900],
]

print(lista_anidada_1, len(lista_anidada_1))

lista_1 = ['A', 'B', 'C']
lista_2 = ['X', 'Y', 'Z']
lista_3 = ['M', 'N', 'O']

lista_anidada_2 = [lista_1, lista_2, lista_3]

print(lista_anidada_2, len(lista_anidada_2))


# => Accediendo a los elementos

print( lista_1 )
print( lista_1[0] )
print( lista_1[1] )
print( lista_1[2] )
print( lista_2 )
print( lista_2[0] )
print( lista_2[1] )
print( lista_2[2] )
print( lista_3 )
print( lista_3[0] )
print( lista_3[1] )
print( lista_3[2] )
#print( lista_3[3] ) #! IndexError: list index out of range
#lista_3[3] #! IndexError: list index out of range


# => Acceso con doble índice => doble corchete
print('\n\n=> Acceso con doble índice => doble corchete\n')
print( lista_anidada_2[0] ) # ['A', 'B', 'C']
print( lista_anidada_2[0][0] ) # A
print( lista_anidada_2[0][1] ) # B
print( lista_anidada_2[0][2] ) # C
print( lista_anidada_2[1] ) # ['X', 'Y', 'Z']
print( lista_anidada_2[1][0] ) # X
print( lista_anidada_2[1][1] ) # Y
print( lista_anidada_2[1][2] ) # Z
print( lista_anidada_2[2] ) # ['M', 'N', 'O']
print( lista_anidada_2[2][0] ) # M
print( lista_anidada_2[2][1] ) # N
print( lista_anidada_2[2][2] ) # O

#! IMPORTANTE !!!