# =======================================
# RECORDEMOS: Los String son inmutables
# =======================================
# MUTABILIDAD / mutable / cambiar - transformarse - modificarse
# INMUTABILIDAD / inmutable / no cambia - no se mueve - no se trasnforma

# cadena de texto => cadena de caracteres / string

# fases de creación de la variable
# 1) crear la variable => cadena
# 2) asignar => =
# 3) poner un valor => 'hola python'
# ==> declaración de una variable en python

# java
# int a;
# a = 20;

# python
# a = 20

# declaración de una variable = creación + asignación

# REASIGNACIÓN
# a = 40

cadena = 'hola python'
#(+)      01234578901
#(-)             4321

print(cadena)
print( hex(id(cadena)) )

# indexing
# str / listas / colecciones de datos (listas, tuplas, set, diccionarios, rangos)
# => elementos iterables
print(cadena[0]) # el primer elemento de la cadena
print(cadena[-1]) # al último elemento

# el string es inmutable
#cadena[0] = 'X'
#! TypeError: 'str' object does not support item assignment
#! el string es inmutable

cadena[0].upper()
print( cadena[0].upper() )
print(cadena)

# RECORDAR:
# - los métodos de string, no cambian al original

#cadena[0] = cadena[0].upper()
#! TypeError: 'str' object does not support item assignment
#! el string es inmutable

# ----------------------------------------------------------
# - la asignación se da al momento que ponemos variable =
# - ya sea con un método o sobreescribiendo
# - no podemos hacer esto con strings

# => pero recordemos el truco
# - si bien es cierto
# - no podemos cambiar un índice
# - pero podemos reasignar la variable entera
# ----------------------------------------------------------

cadena = 'hola python'
print( hex(id(cadena)) )

# hex() / id() => otras built-in functions de python

cadena = 'H' + cadena[1:] #! NO ES MODIFICAR => ES REASIGNAR
print(cadena)
print( hex(id(cadena)) )

print('----------')

cadena = cadena[0].upper() + cadena[1:]
print(cadena)

cadena = cadena[0].upper() + cadena[1:-1] + cadena[-1].upper()
print(cadena) # Hola pythoN

"""
num1 = 10
num2 = 10
num3 = 20

print( num1, hex(id(num1)) )
print( num2, hex(id(num2)) )
print( num3, hex(id(num3)) )
"""