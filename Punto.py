"""
Nombre: Punto.py
Objetivo: es la superclase en la jerarquia de herencia
Autor: 
Fecha: 14/11/2019
"""

class Punto(object):
	# Metodo constructor
	def __init__(self, valorX, valorY):
		#cuerpo del constructor
		self.x = valorX
		self.y = valorY

	# Lista de métodos get
	def getX(self):
		return self.x

	def getY(self):
		return self.y

	# Lista de métodos set
	def setX(self, valorX):
		self.x = valorX

	def setX(self, valorY):
		self.y = valorY

	# Método toString()
	def toString(self):
		return "Las coordenadas del punto son: ", self.x,",",self.y