# ===============================================================
# break-continue-pass

# Son sentencias para el control de un bucle
# pass => también tiene otras utilidades además de los bucles

#* pass
# => se lo utiliza como un placeholder
# => para definir algo y trabajar en eso luego

#* break
# => interrumpimos / terminamos un bucle de manera total

#* continue
# => para saltarnos a la siguiente iteración de un bucle

# ===============================================================


#? 1) continue => para saltar iteración en bucle
print('\n1) continue => para saltar iteración en bucle')
# - como vimos igual podemos utilizar pass
# - pero más sentido tiene continue
# - incluso por su sintaxis

# EJ: imprimir números del 1 al 20, exceptuando los múltiplos de 3

lista_numeros = []

for i in range(1, 21):
    if i % 3 == 0:
        continue
    else:
        lista_numeros.append(i)
else:
    print('La lista generada es:')
    print(lista_numeros)
# end for

"""
La lista generada es:
[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]
"""