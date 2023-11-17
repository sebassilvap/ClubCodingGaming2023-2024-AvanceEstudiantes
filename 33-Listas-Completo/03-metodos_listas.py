# ==============================================================
# Métodos de Listas
# - Python tiene elementos internos
# - para poder trabajar con listas
#! OJO: muchos de estos modifican la lista original

# https://www.w3schools.com/python/python_lists_methods.asp
# ==============================================================


#? 1) .index()
print('\n1) .index()')
# - devuelve el índice de una búsqueda
# ! ERROR cuando la búsqueda no existe

# EJ:
lista = ['x', 'y', 'z', 100, 200, 300, True]
#         0    1    2     3   4    5    6

print( lista.index('z') ) # 2
print( lista.index(True) ) # 6
print( lista.index(200) ) # 4

#print( lista.index('A') ) #! ValueError: 'A' is not in list



#? 2) .append()
print('\n2) .append()')
# - para agregar elemento
# - al FINAL de la lista
# * modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

print( lista, len(lista) )

lista.append('sebas')

print( lista, len(lista) )

lista.append(-111.222)

print( lista, len(lista) )



#? 3) .insert()
print('\n3) .insert()')
# - para insertar un elemento en una posición exacta
# - recibe 2 argumentos
# .insert(index, elemento)
# * modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

print( lista, len(lista) )

lista.insert(2 , 'hola')
print( lista, len(lista) ) # ['x', 'y', 'hola', 'z', 100, 200, 300, True] 8

lista.insert(-3, 'python')
print( lista, len(lista) ) # ['x', 'y', 'hola', 'z', 100, 'python', 200, 300, True] 9

#! utilizar un índice muy alto, no nos da error!!!

lista.insert(-100, 'test')
print( lista, len(lista) ) # ['test', 'x', 'y', 'hola', 'z', 100, 'python', 200, 300, True] 10

lista.insert(100, 'test2')
print( lista, len(lista) ) # ['test', 'x', 'y', 'hola', 'z', 100, 'python', 200, 300, True, 'test2'] 11



#? 4) del lista[indice]
print('\n4) del lista[indice]')
# - eliminar un elemento de la lista
# - proporcionando la lista y el índice
# - el índice entre corchetes
# * modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

print( lista, len(lista) )

del lista[3]
print( lista, len(lista) )

#del lista[100] #! IndexError: list assignment index out of range



#? 5) .pop()
print('\n5) .pop()')
# - por defecto: elimina último elemento de la lista
# - también se puede especificar el índice del elemento a eliminar
# - devuelve el elemento eliminado
# * modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

# ------------------------
# por defecto
print('\npor defecto\n')
# ------------------------

print( lista, len(lista) )

lista.pop()
print( lista, len(lista) ) # ['x', 'y', 'z', 100, 200, 300] 6


# -------------------------------
# especificando index
print('\nespecificando index\n')
# -------------------------------

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

print( lista, len(lista) )

lista.pop(4)
print( lista, len(lista) ) # ['x', 'y', 'z', 100, 300, True] 6


# ----------------------------------------
# retorna el elemento eliminado
print('\nretorna el elemento eliminado\n')
# ----------------------------------------

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

elemento_eliminado = lista.pop()
print( lista, len(lista) ) # ['x', 'y', 'z', 100, 200, 300] 6
print( elemento_eliminado ) # True
print( lista.pop() ) # 300
print( lista, len(lista) ) # ['x', 'y', 'z', 100, 200] 5
print( lista.pop(1) ) # y
print( lista, len(lista) ) # ['x', 'z', 100, 200] 4


lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

#lista.pop(10) #! IndexError: pop index out of range

lista = [1,2,3]
print( lista ) # [1, 2, 3]
print( lista.pop() , lista ) # 3 [1, 2]
print( lista.pop() , lista ) # 2 [1]
print( lista.pop() , lista ) # 1 []
#lista.pop() #! IndexError: pop from empty list



#? 6) .remove()
print('\n6) .remove()')
# - elimina un elemento de la lista
# - el elemento lo pasamos como parámetro
# * modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2     3   4    5    6
#(-)      7    6    5     4   3    2    1

print( lista, len(lista) )

lista.remove('z')
print( lista, len(lista) )

lista.remove(200)
print( lista, len(lista) )

#lista.remove(1000) #! ValueError: list.remove(x): x not in list



# ------------------------------------------
# * RECORDAR
# 3 maneras de eliminar elementos en listas:

# 1)  del lista[indice]
# 2)  .pop() / .pop(indice)
# 3)  .remove(elemento)
# ------------------------------------------



#? 7) .sort()
print('\n7) .sort()')
# - para ordenar listas
# - recibe 2 argumentos: reverse & key
# * modifica la lista original


lista_1 = ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

print(lista_1)
print(lista_2)


# ----------------------------------
# 7.1) sort por defecto
print('\n7.1) sort por defecto\n')
# ----------------------------------
# - por defecto: orden ascendente
# - (A-Z) & menor a mayor

lista_1.sort()
lista_2.sort()

print(lista_1)
print(lista_2)

lista_1 = ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

lista_1.sort(reverse=False) # por defecto / no poner
lista_2.sort(reverse=False) # por defecto / no poner

print(lista_1)
print(lista_2)



# ---------------------------------------
# 7.2) sort con reverse True
print('\n7.2) sort con reverse True\n')
# ---------------------------------------
# - orden descendente
# - (Z-A) & mayor a menor

lista_1 = ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

print(lista_1)
print(lista_2)

lista_1.sort(reverse=True)
lista_2.sort(reverse=True)

print(lista_1)
print(lista_2)

# => por default es False / o como no ponerlo



# -----------------------------
# 7.3) sort con key
print('\n7.3) sort con key\n')
# -----------------------------
# - key permite un ordenado especial
# - en función a una característica de la lista

lista = ['superPalabraGrande', 'sol', 'amigos', 'palabra']
print(lista) # ['superPalabraGrande', 'sol', 'amigos', 'palabra']

lista.sort()
print(lista) # ['amigos', 'palabra', 'sol', 'superPalabraGrande']

lista.sort(reverse=True)
print(lista) # ['superPalabraGrande', 'sol', 'palabra', 'amigos']

lista.sort(key=len)
print(lista) # ['sol', 'amigos', 'palabra', 'superPalabraGrande']

lista.sort(key=len, reverse=True)
print(lista) # ['superPalabraGrande', 'palabra', 'amigos', 'sol']



#? 8) sorted()
print('\n8) sorted()')
# - esta es una función interna de Python - no un método exclusivo de listas
# ! a diferencia de sort no me afecta la lista original
# *     sorted( lista , reverse, key )


# -------------------------------------
# 8.1) sorted() por defecto
print('\n8.1) sorted() por defecto\n')
# -------------------------------------
# - por defecto: orden ascendente
# - (A-Z) & menor a mayor

lista_1 = ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

print('\nlistas originales:\n')
print(lista_1)
print(lista_2)

print('\naplicando sorted\n')
sorted( lista_1 )
sorted( lista_2 )

# print(lista_1)
# print(lista_2)

print( sorted( lista_1 ) )
print( sorted( lista_2 ) )

l1_sorted = sorted(lista_1)
l2_sorted = sorted(lista_2)

print( l1_sorted )
print( l2_sorted )

l1_sorted = sorted(lista_1, reverse=False)
l2_sorted = sorted(lista_2, reverse=False)

print( l1_sorted )
print( l2_sorted )

# --------------------------------------------
# 8.2) sorted() con reverse True
print('\n8.2) sorted() con reverse True\n')
# --------------------------------------------
# - orden descendente
# - (Z-A) & mayor a menor


lista_1 = ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

print('\nlistas originales:\n')
print(lista_1) # ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
print(lista_2) # [10, -80, 0, 6.5, -8.9, -20, 15]

print('\naplicando sorted sin reverse\n')
print( sorted( lista_1 ) ) # ['Beto', 'Daniel', 'Mauro', 'Sebas', 'Ximena']
print( sorted( lista_2 ) ) # [-80, -20, -8.9, 0, 6.5, 10, 15]

print('\naplicando sorted con reverse=False\n')
print( sorted( lista_1 , reverse=False ) ) # ['Beto', 'Daniel', 'Mauro', 'Sebas', 'Ximena']
print( sorted( lista_2 , reverse=False ) ) # [-80, -20, -8.9, 0, 6.5, 10, 15]

print('\naplicando sorted con reverse=True\n')
print( sorted( lista_1 , reverse=True ) ) # ['Ximena', 'Sebas', 'Mauro', 'Daniel', 'Beto']
print( sorted( lista_2 , reverse=True ) ) # [15, 10, 6.5, 0, -8.9, -20, -80]


# ----------------------------------
# 8.3) sorted() con key
print('\n8.3) sorted() con key\n')
# ----------------------------------
# - key permite un ordenado especial
# - en función a una característica de la lista
# *     sorted( lista , reverse, key )

print('\nLista Original:\n')

lista = ['superPalabraGrande', 'sol', 'amigos', 'palabra']
print(lista) # ['superPalabraGrande', 'sol', 'amigos', 'palabra']

print('\nsorted() + key=len + reverse=False\n')
# - menor len A mayor len

lista_orden_len_1 = sorted( lista, key=len )
lista_orden_len_2 = sorted( lista, reverse=False, key=len )

print( lista_orden_len_1 )
print( lista_orden_len_2 )

print('\nsorted() + key=len + reverse=True\n')
# - mayor len A menor len

lista_orden_len_3 = sorted( lista, reverse=True, key=len )

print( lista_orden_len_3 )




#? 9) .split()
print('\n9) .split()')
# - para dividir un string
# - en elementos de lista

# => por defecto divide tomando en cuenta los espacios

mensaje = 'Queridos estudiantes les saludo desde Alemania'
print( mensaje , type(mensaje) )

lista_palabras = mensaje.split()
print( lista_palabras, type(lista_palabras) , len(lista_palabras) )
# ['Queridos', 'estudiantes', 'les', 'saludo', 'desde', 'Alemania'] <class 'list'> 6

# => podemos especificar el caracter a dividir


print()
texto_1 = 'python,java,javascript,c++,pascal'
print( texto_1 ) # python,java,javascript,c++,pascal
print( texto_1.split(',') ) # ['python', 'java', 'javascript', 'c++', 'pascal']


print()
texto_2 = 'manzana/banana/pera/durazno*sandia'
print(texto_2) # manzana/banana/pera/durazno*sandia
print(texto_2.split('/')) # ['manzana', 'banana', 'pera', 'durazno*sandia']




#? 10) .join()
print('\n10) .join()')
# - para formar un string
# - aplicable a lista o string

# --------------------------
# => aplicado a un string
# --------------------------
caracter = '*'
palabra = 'python'

print( caracter.join(palabra) ) # p*y*t*h*o*n


# ----------------------
# => aplicado a lista
# ----------------------

lista = ['Carlos' , 'Andres' , 'Sebas' , 'Karla']

caracter = '--'

print( caracter.join(lista) ) # Carlos--Andres--Sebas--Karla
print( '*****'.join(lista) ) # Carlos*****Andres*****Sebas*****Karla

# guardarlo en una variable
cadena = caracter.join(lista)
print( cadena , type(cadena) ) # Carlos--Andres--Sebas--Karla <class 'str'>



#? 11) .list()
print('\n11) .list()')
# - casting a lista
# - también: para crear lista o lista vacía

# => crear lista / crear lista vacía
lista = list([1,2,3,4,5])
lista_vacia = list()

print( lista , len(lista) ) # [1, 2, 3, 4, 5] 5
print( lista_vacia , len(lista_vacia) ) # [] 0

# => CASTING de string a lista
print()
cadena = 'python'
lista = list(cadena)
print(cadena) # python
print(lista) # ['p', 'y', 't', 'h', 'o', 'n']

# => CASTING de range a list
print()
rango = range(1,11)
lista = list(rango)

print( rango , type(rango) ) # range(1, 11) <class 'range'>
print( lista , type(lista) ) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>




#? 12) .clear()
print('\n12) .clear()')
# - deja la lista en blanco
# * modifica la lista original


lista = ['Carlos','Andres','Sebas','Karla']
print( lista, len(lista) ) # ['Carlos', 'Andres', 'Sebas', 'Karla'] 4

lista.clear()
print( lista, len(lista) ) # [] 0

lista.append('A')
print( lista, len(lista) )



#? 13) .count()
print('\n13) .count()')
# - para contar coincidencias
# - de un elemento en la lista
# * modifica la lista original

numeros = [1,2,3,4,5,1,6,9,8,1,2]

print(numeros , len(numeros)) # [1, 2, 3, 4, 5, 1, 6, 9, 8, 1, 2] 11

print( numeros.count(1) ) # 3
print( numeros.count(100) ) # 0



#? 14) .extend()
print('\n14) .extend()')
# - otra manera de concatenar
# - pero modifica la lista original

lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

print( "lista_1 =" , lista_1 )
print( "lista_2 =" , lista_2 )

# ----------------------------
# extend a lista_1
print('\nextend a lista_1\n')
# ----------------------------

lista_1.extend(lista_2)

print( "lista_1 =" , lista_1 ) # lista_1 = ['A', 'B', 'C', 100, 200, 300]
print( "lista_2 =" , lista_2 ) # lista_2 = [100, 200, 300]

# ----------------------------
# extend a lista_2
print('\nextend a lista_2\n')
# ----------------------------

lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

lista_2.extend(lista_1)

print( "lista_1 =" , lista_1 ) # lista_1 = ['A', 'B', 'C']
print( "lista_2 =" , lista_2 ) # lista_2 = [100, 200, 300, 'A', 'B', 'C']


# ---------------------------------------------
# lo mismo que usar concatenación
print('\nlo mismo que usar concatenación\n')
# ---------------------------------------------

# original
lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

lista_1 += lista_2

print( 'lista_1 =', lista_1 ) # lista_1 = ['A', 'B', 'C', 100, 200, 300]

# ------------------

lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

lista_2 += lista_1

print( 'lista_2 =', lista_2 ) # lista_2 = [100, 200, 300, 'A', 'B', 'C']




#? 15) .reverse()
print('\n15) .reverse()')
# - para revertir el orden de la lista
# * modifica la lista original

lista_1 = [10, 50, -60, 20, 100.5, 90,8]
lista_2 = [ 'python', 'java', 'c++', 'pascal' ]

print('\nListas Originales\n')
print( lista_1 ) # [10, 50, -60, 20, 100.5, 90, 8]
print( lista_2 ) # ['python', 'java', 'c++', 'pascal']

print('\nAplicando .reverse()\n')
lista_1.reverse()
lista_2.reverse()

print( lista_1 ) # [8, 90, 100.5, 20, -60, 50, 10]
print( lista_2 ) # ['pascal', 'c++', 'java', 'python']
