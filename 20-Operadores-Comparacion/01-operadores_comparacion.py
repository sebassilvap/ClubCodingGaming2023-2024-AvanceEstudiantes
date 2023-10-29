# =====================================
# Operadores Booleanos de Comparación
# (también: Operadores Relacionales)

# - Aplicado a valores numéricos

'''
Operador |  Definición
-------------------------------
   >     |  Mayor que
   <     |  Menor que
   >=    |  Mayor o igual que
   <=    |  Menor o igual que
   ==    |  Igual que
   !=    |  Diferente de
'''
# =====================================

num_1 = 5
num_2 = 3


print('\n1) Mayor que (>)')
print(num_1, '>', num_2, ' : ', num_1 > num_2) # 5 > 3  :  True
print(num_1, '>', num_1, ' : ', num_1 > num_1) # 5 > 5  :  False


print('\n2) Menor que (<)')
print(num_1, '<', num_2, ' : ', num_1 < num_2) # 5 < 3  :  False
print(num_1, '<', num_1, ' : ', num_1 < num_1) # 5 < 5  :  False



print('\n3) Mayor o Igual que (>=)')
print(num_1, '>=', num_2, ' : ', num_1 >= num_2) # 5 >= 3  :  True
print(num_1, '>=', num_1, ' : ', num_1 >= num_1) # 5 >= 5  :  True



print('\n4) Menor o Igual que (<=)')
print(num_1, '<=', num_2, ' : ', num_1 <= num_2) # 5 <= 3  :  False
print(num_1, '<=', num_1, ' : ', num_1 <= num_1) # 5 <= 5  :  True

#print( num_1 =< num_2 )
#! SyntaxError: invalid syntax



print('\n5) Igual que (==)')
print(num_1, '==', num_2, ' : ', num_1 == num_2) # 5 == 3  :  False
print(num_1, '==', num_1, ' : ', num_1 == num_1) # 5 == 5  :  True
#print( 5 = 5 )
#! SyntaxError: expression cannot contain assignment, perhaps you meant "=="?



print('\n6) Distinto de (!=)')
print(num_1, '!=', num_2, ' : ', num_1 != num_2) # 5 != 3  :  True
print(num_1, '!=', num_1, ' : ', num_1 != num_1) # 5 != 5  :  False

#print( num_1 =! num_2 )
#! SyntaxError: invalid syntax

print('\n\nTEST:')
print( 10 > 8 ) # True
print( 10 >= 80 ) # False
print( 10 != 80 ) # True
print( 10 == 100 ) # False
print( 10 == 10 ) # True
