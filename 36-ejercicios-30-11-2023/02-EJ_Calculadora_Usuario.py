# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# Calculadora que Interactúe con el Usuario
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

def sumar(x,y):
    return x + y
# end def

def restar(x,y):
    return x - y
# end def

def multiplicar(x,y):
    return x - y
# end def

def dividir(x,y):
    return x / y
# end def

def modulo(x,y):
    return x % y
# end def

def potencia(x,y):
    return x ** y
# end def

"""
a = '        saltar el abismo     '

print(a)
print(a.replace(' ' , ''))
print(a.strip(' '))
"""


while True:
    print('\nBienvenidos a nuestro Programa')
    print('(1) - Realizar Cálculos')
    print('(2) - Salir del Programa (q)')
    print('--------------------------------\n')
    
    opcion_user = input('Elija su opción : ')
    opcion_user = opcion_user.lower().strip(' ')
    
    if opcion_user == '1':
        numero_1 = input('Número 1 para el Cálculo : ')
        numero_2 = input('Número 2 para el Cálculo : ')
        
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        
        print( '{} + {} = {}'.format(numero_1, numero_2, sumar(numero_1, numero_2)) )
        print( '{} - {} = {}'.format(numero_1, numero_2, restar(numero_1, numero_2)) )
        print( '{} * {} = {}'.format(numero_1, numero_2, multiplicar(numero_1, numero_2)) )
        print( '{} / {} = {:.4f}'.format(numero_1, numero_2, dividir(numero_1, numero_2)) )
        print( '{} % {} = {}'.format(numero_1, numero_2, modulo(numero_1, numero_2)) )
        print( '{} ^ {} = {}'.format(numero_1, numero_2, potencia(numero_1, numero_2)) )
        
    elif opcion_user == '2' or opcion_user == 'q':
        print('Gracias por usar nuestro programa. See you! :(')
        break
    
    else:
        print( 'ERROR - {} no es una opción válida!! :('.format(opcion_user) )
# end while
