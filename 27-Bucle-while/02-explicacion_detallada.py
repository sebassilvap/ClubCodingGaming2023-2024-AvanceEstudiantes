# =======================================================================
# Explicación - Funcionamiento Bucle while

# - vamos a analizar un while sencillo
# - y una slide preparada para esta clase
# - el objetivo es analizar a profundidad lo que pasa en el bucle while
# - y dentro de un bucle en sí
# =======================================================================

#? 1) Imprimir un contador del 1 al 4
print('\n1) Imprimir un contador del 1 al 4')

contador = 1

while contador <= 4:
    print('contador =', contador) # print en cada iteración
    contador += 1
# end while

# consola:
# contador = 1
# contador = 2
# contador = 3
# contador = 4

# ITERACIONES
# condición: contador <= 4
# --------------------------------------------------
# 1era iteración contador <= 4 =>  1 <= 4 => True
# print('contador = 1')
# contador = 2
# --------------------------------------------------
# 2da iteración => 2 <= 4 => True
# print('contador = 2')
# contador = 3
# --------------------------------------------------
# 3ra iteración => 3 <= 4 => True
# print('contador = 3')
# contador = 4
# --------------------------------------------------
# 4ta iteración => 4 <= 4 => True
# print('contador = 4')
# contador = 5
# --------------------------------------------------
# ! INTENTO de una 5ta iteración => 5 <= 4 => False
# - se sale del while 
# - ni el print / ni la suma en asignación
# - el contador queda valiendo 5

print(contador)