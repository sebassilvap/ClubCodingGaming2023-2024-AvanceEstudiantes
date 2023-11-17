# =================================
# Listas - Completo
# => Recordatorio de Fundamentos

# - Creación
# - Lista Vacía
# - Función len()
# - Concatenación
# =================================


#? 1) Creación de Listas
print('\n1) Creación de Listas')
# - una lista se crea con corchetes []
# - y separando los elementos con coma

lista_numeros = [1,2,3,4,5]
print( lista_numeros , type(lista_numeros) ) # [1, 2, 3, 4, 5] <class 'list'>

# => puede albergar VARIOS tipos de datos

lista = ['A', True, 100, 5.5, None]
#         0     1    2    3    4

print()
print( lista , type(lista) )
print( lista[0] , type(lista[0]) ) # A <class 'str'>
print( lista[1] , type(lista[1]) ) # True <class 'bool'>
print( lista[2] , type(lista[2]) ) # 100 <class 'int'>
print( lista[3] , type(lista[3]) ) # 5.5 <class 'float'>
print( lista[4] , type(lista[4]) ) # None <class 'NoneType'>


# => puede albergar incluso otras listas

lista = [ 1,2,3, ['a','b','c'] ]
#         0 1 2        3

print()
print(lista)
print( lista[0] , type(lista[0]) ) # 1 <class 'int'>
print( lista[1] , type(lista[1]) ) # 2 <class 'int'>
print( lista[2] , type(lista[2]) ) # 3 <class 'int'>
print( lista[3] , type(lista[3]) ) # ['a', 'b', 'c'] <class 'list'>


# - también se la puede crear de manera mucho más formal
# - utilizando la función list
# - el cual sirve también para hacer casting a lista

lista_1 = list( [1,2,3] )
lista_2 = list( range(1,11,2) )

print()
print( lista_1 , type(lista_1) ) # [1, 2, 3] <class 'list'>
print( lista_2 , type(lista_2) ) # [1, 3, 5, 7, 9] <class 'list'>



#? 2) Creación Lista Vacía
print('\n2) Creación Lista Vacía')
# - Nos sirve para iniciar un valor de lista
# - Y poder trabajarlo luego

# ----------------------------------
# 1 manera de declarar lista vacía
# ----------------------------------
lista_numeros = []  # lista vacía
print( lista_numeros , type(lista_numeros) ) # [] <class 'list'>

for i in range(1,6):
    lista_numeros.append(i)
# end for

print( lista_numeros )


# --------------
# otra manera
# --------------
lista_vacia = list()

print( lista_vacia , type(lista_vacia) ) # [] <class 'list'>



#? 3) Función len()
print('\n3) Función len()')
# - len() => devuelve el número de elementos
# - de un elemento iterable

string = 'python'
lista = [1,2,3,4,5]

print( len(string) , type(len(string)) ) # 6 <class 'int'>
print( len(lista) , type(len(lista)) ) # 5 <class 'int'>



#? 4) in + Listas
print('\n4) in + Listas')
# - una manera de averiguar si un elemento está en una lista

lista = [10, True, 'hola', -5.5]

print( 20 in lista ) # False
print( False in lista ) # False
print( 'hola' in lista ) # True



#? 5) Concatenación
print('\n5) Concatenación')
# - al igual que strings
# - une una lista con otra

# =========
# STRINGS
# =========
c1 = 'hola'
c2 = ' mundo'

print( c1 + c2 )

c3 = c1 + c2
c4 = c2 + c1

print( c1 , type(c1) , len(c1) ) # hola <class 'str'> 4
print( c2 , type(c2) , len(c2) ) #  mundo <class 'str'> 6
print( c3 , type(c3) , len(c3) ) # hola mundo <class 'str'> 10
print( c4 , type(c4) , len(c4) ) #  mundohola <class 'str'> 10

# ========
# LISTAS
# ========

lista_1 = ['a', 'b', 'c']
lista_2 = [100, 200, 300]

print( lista_1 + lista_2 )
print( lista_2 + lista_1 )

# => guardar en variable

r1 = lista_1 + lista_2
r2 = lista_2 + lista_1

print( r1 , type(r1) , len(r1) ) # ['a', 'b', 'c', 100, 200, 300] <class 'list'> 6
print( r2 , type(r2) , len(r2) ) # [100, 200, 300, 'a', 'b', 'c'] <class 'list'> 6


#? 6) Operador * en listas
print('\n6) Operador * en listas')
# - repite el número de veces indicado

numeros = [100,200,300]

numeros_x_2 = numeros * 2
numeros_x_3 = numeros * 3

print( numeros, type(numeros) , len(numeros) ) # [100, 200, 300] <class 'list'> 3
print( numeros_x_2, type(numeros_x_2) , len(numeros_x_2) ) # [100, 200, 300, 100, 200, 300] <class 'list'> 6
print( numeros_x_3, type(numeros_x_3) , len(numeros_x_3) ) # [100, 200, 300, 100, 200, 300, 100, 200, 300] <class 'list'> 9 

#resultado_raro = numeros * 'A'
#! TypeError: can't multiply sequence by non-int of type 'str'