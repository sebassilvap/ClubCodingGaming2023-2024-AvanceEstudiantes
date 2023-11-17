# ========================================================
# Pares e Impares

# - Una práctica común en programación
# - Y en ejercicios introductorios
# - Es la identificación de pares e impares

# - El fundamento se basa en el módulo => %
# EJ:

#   4  |__2
#  -4    2
#*  0

# - El módulo de cualquier número par evaluado en 2 es 0
# - Y de cualquier número impar es diferente de 0 
# ========================================================


#? 1) Números pares del 0 al 20
print('\n1) Números pares del 0 al 20')

# ----------------------------
# 1.1) Utilizado for
print('\n1.1) Utilizado for')
# ----------------------------

for numero in range(0, 21):
    if numero % 2 == 0:
        print(numero)
    else:
        continue
# end for


# -------------------------------
# 1.2) Utilizado while
print('\n1.2) Utilizado while')
# -------------------------------

contador = 0

while contador <= 20:
        
    if contador % 2 == 0:
        print(contador)
        contador += 1 # incremento
    else:
        contador += 1 # incremento
        continue  
# end while



#? 2) Guardando los valores en listas
print('\n2) Guardando los valores en listas')

# -------------------------------
# 2.1) Utilizado for
print('\n2.1) Utilizado for\n')
# -------------------------------

lista_pares = []
lista_impares = []

for x in range(1,21):
    if x % 2 == 0:
        lista_pares.append(x)
    else:
        lista_impares.append(x)
# end for

print( "lista_pares =" , lista_pares ) # lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print( "lista_impares =" , lista_impares ) # lista_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



# -------------------------------
# 2.2) Utilizado while
print('\n2.2) Utilizado while')
# -------------------------------

lista_pares = []
lista_impares = []

contador = 1

while contador <= 20:
    if contador % 2 == 0:
        lista_pares.append(contador)
    else:
        lista_impares.append(contador)
    # end if
    
    contador += 1
# end while

print( "lista_pares =" , lista_pares ) # lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print( "lista_impares =" , lista_impares ) # lista_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



#? 3) Filtrando elementos pares de una lista
print('\n3) Filtrando elementos pares de una lista')

lista_nombres = [
    'Goku',
    'Piccolo',
    'Vegueta',
    'Broly',
    'Freezer',
    'Majin Boo',
    'Androide 18'        
]

print( lista_nombres , type(lista_nombres) )

lista_pares = []

contador = 0

for nombre in lista_nombres:
    contador += 1
    
    if contador % 2 == 0:
        lista_pares.append(nombre)
    else:
        continue
    # end if
# end for

print(lista_pares) # ['Piccolo', 'Broly', 'Majin Boo']