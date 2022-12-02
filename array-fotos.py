import os
import random
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, ttk

#CON FUNCION
contenido = os.listdir('Imagenes')
print(contenido)

#A MANO
imagenes=['Imagenes/1.png','Imagenes/2.png','Imagenes/3.png']

#CREAMOS VENTANA
ventana = tk.Tk()
ventana.resizable(width=False, height=False)  # para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023")  # titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0")  # dimensiones de la ventana

num=random.randint(0,2)
imgfondo = PhotoImage(file=imagenes[num])
fondo = Label(ventana, image=imgfondo)
fondo.place(relwidth=1, relheight=1)

ventana.mainloop()