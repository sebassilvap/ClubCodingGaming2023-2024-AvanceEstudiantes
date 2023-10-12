# =======================================================
# Métodos para dar formato a un string

# - Lista de los métodos más importantes
# - No afectan la variable original
# - Transforman al string para un propósito específico
# =======================================================

#? 1) Para cambiar el tipo
print('\n1) Para cambiar el tipo')
# .capitalize() => Primera letra con mayúscula
# .title()      => Primera letra de cada palabra con mayúscula
# .upper()      => Todo en mayúsculas
# .lower()      => Todo en minúsculas
# .swapcase()   => Invierte el case del texto



#! NOTA IMPORTANTE
# - veremos más luego que algunos métodos MODIFICAN la variable original
# - en este caso los métodos de string no lo hacen
# - para ver su funcionamiento tenemos:
# - que hacer un print
# - guardarlos en otra variable


#? 2) Para justificación del texto
print('\n2) Para justificación del texto')
# .center(x) => Justificación al centro en x espacios
# .ljust(x) => Justificación a la izquierda en x espacios
# .rjust(x) => Justificación a la derecha en x espacios


# .center(x)


# .ljust(x)


# .rjust(x)



#? 3) Conteo de caracteres repetidos
print('\n3) Conteo de caracteres repetidos')
# .count(substring, start, end) => búsqueda de izquierda a derecha con inicio y fin opcionales

var_1 = 'nunca digas nunca en esta vida.'
#(+)     0123456789012345678901234567890
#        0         1         2         3

# .count()


#? 4) Búsqueda por caracter => Retorno de índice CON ERROR
print('\n4) Búsqueda por caracter => Retorno de índice CON ERROR')
# .index(substring, start, end) => búsqueda de un caracter de izquierda a derecha
# .rindex(substring, start, end) => búsqueda de un caracter de derecha a izquierda

var_1 = 'contextualización'
#(+)     01234567890123456
#        0         1

# .index()
print('\nUtilizando .index()')


# .rindex()
print('\nUtilizando .rindex()')


#? 5) Búsqueda por caracter => Retorno de índice SIN ERROR
print('\n5) Búsqueda por caracter => Retorno de índice SIN ERROR')
# find(substring, start, end)
# rfind(substring, start, end)

# => básicamente lo mismo que index
# => pero no devuelve error si no encuentra
# => en su lugar devuelve -1

var_1 = 'contextualización'
#(+)     01234567890123456
#        0         1

# .find()


# .rfind()
var_1 = 'Xuna palabraX que se forma conX'



#? 6) Eliminar espaciados y caracteres
print('\n6) Eliminar espaciados y caracteres')
# .strip()  => eliminación a ambos lados
# .lstrip() => eliminación a la izquierda
# .rstrip() => eliminación a la derecha
# => por defecto sin argumento elimina todo tipo de espaciado


# .strip()


# .lstrip() y .rstrip()


#? 7) .join()
print('\n7) .join()')
# - Une cada caracter de una cadena
# - Con el valor de otra cadena


#? 8) .split()
print('\n8) .split()')
# - transforma una cadena en una lista
#! TEMA Listas: Ya lo veremos a profundidad luego
# - básicamente una lista es una colección de datos
# - cuando no se da el parámetro por defecto separa por espacios



#! Ya veremos luego => len() también se puede aplicar en listas
# - en este caso len devuelve el número de elementos en la lista


#? 9) .splitlines()
print('\n9) .splitlines()')
# - transforma un string en lista
# - separando los saltos de línea (\n)

texto = 'Yo programo en Python\nEl programa en Java\nElla en C++'


# - Se acopla de mejor manera a un string multilínea

poema = '''
En una noche de verano
Yo la conocí
Nunca lo olvidé
Siempre la recordaré
'''


#? 9) .expandtabs()
print('\n9) .expandtabs()')
# - como su nombre lo indica
# - sirve para incrementar el tamaño de un tab
# - dentro de un string


#? 10) .replace()
print('\n10) .replace()')
#! UNO DE LOS MÁS IMPORTANTES
# - para reemplazar un caracter o subcadena
# - dentro de una cadena

# => reemplazando un caracter


# => reemplazando una subcadena (substring)
