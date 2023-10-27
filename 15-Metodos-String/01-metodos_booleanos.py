# ================================================================================
# Métodos booleanos de los String

# - Se llaman métodos booleanos
# - Porque al aplicarlos devuelven un valor booleano
# - Es decir, True o False

'''
Método        |  Descripción
--------------|----------------------------------------------------------------
.isalpha()    |  True si todos los caracteres son alfabéticos (A-Z)
.isalnum()    |  True si los caracteres son sólo letras y/o números (A-Z) (0-9)
.isdigit()    |  True si el string es numérico - entero
.islower()    |  True si todos los caracteres son minúsculas
.isupper()    |  True si todos los caracteres son mayúsculas
.istitle()    |  True si el string tiene formato de título
.startswith() |  True si el string comienza con caracter o substring indicado
.endswith()   |  True si el string finaliza con caracter o substring indicado
.isspace()    |  True si el string tiene solo espacios vacíos
'''
# ================================================================================

#? 1) .isalpha()
print('\n1) .isalpha()')
# - True si todos los caracteres son alfabéticos (A-Z)
# - van escuchar: retorna / devuelve True 

var_1 = 'abcde'
var_2 = 'XYZabc'
var_3 = 'abc1'
var_4 = 'a bcde'
var_5 = ''
var_6 = ' '
var_7 = 'abc#'

# TEST
"""
#!    var_1.isalpha() # método
#!    type(var_1) # función

print( var_1.isalpha() )
respuesta = var_1.isalpha()
print( respuesta, type(respuesta) )
"""

print( var_1, '|', var_1.isalpha() ) # abcde | True
print( var_2, '|', var_2.isalpha() ) # XYZabc | True
print( var_3, '|', var_3.isalpha() ) # abc1 | False
print( var_4, '|', var_4.isalpha() ) # a bcde | False
print( var_5, '|', var_5.isalpha() ) #  | False
print( var_6, '|', var_6.isalpha() ) #   | False
print( var_7, '|', var_7.isalpha() ) # abc# | False





#? 2) .isalnum()
print('\n2) .isalnum()')
# - True si los caracteres son sólo letras y/o números (A-Z) (0-9)
# - is alphanumeric?
# - revisa si es alfa-numérico

var_1 = '12345'
var_2 = 'ABCdef'
var_3 = '123XYZ'
var_4 = '123 XYZ'
var_5 = 'abc$123'

print( var_1, '|', var_1.isalnum() ) # 12345 | True
print( var_2, '|', var_2.isalnum() ) # ABCdef | True
print( var_3, '|', var_3.isalnum() ) # 123XYZ | True
print( var_4, '|', var_4.isalnum() ) # 123 XYZ | False
print( var_5, '|', var_5.isalnum() ) # abc$123 | False


#? 3) .isdigit()
print('\n3) .isdigit()')
# - True si el string es numérico - entero
#! entero
# '123'

var_1 = '123'
var_2 = '123.56'
var_3 = '123,56'
var_5 = '123a'
var_6 = '12 3'
var_7 = '0'
var_8 = ' 0'


print( var_1, '|', var_1.isdigit() ) # 123 | True
print( var_2, '|', var_2.isdigit() ) # 123.56 | False
print( var_3, '|', var_3.isdigit() ) # 123,56 | False
print( var_4, '|', var_4.isdigit() ) # 123 XYZ | False
print( var_5, '|', var_5.isdigit() ) # 123a | False
print( var_6, '|', var_6.isdigit() ) # 12 3 | False
print( var_7, '|', var_7.isdigit() ) # 0 | True
print( var_8, '|', var_8.isdigit() ) #  0 | False



#? 4) .islower()
print('\n4) .islower()')
# - True si todos los caracteres son minúsculas

var_1 = 'hola sebastián'
var_2 = 'Hola mundo'
var_3 = '  hola mundo'
var_4 = 'me gusta python 123'
var_5 = 'me gusta pythOn 123'

print( var_1, '|', var_1.islower() ) # hola sebastián | True
print( var_2, '|', var_2.islower() ) # Hola mundo | False
print( var_3, '|', var_3.islower() ) #   hola mundo | True
print( var_4, '|', var_4.islower() ) # me gusta python 123 | True
print( var_5, '|', var_5.islower() ) # me gusta pythOn 123 | False



#? 5) .isupper()
print('\n5) .isupper()')
# - True si todos los caracteres son mayúsculas

var_1 = 'hOLA'
var_2 = 'Hola Mundo'
var_3 = 'PYTHON'
var_4 = 'PYTHON  '
var_5 = 'PYTHON  a'

print( var_1, '|', var_1.isupper() ) # hOLA | False
print( var_2, '|', var_2.isupper() ) # Hola Mundo | False
print( var_3, '|', var_3.isupper() ) # PYTHON | True
print( var_4, '|', var_4.isupper() ) # PYTHON   | True
print( var_5, '|', var_5.isupper() ) # PYTHON  a | False


#? 6) .istitle()
print('\n6) .istitle()')
# - True si el string tiene formato de título
# - cuando las palabras de un string comienzan con mayúscula
# - la 1era letra de cada palabra d eun texto

var_1 = 'Hola'
var_2 = 'Hola Mundo'
var_3 = 'Hola mundo'
var_4 = 'hola mundo'
var_5 = 'hola Mundo'
var_6 = 'holaMundo'
var_7 = 'HolaMundo'


print( var_1, '|', var_1.istitle() ) # Hola | True
print( var_2, '|', var_2.istitle() ) # Hola Mundo | True
print( var_3, '|', var_3.istitle() ) # Hola mundo | False
print( var_4, '|', var_4.istitle() ) # hola mundo | False
print( var_5, '|', var_5.istitle() ) # hola Mundo | False
print( var_6, '|', var_6.istitle() ) # holaMundo | False
print( var_7, '|', var_7.istitle() ) # HolaMundo | False



#? 7) .startswith()
print('\n7) .startswith()')
# - True si el string comienza con caracter o substring indicado

var_1 = 'aprendiendo python'
print( "var_1.startswith('a') =>", var_1.startswith('a') ) # True
print( "var_1.startswith('') =>", var_1.startswith('') ) # True
print( "var_1.startswith(' ') =>", var_1.startswith(' ') ) # False
print( "var_1.startswith('A') =>", var_1.startswith('A') ) # False


var_2 = ' HEllo World'
print()
print( "var_2.startswith('H') =>", var_2.startswith('H') ) # False
print( "var_2.startswith(' H') =>", var_2.startswith(' H') ) # True
print( "var_2.startswith(' HE') =>", var_2.startswith(' HE') ) # True
print( "var_2.startswith(' HEllo W') =>", var_2.startswith(' HEllo W') ) # True
print( "var_2.startswith(' HEllo WO') =>", var_2.startswith(' HEllo WO') ) # False



#? 8) .endswith()
print('\n8) .endswith()')
# - True si el string finaliza con caracter o substring indicado
# todo string comienza y termina con un string vacío => ''

var_1 = 'aprendo PythON'

print("var_1.endswith('') =>" , var_1.endswith('')) # True
print("var_1.endswith('N') =>" , var_1.endswith('N')) # True
print("var_1.endswith('ON') =>" , var_1.endswith('ON')) # True
print("var_1.endswith(' ON') =>" , var_1.endswith(' ON')) # False
print("var_1.endswith('o PythON') =>" , var_1.endswith('o PythON')) # True



#? 9) .isspace()
print('\n9) .isspace()')
# - True si el string tiene solo espacios vacíos

var_1 = '' # no es espacio
var_2 = ' '
var_3 = '\t'
var_4 = '\n'
var_5 = ' 1'
var_6 = 'XYZ'

print( var_1, '|', var_1.isspace() ) # False
print( var_2, '|', var_2.isspace() ) # True
print( var_3, '|', var_3.isspace() ) # True
print( var_4, '|', var_4.isspace() ) # True
print( var_5, '|', var_5.isspace() ) # False
print( var_6, '|', var_6.isspace() ) # False


# EXTRA
print('\n\nEXTRA')

nombre = 'python'

print( nombre.islower() ) # True
print( 'Python'.islower() ) # False
print( 'java'.islower() ) # True

num = 5
#num.islower()
#! AttributeError: 'int' object has no attribute 'islower'

#print( 10.isupper() )
#10.isupper()
#! SyntaxError: invalid syntax

verdadero = True
#verdadero.isalpha()
#! AttributeError: 'bool' object has no attribute 'isalpha'