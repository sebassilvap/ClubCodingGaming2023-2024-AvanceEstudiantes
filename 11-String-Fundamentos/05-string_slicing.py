# =============================================================
# String Slicing

# - Slicing es una técnica para construir subcadenas de texto
# - substrings
# - a partir de los índices del string original

#* string[ inicio : final ]
# => inicio - incluyente
# => final  - excluyente
# =============================================================


#? 1) Slicing con índices positivos
print('\n1) Slicing con índices positivos')

palabra = 'programa'
#(+)       01234567
#(-)       87654321



#? 2) Slicing con índices negativos
print('\n2) Slicing con índices negativos')
# - Recordar que aunque sea índice negativo
# - El 'END' => sigue siendo exclusivo


#? 3) El Slicing no tiene Index Error
print('\n3) El Slicing no tiene Index Error')

palabra = 'Python'
#(+)       012345


#? 4) Pequeño adelanto => casting de variables | casting a número entero
print('\n4) Pequeño adelanto => casting de variables | casting a número entero')



# - veremos a profundidad el tema casting en la siguiente lección
# - por el momento entender que es la manera
# - como podemos transformar de un tipo de variable a otro



# - en este caso los números flotantes han sido transformados a enteros
# - prácticamente la parte decimal desaparece
# - y nos quedamos con la parte entera
# - Si recordamos la función len()
# - esta nos devuelve como entero la longitud de una cadena


#? 5) Dividir cualquier palabra a la mitad => slicing + len()
print('\n5) Dividir cualquier palabra a la mitad => slicing + len()')

palabra_1 = 'programa'
#(+)         01234567

palabra_2 = 'sol'
#(+)         012



# - obviamente la división de una palabra funciona al 100%
# - si el tamaño (número de caracteres) del string es PAR
# - en el segundo ejemplo como son 3 letras
# - divide en 1 y 2 letras respectivamente