# =====================================================
# String Slicing con STEP (pasos)

# - el slicing tendría la siguiente fórmula general:
#*       variable_string[START : END : STEP]

# - START: índice de inicio => INCLUYENTE
# - END: índice de fin => EXCLUYENTE
# - STEP: salto o pasos
# =====================================================


#? 1) REPASO: Substring con índices positivos
print('\n1) REPASO: Substring con índices positivos')

cadena = 'superPalabraGrande'
#(+)      012345678901234567
#         0         1

# super
# Palabra
# Grande



#? 2) REPASO: Substring omitiendo índices redundantes
print('\n2) REPASO: Substring omitiendo índices redundantes')

# super
# Palabra
# Grande



#? 3) Aplicando salto (step) 
print('\n3) Aplicando salto (step) ')



#? 4) Salto Negativo => Revertir un String
print('\n4) Salto Negativo => Revertir un String')



#? 5) Ejercicio: string & substring / normal & reverso
print('\n5) Ejercicio: string & substring / normal & reverso')

cadena = 'superPalabraGrande'

# cadena revertida
cadena_r = cadena[::-1]

# 3 substring orden normal
sub_1 = cadena[:5] # no necesitamos el 0
sub_2 = cadena[5:12]
sub_3 = cadena[12:] # no es necesario el final

# 3 substring orden reverso
sub_1_r = cadena[:5:-1]
sub_2_r = cadena[5:12:-1]
sub_3_r = cadena[12::-1]

print('** Orden Normal **')
print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)
print('** Orden Reverso (solución errónea) **')
print(cadena_r)
print(sub_1_r)
print(sub_2_r)
print(sub_3_r)

#! Corrección
# - cuando el orden (salto) es inverso
# - la formación del substring también va en orden inverso
# - tenemos varias soluciones a este problema

# repus
# arbalaP
# ednarG

## --------------------
## a) Solución sencilla
## --------------------


## ----------------------
## b) Solución complicada
## ----------------------
# - la misma regla se aplica
# - el primer índice (START) es incluyente
# - el segundo índice (END) es excluyente

cadena = 'superPalabraGrande'
#(+)      012345678901234567
#         0         1
