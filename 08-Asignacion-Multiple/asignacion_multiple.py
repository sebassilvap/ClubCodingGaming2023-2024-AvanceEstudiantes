# =======================================================
# Asignación Múltiple de Valores

# - Formas permitidas en la SINTAXIS de Python
# - Para crear varias variables en una línea de código
# =======================================================

# 1) Asignación normal aprendida
nombre = 'Sebas'
apellido = 'Silva'
edad = 36
es_estudiante = False
es_profesor = True
nota = 75.8

print( nombre, apellido, edad, es_estudiante, es_profesor, nota )


# 2) Reasignación de valores utilizando técnica de asignación múltiple

nombre, apellido, edad, es_estudiante, es_profesor, nota = 'Diego', 'Costa', 15, True, False, 99.9

print( nombre, apellido, edad, es_estudiante, es_profesor, nota )

# 3) Reasignación de varias variables a valor único

# => manera clásica

edad_bob_esponja = 16
edad_patricio_estrella = 16
edad_arenita = 16
edad_don_cangrejo = 16

print( edad_bob_esponja, edad_patricio_estrella, edad_arenita, edad_don_cangrejo )

# => asignación múltiple

edad_bob_esponja = edad_patricio_estrella = edad_arenita = edad_don_cangrejo = 20

print( edad_bob_esponja, edad_patricio_estrella, edad_arenita, edad_don_cangrejo )


# => si deseo cambiar ahora solo 1
edad_bob_esponja = 19
print( edad_bob_esponja, edad_patricio_estrella, edad_arenita, edad_don_cangrejo )

#! esto pasa con estas variables básicas
# => ya veremos que cuando hacemos esto con otras variables (listas) => se cambia el valor