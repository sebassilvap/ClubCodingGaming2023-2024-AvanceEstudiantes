# =============================================================
# String Slicing

# - Slicing es una técnica para construir subcadenas de texto
# - substrings
# - a partir de los índices del string original

#* string[ inicio : final ]
#  => inicio - incluyente
#! => final  - excluyente
# =============================================================


#? 1) Slicing con índices positivos
print('\n1) Slicing con índices positivos')

palabra = 'programa'
#(+)       01234567
#(-)       87654321

print( palabra[0:2] )
print( palabra[0:3] )
print( palabra[:3] )
print( palabra[:] )
print()
print( palabra[3:7] )
print( palabra[3:8] )
print( palabra[3:10] )
print( palabra[3:100] )
print( palabra[3:1000] )
print( palabra[3:] )
print()
print( palabra[-1:3], 't' )
print( palabra[3:-1], 't' )


#? 2) Slicing con índices negativos
print('\n2) Slicing con índices negativos')
# - Recordar que aunque sea índice negativo
# - El 'END' => sigue siendo exclusivo

palabra = 'programa'
#(+)       01234567
#(-)       87654321

print( palabra[-8:-5] )
print( palabra[-8:-6] )
print()
print( palabra[-5:-1] )
print( palabra[-5:0], 't' )
print( palabra[-5:] ) #! útil


#? 3) El Slicing no tiene Index Error
print('\n3) El Slicing no tiene Index Error')

palabra = 'Python'
#(+)       012345

palabra[5]
#palabra[6] #! IndexError: string index out of range

print( palabra[0:3] )
print( palabra[3:6] )
print( palabra[3:8] )
print( palabra[3:1000] )
print()
print( palabra[-80:3] )



#? 4) Pequeño adelanto => casting de variables | casting a número entero
print('\n4) Pequeño adelanto => casting de variables | casting a número entero')

# float
num_1 = 4.2
num_2 = 4.5
num_3 = 4.9

print( num_1, type(num_1) )
print( num_2, type(num_2) )
print( num_3, type(num_3) )

# - veremos a profundidad el tema casting en la siguiente lección
# - por el momento entender que es la manera
# - como podemos transformar de un tipo de variable a otro

ent_1 = int(num_1)
ent_2 = int(num_2)
ent_3 = int(num_3)

print()
print( ent_1, type(ent_1) )
print( ent_2, type(ent_2) )
print( ent_3, type(ent_3) )

# - en este caso los números flotantes han sido transformados a enteros
# - prácticamente la parte decimal desaparece
# - y nos quedamos con la parte entera
# - Si recordamos la función len()
# - esta nos devuelve como entero la longitud de una cadena

cadena = 'hola'
print(cadena, len(cadena))


#? 5) Dividir cualquier palabra a la mitad => slicing + len()
print('\n5) Dividir cualquier palabra a la mitad => slicing + len()')

palabra_1 = 'programa'
#(+)         01234567

palabra_1 = 'sol'
#(+)         012

palabra_1 = 'contextualizacion'

print( 'len(palabra_1) = ', len(palabra_1))
#print( 'len(palabra_2) = ', len(palabra_2))

print('Dividir esta palabra_1 con len()')
final_primera_mitad = int( len(palabra_1) / 2 )

print( final_primera_mitad, type(final_primera_mitad) )

palabra_1_primera_mitad = palabra_1[:final_primera_mitad]
palabra_1_segunda_mitad = palabra_1[final_primera_mitad:]

print(palabra_1_primera_mitad)
print(palabra_1_segunda_mitad)


# - obviamente la división de una palabra funciona al 100%
# - si el tamaño (número de caracteres) del string es PAR
# - en el segundo ejemplo como son 3 letras
# - divide en 1 y 2 letras respectivamente