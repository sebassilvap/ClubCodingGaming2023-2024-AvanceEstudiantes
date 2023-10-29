# =========================================================
# Condicional if + input

# - una muy buena combinación al inicio en el aprendizaje
# - para evaluar la entrada dada por el usuario
# ! RECORDAR: el input siempre devuelve un string!
# =========================================================

opcion = input('Ingrese un número del 1 al 100: ') # ! str

"""
if opcion < 50:
    print('El número es menor a 50!')
else:
    print('El número es mayor o igual a 50')
# end if
"""

#! TypeError: '<' not supported between instances of 'str' and 'int'


# => de esta manera no me va a dar error de sintaxis
# - no lo detecta el editor
# - el error se da al ejecutar e ingresar un valor
# - porque estoy evaluando un string

# SOLUCIÓN:
# ---------

if int(opcion) < 50:
    print('número menor a 50')
else:
    print('número mayor o igual a 50 !!!')