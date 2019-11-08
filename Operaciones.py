"""
Nombre: Operaciones.py
Objetivo:  
Autor:
Fecha: 07/11/2019
"""

# ------------------------------------------
# Funcion para sumar dos enteros
# ------------------------------------------
def suma(num1, num2):
	res = num1 + num2
	return res

# ------------------------------------------
# Funcion para restar dos enteros
# ------------------------------------------
def resta(num1, num2):
	res = num1 - num2
	return res

# ------------------------------------------
# Funcion para multiplicar dos enteros
# ------------------------------------------
def multiplica(num1, num2):
	res = num1 * num2
	return res

# ------------------------------------------
# Funcion para dividir dos enteros
# ------------------------------------------
def divide(num1, num2):
	res = num1 / num2
	return res

# ------------------------------------------
# Funcion para comparar dos enteros
# ------------------------------------------
def comparar(num1, num2):
	if(num1>num2):
		print("Numero uno es el mayor",num1,",",num2)
	elif(num1<num2):
		print("Numero dos es el mayor",num1,",",num2)
	else:
		print("Los numeros son iguales")

# ------------------------------------------
# Funcion para contar de un entero hasta otro
# ------------------------------------------
def contar(num1, num2):
	if(num2>num1):
		#contar de manera ascendente
		for i in range(num1,num2+1,1):
			print(i)
	elif(num1>num2):
		for i in range(num1,num2-1,-1):
			print(i)
	else:
		print("No hay necesidad de contar, los numeros son iguales")

# Funcion main
def main():
	ciclo="S"
	while ciclo=="S" or ciclo=="s":
		print("--- Operaciones Basicas ---")
		n1 = int(input("Introduce primer numero: "))
		n2 = int(input("Introduce segundo numero: "))

		# Invocamos las funciones
		print("La suma es: ", suma(n1,n2))
		print("La suma es: ", resta(n1,n2))
		print("La suma es: ", multiplica(n1,n2))
		print("La suma es: ", divide(n1,n2))
		comparar(n1,n2)
		contar(n1,n2)
		# Preguntar si desea continuar
		ciclo=input("¿Otra operacion (S/N)?")
	else:
		print("*** Fin de programa ***")

# Para main
if __name__ == '__main__':
	main()
