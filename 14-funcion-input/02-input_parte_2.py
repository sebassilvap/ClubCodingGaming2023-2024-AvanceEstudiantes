# =========================================================================
# Función Interna input()
# PARTE 2

# -   Lectura por teclado / Entrada de datos
# -   Otra función interna de Python
# -   De esta manera podemos almacenar entradas del usuario en la terminal
# -   y adicionalmente podemos guardar este valor en una variable
# !   NOTA IMPORTANTE:
# -   el valor que devuelve la consola es un string <str>
# =========================================================================


#? 1) Script de Python para saludar e interactuar con el usuario
print('\n1) Script de Python para saludar e interactuar con el usuario')

# Datos ingresados por el usuario
nombre = input('Ingrese por favor su nombre: ')

"""
edad = input('Ingrese su edad: ')
edad = int(edad)
"""

edad = int( input('Ingrese su edad: ') )

edad_next_year = edad + 1

# Impresión en la consola
print('\n------------------------------')
print('Es un gran gusto conocerte,' , nombre)
print('El día de ahora tu tienes', edad, 'años...')
print('El próximo año vas a tener', edad_next_year, 'años!!')
print('Bueno, me despido mi estimado' , nombre)
print('------------------------------')
