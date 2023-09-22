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
print(nombre)
#type(nombre) # para ver el resultado necesito usar print
print(type(nombre))

# podemos hacerlo de una manera más ELEGANTE
print(nombre , type(nombre))




#? 2) string - str
# - string / cadena de texto / serie, cadena de caracteres
# - se definen con:
#   #  A) Con comilla simple => ''
#   #  B) Con comilla doble   => ""
#   #  C) Con 6 comillas dobles o simples => para textos largos (lo usamos para comentarios multilínea)

# - puede ser 1 o más caracteres
# - (en otros lenguajes cuando solo es uno se tiene el tipo char)





#? 3) int
# - int viene del inglés INTEGER / número entero (sin decimales)
# - números positivos
# - números negativos
# - números CERO
# - SIN DECIMALES




#? 4) float
# - float => punto flotante / número decimal
# - números decimales positivos
# - números decimales negativos
# - CERO decimal => 0.0




#? 5) bool
# - bool => del inglés BOOLEAN
# - valor booleano => Verdadero o Falso
# - Los valores en inglés con la primera letra en mayúscula




#? 6) None
# - None => nada
# - es muy útil para SIMULAR la creación de una variable "sin asignación"
# - porque a la final le asignamos el valor None
# - para declarar / crear una variable y ponerle un valor luego
# - cambiar el valor a la variable => REASIGNAR VALOR DE VARIABLE
#!  REASIGNAR VALOR DE VARIABLE => veremos a continuación







