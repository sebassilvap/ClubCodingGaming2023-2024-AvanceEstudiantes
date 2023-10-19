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

var_1 = 'abcde'
var_2 = 'XYZabc'
var_3 = 'abc1'
var_4 = 'a bcde'
var_5 = ''
var_6 = ' '
var_7 = 'abc#'



#? 2) .isalnum()
print('\n2) .isalnum()')
# - True si los caracteres son sólo letras y/o números (A-Z) (0-9)
# - is alphanumeric?

var_1 = '12345'
var_2 = 'ABCdef'
var_3 = '123XYZ'
var_4 = '123 XYZ'
var_5 = 'abc$123'



#? 3) .isdigit()
print('\n3) .isdigit()')
# - True si el string es numérico - entero

var_1 = '123'
var_2 = '123.56'
var_3 = '123,56'
var_5 = '123a'
var_6 = '12 3'
var_7 = '0'
var_8 = ' 0'



#? 4) .islower()
print('\n4) .islower()')
# - True si todos los caracteres son minúsculas

var_1 = 'hola sebastián'
var_2 = 'Hola mundo'
var_3 = '  hola mundo'



#? 5) .isupper()
print('\n5) .isupper()')
# - True si todos los caracteres son mayúsculas

var_1 = 'hOLA'
var_2 = 'Hola Mundo'
var_3 = 'PYTHON'
var_4 = 'PYTHON  '
var_5 = 'PYTHON  a'



#? 6) .istitle()
print('\n6) .istitle()')
# - True si el string tiene formato de título

var_1 = 'Hola'
var_2 = 'Hola Mundo'
var_4 = 'Hola mundo'
var_5 = 'hola mundo'
var_6 = 'hola Mundo'
var_7 = 'holaMundo'
var_8 = 'HolaMundo'



#? 7) .startswith()
print('\n7) .startswith()')
# - True si el string comienza con caracter o substring indicado

var_1 = 'aprendiendo python'


var_2 = ' HEllo World'



#? 8) .endswith()
print('\n8) .endswith()')
# - True si el string finaliza con caracter o substring indicado

var_1 = 'aprendo PythON'



#? 9) .isspace()
print('\n9) .isspace()')
# - True si el string tiene solo espacios vacíos

var_1 = ''
var_2 = ' '
var_3 = '\t'
var_4 = '\n'
var_5 = ' 1'
var_6 = 'XYZ'