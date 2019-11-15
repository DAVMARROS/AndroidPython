"""
Nombre: Circulo.py
Objetivo: es la subclase de segundo nivel en la jerarquia de herencia
Autor: 
Fecha: 14/11/2019
"""
from Punto import Punto
import math

class Circulo(Punto):

	# Constructr
	def __init__(self, vradio, valorX, valorY):
		# creamos atributo de la clase Circulo
		self.radio=vradio
		# Invocar a constructor de la superclase
		Punto.__init__(self, valorX, valorY)

	# Lista de metodos get
	def getRadio(self):
		return self.radio

	# Metodod para calcular area de la circunferencia
	def getArea(self):
		return math.pi * math.pow(self.radio,2)

	# Lista de metodos set
	def setRadio(self,valorRadio):
		self.radio = valorRadio

	# Método toString()
	def toString(self):
		return "La circunferencia tiene como centro: ", self.getX(),",",self.getY(), "y radio igual a:",self.radio