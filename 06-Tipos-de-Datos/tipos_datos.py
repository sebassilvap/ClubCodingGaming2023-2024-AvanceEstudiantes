# ===========================================================================================================
# Tipos de Datos / Tipado de Datos / Data Types

#! IMPORTANTE
# - de manera incorrecta muchos cursos / videos / tutoriales
# - dicen al estudiante que Python tiene solo 4 tipos de datos

'''
Tipo de Dato     |  Denominación  |  Ej:
---------------------------------------------------------
Entero           |  int           |  -20, 0, 5
Punto Flotante   |  float         |  2.5, 0.669, -89.52
Cadena de Texto  |  str           |  'Hola', "Python"
Booleano         |  bool          |  True, False
'''

#! Estos son los tipos BÁSICOS

# Aunque es un poco avanzado nombrar todos los tipos de datos, es importante conocerlos
# saber que existen y son los siguientes:

# Por DEFAULT Python tiene los siguientes tipos de datos que vienen internamente al momento de instalar

'''
https://www.w3schools.com/python/python_datatypes.asp

----------------------------------------------------
Text Type:	     |    str
Numeric Types:   |    int, float, complex
Sequence Types:  |    list, tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType
----------------------------------------------------
'''
# => Como nuestro estudio de Python es progresivo
# - no vamos a ver todos y cada uno en este momento
# - vamos a ver los básicos
# - pero siempre tener en cuenta esta INFO

# ===========================================================================================================

#? 1) type()
# - para averiguar el tipo de dato
# - función interna de python / built-in function
# - función interna como por ejemplo: print()
# - nos va a salir una palabrita "class" => no prestar atención por el momento
# - hacer de cuenta que nos dice el tipo / ¿qué tipo de dato es?
#! RECORDAR: tema funciones & clases lo veremos luego
print()
print('-------- 1) type() --------')

nombre = 'Sebas'
edad = 36
es_profesor = True

print(nombre)
print(edad)
print(es_profesor)

# Averiguando el tipo de dato
#type(nombre) #! de esta manera no vamos a ver nada necesitamos usar el print

print( type(nombre) )
print( type(edad) )
print( type(es_profesor) )

# podemos hacer esto / imprimir en la consola
# de una manera elegante
print( nombre , '|' , type(nombre) )
print( edad , '|' , type(edad) )
print( es_profesor , '|' , type(es_profesor) )



#? 2) string - str
# - string / cadena de texto / serie, cadena de caracteres
# - se definen con:
#   #  A) Con comilla simple => ''
#   #  B) Con comilla doble   => ""
#   #  C) Con 6 comillas dobles o simples => para textos largos (lo usamos para comentarios multilínea)

print()
print('-------- 2) string --------')

# - puede ser 1 o más caracteres
# - (en otros lenguajes cuando solo es uno se tiene el tipo char)

string_1 = 'hola mundo'
string_2 = '     hola mundo      '
string_3 = 'A'
string_4 = "hola mundo"
string_5 = '123456'
string_6 = ''
string_7 = ""
string_8 = "Hola esto va en 'comillas simples' #$%^^"
string_9 = 'Hola esto va en "comillas simples" #$%^^'
#string_test = 'es palabra va en 'comillas simples' ' #! ERROR
string_10 = '''hola mis queridos alumnos
cómo han estado
espero estén bien
att. profe sebas'''

string_11 = """me gusta programar
me gusta python
python es chévere"""

# => impresión en la consola
print( string_1 , '| TIPO =' , type(string_1)  )
print( string_2 , '| TIPO =' , type(string_2)  )
print( string_3 , '| TIPO =' , type(string_3)  )
print( string_4 , '| TIPO =' , type(string_4)  )
print( string_5 , '| TIPO =' , type(string_5)  )
print( string_6 , '| TIPO =' , type(string_6)  )
print( string_7 , '| TIPO =' , type(string_7)  )
print( string_8 , '| TIPO =' , type(string_8)  )
print( string_9 , '| TIPO =' , type(string_9)  )
print( string_10 , '| TIPO =' , type(string_10)  )
print( string_11 , '| TIPO =' , type(string_11)  )



#? 3) int
# - int viene del inglés INTEGER / número entero (sin decimales)
# - números positivos
# - números negativos
# - números CERO
# - SIN DECIMALES

print()
print('-------- 3) int --------')

entero_1 = 20
entero_2 = -2
entero_3 = +5 # no es necesario
#entero_test += 5 #! ya vamos a ver luego => suma en la signación!
entero_4 = 0

print( entero_1, '| TIPO =', type(entero_1) )
print( entero_2, '| TIPO =', type(entero_2) )
print( entero_3, '| TIPO =', type(entero_3) )
print( entero_4, '| TIPO =', type(entero_4) )



#? 4) float
# - float => punto flotante / número decimal
# - números decimales positivos
# - números decimales negativos
# - CERO decimal => 0.0

print()
print('-------- 4) float --------')

decimal_1 = 10.5
decimal_2 = 5.888888888888888888888888888
decimal_3 = -100000.9999
decimal_4 = 0.000000000000001
# notación científica
# 2 e -5 = 2 x 10 ^ -5
# 1.333 x 10 ^ -8 => 1.333 e -8
decimal_5 = 0.0
decimal_6 = -0.0
decimal_7 = 0.0000000000000000000


print( decimal_1 , '| TIPO =' , type(decimal_1) )
print( decimal_2 , '| TIPO =' , type(decimal_2) )
print( decimal_3 , '| TIPO =' , type(decimal_3) )
print( decimal_4 , '| TIPO =' , type(decimal_4) )
print( decimal_5 , '| TIPO =' , type(decimal_5) )
print( decimal_6 , '| TIPO =' , type(decimal_6) )
print( decimal_7 , '| TIPO =' , type(decimal_7) )




#? 5) bool
# - bool => del inglés BOOLEAN
# - valor booleano => Verdadero o Falso
# - Los valores en inglés con la primera letra en mayúscula

print()
print('-------- 5) bool --------')

booleano_verdadero = True
booleano_falso = False

booleano_verdadero_2 = 1
booleano_falso_2 = 0

print( booleano_verdadero , 'TIPO =' , type(booleano_verdadero) )
print( booleano_falso , 'TIPO =' , type(booleano_falso) )
print( booleano_verdadero_2 , 'TIPO =' , type(booleano_verdadero_2) )
print( booleano_falso_2 , 'TIPO =' , type(booleano_falso_2) )



#? 6) None
# - None => nada
# - es muy útil para SIMULAR la creación de una variable "sin asignación"
# - porque a la final le asignamos el valor None
# - para declarar / crear una variable y ponerle un valor luego
# - cambiar el valor a la variable => REASIGNAR VALOR DE VARIABLE
#!  REASIGNAR VALOR DE VARIABLE => veremos a continuación

print()
print('-------- 6) None --------')

#! java
# 2 fases para crear una variable

# int a; => declarar la variable
# a = 20; => asignar valor a variable

# int a = 20 => los 2 pasos en 1 línea


a = None
print( a , type(a) )

a = 20
print( a , type(a) )

a = 'sebas'
print( a , type(a) )

a = True
print( a , type(a) )

a = -10.56789
print( a , type(a) )

#! DATO CURIOSO
