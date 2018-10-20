#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def boton_presionadoa():
	try:
		na = int(textoa.get())
		nb = int(textob.get())
	except ValueError:
		messagebox.showerror(message= "Solo se permite numeros." , title="Error")
	else:
		messagebox.showinfo(message= f"Respuesta:  {na + nb}" , title="Resultado")
		
def boton_presionadob():
	try:
		na = int(textoa.get())
		nb = int(textob.get())
		
	except ValueError:
		messagebox.showerror(message= "Solo se permite numeros." , title="Error")
	else:
		messagebox.showinfo(message= f"Respuesta:  {na - nb}" , title="Resultado")
	
def boton_presionadoc():
	try:
		na = int(textoa.get())
		nb = int(textob.get())
	except ValueError:
		messagebox.showerror(message= "Solo se permite numeros." , title="Error")
	else:
		messagebox.showinfo(message= f"Respuesta:  {na * nb}" , title="Resultado")
		
def boton_presionadod():
	try:
		na = int(textoa.get())
		nb = int(textob.get())
		messagebox.showinfo(message= f"Respuesta:  {int(na / nb)}" , title="Resultado")
	except ValueError:
		messagebox.showerror(message= "Solo se permite numeros." , title="Error")
	except ZeroDivisionError:
		messagebox.showerror(message= "No se puede Dividir por cero" , title="Error")
	
	
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(width=400, heigh=300)

textoa = tk.Entry()
textoa.place(x=70, y=60, width=100, height=25)

labela = tk.Label(text="A:")
labela.place(x=30, y=60)

textob = tk.Entry()
textob.place(x=250, y=60, width=100, height=25)

labelb = tk.Label(text="B:")
labelb.place(x=210, y=60)

botona =tk.Button(text="Suma", command=boton_presionadoa)
botona.place(x=70, y=90, width=100, heigh=30)

botonb =tk.Button(text="Resta", command=boton_presionadob)
botonb.place(x=250, y=90, width=100, heigh=30)

botonc =tk.Button(text="Multi", command=boton_presionadoc)
botonc.place(x=250, y=150, width=100, heigh=30)

botond =tk.Button(text="Div", command=boton_presionadod)
botond.place(x=70, y=150, width=100, heigh=30)


ventana.mainloop()
