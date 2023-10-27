# ===========================================================
# Ejercicio

# Calculadora Básica en Python con input()

# - Realizar una calculadora básica con lo aprendido
# - Básicamente el usuario debe ingresar 2 números
# - Por la terminal con el teclado
# - Efectuar las operaciones aritméticas básicas aprendidas
# - Mostrar los resultados al usuario utilizando print
# ===========================================================

print('\n\n**** CALCULADORA BÁSICA CREADA EN PYTHON ****')

n1 = float( input('Ingrese un PRIMER número: ') )
n2 = float( input('Ingrese un SEGUNDO número: ') )

#print( n1, type(n1) )
#print( n2, type(n2) )

# => Operaciones artiméticas
# y almacenamiento en variables

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2 # float
exponente = n1 ** n2 # n1 ^ n2
modulo = n1 % n2

# qué era el módulo

#  10 |___ 3
#  -9      3
#   1 (RESIDUO)

#print( 10 % 3 ) # 1

print('\n\n**** LOS RESULTADOS SON LOS SIGUIENTES ****')
print('1) SUMA :', n1, '+', n2, '=', suma)
print('2) RESTA :', n1, '-', n2, '=', resta)
print('3) PRODUCTO :', n1, 'x', n2, '=', producto)
print('4) DIVISIÓN :', n1, '/', n2, '=', division)
print('5) EXPONENTE :', n1, '**', n2, '=', exponente)
print('6) MÓDULO :', n1, '%', n2, '=', modulo)
print('**** FIN DE LOS CÁCLULOS ****')