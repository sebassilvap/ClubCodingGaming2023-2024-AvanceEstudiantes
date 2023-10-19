# ====================================================================
# Buenas prácticas de programación

# - recordar que nuestro código siempre debe ser legible / entendible
# - no solo para nosotros sino para cualquiera que lo lea
# - debemos hacer uso de los recursos siempre que sea posible
# - en este caso, siempre que sea posible usar elif y no varios if
# ====================================================================


#? 1) Utilizando varios if - CASO ACEPTABLE
print('\n1) Utilizando varios if - CASO ACEPTABLE')

#! buena/mala práctica depende
# - en lo posible siempre usar elif para unir varias condiciones
# - en este caso el resultado va a ser el mismo
# - pero el código es más elegante con una buena estructura

comando_usuario = input('Ingrese comando: ')

if comando_usuario == 'atacar':
    print('Player 1 - Ataca')
if comando_usuario == 'esquivar':
    print('Player 1 - Esquiva')
if comando_usuario == 'salir':
    print('Fin del Juego')

# - muchos programadores a veces plantean el código de esta manera
# - no es que esté mal / o haya error
# - en este caso puede haber error si el comando es otra cosa
#! debemos siempre adelantarnos a los errores
# - así sean casi imposibles de que ocurran
# - a continuación se muestra una versión más elegante


## REFACTORIZACIÓN => Versión elegante
# - de esta manera estamos reconociendo cualquiera de los 3 comandos
# - sin importar mayúsculas, minúsculas y espacios



# ====================================================================

#? 2) Utilizando varios if - CASO ERRÓNEO
print('\n2) Utilizando varios if - CASO ERRÓNEO')

# (2.1) versión errónea
print('\n(2.1) versión errónea\n')

# - en este caso, varios if me da un resultado erróneo, todas las condiciones se cumplen


# (2.2) versión no tan óptima - rango simple
print('\n(2.2) versión no tan óptima - rango simple\n')


    
# - el problema de este código es que es muy susceptible a errores
# - si inicio de 10 a 30 siempre se me va a activar el 10, porque todas las condiciones cumplen
# - adicionalmente no se analiza si el ataque es menor a cero
# - es mejor trabajar con rangos y operadores lógicos => para análisis de rangos de valores
# - siempre tratar de cubrir todas las posibilidades existentes


# (2.3) versión óptima - OK
print('\n(2.3) versión óptima - OK\n')

    
    
# - aquí no importa cual condición se analice primero
# - o el orden de las condiciones
# - se cumple si y solo si, el valor está dentro del rango indicado
# - pero igual es una buena práctica dar un orden a estos rangos también