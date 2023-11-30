# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ? EJERCICIO
"""
2x - 3y + z = 15
-5x + 8y - 6z = -20
2x + 7y - 15z = 14

x, y, z => ?
"""
# - Realizar un programa en Python
# - Para calcular los valores de x, y, z

# FUENTES
# - https://es.wikipedia.org/wiki/Regla_de_Cramer
# - http://matematicas.relatividad.org/widget-sistema-tres-incognitas.html

# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡


# =======
# Intro
# =======

"""
lista = [1,2,3,4,5]
arreglo = [1,2,3,4,5]
array = [1,2,3,4,5]

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)

for fila in matriz:
    print(fila)
    
for fila in matriz:
    for columna in fila:
        print(columna)"
"""

"""
2x - 3y + z = 15
-5x + 8y - 6z = -20
2x + 7y - 15z = 14

x, y, z => ?
"""

matriz_ecuaciones = [
    [2, -3, 1, 15],
    [-5, 8, -6, -20],
    [2, 7, -15, 14],
]

# ======================================
# Funciones para formar A, Ax, Ay, Az
# ======================================

def formar_A(m):
    return [
        m[0][0:3], # indexing & slicing
        m[1][0:3],
        m[2][0:3],
    ]
# end def

print( formar_A(matriz_ecuaciones) )

def formar_Ax(m):
    return [
        [ m[0][3] , m[0][1] , m[0][2] ],
        [ m[1][3] , m[1][1] , m[1][2] ],
        [ m[2][3] , m[2][1] , m[2][2] ],
    ]
# end def

def formar_Ay(m):
    return [
        [ m[0][0] , m[0][3] , m[0][2] ],
        [ m[1][0] , m[1][3] , m[1][2] ],
        [ m[2][0] , m[2][3] , m[2][2] ],
    ]
# end def

def formar_Az(m):
    return [
        [ m[0][0] , m[0][1] , m[0][3] ],
        [ m[1][0] , m[1][1] , m[1][3] ],
        [ m[2][0] , m[2][1] , m[2][3] ],
    ]
# end def

print( formar_Ax(matriz_ecuaciones) )
print( formar_Ay(matriz_ecuaciones) )
print( formar_Az(matriz_ecuaciones) )


def retornar_matrices_A(m):
    A = formar_A(m)
    Ax = formar_Ax(m)
    Ay = formar_Ay(m) 
    Az = formar_Az(m) 
    
    return [A, Ax, Ay, Az]
# end def


# =========================================
# Función para calcular determinante
# =========================================

"""
m = [
        [ a11 , a12 , a13 ],
        [ a21 , a22 , a23 ],
        [ a31 , a32 , a33 ],
]


det = a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a31*a22*a13 - a32*a23*a11 - a33*a21*a12

==> en términos de programación:

m = [
        [ m[0][0] , m[0][1] , m[0][2] ],
        [ m[1][0] , m[1][1] , m[1][2] ],
        [ m[2][0] , m[2][1] , m[2][2] ],
]

det =    m[0][0] * m[1][1] * m[2][2]  +
      +  m[0][1] * m[1][2] * m[2][0]  +
      +  m[0][2] * m[1][0] * m[2][1]  -
      -  m[2][0] * m[1][1] * m[0][2]  -
      -  m[2][1] * m[1][2] * m[0][0]  -
      -  m[2][2] * m[1][0] * m[0][1] 
      
"""

def calcular_determinante_3x3(m):
    X1 = m[0][0] * m[1][1] * m[2][2]
    X2 = m[0][1] * m[1][2] * m[2][0]
    X3 = m[0][2] * m[1][0] * m[2][1]
    Y1 = m[2][0] * m[1][1] * m[0][2]
    Y2 = m[2][1] * m[1][2] * m[0][0]
    Y3 = m[2][2] * m[1][0] * m[0][1]
    
    return X1 + X2 + X3 - Y1 - Y2 - Y3
# end def


# ==================
# Calcular X, Y, Z
# ==================

"""
# Regla de Cramer
X = calcular_determinante_3x3(formar_Ax(matriz_ecuaciones)) / calcular_determinante_3x3(formar_A(matriz_ecuaciones))
Y = calcular_determinante_3x3(formar_Ay(matriz_ecuaciones)) / calcular_determinante_3x3(formar_A(matriz_ecuaciones))
Z = calcular_determinante_3x3(formar_Az(matriz_ecuaciones)) / calcular_determinante_3x3(formar_A(matriz_ecuaciones))

print('X es igual a {}'.format(X))
print('Y es igual a {}'.format(Y))
print('Z es igual a {}'.format(Z))
"""


def presentar_resultados(m):
    A = formar_A(m)
    Ax = formar_Ax(m)
    Ay = formar_Ay(m)
    Az = formar_Az(m)
    
    det_A = calcular_determinante_3x3(A)
    det_Ax = calcular_determinante_3x3(Ax)
    det_Ay = calcular_determinante_3x3(Ay)
    det_Az = calcular_determinante_3x3(Az)
    
    X = det_Ax / det_A
    Y = det_Ay / det_A
    Z = det_Az / det_A
    
    print( 'X es igual a {:.2f}'.format(X) )
    print( 'Y es igual a {:.2f}'.format(Y) )
    print( 'Z es igual a {:.2f}'.format(Z) )
# end def

presentar_resultados(matriz_ecuaciones)

matriz_ecuaciones = [
    [10, -3, 1, 100],
    [-5, -50, -6, -20],
    [2, 80, -15, 50],
]

print('\n\n\n')
presentar_resultados(matriz_ecuaciones)



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
#! TAREA
# - analizar el siguiente código
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ==============
# COMPROBACIÓN
# ==============
"""
2x - 3y + z = 15
-5x + 8y - 6z = -20
2x + 7y - 15z = 14
"""

#print(matriz_ecuaciones)
def calcular(m):
    X = calcular_determinante_3x3( formar_Ax(m) ) / calcular_determinante_3x3( formar_A(m) )
    Y = calcular_determinante_3x3( formar_Ay(m) ) / calcular_determinante_3x3( formar_A(m) )
    Z = calcular_determinante_3x3( formar_Az(m) ) / calcular_determinante_3x3( formar_A(m) )
    
    return [X, Y, Z]
# end def
resultados = calcular(matriz_ecuaciones)

#print( len(matriz_ecuaciones) , len(resultados) )

i = 0
j = 0

# ==> Paso 1 a Entender
"""
for i in matriz_ecuaciones:
    for j in i:
        print(j)
    print()
# end for
"""

# ==> Paso 2 a Entender
"""
for i in matriz_ecuaciones:
    for index, j in enumerate(i):
        print(index, j)
    print()
# end for
"""

# ==> Paso 3 a Entender
"""
for i in matriz_ecuaciones:
    for index, j in enumerate(i):
        if index < len(resultados):
            print(j , resultados[index])
        else:
            print(j)         
    print()
# end for
"""

# ==> Paso 4 a Entender
"""
for i in matriz_ecuaciones:
    temp = 0
    for index, j in enumerate(i):
        if index < len(resultados):
            temp += j * resultados[index]
        else:
            print(temp , j)         
    print()
# end for
"""

# ==> Paso 5 a Entender
"""
for i in matriz_ecuaciones:
    temp = 0
    for index, j in enumerate(i):
        if index < len(resultados):
            temp += j * resultados[index]
        else:
            print(temp , j, temp == j)
    print()
# end for
"""

print('\n\nCOMPROBACIÓN Y TEST')


def comprobacion(m):
    incognitas = ['X', 'Y', 'Z']
    resultados = calcular(m)
    
    # -- Sistema de Ecuaciones
    print('=> Sistema de Ecuaciones')
    
    for i in m:
        temp = ''
        for index, j in enumerate(i):
            if index < len(resultados):
                temp += '{}*{} +'.format(j, incognitas[index])
            else:
                temp += '\b= {}'.format(j)
        # end for
        print(temp)
    # end for
    
    # -- Reemplazando incógnitas
    print('\n=> Reemplazando Incógnitas')
    
    for i in m:
        temp = ''
        for index, j in enumerate(i):
            if index < len(resultados):
                temp += '{}*{:.2f} +'.format(j, resultados[index])
            else:
                temp += '\b= {}'.format(j) # secuencia de escape \b ==> ¿por qué lo hago?
        # end for
        print(temp)
    # end for
    
    # -- Realizando Cálculos
    print('\n=> Realizando Cálculos')
    
    for i in m:
        temp = 0
        for index, j in enumerate(i):
            if index < len(resultados):
                temp += j * resultados[index]
            else:
                print('{:.2f} || {:.2f}'.format(temp, j))
        # end for
    # end for
    
# end def

comprobacion(matriz_ecuaciones)