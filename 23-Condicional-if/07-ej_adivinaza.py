# ===============================================
# Ejercicio

# - juego de adivinanza múltiple
# - 3 posibilidades de premio
# - depende de si el número que de el usuario
# - esté dentro de los rangos establecidos
# ===============================================

# => RANGO DE PREMIOS
premio_1 = [1,5,8,15,19]
premio_2 = [3,9,12]
premio_3 = 11

print('\n\n\n*******************************************')
print('Bienvenido al Juego de Adivinanza\n')

opcion_user = int( input('Adivine el Número Especial: ') )

# => Análisis Condicional

if opcion_user in premio_1:
    print('Usted ha ganado el PREMIO 1')
elif opcion_user in premio_2:
    print('Felicidades, ha ganado el premio especial # 2')
elif opcion_user == premio_3:
    print('GUAU!!! Ha ganado el PREMIO MAYOR!!!')
else:
    print("Lo siento, no ha ganado nada.... :'(")
# end if

print('*******************************************')