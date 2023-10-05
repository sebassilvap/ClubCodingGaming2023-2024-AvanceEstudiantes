# =========================================================================================
# Secuencias de Escape

# SECUENCIA  NOMBRE           DEFINICIÓN
#   \\       Backslash        Para insertar el caracter \ en un String
#   \'       Comilla Simple   Para insertar la comilla simple en un String
#   \"       Comilla doble    Para insertar la comilla doble en un String
#   \b       Retroceso        Elimina un caracter del String al momento de aparecer en el output de la consola.
#   \f       Formfeed         Imprime una nueva línea indentada al final de la línea anterior.
#   \v       Tab Vertical     Realiza lo mismo que el Formfeed
#   \t       Tab Horizontal   Inserta un espaciado de tabulación
#   \r       Carriage return  Inserta los caracteres después de \r al inicio del String
#   \n       Nueva Línea      Inserta un salto del línea en tabulación 0
# =========================================================================================

#? 1)  \\ Backslash
print('---------------------')
print('1)  \\ Backslash')
print('---------------------')

print('sebas \python')
print('sebas \\python')

print('Aquí voy a escribir una línea 1')
print('Aquí voy a escribir una línea 2')

print('Aquí voy a escribir una línea 1\nAquí voy a escribir una línea 2')

print('Esta secuencia \n me sirve para poner nueva línea')

print('Esta secuencia \\n me sirve para poner nueva línea')

print('Esta es la manera segura de poner un backslash \\')

var_1 = 'Esta es la manera segura de poner un backslash \\'
var_2 = 'Hola\nMe llamo Sebas\nMe gusta Python'
var_3 = "Recuerden que con \\n ponemos una nueva línea"

print(var_1)
print(var_2)
print(var_3)




#? 2) \' Comilla Simple
#? 3) \" Comilla Doble
print()
print('---------------------')
print('2) \' Comilla Simple')
print('3) \" Comilla Doble')
print('---------------------')

string_1 = 'python'
string_2 = "python c"
string_3 = '''python java'''
string_4 = """sebas python profe"""

print( string_1 , type(string_1) )
print( string_2 , type(string_2) )
print( string_3 , type(string_3) )
print( string_4 , type(string_4) )

#string_5 = "esta "palabra" es especial"
string_5 = "esta \"palabra\" es especial"
print(string_5)

string_5 = 'esta "palabra" es especial' # por eso es que python me permite utilizar ' ó " para el string
print(string_5)

string_5 = "esta 'palabra' es especial"
print(string_5)

string_6 = 'esto es un poema muy \'lindo\' espero les guste'
print(string_6)


#? 4) \b Retroceso
# - elimina el caracter que tiene a la izquierda

print()
print('---------------------')
print('4) \b Retroceso')
print('---------------------')

print('palabra')
print('pala\bbra')
print('Hola Sebas Silva')
print('Hola \bSebas \bSilva')



#? 5) \f Formfeed
# - Para añadir nueva línea con tab secuencial
# - Puede ser que algunos editores de código no lo reconozcan
print()
print('---------------------')
print('5) \f Formfeed')
print('---------------------')

print('HolaSebasSilva')
print('Hola\fSebas\fSilva')



#? 6) \v Tab Vertical
# - Hace lo mismo que el Formfeed
# - Puede ser que algunos editores de código no lo reconozcan

print()
print('---------------------')
print('6) \v Tab Vertical')
print('---------------------')

print('HolaSebasSilva')
print('Hola\vSebas\vSilva')


#? 7) \t Tab Horizontal
# - Para introducir un espaciado de tab

print()
print('---------------------')
print('7) \t Tab Horizontal')
print('---------------------')

print('HolaAmigoSebasSilva')
print('Hola\tAmigo\tSebas\tSilva')
print('Hola\t\tAmigo\t\tSebas\tSilva')

print('Dato 1\tMoneda\tdolar')
print('Dato 2\tComida\tpizza')
print('Dato 3\tValor\t532.2')



#? 8) \r Carriage Return
# - Básicamente toma lo que tiene a la derecha
# - Y lo pone al inicio
# - Ocupando el número de caracteres de lo que hay a la derecha
print()
print('---------------------')
print('8) \r Carriage Return')
print('---------------------')

print('abcdef xyz')
print('abcdef\rxyz')
print('abcdef\r123')

# - Se ejecuta de izquierda a derecha (?)
print('abcdef\rxyz\r12')
# abcdef\r12z
# 12zdef


#? 9) \n Nueva línea
#! IMPORTANTE

print('\n---------------------')
print('9) Nueva línea')
print('---------------------')

# - Inserta un nuevo salto de línea

print('HolaMisQueridosAlumnos')
print('Hola\nMis\nQueridos\nAlumnos')


# - ahora podremos olvidarnos de esta técnica
print('Línea 1')
print('Línea 2')
print()
print('Línea 3')
print('Línea 4')
print('')
print('Línea 5')

print('-------------')
print('Línea 1')
print('Línea 2')
print('\nLínea 3')
print('Línea 4')
print('\nLínea 5')