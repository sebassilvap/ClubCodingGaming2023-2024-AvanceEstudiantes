# =====================================================
#   Expresiones Lógicas

# - Uniendo todos los elementos vistos anteriormente
# - Podemos crear expresiones lógicas
# - Debemos recordar siempre la filosofía de Python:

# ?     "El código debe ser fácil de leer y entender
# ?      para cualquier persona que lo lea,
# ?      no solo para el autor del código"

'''
   #* Operadores de Comparación:
    >   <   >=   <=   ==   !=
     
   #* Operadores Lógicos:
   not   and  or
   
   #* Keyword in
   EJ:   'p' in 'python' => True
   
   #* Condicional if
'''

# - Una muy buena práctica
# - Antes de empezar temas más complicados 
# - Es tratar de interpretar el código de Python
# - Con nuestras propias palabras

# =====================================================


#? 1) Ejemplo: Análisis de in / elemento y lista
print('\n1) Ejemplo: Análisis de in / elemento y lista')

lista_1 = [1,2,3,4,5]
lista_2 = [1,8,6,5,7]
lista_3 = []

n1 = 3


# ----------------------------------------------
# 1.1) elemento dentro de una lista
print('\n1.1) elemento dentro de una lista\n')
# ----------------------------------------------




# ----------------------------------------------------
# 1.2) Otra alternativa: not + paréntesis
print('\n1.2) Otra alternativa: not + paréntesis\n')
# ----------------------------------------------------
# - otra manera de usar el not
# - pero más lógica y sentido tiene el "not in"



# ---------------------------------------------------------
# 1.3) not al inicio sin paréntesis => puede confundir
print('\n1.3) not al inicio sin paréntesis => puede confundir\n')
# ---------------------------------------------------------
# - también podemos prescindir de los paréntesis
# - pero la lectura se dificulta
# - y esto puede tender a errores luego
# ! No recomendable



# -------------------------------------------------
# 1.4) Manera redundante, no recomendable
print('\n1.4) Manera redundante, no recomendable\n')
# -------------------------------------------------
# - no olvidar envolver la expresión en ()
# - antes de hacer la comparación
# - caso contrario nos da una respuesta equivocada
# ! No recomendable




# ! ERROR



# -----------------------------------------------------------------------
# 1.5) Análizar de manera equivocada que una lista está vacía
print('\n1.5) Análizar de manera equivocada que una lista está vacía\n')
# -----------------------------------------------------------------------
# - cuando comparamos una lista directamente a False o True
# - lo que hacemos aquí es comparar el valor de un elemento y otro
# - de una manera literal
# - daría False por el simple hecho que una lsita no es igual a un booleano
# ! Uso ERRÓNEO de la comparación



# -----------------------------------------------------
# 1.6) Correción del uso de la comparación
print('\n1.6) Correción del uso de la comparación\n')
# -----------------------------------------------------
# - si lo que deseamos es evaluar si una lista está vacía
# - si está vacía esto es False
# - si tiene algo esto es True
# - podemos hacer un casting primero a bool()
# - una lista vacía tiene un VALOR BOOLEANO de False
# * RECORDAR: valor booleano de las variables !



#? 2) Ejemplo: Analizar la temperatura / clima
print('\n2) Ejemplo: Analizar la temperatura / clima')



#? 3) Ejemplo: Control Básico de Asistencia
print('\n3) Ejemplo: Control Básico de Asistencia')



#? 4) Ejemplo: Análisis de notas sobre 20
print('\n4) Ejemplo: Análisis de notas sobre 20')
# - Básicamente si el promedio es de 15 para arriba, el estudiante aprueba
# - si es de 14 para abajo, el estudiante reprueba



#? 5) Comprobar un elemento dentro de lista
print('\n5) Comprobar un elemento dentro de lista')
# - veremos aquí maneras correctas e incorrectas
# - de formular una expresión lógica


# ----------------------------------------------
# 5.1) Ejemplo # 1: Manera Correcta
print('\n5.1) Ejemplo # 1: Manera Correcta\n')
# ----------------------------------------------
# * MANERA CORRECTA !


# ----------------------------------------------
# 5.2) Ejemplo # 2: Manera Correcta
print('\n5.2) Ejemplo # 2: Manera Correcta\n')
# ----------------------------------------------
# * MANERA CORRECTA !


# ----------------------------------------------
# 5.3) Ejemplo # 3: Manera Incorrecta
print('\n5.3) Ejemplo # 3: Manera Incorrecta\n')
# ----------------------------------------------
# ! MANERA INCORRECTA !


# ----------------------------------------------
# 5.4) Ejemplo # 4: Manera Incorrecta
print('\n5.4) Ejemplo # 4: Manera Incorrecta\n')
# ----------------------------------------------
# ! MANERA INCORRECTA !