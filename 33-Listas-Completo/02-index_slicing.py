# =================================
# Listas - Completo

# => Indexing & Slicing
# =================================


#? 1) Indexing
print('\n1) Indexing')
# - Acceder a los subelementos
# - de elementos iterables
# - por medio de su index / posición

lista = [100,200,300,400,500]
#(+)      0   1   2   3   4
#(-)      5   4   3   2   1 

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
#print(lista[5]) #! IndexError: list index out of range

# => cómo acceder al último elemento
print( lista[-1] ) # 500



#? 2) Slicing
print('\n2) Slicing')
# - técnica para acceder a una sublista
# - de una lista dada
# - recordar que el end es exclusivo
# *      [start : end : step]


letras = ['a','b','c','d','e','f','g','h']
#          0   1   2   3   4   5   6   7

print( letras , type(letras) , len(letras) ) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] <class 'list'> 8

print( letras[0:4] ) # ['a', 'b', 'c', 'd']
print( letras[3:8] ) # ['d', 'e', 'f', 'g', 'h']
print('-----')
print( letras[:4] ) # ['a', 'b', 'c', 'd']
print( letras[3:] ) # ['d', 'e', 'f', 'g', 'h']
print('-----')
print( letras[1:7:2] ) # ['b', 'd', 'f']

# => salto para toda la lista
print( letras[::1] ) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print( letras[::2] ) # ['a', 'c', 'e', 'g']
print( letras[::3] ) # ['a', 'd', 'g']
print( letras[::4] ) # ['a', 'e']
print('-----')

# => dato curioso
print(letras[::]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letras) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']



#? 3) IndexError
print('\n3) IndexError')
# - se produce en el indexing
# - más no en el slicing

lista = [1,2,3,4,5]
#(+)     0 1 2 3 4
#(-)     5 4 3 2 1

# EJ: en slicing
print( lista[2:1000] ) # [3, 4, 5]

# EJ: en el indexing
#print( lista[1000] ) #! IndexError: list index out of range
#print(lista[-6]) #! IndexError: list index out of range
