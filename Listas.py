"""
Nombre: Listas.py
Objetivo: muestra la operacion de la estructura de datos llamada lista
Autor:
Fecha: 07/11/2019
"""

# Lista vacia
lista = []
listados = [23, False, "Leonardo", 34.12, 'C', lista]

for i in listados:
	print(i)

# agregar elemento
listados.append("perro")
listados.append(45)
for i in listados:
	print(i)
print(listados[0])
print(listados[-1])