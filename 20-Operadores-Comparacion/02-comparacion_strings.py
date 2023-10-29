# =====================================
# Operadores Booleanos de Comparación
# (también: Operadores Relacionales)

# - Aplicado a strings
# - Se analiza por orden alfabético
# ! ej: Z es mayor a A
# =====================================

letra_1 = 'c'
letra_2 = 'x'


#? 1) Comparación entre 2 letras distintas
print('\n1) Comparación entre 2 letras distintas')

print('\nComparación entre',letra_1,'y',letra_2,':')

print(letra_1, '>', letra_2, ':', letra_1 > letra_2) # c > x : False
print(letra_1, '>=', letra_2, ':', letra_1 >= letra_2) # c >= x : False
print(letra_1, '<', letra_2, ':', letra_1 < letra_2) # c < x : True
print(letra_1, '<=', letra_2, ':', letra_1 <= letra_2) # c <= x : True
print(letra_1, '==', letra_2, ':', letra_1 == letra_2) # c == x : False
print(letra_1, '!=', letra_2, ':', letra_1 != letra_2) # c != x : True




#? 2) Comparación entre 2 letras iguales
print('\n2) Comparación entre 2 letras iguales')

print('\nComparación entre',letra_1,'y',letra_1,':')

print(letra_1, '>', letra_1, ':', letra_1 > letra_1) # c > c : False
print(letra_1, '>=', letra_1, ':', letra_1 >= letra_1) # c >= c : True
print(letra_1, '<', letra_1, ':', letra_1 < letra_1) # c < c : False
print(letra_1, '<=', letra_1, ':', letra_1 <= letra_1) # c <= c : True
print(letra_1, '==', letra_1, ':', letra_1 == letra_1) # c == c : True
print(letra_1, '!=', letra_1, ':', letra_1 != letra_1) # c != c : False





#? 3) Comparación entre 2 cadenas
print('\n3) Comparación entre 2 cadenas')

c_1 = 'AA'
c_2 = 'AAA'

print(c_1, '>', c_2, ':', c_1 > c_2) # AA > AAA : False
print(c_1, '>=', c_2, ':', c_1 >= c_2) # AA >= AAA : False
print(c_1, '<', c_2, ':', c_1 < c_2) # AA < AAA : True
print(c_1, '<=', c_2, ':', c_1 <= c_2) # AA <= AAA : True
print(c_1, '==', c_2, ':', c_1 == c_2) # AA == AAA : False
print(c_1, '!=', c_2, ':', c_1 != c_2) # AA != AAA : True

print('\nComparación entre',c_1,'y',c_2,':')


c_1 = 'amigo'
c_2 = 'amiga'

print(c_1, '>', c_2, ':', c_1 > c_2) # amigo > amiga : True
print(c_1, '>=', c_2, ':', c_1 >= c_2) # amigo >= amiga : True
print(c_1, '<', c_2, ':', c_1 < c_2) # amigo < amiga : False
print(c_1, '<=', c_2, ':', c_1 <= c_2) # amigo <= amiga : False
print(c_1, '==', c_2, ':', c_1 == c_2) # amigo == amiga : False
print(c_1, '!=', c_2, ':', c_1 != c_2) # amigo != amiga : True

print('\nComparación entre',c_1,'y',c_2,':')
# por orden alfabético (Z es la más poderosa, la mayor) #! grado 1
# por tamaño de string (el que tiene mayor tamaño es más poderoso) #! grado 2

c_1 = 'Z'
c_2 = 'AAAAAAAAA'

print('\nComparación entre',c_1,'y',c_2,':')

print(c_1, '>', c_2, ':', c_1 > c_2) # Z > AAAAAAAAA : True
print(c_1, '>=', c_2, ':', c_1 >= c_2) # Z >= AAAAAAAAA : True
print(c_1, '<', c_2, ':', c_1 < c_2) # Z < AAAAAAAAA : False
print(c_1, '<=', c_2, ':', c_1 <= c_2) # Z <= AAAAAAAAA : False
print(c_1, '==', c_2, ':', c_1 == c_2) # Z == AAAAAAAAA : False
print(c_1, '!=', c_2, ':', c_1 != c_2) # Z != AAAAAAAAA : True


#? 4) Comparación entre 2 símbolos
print('\n4) Comparación entre 2 símbolos')

c_1 = '@'
c_2 = '%'

print('\nComparación entre',c_1,'y',c_2,':')

print(c_1, '>', c_2, ':', c_1 > c_2) # @ > % : True # 64 > 37
print(c_1, '>=', c_2, ':', c_1 >= c_2) # @ >= % : True
print(c_1, '<', c_2, ':', c_1 < c_2) # @ < % : False
print(c_1, '<=', c_2, ':', c_1 <= c_2) # @ <= % : False
print(c_1, '==', c_2, ':', c_1 == c_2) # @ == % : False
print(c_1, '!=', c_2, ':', c_1 != c_2) # @ != % : True

# -----------------------------------------------------------------
# => ¿Por qué?
# código decimal de caracteres: https://www.ascii-code.com/
# @ ===> DEC = 64
# % ===> DEC = 37
# -----------------------------------------------------------------

# TECLA ALT + código decimal

# alt + 64 = @
# alt + 164 = ñ
# alt + 165 = Ñ
# alt + 225 = ß