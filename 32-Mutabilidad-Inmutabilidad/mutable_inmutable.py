# ==================================================================
# Mutabilidad e Inmutabilidad

# - En programación muchas veces veremos el concepto
# - de elementos mutables
# - y elementos inmutables

# *     Mutable   => que se pueden modificar
# *     Inmutable => que no se puede modificar / cambiar

# - En Python hay algunos elementos que cumplen esta característica
# - Veremos solo algunos ejemplos básicos para entender el concepto
# ==================================================================


#? 1) Listas - Elementos Mutables
print('\n1) Listas - Elementos Mutables')

lista_letras = ['a','b','c','d','e','f']
print(lista_letras)

print( lista_letras[0] )
lista_letras[0] = 'ZZZ'

print(lista_letras) # ['ZZZ', 'b', 'c', 'd', 'e', 'f']



#? 2) String - Elemento Inmutable
print('\n2) String - Elemento Inmutable')

string = 'python'
#         012345
print( string )
print( string[0] )
print( string[1] )
print( string[2] )
print( string[3] )
print( string[4] )
print( string[5] )
#print( string[6] ) #! IndexError: string index out of range


#string[0] = 'Z' #! TypeError: 'str' object does not support item assignment

# REASIGNACIÓN

string = 'Zython'

print(string) # Zython
