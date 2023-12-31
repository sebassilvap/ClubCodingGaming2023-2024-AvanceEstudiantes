# ==========================================================================
# Operadores de Asignación
#! REPASAR 

# - operaciones matemáticas al momento de asignar un valor a la variable
# - por ejemplo el incremento en 1
# - se realizan anteponiendo la operación al igual

#*  Operador  Descripción
#|     +=     Suma en la asignación
#|     -=     Resta en la asignación
#|     *=     Producto en la asignación
#|     /=     División en la asignación
#|    **=     Potencia en la asignación
#|     %=     Módulo en la asignación

# ==========================================================================


#? 1) Operación Incremento Básico
num_1 = 5
num_2 = 3

print(num_1)

num_1 = num_1 + 1
print(num_1)

num_1 = num_1 + 1 # es lo mismo -> num_1 += 1
print(num_1)

num_1 += 1
print(num_1)

num_1 += 1 # Suma en la asignación
print(num_1)

num_1 += 100
print(num_1)

#? 2) Shortcut de Operaciones / Operadores de Asignación
print('\n*** Suma en Asignación ***')
num_1 = 2
num_1 += 100
print(num_1)


print('\n*** Resta en Asignación ***')
num_1 = 2
num_1 -= 5
print(num_1)


print('\n*** Producto en Asignación ***')
num_1 = 2
num_1 *= 3
print(num_1)


print('\n*** División en Asignación ***')
num_1 = 2
num_1 /= 2
print(num_1)
# num_1 = 2 / 2 #! de la división siempre nos resulta float
# 1.0


print('\n*** Potencia en Asignación ***')
num_1 = 2
num_1 **= 3 # num_1 = 2 ^ 3 = 8
print(num_1)


print('\n*** Módulo en Asignación ***')
num_1 = 5
num_1 %= 2
# num_1 = 5 % 2

# 5 |____ 2
# -4       2
#  1

print(num_1)