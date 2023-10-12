# =================================================
# Concatenación de Strings

# - operador para concatenar => +
# - se basa en "sumar" strings para formar 1 solo
# =================================================

#? 1) Concatenación básica => +
print('\n1) Concatenación básica => +')

string_1 = 'hola mundo'
print(string_1)

string_2 = string_1 + string_1
print(string_2)

string_3 = 'hola sebas' + 'hola sebas'
print(string_3)

print('hola' + ' python')


#? 2) Concatenación dentro de print
print('\n2) Concatenación dentro de print')
# - básicamente es otra manera como podemos usar print

string_1 = 'hola mundo'
print('hola mundo' + 'hola mundo' + 'hola mundo' + 'hola mundo')
print('hola mundo', 'hola mundo')

string_2 = 'sebas'

print('sebas' + ' sebas')
print('sebas'+'      sebas')
print(    'sebas'+' sebas'     )
print(string_2, string_2)
print(   string_2   ,    string_2  )


#? 3) Concatenación sin '+'
print('\n3) Concatenación sin '+'')
# - cuando usamos valores directos
# - se puede omitir el '+'
#! - CUIDADO: esto es error si se trabaja con variables

string_1 = 'sebas python'
print(string_1)

string_2 = 'sebas python' 'sebas python'
print(string_2)

# => Error al usar variables
string_3 = 'hola mundo'
#resultado = string_3 string_3
#! SyntaxError: invalid syntax

print('python')