# ===============================================================================
# match-case

#! disponible a partir de python 3.10 - no en versiones anteriores
# - comportamiento de condicional del legendario switch-case
# - switch-case en otros lenguajes de programación
# - se usa cuando una condición puede tener una exagerada cantidad de if & elif

#! para los que vienen de otro lenguaje:
# => en este caso no se necesita poner 'break' al final de cada case
# ===============================================================================

print(""""
      opción 1 - ATAQUE
      opción 2 - DEFENSA
      opción 3 - CURAR COMPAÑEROS
      opción 4 - HUIR DE LA BATALLA
      opción 5 - USAR ÍTEM
      opción 6 - SALIR DEL JUEGO
      ************************************
      """)

player_option = input('Player 1, ingresa tu opción de juego (1-6): ')
print( type(player_option) )

print()

# -----------------------------
# => UTILIZANDO el match-case
# -----------------------------
print('\n=> UTILIZANDO el match-case\n')

match player_option:
    case '1':
        print('opción 1 - EL PLAYER ATACA !')
    case '2':
        print('opción 2 - EL PLAYER SE DEFIENDE !')
    case '3':
        print('opción 3 - CURANDO HP DE COMPAÑEROS')
    case '4':
        print('opción 4 - NOS VAMOS DE AQUÍ... :(')
    case '5':
        print('opción 5 - USANDO ÍTEM')
    case '6':
        print('opción 6 - GAME OVER')
    case _: # opción por defecto = else
        print('ERROR - opción incorrecta')
# end match-case


# -------------------------------
# => UTILIZANDO el if-elif-else
# -------------------------------
print('\n=> UTILIZANDO el if-elif-else\n')

if player_option == '1':
    print('opción 1 - EL PLAYER ATACA !')
elif player_option == '2':
    print('opción 2 - EL PLAYER SE DEFIENDE !')
elif player_option == '3':
    print('opción 3 - CURANDO HP DE COMPAÑEROS')
elif player_option == '4':
    print('opción 4 - NOS VAMOS DE AQUÍ... :(')
elif player_option == '5':
    print('opción 5 - USANDO ÍTEM')
elif player_option == '6':
    print('opción 6 - GAME OVER')
else:
    print('ERROR - opción incorrecta')
# end if

# ----------------------------------------------------------
# - en caso de no contar con una versión de python >= 3.10
# - esta sería la manera de simular un match-case
# - usando if-elif-else
# ----------------------------------------------------------