# ===================================================
# Encadenamiento de Funciones
# (Function - Chaining)

# - chaining / encadenamiento
# - es un estilo de programación
# - se invocan varias funciones de manera múltiple
# - que se ejecutan de manera secuencial
# - en las funciones => desde dentro hacia afuera
# ===================================================


#? 1) Sin usar function-chaining
print('\n1) Sin usar function-chaining\n')

print('Calcular el redondeo absoluto de un número:')

"""
numero = input( 'Ingrese un número: ' ) # input al usuario - str 1)
numero = float(numero) # float 2)
numero = abs(numero) # valor absoluto 3)
numero = round(numero) # calculamos el redondeo del número 4)
print( numero ) # 5)
"""




#? 2) CON function-chaining
print('\n2) CON function-chaining\n')

print('Calcular el redondeo absoluto de un número:')

print(  round(abs(float(input('Ingrese un número: '))))  ) # 1 línea de código




#? 3) Buenas Prácticas de Programación
print('\n3) Buenas Prácticas de Programación')
# - el código debe ser legible
# - legible para el programador y cualquiera que lo lea
# - un excesivo uso de funciones encadenadas hace al código difícil de leer
# - en programas avanzados será común ver esto
# - para empezar usarlo con mesura