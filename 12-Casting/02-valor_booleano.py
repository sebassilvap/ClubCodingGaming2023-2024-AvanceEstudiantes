# =============================================================
# Valor Booleano de los Datos

# - como vimos cualquier dato puede ser transformado a string
# - de igual manera cualquier dato tiene un valor booleano

# - type() => retornamos el tipo de dato / str, int, float, bool, NoneType
# - str() / int() / float() / bool()
# var_1 = 10 # int

# ==> CASTING
# nueva_variable = float(var_1)
# nueva_variable_2 = str(var_1)

# - como veremos prácticamente
# - un valor vacío, cero, nulo nos da False
# - cualquier otro valor diferente nos da True
# =============================================================

var_1 = 1
var_2 = 0 #!
var_3 = -1
var_4 = 100
var_5 = 0.01
var_6 = -0.0002
var_7 = -0.00 #!
var_8 = 'a'
var_9 = ' '
var_10 = " "
var_11 = '' #!
var_12 = None


print( 'var_1 =' , var_1 , '=> a bool =>' , bool(var_1) ) # var_1 = 1 => a bool => True
print( 'var_2 =' , var_2 , '=> a bool =>' , bool(var_2) ) # var_2 = 0 => a bool => False
print( 'var_3 =' , var_3 , '=> a bool =>' , bool(var_3) ) # var_3 = -1 => a bool => True
print( 'var_4 =' , var_4 , '=> a bool =>' , bool(var_4) ) # var_4 = 100 => a bool => True
print( 'var_5 =' , var_5 , '=> a bool =>' , bool(var_5) ) # var_5 = 0.01 => a bool => True
print( 'var_6 =' , var_6 , '=> a bool =>' , bool(var_6) ) # var_6 = -0.0002 => a bool => True
print( 'var_7 =' , var_7 , '=> a bool =>' , bool(var_7) ) # var_7 = -0.0 => a bool => False
print( 'var_8 =' , var_8 , '=> a bool =>' , bool(var_8) ) # var_8 = a => a bool => True
print( 'var_9 =' , var_9 , '=> a bool =>' , bool(var_9) ) # var_9 =   => a bool => True
print( 'var_10 =' , var_10 , '=> a bool =>' , bool(var_10) ) # var_10 =   => a bool => True
print( 'var_11 =' , var_11 , '=> a bool =>' , bool(var_11) ) # var_11 =  => a bool => False
print( 'var_12 =' , var_12 , '=> a bool =>' , bool(var_12) ) # var_12 = None => a bool => False


# -------------------------------------------------------------
# => Conclusión
# - si el valor es 0 (entero o flotante) => esto es un False
# - diferente de 0 (positivo o negativo) => True
# - un string vacío => False
# - un solo caracter, así sea 1 espacio en blanco => True
# - un valor nulo (None) => False
# -------------------------------------------------------------