# ==================================================================
# Casting

# - funciones internas de python
# - con el mismo nombre del tipo de variable
# - las utilizamos para transformar de un tipo de variable a otro
# ==================================================================

#? 1) Casting entre tipos básicos
print('\n1) Casting entre tipos básicos')

var_1 = '25' # string numérico!
var_2 = 41
var_3 = -8.9
var_4 = True
var_5 = False
var_6 = 0
var_7 = 100
var_8 = None


# => Casting
"""
var_1_to_int 
var_2_to_float 
var_3_to_str 
var_4_to_int 
var_5_to_float_
var_6_to_bool 
var_7_to_bool 
var_8_to_bool 
"""



#? 2) Si el casting no tiene sentido nos va a dar un error
print('\n2) Si el casting no tiene sentido nos va a dar un error')
#! ValueError ó TypeError

## EJEMPLO - ValueError:
# - querer pasar un string de texto a int o float
# - esto nos daría un ValueError



## EJEMPLO - TypeError:
# - un valor None no puede ser convertido a número
# esto nos da un TypeError



#? 3) Todo puede ser convertible a string
print('\n3) Todo puede ser convertible a string')

var_1 = 25
var_2 = -6.33
var_3 = True
var_4 = False
var_5 = None


# => comprobamos que sea un string
