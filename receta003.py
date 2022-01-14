# Receta Python 003: Obtener los elementos más frecuentes en una lista.

from collections import Counter

numeros = [4, 8, 2, 5, 1, 9, 8, 6, 3, 2, 7, 4, 3, 1, 9, 4]
contador = Counter(numeros)
print(contador.most_common(1))

palabras = 'Viernes noche y yo aquí, Terrible!!!'
print(Counter(palabras).most_common(5))

