# ==========================================================
# Condicional - if
# Sentencia - if
# (if statement)

# - uno de los elementos más importantes de un programa
# - yo lo he visto en el 99% de programas
# - podemos dividir el flujo / el camino de un programa
# - se traduce al español como SI
# - le damos al programa opciones
# - al enunciarlo el bloque de código va indentado
#! - se ejecuta una instrucción cuando la condición es True
# ==========================================================


#? 1) Ejemplo básico => Análisis de una nota
print('\n1) Ejemplo básico => Análisis de una nota\n')
# - 20 es sobresaliente
# - 15 a 19 => el estudiante ha aprobado
# - 12 a 14 => el estudiante pierde el cupo
# - menor a 12 => estudiante pierde el año



#? 2) Explicación de los elementos del bloque if
print('\n2) Explicación de los elementos del bloque if\n')

print('''
if (condicion_1): #! => si condicion_1 se cumple:
    - entramos en modo condición
    - esto se ejecuta si condicion_1 == True
    - se crea un nuevo bloque de código
    - este nuevo bloque va indentado
    - con la indentación python sabe que estamos en un nuevo bloque
    
elif (condicion_2): #! => o en caso de que condicion_2 se cumpla:
    - pasamos a una nueva condición
    - en caso de que condicion_1 no se cumpla
    - condicion_1 == False
    - se ejecuta este bloque si condicion_2 == True
    
elif (condicion_3): #! => o en caso de que condicion_3 se cumpla:
    - si condicion_1 y condicion_2 no se cumplen
    - condicion_1 == False and condicion_2 == False
    - se ejecuta este nuevo bloque si condicion_3 es False
    
else: #! => si nada de arriba se cumple, para cualquier otro caso:
    - este bloque se ejecuta si ni if o cualquier elif se cumple
    - caso por default
    - caso por defecto
''')



#? 3) El if / elif se ejecuta cuando la condición es True
print('\n3) El if / elif se ejecuta cuando la condición es True\n')

# => ejemplo 1
print('\n=> ejemplo 1\n')



# => ejemplo 2
print('\n=> ejemplo 2\n')


# => ejemplo 3
print('\n=> ejemplo 3\n')
    


#? 4) Orden de ejecución del condicional if
print('\n4) Orden de ejecución del condicional if\n')
# - la ejecución del código como en un script de python
# - es de arriba hacia abajo
# - también tiene sentido trabajar con un orden en la comparación



# => esto no tendría sentido si no aplico un orden en las comparaciones
#! mal ejemplo de programación del if

numero = 1



'''
- en los 2 códigos anteriores el primer if se cumple
- de hecho el if no tiene sentido 
- el sentido viene dado por el programador
- recordar al final que el computador solo interpreta las intenciones del programador
- lo anteriormente expuesto no es un error pero muy mala práctica y uso del if
'''



#? 5) Inicio y Fin de un Condicional if
print('\n5) Inicio y Fin de un Condicional if\n')

# => varias posibilidades de un bloque if
##  (A) inicia con if y termina con else
##  (B) inicia con if y termina con elif
##  (C) inicia con if y termina con el inicio de un nuevo if

print('\n(A) inicia con if y termina con else\n')

# ejemplo 5.1)


# ejemplo 5.2)

    
# => una buena práctica en una condición es abarcar todas las posibilidades que puedan darse!


print('\n(B) inicia con if y termina con elif')
print('(C) inicia con if y termina con el inicio de un nuevo if\n')

numero = 100
# numero = 1000


# => con el else nos aseguramos de abarcar todas las posibilidades que pueden darse!