"""
Nombre: Cilindro.py
Objetivo: es la subclase de tercer nivel en la jerarquia de herencia
Autor: 
Fecha: 14/11/2019
"""
from Circulo import Circulo

class Cilindro(Circulo):
	def __init__(self, valorX, valorY, vradio, valtura):
		# Creamos el atributo de cilindro
		self.altura = valtura
		# Construir objeto cilindro
		Circulo.__init__(self, vradio, valorX, valorY)
	
	# Lista de metodos get
	def getAltura(self):
		return self.altura

	# Metodod para calcular el volumen
	def getVolumen(self):
		return Circulo.getArea(self) * self.altura

	# Lista de metodos set
	def setAltura(self,valtura):
		self.altura = valtura

	# Método toString()
	def toString(self):
		return "El cilindro tiene como coordenadas: ", str(self.getX()),",",str(self.getY()), "y radio igual a:",str(self.getRadio()),"y altura:",str(self.getAltura()),"y el volumen es:",str(self.getVolumen())