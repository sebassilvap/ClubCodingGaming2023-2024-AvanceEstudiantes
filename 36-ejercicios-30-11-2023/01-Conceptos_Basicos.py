# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 2 conceptos básicos para el ejercicio a realizar
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# =================================
#? 1) Funciones en Python
print('\n1) Funciones en Python')
# =================================

# ==> Función sin retorno
def sumar(x, y):
    print('La suma de', x, '+', y, '=', x + y)
# end def

sumar(2,6)
sumar(3,10)

def saludar(nombre):
    print('Hola', nombre)
# end def

saludar('Sebas')
saludar('Valentina')
saludar('Ana Paula')

# ==> Función con retorno
# (keyword return)

def sumar_2(x, y): # argumentos
    return x + y
# end def

sumar_2(10,5) # parámetros
print( sumar_2(10,5) )

resultado = sumar_2(5,8)
print(resultado)

# ==> retorno y print
def sumar_3(x, y):
    print(x, '+', y, '=', x+y)
    return x + y
    print('Hola Sebas')
# end def

sumar_3(14, 10.5)
print( sumar_3(12, 10.5) ) # method chaining

lista=[1,2,3]

print( type(len(lista)) )



# ==================================
#? 2) String Format Básico
print('\n2) String Format Básico')
# ==================================

nombre = 'Sebas'
edad = 36
nota = 14.5
es_estudiante = False

print( nombre , edad , nota , es_estudiante ) # Sebas 36 14.5 False
#print( nombre + edad + nota + es_estudiante )
print( nombre + str(edad) + str(nota) + str(es_estudiante) ) # Sebas3614.5False
print( nombre + ' ' + str(edad) + ' ' + str(nota) + ' ' + str(es_estudiante) ) # Sebas 36 14.5 False


# str.format()
print( '{} {} {} {}'.format(nombre, edad, nota, es_estudiante) ) # Sebas 36 14.5 False
print( 'Hola {}, tu tienes {} años. Tu nota es: {}. ¿Eres Estudiante? {}'.format(nombre, edad, nota, es_estudiante) ) # Hola Sebas, tu tienes 36 años. Tu nota es: 14.5. ¿Eres Estudiante? False


# f'String'
print( f'Hola {nombre}, tu tienes {edad} años. Tu nota es: {nota}. ¿Eres Estudiante? {es_estudiante}') # Hola Sebas, tu tienes 36 años. Tu nota es: 14.5. ¿Eres Estudiante? False 


# str.format() => números
pi = 3.14159

print( pi )
print( '{}'.format(pi) )
print( '{:.2f}'.format(pi) )

pi = '{:.2f}'.format(pi)
print( type(pi) )
pi = float(pi)
print(pi , type(pi))