# ========================================
# Condicional - Anidado

# - es básicamente un if dentro de un if
# ========================================

#? 1) Ejemplo de Condicional Anidado
print('\n1) Ejemplo de Condicional Anidado')

# Análisis de un número

#numero = 8

# => interactuar con input
numero =  int( input('Ingrese un número: ') )
print(numero)

if numero >= 0 and numero <= 10.0: # [0, 10]  ]0 , 10[
    print('Número está entre 0 y 10')
    
    if numero >= 0 and numero <= 5:
        print('Número entre 0 y 5')
    elif numero > 5 and numero <= 10:
        print('Número es mayor que 5 y menor o igual a 10')
else:
    print('Número no está entre 0 y 10')
    
# end if

print( 10 < 5 )
print( 10 < 5.0 )
print( 10 < 5.00000 )
print( 10.0 < 5 )
#print( '10' < 5 )
print( '10' < '5' )