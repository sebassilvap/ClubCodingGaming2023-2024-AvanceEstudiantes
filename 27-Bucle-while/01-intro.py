# =================================================================
# Bucle while

# - bucle / loop => bloque de código que se ejecuta varias veces
# - se ejecuta siempre y cuando la condición que se evalúa es True
# - cada que vez que se ejecuta => se llama iteración
# - while == MIENTRAS
# - mientras una condición sea True => se ejecuta por siempre
# ! tener cuidado de caer en un bucle infinito

'''
while (condicion):
    bloque de código
'''

#* NOTA:
# - los bucles nos permiten sacar el mayor provecho a nuestro computador
# - podemos realizar una serie de cálculos en fracciones de segundo
# - en cada iteración
# - aquí empieza lo bueno de esto :)
# =================================================================


#? 1) ERROR común siempre a evitar
print('\n1) ERROR común siempre a evitar')
# ! IMPORTANTE

"""
while True:
    print('Lo siento estoy atascado en un bucle infinito! :(')
# end while
"""


#? 2) La condición debe cambiar algún momento a False
print('\n2) La condición debe cambiar algún momento a False')

iterador = 1

# => cuidado 
# - error común al inicio
"""
while iterador <= 10:
    print('ITERADOR =', iterador)
# end while
"""

# => corrigiendo el error

while iterador <= 10:
    print('ITERADOR =', iterador)
    iterador += 1 # iterador = iterador + 1 => incremento
# end while

# ITERADOR = 1
# ITERADOR = 2
# ITERADOR = 3
# ITERADOR = 4
# ITERADOR = 5
# ITERADOR = 6
# ITERADOR = 7
# ITERADOR = 8
# ITERADOR = 9
# ITERADOR = 10



#? 3) Bucle while básico para incremento & decremento
print('\n3) Bucle while básico para incremento & decremento')

contador_a = 0 # para contar del 0 al 5
contador_b = 5 # contar del 5 al 0



# ---------------------------
# 3.1) Incremento
print('\n3.1) Incremento\n')
# ---------------------------

while contador_a <= 5:
    print('Contador A =', contador_a)
    contador_a += 1 #! no olvidar - incremento
# end while

# Contador A = 0
# Contador A = 1
# Contador A = 2
# Contador A = 3
# Contador A = 4
# Contador A = 5


# ---------------------------
# 3.2) Decremento 
print('\n3.2) Decremento\n')
# ---------------------------

while contador_b >= 0:
    print('Contador B =', contador_b)
    contador_b -= 1 #! no olvidar - decremento
# end while

# Contador B = 5
# Contador B = 4
# Contador B = 3
# Contador B = 2
# Contador B = 1
# Contador B = 0

# => al final del bucle / los valores quedan alterados
print()
print('contador_a =', contador_a) # 6
print('contador_b =', contador_b) # -1 #! LUEGO

# * NOTA:
# - al poner <= y >= con el igual incluimos el valor límite
# - esto pasaría al no incluirlo


contador_a = 0
contador_b = 5



# ---------------------------------------
# 3.3) Incremento - Ejemplo 2
print('\n3.3) Incremento - Ejemplo 2\n')
# ---------------------------------------

while contador_a < 5: # quitamos =
    print('CONTADOR A =', contador_a)
    contador_a += 1 #! importante
# end while

# CONTADOR A = 0
# CONTADOR A = 1
# CONTADOR A = 2
# CONTADOR A = 3
# CONTADOR A = 4

# ----------------------------------------
# 3.4) Decremento - Ejemplo 2
print('\n3.4) Decremento - Ejemplo 2\n')
# ----------------------------------------

while contador_b > 0: # quitamos =
    print('CONTADOR B =', contador_b)
    contador_b -= 1 #! importante
# end while

# CONTADOR B = 5
# CONTADOR B = 4
# CONTADOR B = 3
# CONTADOR B = 2
# CONTADOR B = 1


print()
print('contador_a =', contador_a) # 5
print('contador_b =', contador_b) # 0 #! LUEGO
