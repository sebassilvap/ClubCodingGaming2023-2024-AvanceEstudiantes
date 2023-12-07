# -------------------------
# Club de Coding & Gaming
# Ejercicios 07.12.2023
# -------------------------

# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO 1)
print('\n\nEJERCICIO 1)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - por medio de un bucle convertir la variable "palabra" => palabra = 'neueschule'
# - a "nueva_palabra"
# - de tal manera que nueva_palabra = 'nEuEsChUlE'
# - queda prohibido utilizar una modificación directa
# - como por ejemplo:
# - nueva_palabra = 'nEuEsChUlE'
# - se debe usar un bucle

'''
palabra = 'neueschule'
nueva_palabra = 'nEuEsChUlE'
'''



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO 2)
print('\n\nEJERCICIO 2)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - definir una función "promedio"
# - que acepte 3 parámetros x, y, z
# - RETORNAR un diccionario de la siguiente manera
# - tal que al ejecutar el siguiente test, se tenga el siguiente resultado
"""
# TEST
print( promedio(15,20,14) ) 
print( type(promedio(15,20,14)) )
# {'nota 1': 15, 'nota 2': 20, 'nota 3': 14, 'promedio': 16.333333333333332}
# <class 'dict'>
"""





# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO 3)
print('\n\nEJERCICIO 3)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Pedir al usuario una palabra con input
# - si el usuario da una palabra, ej: '          hOlA          ' 
# - la consola debe retornar:
# - CUIDADO: con espacios y case / todo debe presentarse en minúsculas
"""
h
oo
lll
aaaa
"""



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO 4)
print('\n\nEJERCICIO 4)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Escribir un juego de adivinanzas
# - El usuario da un número del 1 al 10 (input)
# - Si da 0 => se sale del programa
# - Si da menos de 0 o mayor a 10 - ERROR se repite el programa
# - Debe haber 2 jugadores de la computadora que generen números aleatorios del 1 al 10
# - Realizar la comparación:

#   a) Si hay empate entre los 3 todos se llevan 3 puntos
#   b) Si hay empate entre 2, los que empataron se llevan 1 punto, el que perdió 0
#   c) De manera normal, el primer lugar se lleva 2 puntos, el 2do lugar 1, el 3ero cero puntos

# - Mostrar el marcador de los 3 en cada iteración

