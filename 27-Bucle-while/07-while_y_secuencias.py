# ===============================================================================
# Usando while para iterar secuencias de datos

# - aunque el bucle por excelencia para iterar secuencias en python es el => for
# - también podemos usar while usando un contador externo
#!  las secuencias son aquellas a las cuales podemos acceder con sus índices

# - por el momento hemos visto 3 secuencias: string, lista, range
# ===============================================================================


#? 1) while iterando string
print('\n1) while iterando string')

cadena = 'python'
#         012345

print( cadena , type(cadena) )
print( 'cadena[0] =' , cadena[0] ) # cadena[0] = p
print( 'cadena[1] =' , cadena[1] ) # cadena[1] = y
print( 'cadena[2] =' , cadena[2] ) # cadena[2] = t
print( 'cadena[3] =' , cadena[3] ) # cadena[3] = h
print( 'cadena[4] =' , cadena[4] ) # cadena[4] = o
print( 'cadena[5] =' , cadena[5] ) # cadena[5] = n

# while + contador
print()

index = 0

while index < len(cadena): #* OK
    print( 'cadena['+str(index) + '] =', cadena[index] )
    index += 1
# end while

# cadena[0] = p
# cadena[1] = y
# cadena[2] = t
# cadena[3] = h
# cadena[4] = o
# cadena[5] = n

#! importante fijar correctamente la condición del while
#! de otra manera caemos en un index error

"""
while index <= len(cadena):
    print( 'cadena['+str(index) + '] =', cadena[index] )
    index += 1
# end while

#! IndexError: string index out of range"
"""


#? 2) while iterando listas
print('\n2) while iterando listas')

frutas = ['manzana','piña','durazno','uvas','banana']
#             0        1       2       3       4

for fruta in frutas:
    print(fruta)
# end for

print()

print( frutas , '|' , type(frutas), '|', len(frutas) )
print( 'frutas[0] =' , frutas[0] ) # frutas[0] = manzana
print( 'frutas[1] =' , frutas[1] ) # frutas[1] = piña
print( 'frutas[2] =' , frutas[2] ) # frutas[2] = durazno
print( 'frutas[3] =' , frutas[3] ) # frutas[3] = uvas
print( 'frutas[4] =' , frutas[4] ) # frutas[4] = banana

# utilizando while

print()

index = 0

while index < len(frutas): #* OK
    print('frutas[' + str(index) + '] =', frutas[index])
    index += 1
# end while

# frutas[0] = manzana
# frutas[1] = piña
# frutas[2] = durazno
# frutas[3] = uvas
# frutas[4] = banana

"""
index = 0

while index <= len(frutas): #* OK
    print('frutas[' + str(index) + '] =', frutas[index])
    index += 1
# end while

#! IndexError: list index out of range
"""


#? 3) while iterando range
print('\n3) while iterando range')

# => recordar el rango
rango_1_5 = range(1, 6)
print( rango_1_5, '|', type(rango_1_5), '|', len(rango_1_5) ) # range(1, 6) | <class 'range'> | 5
print( 'rango_1_5[0] =' , rango_1_5[0] ) # rango_1_5[0] = 1
print( 'rango_1_5[1] =' , rango_1_5[1] ) # rango_1_5[1] = 2
print( 'rango_1_5[2] =' , rango_1_5[2] ) # rango_1_5[2] = 3
print( 'rango_1_5[3] =' , rango_1_5[3] ) # rango_1_5[3] = 4
print( 'rango_1_5[4] =' , rango_1_5[4] ) # rango_1_5[4] = 5
#print( 'rango_1_5[5] =' , rango_1_5[5] ) #! IndexError: range object index out of range

# => range + while

print()

index = 0 #! importante

while index < len(rango_1_5):
    print( 'rango_1_5[' + str(index) + '] =' , rango_1_5[index] )
    index += 1
# end while

# rango_1_5[0] = 1
# rango_1_5[1] = 2
# rango_1_5[2] = 3
# rango_1_5[3] = 4
# rango_1_5[4] = 5