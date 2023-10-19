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



# => ¿Cuál es el ERROR típico?
#print( nombre + edad + nota + es_estudiante ) #! TypeError : solo se puede concatenar entre str

# esto no solo pasa en el print, sino en un string en general


## SOLUCIÓN
# - utilizar el casting
# - RECORDAR: que todo puede ser transformado a string



#? 2) RESUMEN: Maneras correcta de utilizar print
print('\n2) RESUMEN: Maneras correcta de utilizar print')

nombre = 'Diego'
edad = 24
es_estudiante = False
