# =========================================================================
# Función Interna input()
# built-in function de Python
# PARTE 1

# - Lectura por teclado / Entrada de datos
# - Otra función interna de Python
# - De esta manera podemos almacenar entradas del usuario en la terminal
# - y adicionalmente podemos guardar este valor en una variable
# ! NOTA IMPORTANTE:
# - el valor que devuelve la consola se GUARDA como un string (str)
# =========================================================================


#? 1) Ejemplo básico de input() y tipo de dato
print('\n1) Ejemplo básico de input() y tipo de dato')

#input('Escriba algo: ')

# => tiene más sentido sin guardamos esto en una variable
# '12345'



#? 2) Guardando el valor de input
print('\n2) Guardando el valor de input')

"""
nombre = input('Escriba su nombre: ')
print( nombre, type(nombre) )
"""

# * LO QUE VIENE DEL INPUT SE GUARDA COMO <str>



#? 3) Si deseo ingresar un número => casting
print('\n3) Si deseo ingresar un número => casting')
#! Clásico error en un inicio

# clásico error
"""
edad = input('¿Cuántos años tiene? : ')
print('Usted tiene', edad, 'años!') # print con parámetros/argumentos
print('El próximo año, usted tendrá', edad + 1, 'años')
"""

# SOLUCIÓN 1:

"""
edad = input('¿Cuántos años tiene? : ')
print(edad, type(edad))

edad = int(edad)
print(edad, type(edad))
"""

# SOLUCIÓN 2:

edad = int( input('¿Cuántos años tiene? : ') )  # function / method CHAINING
#edad = int(edad)
print('Usted tiene', edad, 'años!') 
print('El próximo año, usted tendrá', edad + 1, 'años')