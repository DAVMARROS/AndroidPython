"""
Nombre: MainCilindro.py
Objetivo: instanciar la clase Cilindro
Autor: 
Fecha: 14/11/2019
"""

from tkinter import *
from tkinter import messagebox
from Cilindro import Cilindro

# declaramos una ventana
w = Tk()
w.geometry('350x250')

lblx = Label(w, text="Valor de X")
lblx.grid(column=0, row=0, padx=(40, 30), pady=(10, 10))
txtx = Entry(w,width=10)
txtx.grid(column=1, row=0)

lbly = Label(w, text="Valor de y")
lbly.grid(column=0, row=2, padx=(40, 30), pady=(10, 10))
txty = Entry(w,width=10)
txty.grid(column=1, row=2)

lblrad = Label(w, text="Valor del radio")
lblrad.grid(column=0, row=3, padx=(40, 30), pady=(10, 10))
txtrad = Entry(w,width=10)
txtrad.grid(column=1, row=3)


lblalt = Label(w, text="Valor de la altura")
lblalt.grid(column=0, row=4, padx=(40, 30), pady=(10, 10))
txtalt = Entry(w,width=10)
txtalt.grid(column=1, row=4)

def crearObjeto():
	cir = Cilindro(txtx.get(),txty.get(),txtrad.get(),txtalt.get())
	messagebox.showinfo('Crear', 'Objeto creado correctamente')
btnCrear = Button(w, text="Crear", command=crearObjeto)
btnCrear.grid(column=0, row=5, padx=(20, 10), pady=(10, 10))

def imprimirVolumen():
	cir = Cilindro(float(txtx.get()),float(txty.get()),float(txtrad.get()),float(txtalt.get()))
	messagebox.showinfo('Resultado', cir.toString())
btnImprimir = Button(w, text="Imprimir", command=imprimirVolumen)
btnImprimir.grid(column=1, row=5, padx=(20, 20), pady=(10, 10))

def salir():
	w.destroy()
btnSalir = Button(w, text="Salir", command=salir)
btnSalir.grid(column=2, row=5, padx=(30, 10), pady=(10, 10))

w.mainloop()