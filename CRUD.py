"""
Nombre: CRUD.py
Objetivo: muestra la operacion de la estructura de datos llamada lista
Autor:
Fecha: 07/11/2019
"""

lista = []

def insetarItem():
	item = str(input("Ingrese el elemento a insertar: "))
	lista.append(item)
	pausa()

def buscarItem():
	item = str(input("Ingrese el elemento a buscar: "))
	if item in lista:
		print("Item encontrado: ",item)
	else:
		print("El item no existe en la lista: ")
	pausa()

def buscarPosicion():
	index = int(input("Ingrese la posicion del elemento a buscar: "))
	if(len(lista)>index-1):
		print("Item: ",lista[index-1])
	else:
		print("Indice fuera de rango")
	pausa()

def modificarItem():
	item = str(input("Ingrese el elemento a modificar: "))
	if item in lista:
		index = lista.index(item)
		item = str(input("Ingrese el nuevo elemento: "))
		lista[index] = item
	else:
		print("El item no existe en la lista")
	pausa()

def eliminarItem():
	item = str(input("Ingrese la posicion del elemento a eliminar: "))
	if item in lista :
		lista.remove(item)
	else:
		print("El item no existe en la lista")
	pausa()

def pausa():
	print("\nOperacion realizada")
	wait = input("Oprime una tecla para continuar")

def reporte():
	cont=1
	for i in lista:
		print("Item",cont,":",i)
		cont+=1
	pausa()

# Funcion main
def main():
	ciclo="s"
	while ciclo=="S" or ciclo=="s":
		print("--- CRUD con listas ---\n")

		print("1. Agregar elemento")
		print("2. Buscar elemento")
		print("3. Buscar por posicion")
		print("4. Modificar elemento")
		print("5. Eliminar elemento")
		print("6. Listado")
		print("7. Salir")
		op=int(input("Selecciona la opcion: "))

		if op==1:
			insetarItem()
		elif op==2:
			buscarItem()
		elif op==3:
			buscarPosicion()
		elif op==4:
			modificarItem()
		elif op==5:
			eliminarItem()
		elif op==6:
			reporte()
		elif op==7:
			ciclo="n"
		else:
			print("Opcion no valida")
		print("\n");
	else:
		print("*** Fin de programa ***")

# Para main
if __name__ == '__main__':
	main()
