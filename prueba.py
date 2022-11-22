# importamos las librerias necesarias
import tkinter as tk
from functools import partial
from tkinter import messagebox, ttk

def saludar(ventana):
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")
    ventana.title("Nuevo título")

root = tk.Tk()   #creamos la ventana
root.config(width=300, height=200) #establece las dimensiones de la ventana
root.title("Botón en Tk") #titulo que se muestra en la barra de herramientas de la ventana

boton = ttk.Button(text="¡Hola, mundo!", command=partial(saludar,root))
boton.place(x=50, y=50)

root.mainloop()  #para abrir la ventana creada
