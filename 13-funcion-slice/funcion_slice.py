# ==================================================
# Función slice()
# built-in functions de Python

# - podemos crear un objeto de tipo slice
# - luego podemos hacer uso de este objeto

#* RECORDEMOS el string slice
#  variable_string[START : END : STEP]

# - con la misma lógica se puede utilizar slice()
#* slice(START , END , STEP)

# RECORDAR:
# - START => es inclusivo
# - END   => es exclusivo

# => en este caso separamos con una coma ','
# ==================================================


#? 1) Uso básico sin step
print('\n1) Uso básico sin step')

#(+)         0123456789012
#(-)                             4321
website_1 = 'https://www.facebook.com'
website_2 = 'https://www.google.com'
website_3 = 'https://www.twitter.com'

# facebook
# google
# twitter

# => string slicing
print('\nRECORDATORIO: String Slicing\n')
nombre_website_1 = website_1[12:-4]
nombre_website_2 = website_2[12:-4]
nombre_website_3 = website_3[12:-4]

print( nombre_website_1 ) # facebook
print( nombre_website_2 ) # google
print( nombre_website_3 ) # twitter

# => ejemplo con la función Slice
print('\nejemplo con la función Slice\n')

patron_corte = slice(12,-4) # patrón de corte generado con la función SLICE

name_website_1 = website_1[patron_corte]
name_website_2 = website_2[patron_corte]
name_website_3 = website_3[patron_corte]

print( name_website_1 ) # facebook
print( name_website_2 ) # google
print( name_website_3 ) # twitter





#? 2) Utilizando también step
print('\n2) Utilizando también step')

#! RECORDAR
# Con string slicing => variable_string[START : END : STEP]
# Con función slice  => slice(START , END , STEP) => patrón de corte

# salto = 1 => por defecto
# para ver cambios / resultados / algo => 2 en adelante

#(+)         0123456789012
#(-)                             4321
website_1 = 'https://www.facebook.com'
website_2 = 'https://www.google.com'
website_3 = 'https://www.twitter.com'

patron_corte_step_2 = slice(12, -4, 2)
patron_corte_step_3 = slice(12, -4, 3)


print('\nCon step = 2\n')
website_1_step_2 = website_1[patron_corte_step_2]
website_2_step_2 = website_2[patron_corte_step_2]
website_3_step_2 = website_3[patron_corte_step_2]

print( website_1_step_2 )
print( website_2_step_2 )
print( website_3_step_2 )


print('\nCon step = 3\n')
website_1_step_3 = website_1[patron_corte_step_3]
website_2_step_3 = website_2[patron_corte_step_3]
website_3_step_3 = website_3[patron_corte_step_3]

print( website_1_step_3 )
print( website_2_step_3 )
print( website_3_step_3 )