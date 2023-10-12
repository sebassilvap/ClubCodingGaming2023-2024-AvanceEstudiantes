# ==========================================================
# Operador de Producto en Strings

# - Se puede usar este operador para multiplicar un string
# - Es decir, repetirlo un N número de veces
# ==========================================================

#? 1) Multiplicación básica de strings
print('\n1) Multiplicación básica de strings')

var_1 = 'S'
print(var_1)

# => no importa el orden
resultado_1 = var_1 * 3
resultado_2 = 5 * var_1

print(resultado_1)
print(resultado_2)


#? 2) Ejemplo práctico 1 => incluir espacios
print('\n2) Ejemplo práctico 1 => incluir espacios')

saludo = 'Hola'
nombre = 'Juan'
lenguaje = 'Python'

cinco_espacios = ' ' * 5
diez_espacios = ' ' * 10

print( saludo + nombre + lenguaje )
print( saludo + cinco_espacios + nombre + diez_espacios + lenguaje )


#? 3) Ejemplo práctico 2 => espacios y secuencias
print('\n3) Ejemplo práctico 2 => espacios y secuencias')

tres_nuevas_lineas = '\n' * 3
dos_tabulaciones = '\t' * 2

mensaje_1 = saludo + tres_nuevas_lineas + nombre + dos_tabulaciones + lenguaje
mensaje_2 = saludo + dos_tabulaciones + nombre + tres_nuevas_lineas + lenguaje

print('\nMENSAJE 1\n-----------')
print(mensaje_1)
print('\nMENSAJE 2\n-----------')
print(mensaje_2)