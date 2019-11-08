"""
Nombre: Funciones.py
Objetivo:  
Autor:
Fecha: 07/11/2019
"""

# ------------------------------------------
# Funcion para imprimir un mensaje
# ------------------------------------------
def printMensaje():
	print("Hola soy una funcion sin parametros")

# ------------------------------------------
# Funcion para retornar una cadena
# ------------------------------------------
def printMensajeDos():
	return "soy la funcion que regresa una cadena"

# ------------------------------------------
# Funcion para recibir una cadena
# ------------------------------------------
def printMensajeTres(cad):
	print("Mensaje recibido: "+cad)

# Funcion main
def main():
	printMensaje()
	print(printMensajeDos())
	printMensajeTres("hola")

if __name__ == '__main__':
	main()
