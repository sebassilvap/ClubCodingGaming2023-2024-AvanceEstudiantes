# =======================================================
# Métodos para dar formato a un string

# - Lista de los métodos más importantes
# ! No afectan la variable original
# - Transforman al string para un propósito específico
# =======================================================


#? 1) Para cambiar el tipo
print('\n1) Para cambiar el tipo')
#   .capitalize() => Primera letra con mayúscula
#   .title()      => Primera letra de cada palabra con mayúscula
#   .upper()      => Todo en mayúsculas
#   .lower()      => Todo en minúsculas
#   .swapcase()   => Invierte el case del texto

var_1 = 'Me gusta APRENDER PythoN.'

print( 'var_1 =', var_1 )
print( 'var_1.capitalize() =', var_1.capitalize() )
print( 'var_1.title() =', var_1.title() )
print( 'var_1.upper() =', var_1.upper() )
print( 'var_1.lower() =', var_1.lower() )
print( 'var_1.swapcase() =', var_1.swapcase() )


# -----------------------------------------------------------------------
# ! NOTA IMPORTANTE
# - veremos más luego que algunos métodos MODIFICAN la variable original
# - en este caso los métodos de string no lo hacen
# - para ver su funcionamiento tenemos:
# - que hacer un print
# - guardarlos en otra variable
# -----------------------------------------------------------------------

var_1 = 'Me gusta APRENDER PythoN.'
print(var_1)

var_1.upper()
print(var_1)

var_1_mayusculas = var_1.upper()
print(var_1_mayusculas) # podemos visualizar
print(var_1.upper()) # podemos visualizar



#? 2) Para justificación del texto
print('\n2) Para justificación del texto')
#   .center(x) => Justificación al centro en x espacios
#   .ljust(x) => Justificación a la izquierda en x espacios
#   .rjust(x) => Justificación a la derecha en x espacios

var_1 = 'python'
#        012345

print( 'var_1 =', var_1, 'len =', len(var_1) )


# .center(x)
print()
center_10 = var_1.center(10) #   python  
center_20 = var_1.center(20) #        python
print(center_10)
print(center_20)
print( 'center_10 =', center_10, 'len =', len(center_10) )
print( 'center_20 =', center_20, 'len =', len(center_20) )


# .ljust(x)
print()
ljust_10 = var_1.ljust(10)
ljust_20 = var_1.ljust(20)

print( 'ljust_10 =', ljust_10, 'len =', len(ljust_10) )
print( 'ljust_20 =', ljust_20, 'len =', len(ljust_20) )

# .rjust(x)
print()
rjust_10 = var_1.rjust(10)
rjust_20 = var_1.rjust(20)

print( 'rjust_10 =', rjust_10, 'len =', len(rjust_10) )
print( 'rjust_20 =', rjust_20, 'len =', len(rjust_20) )



#? 3) Conteo de caracteres repetidos
print('\n3) Conteo de caracteres repetidos')
# .count(substring, start, end) => búsqueda de izquierda a derecha con inicio y fin opcionales
# start / end => parámetros / argumentos OPCIONALES

var_1 = 'nunca digas nunca en esta vida.'
#(+)     0123456789012345678901234567890
#        0         1         2         3

# .count()
print( var_1.count('a') ) # 5
print( var_1.count('nunca') ) # 2
print( var_1.count('nunca' , 2 ) ) # 1
print( var_1.count('nunca' , 2, 10 ) ) # 0
print( var_1.count('nunca' , 2, 18 ) ) # 1
print( var_1.count('never' , 2, 18 ) ) # 0


#? 4) Búsqueda de un substring => Retorno de índice CON ERROR
print('\n4) Búsqueda de un substring => Retorno de índice CON ERROR')
# .index(substring, start, end) => búsqueda de un caracter de izquierda a derecha
# .rindex(substring, start, end) => búsqueda de un caracter de derecha a izquierda

# END => exclusivo

var_1 = 'contextualización'
#(+)     01234567890123456
#        0         1

# .index() => IZQ a DER
print('\nUtilizando .index()')
print( var_1.index('x') ) # 5
print( var_1.index('ó') ) # 15
#print( var_1.index('ó', 10, 15) ) #! ValueError: substring not found
print( var_1.index('ó', 10, 16) ) # 15
print( var_1.index('n') ) # 2
print( var_1.index('n', 10) ) # 16
print( var_1.index('n', 10, 200) ) # 16 # no da error
print( var_1.index('liz') ) # 9

# .rindex() => DER a IZQ
print('\nUtilizando .rindex()')
print( var_1.rindex('n') ) # 16
print( var_1.rindex('n', 0, 10) ) # 2

var_1 = 'Xuna palabraX que se forma conX'
#        0123456789012345678901234567890
#        0         1         2         3                  

print( var_1.rindex('X') ) # 30
print( var_1.rindex('X', 0, 5) ) # 0
print( var_1.rindex('X', 5, 20) ) # 12
print( var_1.rindex('X', 0, 20) ) # 12



#? 5) Búsqueda de substring => Retorno de índice SIN ERROR
print('\n5) Búsqueda de substring => Retorno de índice SIN ERROR')
#   .find(substring, start, end)
#   .rfind(substring, start, end)

# start / end => opcionales

# => básicamente lo mismo que index
# => pero no devuelve error si no encuentra
# => en su lugar devuelve -1

var_1 = 'contextualización'
#(+)     01234567890123456
#        0         1

# .find()
print( var_1.find('a') ) # 8
print( var_1.find('y') ) # -1


# .rfind()
print( var_1.rfind('a') ) # 12

var_1 = 'Xuna palabraX que se forma conX'

print( var_1.rfind('X') ) # 30
print( var_1.rfind('X', 0, 5) ) # 0
print( var_1.rfind('X', 5, 20) ) # 12
print( var_1.rfind('X', 0, 20) ) # 12
print( var_1.rfind('X123', 0, 20) ) # -1



#? 6) Eliminar espaciados y caracteres
print('\n6) Eliminar espaciados y caracteres')
#   .strip()  => eliminación a ambos lados
#   .lstrip() => eliminación a la izquierda
#   .rstrip() => eliminación a la derecha

# => por defecto sin argumento elimina todo tipo de espaciado


# .strip()

var_1 = '   hola mundo   '
var_2 = 'a   hola mundo   a'
var_3 = '   hola mundo'
var_4 = '**********hola****'
var_5 = '\nhola mundo\n'

print( var_1, '|', var_1.strip() )
print( var_2, '|', var_2.strip() )
print( var_3, '|', var_3.strip() )
print( var_4, '|', var_4.strip() )
print( var_4, '|', var_4.strip('*') )
print( var_5, '|', var_5.strip() )



# .lstrip() y .rstrip()
print('\nUtilización de .lstrip() & .rstrip()')

var_1 = '**********hola****'

print(var_1)
print( var_1.strip('*') )
print( var_1.lstrip('*') )
print( var_1.rstrip('*') )
print( var_1.rstrip('/') ) #! no da error
print( var_1.rstrip() ) # sin argumento trata de eliminar espacios #! no da error



#? 7) .join()
print('\n7) .join()')
# - Une cada caracter de una cadena
# - Con el valor de otra cadena

c1 = 'X'
c2 = '$'
c3 = '----'

cadena_principal = 'python'

print( c1.join(cadena_principal) ) # pXyXtXhXoXn
print( c2.join(cadena_principal) ) # p$y$t$h$o$n
print( c3.join(cadena_principal) ) # p----y----t----h----o----n



#? 8) .split()
print('\n8) .split()')
# - transforma una cadena en una lista
# ! TEMA Listas: Ya lo veremos a profundidad luego
# - básicamente una lista es una colección de datos
# - cuando no se da el parámetro por defecto separa por espacios

var_1 = 'Python Java C++ Javascript'
resultado = var_1.split()

print(var_1, type(var_1))
print(resultado, type(resultado), len(resultado))

print()

var_1 = 'Python,Java,C++,Javascript'
resultado = var_1.split()

print(var_1, type(var_1))
print(resultado, type(resultado), len(resultado))

print()
resultado = var_1.split(',')
print(resultado, type(resultado), len(resultado))

print()
var_1 = 'Python/Java/C++/Javascript'
resultado_1 = var_1.split()
resultado_2 = var_1.split('/')
print(resultado_1, type(resultado_1), len(resultado_1))
print(resultado_2, type(resultado_2), len(resultado_2))



#? 9) .splitlines()
print('\n9) .splitlines()')
# - transforma un string en lista
# - separando los saltos de línea (\n)

texto = 'Yo programo en Python\nEl programa en Java\nElla en C++'

print(texto)
var_split = texto.split()
var_splitlines = texto.splitlines()
print(var_split, len(var_split))
print(var_splitlines, len(var_splitlines))


poema = '''
En una noche de verano
Yo la conocí
Nunca lo olvidé
Siempre la recordaré
'''

print(poema)
print(poema.splitlines())


#? 10) .expandtabs()
print('\n10) .expandtabs()')
# - como su nombre lo indica
# - sirve para incrementar el tamaño de un tab
# - dentro de un string

var_1 = 'hola\tpython java c++\tsebas'
print(var_1)
print(var_1.expandtabs()) # por defecto me indica 4 espacios
print(var_1.expandtabs(1)) 
print(var_1.expandtabs(2)) 
print(var_1.expandtabs(4)) 
print(var_1.expandtabs(10)) 



#? 11) .replace()
print('\n11) .replace()')
# ! UNO DE LOS MÁS IMPORTANTES
# - para reemplazar un caracter o subcadena
# - dentro de una cadena
# * .replace('substring que queremos cambiar' , 'substring que deseamos implementar')

# ----------------------------
# => reemplazando un caracter
# ----------------------------
var_1 = 'pXlabrX secrXtX'
print(var_1)
print(var_1.replace('X', '*****'))
print(var_1.replace('Y', '*****')) #! no error => pXlabrX secrXtX


# ------------------------------------------
# => reemplazando una subcadena (substring)
# ------------------------------------------

var_1 = 'hola mundo'
print(var_1) # hola mundo
print(var_1.replace('mundo' , 'python')) # hola python
print(var_1.replace('mundo' , 'java')) # hola java
print(var_1.replace('mundo' , 'java'.upper())) # hola JAVA