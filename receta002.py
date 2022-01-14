# Receta Python 002: Obtener el resto de elementos de una secuencia sobre otra secuencia.


tupla = (2, 4, 5, 2, 33, 55, 1)
a, b, * c = tupla
print(a, b, c)


cadena = 'Python'
d, f, g, * h = cadena
print(d, f, g, h)