import random

# ================
# Ejemplo de uso
# ================
# random.shuffle() => me baraja la lista
# random.choice() => selecciona al azar elemento de lista

#print( random.random() ) # 0 - 1 (sin incluir el 1)

"""
lista = [1,2,3,4,5]
print(lista)

random.shuffle(lista) # cambia la variable original

print(lista)

elemento_al_azar = random.choice(lista)
print(elemento_al_azar)
"""

opciones_juego = ['Piedra', 'Papel', 'Tijera']

contar_rondas = 1


while True:
    print('\nBienvenidos a Nuestro Juego Piedra / Papel / Tijera')
    print('Opciones del Juego:')
    print('RONDA Número {}'.format(contar_rondas))
    print('(1) - Piedra')
    print('(2) - Papel')
    print('(3) - Tijera')
    print('(4) - Salir (Q)\n')
    
    opcion_user = input('Elija su opción : ')
    opcion_user = opcion_user.title().strip(' ')
    
    opcion_computadora = random.choice(opciones_juego)
    
    # -- Análisis
    
    if opcion_user == 'Piedra' or opcion_user == '1':
        
        opcion_user = 'Piedra'
        
        if opcion_computadora == 'Piedra':
            print('EMPATE !!')
        elif opcion_computadora == 'Papel':
            print( '{} le gana a {} - COMPUTADORA gana!!'.format(opcion_computadora, opcion_user) )
        elif opcion_computadora == 'Tijera':
            print( '{} le gana a {} - USER gana!!'.format(opcion_user, opcion_computadora) )
        # end if
        
    elif opcion_user == 'Papel' or opcion_user == '2':
        
        opcion_user = 'Papel'
        
        if opcion_computadora == 'Papel':
            print('EMPATE !!')
        elif opcion_computadora == 'Tijera':
            print( '{} le gana a {} - COMPUTADORA gana!!'.format(opcion_computadora, opcion_user) )
        elif opcion_computadora == 'Piedra':
            print( '{} le gana a {} - USER gana!!'.format(opcion_user, opcion_computadora) )
        # end if
        
    elif opcion_user == 'Tijera' or opcion_user == '3':
        
        opcion_user = 'Tijera'
        
        if opcion_computadora == 'Tijera':
            print('EMPATE !!')
        elif opcion_computadora == 'Piedra':
            print( '{} le gana a {} - COMPUTADORA gana!!'.format(opcion_computadora, opcion_user) )
        elif opcion_computadora == 'Papel':
            print( '{} le gana a {} - USER gana!!'.format(opcion_user, opcion_computadora) )
        # end if
        
    elif opcion_user == 'Q' or opcion_user == '4':
        print('Gracias por jugar nuestro juego!')
        print('Hasta la próxima! Auf Wiedersehen!')
        break
    
    else:
        print('ERROR - {} no es una opción válida!! :('.format(opcion_user))
    # end if
    
    contar_rondas += 1
# end while  