# ===========================================================================
# Función Interna range (built-in functions en Python)

# - para crear una secuencia de números
#*        range(start, end, step)

# - start: parámetro opcional, 0 por default, establece inicio (inclusivo)
# - end: parámetro obligatorio, establece final (exclusivo)
# - step: prámetro opcional, establece incremento, 1 por default

#! RECORDAR: los tipos de datos en Python
'''
https://www.w3schools.com/python/python_datatypes.asp

----------------------------------------------------
Text Type:	     |    str(OK)
Numeric Types:   |    int(OK), float(OK), complex
Sequence Types:  |    list(OK), tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool(OK)
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType(OK)
----------------------------------------------------
'''

# - como vemos range es uno de los tipos de datos para secuencia
# ===========================================================================


#? 1) Creación Básica de Rangos
print('\n1) Creación Básica de Rangos\n')
# - range(start, end, step)

# rango de 0 al 9
rango_0_9 = range(10) # recuerden => end exclusivo

# rango del 20 al 30
rango_20_30 = range(20, 31)

# rango del 50 al 100 en saltos de 10
rango_50_100_10 = range(50,101,10)

# resultados

print( 'rango_0_9 = ' , rango_0_9 , '|' , type(rango_0_9) )
print( 'rango_20_30 = ' , rango_20_30 , '|' , type(rango_20_30) )
print( 'rango_50_100_10 = ' , rango_50_100_10 , '|' , type(rango_50_100_10) )

# rango_0_9 =  range(0, 10) | <class 'range'>
# rango_20_30 =  range(20, 31) | <class 'range'>
# rango_50_100_10 =  range(50, 101, 10) | <class 'range'>

# --------------------------------------------------------------------------------
# - como vemos se imprime tal y como se crea
# - así como está posiblemente no vemos su utilidad
# - pero podemos usar casting y transformarlo a algo útil
# - ej: a una lista
# - el casting puede darse no solo como vimos sino entre algunos tipos de datos
# --------------------------------------------------------------------------------



#? 2) Casting de range a list => list()
print('\n2) Casting de range a list => list()\n')

lista_0_9 = list( rango_0_9 )
lista_20_30 = list( rango_20_30 )
lista_50_100_10 = list( rango_50_100_10 )

# resultados

print( 'lista_0_9 =' , lista_0_9 )
print( 'lista_20_30 =' , lista_20_30 )
print( 'lista_50_100_10 =' , lista_50_100_10 )

# lista_0_9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista_20_30 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# lista_50_100_10 = [50, 60, 70, 80, 90, 100]


#? 3) Su uso fundamental => bucle for
print('\n3) Su uso fundamental => bucle for\n')
# ! IMPORTANTE: esto es un abrebocas del tema bucles (ya lo veremos a continuación)
# - el uso fundamental del range es con el bucle for
# - para crear una iteración numérica

# => por ejemplo tomando en cuenta la lista creada anteriormente => lista_0_9

for elemento in lista_0_9:
    print(elemento)
# end for

print()

lista = ['a','b','c']

for letra in lista:
    print(letra)
#end for

# => pero antes de hacer toda esta transformación podemos usar directamente el range

print()

for numero in range(0,10):
    print('Número =', numero)
# end for

# ------------------------------------------------------
# ! IMPORTANTE
# - el range nos brinda una manera útil de iterar
# - un range existe como definición
# - ocupa memoria al momento que lo utilizamos en bucle
# - o cuando le hacemos casting a una lista
# - pero como definición no ocupa espacio
# ------------------------------------------------------



#? 4) Indexing, Slicing & len en range
print('\n4) Indexing & Slicing en range')
# - de esta manera podemos también
# - acceder a los elementos creados en la definición de un range

range1a10 = range(1,11) # start, end / end es exclusivo
print(range1a10 , type(range1a10)) # range(1, 11) <class 'range'>

print('\nIndexing en el range: ')
print( 'range1a10[0] =' , range1a10[0] ) # range1a10[0] = 1
print( 'range1a10[1] =' , range1a10[1] ) # range1a10[1] = 2
print( 'range1a10[2] =' , range1a10[2] ) # range1a10[2] = 3
print( 'range1a10[3] =' , range1a10[3] ) # range1a10[3] = 4
print( 'range1a10[-1] =' , range1a10[-1] ) # range1a10[-1] = 10

print('\nSlicing en el range: ')
# - recordar que en el slicing
# - start, end, step
# - end => exclusivo
print( 'range1a10[4:8] =' , range1a10[4:8] , type(range1a10[4:8]) )
print( 'range1a10[:4] =' , range1a10[:4] , type(range1a10[:4]) )
print( 'range1a10[4:] =' , range1a10[4:] , type(range1a10[4:]) )
print( 'range1a10[2:8:2] =' , range1a10[2:8:2] , type(range1a10[2:8:2]) )
# range1a10[4:8] = range(5, 9) <class 'range'>
# range1a10[:4] = range(1, 5) <class 'range'>
# range1a10[4:] = range(5, 11) <class 'range'>
# range1a10[2:8:2] = range(3, 9, 2) <class 'range'>

print('\nlen() en range: ')
rango_1_100 = range(1, 101)
size = len( rango_1_100 )

print(rango_1_100) # range(1, 101)
print(size) # 100
