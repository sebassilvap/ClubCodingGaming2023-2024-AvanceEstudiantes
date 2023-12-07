# -------------------------
# Club de Coding & Gaming
# Ejercicios 07.12.2023
# -------------------------

# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO 1)
print('\n\nEJERCICIO 1)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - por medio de un bucle convertir la variable "palabra"
# - a "nueva_palabra"
# - de tal manera que nueva_palabra = 'nEuEsChUlE'
# - queda prohibido utilizar una modificación directa
# - como por ejemplo:
# - nueva_palabra = 'nEuEsChUlE'
# - se debe usar un bucle

palabra = "neueschule"
nueva_palabra = ''

for index, letra in enumerate(palabra):
    if (index + 1) % 2 == 0:
        nueva_palabra += letra.upper()
        # nueva_palabra = nueva_palabra + letra.upper()
    else:
        nueva_palabra += letra.lower()
# end for

print(nueva_palabra) # nEuEsChUlE



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

def promedio(x,y,z):
    resultados_dict = dict()
    resultados_lista = [x, y, z, (x+y+z)/3]
    titulos = ['nota 1', 'nota 2', 'nota 3', 'promedio']
    
    for index, elemento in enumerate(resultados_lista):
        resultados_dict[ titulos[index] ] = elemento
    # end for
    
    return resultados_dict
# end def

# TEST
print( promedio(15,20,14) ) 
print( type(promedio(15,20,14)) )
# {'nota 1': 15, 'nota 2': 20, 'nota 3': 14, 'promedio': 16.333333333333332}
# <class 'dict'>



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO 3)
print('\n\nEJERCICIO 3)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Pedir al usuario una palabra con input
# - si el usuario da una palabra, ej: 'hOlA'
# - la consola debe retornar:
# - CUIDADO: con espacios y case / todo debe presentarse en minúsculas
"""
h
oo
lll
aaaa
"""

palabra = input('Ingrese una palabra : ')
palabra = palabra.lower().strip(' ')

counter = 1

while counter != len(palabra) + 1:
    print( palabra[counter-1] * counter )
    counter += 1
# end while



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


import random

player = ''
cpu_1 = ''
cpu_2 = ''

marcador_player = 0
marcador_cpu_1 = 0
marcador_cpu_2 = 0

while True:
    print('**************************************************')
    print( 'Marcador PLAYER = {}'.format(marcador_player) )
    print( 'Marcador CPU 1 = {}'.format(marcador_cpu_1) )
    print( 'Marcador CPU 2 = {}'.format(marcador_cpu_2) )
    print('**************************************************')
    player = input('Número Entero del 1 al 10 / 0 para salir : ')
    player = int( player.strip(' ') )
    
    if player == 0:
        print('Adios !!')
        break
    # end if
    
    if player < 0 or player > 10:
        print('ERROR - Número debe ser entre 1 y 10 !!')
        continue
    
    cpu_1 = random.randint(1,10)
    cpu_2 = random.randint(1,10)
    
    if player > cpu_1 and cpu_1 > cpu_2:
        marcador_player += 2
        marcador_cpu_1 += 1
        marcador_cpu_2 += 0
        print( '1) PLAYER = {} | 2) CPU 1 = {} | 3) CPU 2 = {}'.format(player, cpu_1, cpu_2) )
    elif player > cpu_2 and cpu_2 > cpu_1:
        marcador_player += 2
        marcador_cpu_2 += 1
        marcador_cpu_1 += 0
        print( '1) PLAYER = {} | 2) CPU 2 = {} | 3) CPU 1 = {}'.format(player, cpu_2, cpu_1) )
    elif cpu_1 > player and player > cpu_2:
        marcador_cpu_1 += 2
        marcador_player += 1
        marcador_cpu_2 += 0
        print( '1) CPU 1 = {} | 2) PLAYER = {} | 3) CPU 2 = {}'.format(cpu_1, player, cpu_2) )
    elif cpu_1 > cpu_2 and cpu_2 > player:
        marcador_cpu_1 += 2
        marcador_cpu_2 += 1
        marcador_player += 0
        print( '1) CPU 1 = {} | 2) CPU 2 = {} | 3) PLAYER = {}'.format(cpu_1, cpu_2, player) )
    elif cpu_2 > player and player > cpu_1:
        marcador_cpu_2 += 2
        marcador_player += 1
        marcador_cpu_1 += 0
        print( '1) CPU 2 = {} | 2) PLAYER = {} | 3) CPU 1 = {}'.format(cpu_2, player, cpu_1) )
    elif cpu_2 > cpu_1 and cpu_1 > player:
        marcador_cpu_2 += 2
        marcador_cpu_1 += 1
        marcador_player += 0
        print( '1) CPU 2 = {} | 2) CPU 1 = {} | 3) PLAYER = {}'.format(cpu_2, cpu_1, player) )
    elif player == cpu_1 and cpu_1 == cpu_2:
        marcador_player = marcador_cpu_1 = marcador_cpu_2 = 3
        print( 'EMPATE !! - PLAYER / CPU 1 / CPU 2 = {}'.format(player) )
    elif player == cpu_1 and cpu_1 > cpu_2:
        marcador_player += 1
        marcador_cpu_1 += 1
        marcador_cpu_2 += 0
        print( '1) PLAYER & CPU 1 = {} | 2) CPU 2 = {}'.format(player, cpu_2) )
    elif player == cpu_1 and cpu_1 < cpu_2:
        marcador_cpu_1 += 1
        marcador_player += 0
        marcador_cpu_2 += 0
        print( '1) CPU 2 = {} | 2) PLAYER & CPU 1 = = {}'.format(cpu_2, player) )
    elif player == cpu_2 and cpu_2 > cpu_1:
        marcador_player += 1
        marcador_cpu_2 += 1
        marcador_cpu_1 += 0
        print( '1) PLAYER & CPU 2 = {} | 2) CPU 1 = {}'.format(player, cpu_1) )
    elif cpu_1 == cpu_2 and cpu_2 > player:
        marcador_cpu_1 += 1
        marcador_cpu_2 += 1
        marcador_player += 0
        print( '1) CPU 1 & CPU 2 = {} | 2) PLAYER = {}'.format(cpu_1, player) )
    elif cpu_1 == cpu_2 and player > cpu_2:
        marcador_player += 1
        marcador_cpu_1 += 0
        marcador_cpu_2 += 0
        print( '1) PLAYER = {} | 2) CPU 1 & CPU 2 = {}'.format(player, cpu_1) )
    else:
        print('Player =', player)
        print('CPU 1 =', cpu_1)
        print('CPU 2 =', cpu_2)
    # end if
# end while
