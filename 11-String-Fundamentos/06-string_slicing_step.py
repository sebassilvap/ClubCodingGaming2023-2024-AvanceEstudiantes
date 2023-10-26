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

sub_1 = cadena[0:5]
sub_2 = cadena[5:12]
sub_3 = cadena[12:18]

print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)



#? 2) REPASO: Substring omitiendo índices redundantes
print('\n2) REPASO: Substring omitiendo índices redundantes')

# super
# Palabra
# Grande

sub_1 = cadena[:5]
sub_2 = cadena[5:12]
sub_3 = cadena[12:]

print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)


#? 3) Aplicando salto (step) 
print('\n3) Aplicando salto (step) ')

step_1 = cadena[0:18:1]
print('step_1 =', step_1)

step_2 = cadena[0:18:2]
step_3 = cadena[0:18:3]
step_4 = cadena[0:18:4]

print('step_2 =', step_2)
print('step_3 =', step_3)
print('step_4 =', step_4)



#? 4) Salto Negativo => Revertir un String
print('\n4) Salto Negativo => Revertir un String')

step_1 = cadena[::1]
print('step_1 =', step_1)

step_1_copia = cadena[::]
print('step_1_copia =', step_1_copia)

step_menos1 = cadena[::-1]
print('step_menos1 =', step_menos1)

step_menos2 = cadena[::-2]
print('step_menos2 =', step_menos2)

step_menos3 = cadena[::-3]
print('step_menos3 =', step_menos3)



#? 5) Ejercicio: string & substring / normal & reverso
print('\n5) Ejercicio: string & substring / normal & reverso')

cadena = 'superPalabraGrande'

# cadena invertida
cadena_r = cadena[::-1]

# 3 substring orden normal
#sub_1 = cadena[0:5]
sub_1 = cadena[:5]

sub_2 = cadena[5:12]

sub_3 = cadena[12:18] # no existe el index error
sub_3 = cadena[12:20]
sub_3 = cadena[12:100]
sub_3 = cadena[12:]


print('\n**Orden Normal **')
print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)

# 3 substring orden reverso

cadena = 'superPalabraGrande'
#(+)      012345678901234567
#         0         1

sub_1_r = cadena[0:5:-1]
sub_2_r = cadena[5:12:-1]
sub_3_r = cadena[12::-1]

print('\n\n')
print(cadena)
print(sub_1_r)
print(sub_2_r)
print(sub_3_r)

#! Corrección
# - cuando el orden (salto) es inverso
# - la formación del substring también va en orden inverso
# - tenemos varias soluciones a este problema

print('\n\nSOLUCIÓN SENCILLA')

sub_1 = cadena[:5]
sub_2 = cadena[5:12]
sub_3 = cadena[12:20]


sub_1_r = sub_1[::-1]
sub_2_r = sub_2[::-1]
sub_3_r = sub_3[::-1]

print(sub_1 , sub_1_r) # super repus
print(sub_2 , sub_2_r) # Palabra arbalaP
print(sub_3 , sub_3_r) # Grande ednarG


print('\n\nSOLUCIÓN SENCILLA')

cadena = 'superPalabraGrande'
#(+)      012345678901234567
#         0         1

# - la misma regla se aplica
# - el primer índice (START) es incluyente
# - el segundo índice (END) es excluyente

sub_1_r = cadena[4::-1]
print(sub_1_r)

sub_2_r = cadena[11:4:-1]
print(sub_2_r)

sub_3_r_A = cadena[18:11:-1]
print(sub_3_r_A, 'h')

sub_3_r_B = cadena[:11:-1]
print(sub_3_r_B, 'h')

# ----------------

texto = 'hola'
#        0123

print(texto, type(texto))
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(len(texto))

# ho
print(texto[0:1])
print(texto[0:2])