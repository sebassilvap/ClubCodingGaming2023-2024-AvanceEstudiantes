# ================================================
# Recorriendo los múltiplos

# - Como vimos con el módulo podemos identificar
# - Fácilmente pares e impares
# - Pero no solo eso
# - También podemos identificar los múltiplos

# EJ: cualquier número múltiplo de 5

#   25 |___ 5
#  -25      5
#*   0

# => (25 % 5 = 0)
# ================================================


#? 1) EJ: Múltiplos de 7 en lista del 1 al 100
print('\n1) EJ: Múltiplos de 7 en lista del 1 al 100')

multiplos_siete = []

for i in range(1,101):
    if i % 7 == 0:
        multiplos_siete.append(i)
    # => else no es necesario, con el if basta
# end for

print( multiplos_siete ) # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]



#? 2) EJ: Múltiplos del 8 en lista del 1 al 100
print('\n2) EJ: Múltiplos del 8 en lista del 1 al 100')

multiplos_ocho = []

contador = 1

while contador <= 100:
    if contador % 8 == 0:
        multiplos_ocho.append(contador)
    
    contador += 1
# end while

print( multiplos_ocho ) # [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]