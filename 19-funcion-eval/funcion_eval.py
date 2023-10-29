# ===============================================
# función interna eval()
# ! built-in functions en Python

# - función interna / built-in function
# - me permite evaluar una expresión matemática
# - que está puesta en forma de string
# ===============================================


#? 1) Siempre y cuando la expresión sea válida, no importa el formato
print('\n1) Siempre y cuando la expresión sea válida, no importa el formato')

expression_1 = '2 * 3 + 10 / 2'
expression_2 = "2*3+10/2"
expression_3 = "2    * 3+10    / 2"

print( eval(expression_1) ) # 11.0
print( eval(expression_2) ) # 11.0
print( eval(expression_3) ) # 11.0

expression_4 = ' 2/*3 + 2'

#print( eval(expression_4) )
#! SyntaxError: invalid syntax
#eval(expression_4)
#! SyntaxError: invalid syntax



#? 2) Todas las reglas aritméticas se aplican
print('\n2) Todas las reglas aritméticas se aplican')

expression = '(2+3) * 3**2 - 10/5'

# (2+3) * 3**2 - 10/5
#   5   *   9  - 2.0
#   45 - 2.0
#   43.0

resultado = eval(expression)
print('resultado =', resultado) # resultado = 43.0


#? 3) Interacción de eval + input
print('\n3) Interacción de eval + input\n')

expression = input('Ingrese una expresión matemática a calcular:\n')
print('------------')

#print('=> El resultado es: ', eval(expression))

resultado = eval(expression)

print('=> El resultado es: ', resultado)