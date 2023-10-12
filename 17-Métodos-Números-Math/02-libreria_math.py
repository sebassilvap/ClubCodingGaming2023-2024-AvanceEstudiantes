# =======================================================
# librería / módulo math de python

# - no necesitamos instalarla con pip
#! - pip => asistente de instalación de librerías y módulos en Python
# - ya viene por defecto al momento de instalar python
# - pero debemos importarla para poder usarla
# =======================================================

#? 1) Importación del módulo
print('\n1) Importación del módulo')
# - las importaciones siempre son la 1era línea de código


#? 2) Constantes Matemáticas
print('\n2) Constantes Matemáticas')
# - math.pi
# - math.e


#? 3) Representación Numérica
print('\n3) Representación Numérica')

## 3.1) math.ceil() & math.floor()
print('\n3.1) math.ceil() & math.floor()')
# - math.ceil()  => devuelve el entero superior
# - math.floor() => devuelve el entero inferior


## 3.2) math.fabs()
print('\n3.2) math.fabs()')
# - igual que abs()
# - devuelve el valor absoluto
#! - pero lo devuelve como float


#? 4) Mínimo Común Múltiplo & Máximo Común Divisor
print('\n4) Mínimo Común Múltiplo & Máximo Común Divisor')
# - math.lcm() => mínimo común múltiplo
# - math.gcd() => máximo común divisor


#? 5) Raíces y Potencia
print('\n5) Raíces y Potencia')

## 5.1) math.sqrt()
print('\n5.1) math.sqrt()')
# - raíz cuadrada
# - sqrt = square root
# - IMPORTANTE: devuelve un flotante


## 5.2) math.cbrt()
print('\n5.2) math.cbrt()')
# - raíz cúbica
# - cbrt = cubic root
# - IMPORTANTE: devuelve un flotante


## 5.3) Potencia
print('\n5.3) Potencia')


## 5.4) Truco para raíces
# math.sqrt(25) = 25 ** 0.5 = 25 ** (1/2)

# raíz cuadrada


# raíz cúbica


# raíz de cualquier valor



#? 6) Logaritmos
print('\n6) Logaritmos')
# - math.log()   => logaritmo base e (logaritmo natural ln)
# - math.log10() => logaritmo base 10
# => devuelven valor flotante

# (pequeña explicación)
# log10 1000 => 10 ** x = 1000 => a qué número debo elevar 10 para que me de 1000
# ln 8 => e ** x = 8 => a qué número debo elevar constante e para que me de 8


#? 7) Exponencial e
print('\n7) Exponencial e')
# - math.exp()
# - constante e ** valor = 2.71.. ^ x


#? 8) Conversión de Ángulos
print('\n8) Conversión de Ángulos')
# - math.degrees(x)  => convierte x de radianes a grados
# - math.radians(x)  => convierte x de grados a radianes
# => devuelven valor flotante

# (pequeña explicación)
# 360 (grados) = 2 * pi (radianes)
# 180 (grados) = pi (radianes)
#  90 (grados) = (1/2) * pi (radianes)
#  60 (grados) = (1/3) * pi (radianes)
#  45 (grados) = (1/4) * pi (radianes)
#  30 (grados) = (1/6) * pi (radianes)

#* cuando se trata de una constante
#* es una buena práctica poner el nombre de la variable en mayúsculas


#? 9) Funciones Trigonométricas
print('\n9) Funciones Trigonométricas')
# - los valores deben darse en RADIANES !!

'''
seno          coseno        tangente
math.sin()    math.cos()    math.tan()
math.asin()   math.acos()   math.atan() => arco funciones 
'''

# => ejemplos básicos de comprobación
# seno 30 grados = 0.5
# tangente 45 grados = 1
# arco coseno 0.5 = 60 grados

# => seno de 30 grados


# => tangente de 45 grados


# => arco coseno de 0.5



#? 10) Truncate => Eliminando parte decimal
print('\n10) Truncate => Eliminando parte decimal')
# - math.trunc(x)
# - no redondea
# - sólo elimina todos los decimales y el punto



#? 11) sum() & math.fsum()
print('\n11) sum() & math.fsum()')
# - al igual que sum()
# - math.fsum() => determina el sumatorio de los valores de una lista

# => Recordemos el problema que teníamos


# => math.fsum() resuelve este problema



#? 12) Funciones Hiperbólicas (*)
print('\n12) Funciones Hiperbólicas (*)')
# - (*) Tema de matemática avanzado
# - Utilizado más en temas de ingeniería
# - No los vamos a profundizar
# - Pero es bueno que sepan que hay como hacer esto

'''
seno hiperbólico     coseno hiperbólico     tangente hiperbólica
math.sinh()          math.cosh()            math.tanh()
math.asinh()         math.acosh()           math.atanh()    => arco funciones 
'''

# ejemplos
