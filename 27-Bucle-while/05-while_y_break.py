# ==========================================
# while + break

# - break => rompe el bucle y sale de este
# - el código después del while se ejecuta
# ==========================================


#? 1) Ejemplo de funcionalidad básico
print('\n1) Ejemplo de funcionalidad básico')

print('Código ANTES del while')

contador = 10

while contador != 0:
    print('Valor del contador =', contador)
    contador -= 1
    
    if contador == 2:
        print('contador =', contador, 'APLICAMOS BREAK!')
        break # le fuerza a salir del while, sin necesidad de que se cumpla o no la condición
    # end if
# end while

print('Código DESPUÉS del while')




#? 2) Ejemplo práctico => diseño de menú
print('\n2) Ejemplo práctico => diseño de menú\n')
# - aquí vamos a hacer uso del while True
# - siempre que usemos while True => debe existir un break
# - caso contrario, tendremos un bucle infinito

opcion = ''

while True: #! siempre plantear un break dentro
    print('\nMenú de Usuario')
    print('(1) - Comprar')
    print('(2) - Vender')
    print('(3) - Salir del Programa')
    print('**************************\n')
    
    opcion = input('Ingrese su opción : ')
    
    if opcion == '1':
        print('Realizando compra...')
    elif opcion == '2':
        print('Realizando venta...')
    elif opcion == '3' or opcion.lower().strip(' ') == 'salir':
        print('Gracias por utilizar el programa!')
        print('Adiós!')
        break
    else:
        print('ERROR - Opción Incorrecta')
    # end if
# end while

print('Fuera del bucle')
    