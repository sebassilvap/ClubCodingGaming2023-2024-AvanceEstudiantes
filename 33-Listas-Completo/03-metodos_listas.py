# ==============================================================
# Métodos de Listas
# - Python tiene elementos internos
# - para poder trabajar con listas
#! OJO: muchos de estos modifican la lista original

# https://www.w3schools.com/python/python_lists_methods.asp
# ==============================================================


#? 1) .index()
print('\n1) .index()')
# - devuelve el índice de una búsqueda





#? 2) .append()
print('\n2) .append()')
# - para agregar elemento
# - al FINAL de la lista
# * modifica la lista original





#? 3) .insert()
print('\n3) .insert()')
# - para insertar un elemento en una posición exacta
# - recibe 2 argumentos
# .insert(index, elemento)
# * modifica la lista original





#? 4) del lista[indice]
print('\n4) del lista[indice]')
# - eliminar un elemento de la lista
# - proporcionando la lista y el índice
# - el índice entre corchetes
# * modifica la lista original





#? 5) .pop()
print('\n5) .pop()')
# - por defecto: elimina último elemento de la lista
# - también se puede especificar el índice del elemento a eliminar
# - devuelve el elemento eliminado
# * modifica la lista original


# ------------------------
# por defecto
print('\npor defecto\n')
# ------------------------




# -------------------------------
# especificando index
print('\nespecificando index\n')
# -------------------------------




# ----------------------------------------
# retorna el elemento eliminado
print('\nretorna el elemento eliminado\n')
# ----------------------------------------





#? 6) .remove()
print('\n6) .remove()')
# - elimina un elemento de la lista
# - el elemento lo pasamos como parámetro
# * modifica la lista original



# ------------------------------------------
# * RECORDAR
# 3 maneras de eliminar elementos en listas:

# 1)  del lista[indice]
# 2)  .pop()
# 3)  .remove()
# ------------------------------------------



#? 7) .sort()
# - para ordenar listas
# - recibe 2 argumentos: reverse & key
# * modifica la lista original



# ----------------------------------
# 7.1) sort por defecto
print('\n7.1) sort por defecto\n')
# ----------------------------------
# - por defecto: orden ascendente
# - (A-Z) & menor a mayor




# ---------------------------------------
# 7.2) sort con reverse True
print('\n7.2) sort con reverse True\n')
# ---------------------------------------
# - orden descendente
# - (Z-A) & mayor a menor




# -----------------------------
# 7.3) sort con key
print('\n7.3) sort con key\n')
# -----------------------------
# - key permite un ordenado especial
# - en función a una característica de la lista





#? 8) sorted()
print('\n8) sorted()')
# - a diferencia de sort no me afecta la lista original
# sorted( lista , reverse, key )


# -------------------------------------
# 8.1) sorted() por defecto
print('\n8.1) sorted() por defecto\n')
# -------------------------------------
# - por defecto: orden ascendente
# - (A-Z) & menor a mayor




# --------------------------------------------
# 8.2) sorted() con reverse True
print('\n8.2) sorted() con reverse True\n')
# --------------------------------------------
# - orden descendente
# - (Z-A) & mayor a menor




# ----------------------------------
# 8.3) sorted() con key
print('\n8.3) sorted() con key\n')
# ----------------------------------
# - key permite un ordenado especial
# - en función a una característica de la lista





#? 9) .split()
print('\n9) .split()')
# - para dividir un string
# - en elementos de lista


# => por defecto divide tomando en cuenta los espacios





#? 10) .join()
print('\n10) .join()')
# - para formar un string
# - aplicable a lista o string





#? 11) .list()
print('\n11) .list()')
# - casting a lista
# - también: para crear lista o lista vacía





#? 12) .clear()
print('\n12) .clear()')
# - deja la lista en blanco
# * modifica la lista original





#? 13) .count()
print('\n13) .count()')
# - para contar coincidencias
# - de un elemento en la lista





#? 14) .extend()
print('\n14) .extend()')
# - otra manera de concatenar
# - pero modifica la lista original





#? 15) .reverse()
print('\n15) .reverse()')
# - para revertir el orden de la lista
# * modifica la lista original

