# ===============================================
# Función enumerate

# - una manera sencilla de devolver el índice
# - de los elementos de una lista
# - en lugar de crear un contador externo
# ===============================================


#? 1) bucle for sin enumerate
print('\n1) bucle for sin enumerate')
# - normalmente si deseamos el índice de los elementos que recorremos
# - al utilizar for tenemos que crear un contador extra
# - ej:

lista = [100, 'manzana', True, -8.5, 'python']
#         0        1       2     3       4

print( lista, type(lista), len(lista) )
print( lista[0] )
print( lista[1] )
print( lista[2] )
print( lista[3] )
print( lista[4] )

print('\n\n')

for elemento in lista:
    print(elemento)
# end for

print('\n\n')

index = 0

for elemento in lista:
    print( 'Index =', index, '|' , lista[index] , '|' , elemento )
    index += 1 # suma en la asignación => incremento
# end for



#? 2) Utilizando enumerate
print('\n2) Utilizando enumerate')

lista = [100, 'manzana', True, -8.5, 'python']
#         0        1       2     3       4

for index, elemento in enumerate(lista):
    print('Elemento #', index , '=', elemento)
# end for

# CONSOLA:
"""
Elemento # 0 = 100
Elemento # 1 = manzana
Elemento # 2 = True
Elemento # 3 = -8.5
Elemento # 4 = python
"""