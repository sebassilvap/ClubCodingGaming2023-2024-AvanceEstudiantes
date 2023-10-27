# ====================================
# Función Interna => .isinstance()
# built-in functions en Python

# - devuelve un valor booleano / True / False
# - para confirmar el tipo del dato
# - RECORDAR: el tipo lo sabemos con type()
# ====================================

var_1 = 10 # int
var_2 = 'hola' # str
var_3 = -50.6 # float
var_4 = True # bool

print('\nVariables y tipos')

print( var_1 , type(var_1) ) # 10 <class 'int'>
print( var_2 , type(var_2) ) # hola <class 'str'>
print( var_3 , type(var_3) ) # -50.6 <class 'float'>
print( var_4 , type(var_4) ) # True <class 'bool'>


# => utilizando isinstance( valor , tipo )
print('\nvar_1 => isinstance()')
print( isinstance(var_1 , int) ) # True
print( isinstance(var_1 , str) ) # False
print( isinstance(var_1 , float) ) # False
print( isinstance(var_1 , bool) ) # False

# ¿var_1 es una instancia de int, de entero?

#print( isinstance(int , var_1) )
#! TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union


print('\nvar_2 => isinstance()')
print( isinstance(var_2 , int) )
print( isinstance(var_2 , str) )
print( isinstance(var_2 , float) )
print( isinstance(var_2 , bool) )


print('\nvar_3 => isinstance()')
print( isinstance(var_3 , int) )
print( isinstance(var_3 , str) )
print( isinstance(var_3 , float) )
print( isinstance(var_3 , bool) )


print('\nvar_4 => isinstance()')
# var_4 = True # bool
print( isinstance(var_4 , int) ) #! True
print( isinstance(var_4 , str) ) # False
print( isinstance(var_4 , float) ) # False
print( isinstance(var_4 , bool) ) # True


# * OTRA MANERA => de expresar los valores BOOL
# True = 1
# False = 0

numero_1 = 1
numero_0 = 0

print( isinstance(numero_1, bool) ) # False
print( isinstance(numero_0, bool) ) # False

verdadero = True # 1
falso = False # 0

print('\nisinstance de True:\n')
print( isinstance(verdadero, int) ) # True
print( isinstance(verdadero, float) ) # False
print( isinstance(verdadero, str) ) # False
print( isinstance(verdadero, bool) ) # True

print('\nisinstance de False:\n')
print( isinstance(falso, int) ) # True
print( isinstance(falso, float) ) # False
print( isinstance(falso, str) ) # False
print( isinstance(falso, bool) ) # True