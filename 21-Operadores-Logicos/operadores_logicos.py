# =================================================================
# Operadores Booleanos de Lógica

# - Existen algunos
# - Se van a analizar los 3 más básicos

'''
Operador |  Ejemplo  |  Descripción
----------------------------------------------------------------
not      |  not X    |  Niega al booleano
and      |  X and Y  |  True si todos son True 
or       |  X or Y   |  Basta que 1 sea True, resultado es True
'''
# =================================================================


#? 1) Operador not
print('\n1) Operador not')
# - realiza una negación lógica
# - niega / dice que no

verdadero = True
falso = False

print('verdadero =', verdadero, '|', not verdadero)
print('falso =', falso, '|', not falso)

pregunta = 10 < 5 # False
print(pregunta)
print(not pregunta)

print()
print( True == True ) # True
print( False == False ) # True
print( True == False ) # False
print( False == True ) # False
print( True == (not False) ) # True #! no olvidar el paréntesis 


# * negación de números?

# -----------------------------------------------------
# => RECORDAR el valor booleano de las variables
# 0 => False
# cualquier otro número positivo o negativo => True
# -----------------------------------------------------

print(5)
print(not 5) # False
print(not 0) # True

# -, + diferente de 0 => True
# 0 => False

print(not -20) # False



# * negando un string?

# ----------------------------------------------------
# => RECORDAR el valor booleano de las variables
# string vacío => False
# cualquier otro string así sea un espacio => True
# ----------------------------------------------------

cadena_1 = 'cesar'
cadena_2 = ' '
cadena_3 = '' # False => True

print( cadena_1, cadena_2, cadena_3 ) # cesar
print( not cadena_1, not cadena_2, not cadena_3 ) # False False True



#? 2) Operador and
print('\n2) Operador and')
#  - operador de conjunción
#  - viene de la palabra conjunto => unido, contiguo, cercano
#  - agrupa valores booleanos UNIENDO
#  ! unión lógica (Y)
#  ! basta que uno sea False => el resultado es False

print('\nTabla lógica de and (Y)\n')

print( 'True and True =' , True and True ) # True and True = True
print( 'True and False =' , True and False ) # True and False = False
print( 'False and True =' , False and True ) # False and True = False
print( 'False and False =' , False and False ) # False and False = False


print('\nEjemplo práctico => analizar número en rango\n')

temp_1 = 25
temp_2 = 10
temp_3 = 40
# => si la temperatura está entre 20 y 30 ==> buen clima !!

# => vamos a mezclar / combinar
# operadores lógicos + operadores de comparación

print('TEMP 1 =', temp_1, '¿buen clima? =>', temp_1 >= 20 and temp_1 <= 30)
print('TEMP 2 =', temp_2, '¿buen clima? =>', temp_2 >= 20 and temp_2 <= 30)
print('TEMP 3 =', temp_3, '¿buen clima? =>', temp_3 >= 20 and temp_3 <= 30)
# TEMP 1 = 25 ¿buen clima? => True
# TEMP 2 = 10 ¿buen clima? => False
# TEMP 3 = 40 ¿buen clima? => False


print('\nEjemplo práctico => comprobar una cadena de texto\n')

nombre_user_1 = 'Sebas'
nombre_user_2 = 'dan'

# comprobar:
# - que empiece con mayúscula
# - al menos 5 caracteres
# - que sean sólo letras

# comprobación 1
print( nombre_user_1.istitle(),
       len(nombre_user_1) >= 5,
       nombre_user_1.isalpha()  ,
       '¿Es válido? =>',
       nombre_user_1.istitle() and len(nombre_user_1) >= 5 and nombre_user_1.isalpha()
     )


# comprobación 2
print( nombre_user_2.istitle(),
       len(nombre_user_2) >= 5,
       nombre_user_2.isalpha()  ,
       '¿Es válido? =>',
       nombre_user_2.istitle() and len(nombre_user_2) >= 5 and nombre_user_2.isalpha()
     )


#? 3) Operador or
print('\n3) Operador or')
#  - operador de disyunción
#  - viene de la palabra disyunto => separado, apartado, distante
#  - agrupa valores booleanos SEPARANDO
#  ! separación lógica (O) 
#  ! basta que uno sea True => el resultado es True

print('\nTabla lógica de or (O)\n')

print( 'True or True =' , True or True ) # True or True = True
print( 'True or False =' , True or False ) # True or False = True
print( 'False or True =' , False or True ) # False or True = True
print( 'False or False =' , False or False ) # False or False = False


print('\nEjemplo práctico => analizar número en rango\n')
# una medida debe estar entre 12 y 15
# si no está, entonces está fuera del rango

m_1 = 10
m_2 = 13
m_3 = 15
m_4 = 50

print('¿Están las medidas FUERA del rango?')
#! un mejor ejemplo para or !!
print( 'M1 =', m_1, '==>', m_1 < 12 or m_1 > 15 ) # M1 = 10 ==> True
print( 'M2 =', m_2, '==>', m_2 < 12 or m_2 > 15 ) # M2 = 13 ==> False
print( 'M3 =', m_3, '==>', m_3 < 12 or m_3 > 15 ) # M3 = 15 ==> False
print( 'M4 =', m_4, '==>', m_4 < 12 or m_4 > 15 ) # M4 = 50 ==> True



print('\nEjemplo práctico => analizar comandos en un programa\n')
# tenemos SÓLO 3 comandos posibles
# - añadir
# - eliminar
# - salir

com_1 = 'añadir' #*
com_2 = 'hola'
com_3 = 'eliminar' #*
com_4 = 'mi_nombre'
com_5 = 'salir' #*

print('¿Existe el comando en el programa?')
print(com_1, '? =>',
      com_1 == 'añadir' or com_1 == 'eliminar' or com_1 == 'salir')

print(com_2, '? =>',
      com_2 == 'añadir' or com_2 == 'eliminar' or com_2 == 'salir')

print(com_3, '? =>',
      com_3 == 'añadir' or com_3 == 'eliminar' or com_3 == 'salir')

print(com_4, '? =>',
      com_4 == 'añadir' or com_4 == 'eliminar' or com_4 == 'salir')

print(com_5, '? =>',
      com_5 == 'añadir' or com_5 == 'eliminar' or com_5 == 'salir')

# TEST CONSOLA
# ----------------
# añadir ? => True
# hola ? => False
# eliminar ? => True
# mi_nombre ? => False
# salir ? => True


# ----------------------------------------------
#! Salto en el tiempo
# => veremos que esto es más fácil con listas
# utilizando palabra clave / keyword => in
# ----------------------------------------------

print()

com_1 = 'añadir' #*
com_2 = 'hola'
com_3 = 'eliminar' #*
com_4 = 'mi_nombre'
com_5 = 'salir' #*

lista_comandos = ['añadir', 'eliminar', 'salir']

# EXPLICACIÓN
# => al escribir esto:
# com_1 in lista_comandos
# ==> ¿existe com_1 dentro de la lista_comandos?

print( com_1, '?? =>', com_1 in lista_comandos ) # añadir ?? => True
print( com_2, '?? =>', com_2 in lista_comandos ) # hola ?? => False
print( com_3, '?? =>', com_3 in lista_comandos ) # eliminar ?? => True
print( com_4, '?? =>', com_4 in lista_comandos ) # mi_nombre ?? => False
print( com_5, '?? =>', com_5 in lista_comandos ) # salir ?? => True