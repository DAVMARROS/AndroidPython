"""
Nombre: Circunferencia.py
Objetivo: muestra como usar la libreria math
Autor:
Fecha: 07/11/2019
"""

import math

def getArea(radio):
	return math.pi * math.pow(radio,2)

# Funcion main
def main():
	ciclo="S"
	while ciclo=="S" or ciclo=="s":
		print("Calculo de Area de Circunferencia")
		r = float(input("Introduce el radio: "))

		# Invocamos las funciones
		print("El area es: ", round(getArea(r),4))
		# Preguntar si desea continuar
		ciclo=input("¿Otro calculo (S/N)?")
	else:
		print("*** Fin de programa ***")

# Para main
if __name__ == '__main__':
	main()
