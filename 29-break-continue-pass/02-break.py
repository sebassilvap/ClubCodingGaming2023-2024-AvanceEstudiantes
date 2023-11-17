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


#? 1) break => interrumpir la ejecución del bucle y seguir ejecutando el código
print('\n1) break => interrumpir la ejecución del bucle y seguir ejecutando el código')
# - si utilizamos else en while o for
# - si aplicamos un break
# - el else no se ejecuta

num = 1

"""
while num > 5:
    print('hola bucle')
else:
    print('else dentro de while')
# end while

#else dentro de while"
"""

# =======
# break
# =======

print('línea de código # 1')
print('línea de código # 2')
print('línea de código # 3')

contador = 1

while contador < 10:
    print('Contador =', contador)
    
    if contador == 5:
        print('Salir del bucle cuando Contador =', contador)
        break
    
    contador += 1
else:
    print('Llegamos al final del Bucle')
    print('Al final, Contador =', contador)
# end while

print('línea de código # 4')
print('línea de código # 5')
print('línea de código # 6')

# CONSOLA:
# línea de código # 1
# línea de código # 2
# línea de código # 3
# Contador = 1
# Contador = 2
# Contador = 3
# Contador = 4
# Contador = 5
# Salir del bucle cuando Contador = 5
# línea de código # 4
# línea de código # 5
# línea de código # 6


# =========
# continue
# =========
print('\n\n')

print('línea de código # 1')
print('línea de código # 2')
print('línea de código # 3')

contador = 1

while contador < 10:
    print('Contador =', contador)
    
    if contador == 5:
        print('Saltar el bucle cuando Contador =', contador)
        contador += 1
        continue
    
    contador += 1
else:
    print('Llegamos al final del Bucle')
    print('Al final, Contador =', contador)
# end while

print('línea de código # 4')
print('línea de código # 5')
print('línea de código # 6')

# CONSOLA:
# línea de código # 1
# línea de código # 2
# línea de código # 3
# Contador = 1
# Contador = 2
# Contador = 3
# Contador = 4
# Contador = 5
# Saltar el bucle cuando Contador = 5
# Contador = 6
# Contador = 7
# Contador = 8
# Contador = 9
# Llegamos al final del Bucle
# Al final, Contador = 10
# línea de código # 4
# línea de código # 5
# línea de código # 6




#? 2) break => ejemplo con for
print('\n2) break => ejemplo con for')


print('Ejecutando Instrucción # 1')
print('Ejecutando Instrucción # 2')
print('Ejecutando Instrucción # 3')

for i in range (1,11):
    print('Bucle for - Contador i =', i)
    
    if i == 6:
        print('*** break ***')
        print('Contador i en el break vale =', i)
        break
    # end if
else:
    print('El bucle ha terminado')
    print('Contador i al final =', i)
# end for

print('Ejecutando Instrucción # 4')
print('Ejecutando Instrucción # 5')
print('Ejecutando Instrucción # 6')
