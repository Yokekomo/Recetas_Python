# Receta Python 004: Obtener una cantidad arbitraria de elementos mínimos y máximos.

import heapq

numeros = [4, 8, 2, 5, 1, 9, 8, 6, 3, 2, 7, 4, 3, 1, 9, 4]
print(heapq.nsmallest(3, numeros))
print(heapq.nlargest(3, numeros))

productos = [
    {'nombre': 'Mouse', 'Precio': 324},
    {'nombre': 'Teclado', 'Precio': 684},
    {'nombre': 'Mesa', 'Precio': 567},
    {'nombre': 'Portatil', 'Precio': 2345},
    {'nombre': 'Pc', 'Precio': 234556},
    {'nombre': 'Casa', 'Precio': 1002}
    ]

mas_barato = heapq.nsmallest(1, productos, key=lambda p: p['Precio'])
print(mas_barato)