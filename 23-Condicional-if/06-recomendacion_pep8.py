# =========================================================
# Recomendación de PEP8

# - PEP => Python Enhancement Proposal
# - es un documento técnico para la comunidad de Python
# - que describe nuevas características de Python
# - sus procesos, ambiente, etc...

# https://peps.python.org/pep-0008/

# - Una de sus recomendaciones dice lo siguiente:

"""
Don't compare boolean values to True or False using ==.

Yes:   if greeting:
No:    if greeting == True:
Worse: if greeting is True:
"""

# * keyword is => ya lo veremos después

# =========================================================


#? 1) Ejemplo de buena y mala práctica
print('\n1) Ejemplo de buena y mala práctica')

es_estudiante = True

# => BUENA PRÁCTICA

if es_estudiante:
    print('SI, es estudiante!')
else:
    print('No, no es estudiante!')
# end if


# => MALA PRÁCTICA
if es_estudiante == True:
    print('SI, es estudiante!')
else:
    print('No, no es estudiante!')
# end if


# - al final tendremos el mismo resultado
# - sin embargo hacer esto sería redundante
# - y también en expresiones más complejas
# - esto puede tender a errores



#? 2) Mala práctica que puede llevar a ERROR
print('\n2) Mala práctica que puede llevar a ERROR')
# - RECORDATORIO de lo que vimos la anterior lección

lista = [1,2,3,4,5]
x = 3

#  => BUENA PRÁCTICA
if x in lista:
    print('x está en la lista!!')
else:
    print('x NO está en la lista')
# end if

#* x está en la lista!!


#  => MALA PRÁCTICA, PERO RESULTADO CORRECTO
if (x in lista) == True:
    print('x está en la lista!!')
else:
    print('x NO está en la lista')
# end if

#* x está en la lista!!


#! => MALA PRÁCTICA, Y RESULTADO INCORRECTO!

if x in lista == True:
    print('x está en la lista!!')
else:
    print('x NO está en la lista')
# end if

#! x NO está en la lista

# ----------------------------------------------------------
# RECORDAR
# - esto vendría a ser una comparación en cadena
# x in lista == True --> (x in lista) and (lista == True)
# x in lista == True --> (True) and (False)
# x in lista == True --> False
# ----------------------------------------------------------


#? 3) Con valores no booleanos no hay problema
print('\n3) Con valores no booleanos no hay problema')

a = 10

if a == 10: #* OK !!
    print('Hey el número es 10')
else:
    print('Diferente de 10 !!')
# end if


# -------------------------------------
# - a en este caso no es un booleano
# - a es un int
# - la manera de compararlo es con ==
# -------------------------------------