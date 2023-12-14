# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# EJERCICIO

# JUGANDO CON COLECCIONES
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡


calificaciones_alumnos = {
    'Andrés Pérez' : (15, 19, 14),
    'Sebas Silva' : (14, 13, 20),
    'Carlos Andrade' : (12, 15, 16),
    'Ximena Santillán' : (20, 11, 15),
    'Sofía Cáceres' : (18, 10, 13),
    'Juan Pascuales' : (10, 19, 15),
}



# ====================================================================
# 1) imprimir diccionario, tipo e impresión de recorrido
print('\n\n1) imprimir diccionario, tipo e impresión de recorrido\n')
# ====================================================================

print( calificaciones_alumnos , type(calificaciones_alumnos) )

for clave, valor in calificaciones_alumnos.items():
    print( 'NOMBRE : {} | CALIFICACIONES: {}'.format(clave, valor) )
# end for 

    

# ==================================================================
# 2) Ordenamiento del diccionario en orden alfabético
print('\n\n2) Ordenamiento del diccionario en orden alfabético\n')
# ==================================================================
# - crear una función 
# - que acepte 2 parámetros, el diccionario de los alumnos y notas
# - y un string que puede ser 'A-Z'o 'Z-A'
# - me debe devolver el mismo diccionario pero ordenado
# - con el nombre de los alumnos de A-Z o de Z-A

"""
lista = list(calificaciones_alumnos)
print(lista)

lista_1 = list( calificaciones_alumnos.keys() )
print(lista_1)

lista_2 = list( calificaciones_alumnos.values() )
print(lista_2)

lista_3 = list( calificaciones_alumnos.items() )
print(lista_3)
"""


"""
# función normal
def suma(x, y):
    return x + y
# end def

print( suma(5,8) ) # 13

# función lambda
# 1 sola línea y N argumentos

sumatoria = lambda x, y : x + y

print( sumatoria(10,15) )
"""


"""
lista = list( calificaciones_alumnos.items() )
lista_ordenada = None

lista_ordenada = sorted(
    lista,
    key = lambda fila : fila[0]
)

print(lista_ordenada)

lista_ordenada = sorted(
    lista,
    key = lambda fila : fila[0],
    reverse=True
)

print(lista_ordenada)
"""

def orden_alumnos_nombre( diccionario , tipo_orden ):
    lista = list( diccionario.items() )
    lista_ordenada = None
    
    if tipo_orden == 'A-Z':
        lista_ordenada = sorted(
            lista,
            key = lambda fila : fila[0]
        )
    
    elif tipo_orden == 'Z-A':
        lista_ordenada = sorted(
            lista,
            key = lambda fila : fila[0],
            reverse=True
        )
        
    return dict(lista_ordenada)
# end def


alumnos_notas_a_z = orden_alumnos_nombre(calificaciones_alumnos, 'A-Z')
alumnos_notas_z_a = orden_alumnos_nombre(calificaciones_alumnos, 'Z-A')

print(alumnos_notas_a_z, type(alumnos_notas_a_z))

print(alumnos_notas_z_a, type(alumnos_notas_z_a))

    


# =====================================================================================
# 3) Función para crear una lista de 4 elementos, el 4to es el promedio
print('\n\n3) Función para crear una lista de 4 elementos, el 4to es el promedio\n')
# =====================================================================================
# - devolver como lista !!!
# - usar función lambda

"""
notas = calificaciones_alumnos.values()
print(notas , type(notas))

notas = list(notas)
print(notas , type(notas))

lista_notas_promedio = map(
    lambda fila : [ fila[0], fila[1], fila[2], sum(fila)/len(fila) ],
    notas
)

lista_notas_promedio = list(lista_notas_promedio)

print(lista_notas_promedio)

lista = [1,2,3]
print( sum(lista) )
print( len(lista) )
"""

def lista_notas_promedio( diccionario ):
    
    notas = diccionario.values()
    
    notas_y_promedio = map(
        lambda x : [ x[0], x[1], x[2], sum(x)/len(x) ],
        notas
    )
    
    return list(notas_y_promedio)
# end def

# TEST
print( lista_notas_promedio( calificaciones_alumnos ) )

      
        

# ======================================================
# 4) Devolver el promedio con 2 decimales
print('\n\n4) Devolver el promedio con 2 decimales\n')
# ======================================================
# - devolver como tupla !!!

def promedio_2_decimales( notas ):
    nota_1 = float(notas[0])
    nota_2 = float(notas[1])
    nota_3 = float(notas[2])
    
    promedio = sum(notas) / len(notas)
    promedio = '{:.2f}'.format(promedio) # string
    promedio = float(promedio) # float
    
    return (nota_1, nota_2, nota_3, promedio)
# end def


notas_ejemplo = [14,13,20]

print( promedio_2_decimales(notas_ejemplo) )




# ==========================================================================================
# 5) Redefinir función notas_promedio pero mostrando promedio con 2 decimales
print('\n\n5) Redefinir función notas_promedio pero mostrando promedio con 2 decimales\n')
# ==========================================================================================
# - utilizar la función definida en paso 4
# - en lugar de la función lambda

def lista_notas_promedio( diccionario ):
    
    notas = diccionario.values()
    
    notas_y_promedio = map(
        #lambda x : [ x[0], x[1], x[2], sum(x)/len(x) ],
        promedio_2_decimales,
        notas
    )
    
    return list(notas_y_promedio)
# end def

# TEST
print( lista_notas_promedio( calificaciones_alumnos ) )




# ====================================================================================
# 6) Mostrar diccionario con alumnos, notas y promedio con una función
print('\n\n6) Mostrar diccionario con alumnos, notas y promedio con una función\n')
# ====================================================================================

# sin función
"""
#nombres = calificaciones_alumnos.keys()
#nombres = list(nombres)

nombres = list( calificaciones_alumnos.keys() )
print(nombres)
print()

calificaciones = list( calificaciones_alumnos.values() )
print(calificaciones)
print()

calificaciones_y_promedio = lista_notas_promedio(calificaciones_alumnos)
print(calificaciones_y_promedio)
print()


l1 = [100, 200, 300]
l2 = ['a', 'b', 'c']

resultado = zip(l1, l2)
print(resultado)

print( dict(resultado) )

nombres_notas_promedio = dict(zip(nombres, calificaciones_y_promedio))
print(nombres_notas_promedio)
"""

def dict_alumnos_notas_promedio( diccionario ):
    nombres = list( diccionario.keys() )
    notas_promedio = lista_notas_promedio(diccionario)
    
    nombres_notas_promedio = dict(zip(nombres, notas_promedio))
    
    return nombres_notas_promedio
# end def

alumnos_notas_promedio = dict_alumnos_notas_promedio( calificaciones_alumnos ) #!!!!
print(alumnos_notas_promedio)


for clave, valor in alumnos_notas_promedio.items():
    print( 'ALUMNOS: {} | Notas y Promedio: {}'.format(clave, valor) )
# end for




# ===============================================================================
# 7) Función para imprimir diccionario Alumnos / Notas / Promedio
print('\n\n7) Función para imprimir diccionario Alumnos / Notas / Promedio\n')
# ===============================================================================

def imprimir_alumnos_notas_promedio_1( diccionario ):
    for clave, valor in diccionario.items():
        print( 'ALUMNO: {} / NOTAS Y PROMEDIO: {}'.format(clave, valor) )
    # end for
# end def
        
imprimir_alumnos_notas_promedio_1( alumnos_notas_promedio )    

print('\n\n')

def imprimir_alumnos_notas_promedio_2( diccionario ):
    for clave, valor in diccionario.items():
        print( 'ALUMNO: {} / NOTAS: {} / PROMEDIO: {}'.format(clave, valor[0:3], valor[3]) )
    # end for
# end def   

imprimir_alumnos_notas_promedio_2( alumnos_notas_promedio ) 



# ==============================================
# 8) Ordenar alumnos por promedio
print('\n\n8) Ordenar alumnos por promedio\n')
# ==============================================

"""
{
    'nombre alumno_A' : (nota_1, nota_2, nota_3, promedio),
    'nombre alumno_B' : (nota_1, nota_2, nota_3, promedio),
    'nombre alumno_C' : (nota_1, nota_2, nota_3, promedio),
    'nombre alumno_D' : (nota_1, nota_2, nota_3, promedio),
    ....
    ...
    .
}
"""


def orden_notas( diccionario, tipo_orden ):
    lista = list( diccionario.items() )
    lista_ordenada = None
    
    if tipo_orden == 'menor-mayor':
        lista_ordenada = sorted(
            lista,
            key = lambda fila : fila[1][3]
        )
    
    elif tipo_orden == 'mayor-menor':
        lista_ordenada = sorted(
            lista,
            key = lambda fila : fila[1][3],
            reverse=True
        )
        
    return dict(lista_ordenada)
# end def

# TEST
orden_de_mayor_menor = orden_notas( alumnos_notas_promedio, 'mayor-menor' )
orden_de_menor_mayor = orden_notas( alumnos_notas_promedio, 'menor-mayor' )

imprimir_alumnos_notas_promedio_2(orden_de_mayor_menor)

print('\n\n')

imprimir_alumnos_notas_promedio_2(orden_de_menor_mayor)



# ==========================================================
# 9) Crear un Gráfico Comparativo de los Alumnos
print('\n9) Crear un Gráfico Comparativo de los Alumnos')
# ==========================================================

# nombres, apellidos
nombres_apellidos = list( alumnos_notas_promedio.keys() )

nombres = map(
    lambda x : x.split()[0],
    nombres_apellidos
)

nombres = list(nombres)
print(nombres)


apellidos = list(map(
    lambda x : x.split()[1],
    nombres_apellidos
))
print(apellidos)

# id
nombres_id = list(map(
    lambda x : (x.split()[0]).upper()[0:3],
    nombres_apellidos
))
print(nombres_id)


# promedios
dict_a_list = list( alumnos_notas_promedio.items() )
print(dict_a_list)

promedios = map(
    lambda fila : fila[1][3],
    dict_a_list
)

print(promedios)
promedios = list(promedios)
print(promedios)


# plot
import matplotlib.pyplot as plt # generalmente esto va en la 1era línea de código

plt.title('Alumnos y Promedio')
plt.xlabel('Nombres de los Alumnos')
plt.ylabel('Promedio de Notas')

plt.plot(
    nombres_id,
    promedios,
    'o-y',
    linewidth = 5,
    ms = 10,
    mfc = 'r',
    mec = 'g'
)

plt.grid()

plt.show()

