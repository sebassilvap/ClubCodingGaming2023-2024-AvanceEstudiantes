# =============================================================
# Problema con la concatenación de strings

# - un problema / error común con la concatenación de strings
# - que genera muchos errores en principantes
# - es querer concatenar un dato que no sea string
# - la solución a esto es el casting
# =============================================================


#? 1) Ejemplo de Error CLÁSICO
print('\n1) Ejemplo de Error CLÁSICO')

nombre = 'sebas'
edad = 36
nota = 18.5
es_estudiante = False

# => De esta manera como conocemos no hay error

print(nombre , type(nombre) )
print(edad , type(edad) )
print(nota , type(nota) )
print(es_estudiante , type(es_estudiante) )
print('---------------------------')
print(nombre, edad, nota, es_estudiante) # print con parámetros

# print => función interna de python
# built-in function
# función => aquella donde podemos poner parámetros
# parámetros / argumentos / funciones => esto lo vamos a ver luego*

#! Adelanto
# suma(x,y) => x + y ## definición de una función / PARÁMETROS
# print( suma(2,3) ) ## 5 => inovacar la función / ejecutar la función / ARGUMENTOS

# type() => función interna de python

print('--------------------------')

print( nombre , type(nombre), '=>', type( type(nombre) ) )
print( edad , type(edad), '=>', type( type(edad) ) )
print( nota , type(nota), '=>', type( type(nota) ) )
print( es_estudiante , type(es_estudiante), '=>', type( type(es_estudiante) ) )

# => CONSOLA:
#sebas <class 'str'> => <class 'type'>
#36 <class 'int'> => <class 'type'>
#18.5 <class 'float'> => <class 'type'>
#False <class 'bool'> => <class 'type'>

#! type => me devuelve el tipo de dato*
# class / POO / OOP / Programación Orientada a Objetos / clase / objeto



# => ¿Cuál es el ERROR típico?
#print( nombre + edad + nota + es_estudiante ) #! TypeError : solo se puede concatenar entre str

# esto no solo pasa en el print, sino en un string en general

nombre = 'sebas'
apellido = 'silva'
edad = 36
nota = 18.5
es_estudiante = False

nombre_completo = nombre + apellido
nombre_completo_2 = nombre + ' ' + apellido
print(nombre_completo)
print(nombre_completo_2)

print(nombre, edad, nota, es_estudiante) # sebas 36 18.5 False
print(nombre,edad,nota,es_estudiante) # sebas 36 18.5 False
print(nombre,    edad,    nota,es_estudiante) # sebas 36 18.5 False

#print( nombre + edad + nota + es_estudiante)
#! TypeError: can only concatenate str (not "int") to str

# => RECORDAR: que todo puede ser "casteado" a string

print( nombre + str(edad) + str(nota) + str(es_estudiante) ) # sebas3618.5False

print( nombre + ' ' + str(edad) + ' ' + str(nota) + ' ' + str(es_estudiante) )

# print en varias líneas

print('\nprint en varias líneas de código\n')
print( nombre + ' ' + 
      str(edad) + ' ' + 
      str(nota) + ' ' +
      str(es_estudiante)
     )


e = '   '
t = '\t'

print( nombre + e + 
      str(edad) + e + 
      str(nota) + e +
      str(es_estudiante)
     )

print( nombre + t + 
      str(edad) + t + 
      str(nota) + t +
      str(es_estudiante)
     )

## SOLUCIÓN
# - utilizar el casting
# - RECORDAR: que todo puede ser transformado a string



#? 2) RESUMEN: Maneras correcta de utilizar print
print('\n2) RESUMEN: Maneras correcta de utilizar print')

nombre = 'Diego'
edad = 24
es_estudiante = False

# format => luego!

# 2.1) print con parámetros y argumentos
print(nombre, 'tiene', edad, 'años. ¿Es estudiante? ==>', es_estudiante)

# 2.2) print con concatenación de string
print(nombre + ' tiene ' + str(edad) + ' años. ¿Es estudiante? ==> ' + str(es_estudiante))