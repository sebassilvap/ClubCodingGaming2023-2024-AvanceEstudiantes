# =================================
# Variables

# - una variable es un CONTENEDOR
# - para almacenar un VALOR
# =================================


#? 1) Crear una variable en python
x = 'Hola Mundo'

# a) x => declarando la variable con el nombre 'x'
# b) = 'Hola Mundo' => ASIGNANDO un valor a la variable de nombre 'x'
print()
print('-------------------- (1) --------------------')

print('Hola Sebas')
print(x)




#? 2) Por el momento conocemos 2 tipos de datos
#   - cadena de texto (string - str)
#   - número entero   (int)
#! La siguiente lección hablamos en profundidad de los tipos de datos en Python

print()
print('-------------------- (2) --------------------')

nombre = 'Sebastián'
apellido = "Silva" # podemos usar '' ó ""
edad = 36
es_estudiante = False # tipo booleano - False (Falso)
es_profesor = True # tipo booleano - True (Verdadero)

# => imprimir en la consola

print('nombre : ', nombre)
print('apellido : ', apellido)
print('edad : ', edad)
print('es_estudiante : ', es_estudiante)
print('es_profesor : ', es_profesor)

print('***')

print(nombre)
print(apellido)
print(edad)
print(es_estudiante)
print(es_profesor)



#? 3) Normas de buena escritura en Python
# - nombre de la variable en minúsculas
# - cuando son varias palabras => separadas con guión bajo => _
# - se utiliza mayúculas para constantes
# - no iniciar con mayúsculas => eso se hace en clases (tema que veremos luego)
# - recomendaciones para buena práctica de programación en python
# - su nombre tiene que ser descriptivo de lo que es la variable

print()
print('-------------------- (3) --------------------')

# => variable que describa: nivel de gasolina de un auto
nivel_de_gasolina_auto_1 = 80 # minusculas separadas con _
nivel_gasolina_auto1 = 80

nivelGasolinaAuto = 80 # camelcase (java, javascript)

Nivel = 80 # (X => esta nomenclatura se utiliza para el tema "CLASES - POO (Programación Orientada a Objetos)")

CONSTANTE_PI = 3.14159 # para constantes



#? 4) Impresión de variables en print

print()
print('-------------------- (4) --------------------')

nombre = 'Sebastián'
apellido = "Silva"
edad = 36
es_estudiante = False
es_profesor = True

# 1 FORMA ==> pasarlos como PARÁMETROS de la función print / separados con una coma
#! función / parámetros / argumentos, etc....

print(nombre, apellido, edad, es_estudiante, es_profesor)
print('nombre :',nombre)
print(apellido, 123, nombre, False, True, edad, 'Hola amigo!')

#! no importa los espacios después o antes de la coma
# (o si hay o no espacios)

print('INICIO')
print(nombre,apellido)
print(nombre, apellido)
print(nombre , apellido) #* (me van a ver hacer esto!)
print(nombre ,                             apellido)
print('FIN')

# sumar(x,y)
# sumar(3,2) => 5
# sumar(3,              2) => 5
# sumar(3 , 2) => 5


#! hay otras maneras pero veremos luego !
# adelante sin profundizar

print(nombre + apellido)
print(nombre + ' ' + apellido) #! Ya veremos luego => concatenación


#? 5) Ejercicio Básico - print() de variables y valores 
# Podemos utilizar lo aprendido para imprimir información de manera más estructurada

print()
print('-------------------- (5) --------------------')

nombre = 'Sebastián'
apellido = "Silva"
edad = 36
es_estudiante = False
es_profesor = True

print()
print('*******************************************')
print('Su nombre es : ', nombre , apellido)
print('Tiene : ', edad , "años")
print('¿Es estudiante? : ', es_estudiante)
print('¿Es profesor? : ', es_profesor)
print('*******************************************')



#? 6) DATO CURIOSO
# - en otros lenguajes de programación para declarar una variable
# - se debe especificar el tipo de dato
# - en python no
# - en python el tipado es asumido por python mismo

# EJ en JAVA:
# int edad = 36;

# En Python:
# edad = 36