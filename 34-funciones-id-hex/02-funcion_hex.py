# ===================================================
# Función interna => hex()

# - convierte un número en un valor HEXADECIMAL
# - se retorna un string
# - este string comienza siempre con el prefijo "0x"

# https://www.w3schools.com/python/ref_func_hex.asp

# ===================================================


#? 1) Aplicación de números hexadecimales => colores
print('\n1) Aplicación de números hexadecimales => colores')
# - entre muchas maneras como se pueden expresar los colores
# - tenemos 2 muy conocidas

# *    a) con valores RGB (0 - 255)
# *    b) con valores hexadecimales

# - RGB => RED / GREEN / BLUE
# - básicamente es la cantidad de rojo, verde y azul de 0 a 255
# - esto es muy básico para el diseño WEB, donde se trabaja mucho con colores
# - una herramienta muy útil es el Google Color Picker

# https://g.co/kgs/7ZLMrw

# EJEMPLO
# - en google color picker podemos ver 
# *    RGB(20,50,80) = HEX(#143250)

# => vamos a transformar cada valor RGB a hexadecimal
# - para eso usamos la función interna hex()




#? 2) Aplicación de hex() => dirección en la memoria
print('\n2) Aplicación de hex() => dirección en la memoria')
# - la dirección en la memoria tiene el siguiente formato
# *         0x0243FF

# - así lo hemos podido ver algunas veces
# - como se indicó anteriormente
# - la función interna id() devuelve esta dirección en la memoria como entero
# - con hex() podemos averiguar su valor real tal y como es

