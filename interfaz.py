#Importamos librerias a usar
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel,ttk

ventana=tk.Tk() #creamos la ventana principal
ventana.resizable(width=False, height=False) #para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023") #titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0") #dimensiones de la ventana
#ventana.config(width=1300, height=700)

#Establecemos la imagen como fondo
imgfondo = PhotoImage(file = "tablero.png")
fondo = Label(image = imgfondo)
fondo.place(x = 422, y = 0)

#Definimos funciones
def izq_verde1():
    izq_v1=tk.Toplevel(ventana)
    izq_v1.resizable(width=False, height=False)
    izq_v1.title("Casilla 1")
    izq_v1.geometry("500x500+422+100")
    # Establecemos la imagen como fondo
    imgfondo = PhotoImage(file="verde.png")
    fondo = Label(image=imgfondo)
    fondo.place(x=0, y=0)

    cerrar = ttk.Button(izq_v1, text="Cerrar", command=izq_v1.destroy)
    cerrar.place(x=202, y=460)
    izq_v1.focus() #para que cuando se pulsa el boton salga en primer lugar esta ventana
    izq_v1.grab_set() #para que no se pueda utilizar la ventana principal

#Definición de las imagenes de los botones
img_verde = tk.PhotoImage(file="plato_verde.png")
img_azul=tk.PhotoImage(file="plato_azul.png")

#Definicion botones verdes
boton_izq_v1=tk.Button(image=img_verde, height=97, width=98, command=izq_verde1)
boton_izq_v1.place(x=422, y=205)

boton_izq_v2=tk.Button(image=img_verde, height=96,width=98)
boton_izq_v2.place(x=422, y=580)

boton_izq_v3=tk.Button(image=img_verde, height=96,width=98)
boton_izq_v3.place(x=660, y=580)

boton_izq_v4=tk.Button(image=img_verde, height=96,width=98)
boton_izq_v4.place(x=774, y=375)

#Definicion botones azules
boton_izq_a1=tk.Button(image=img_azul, height=97,width=98)
boton_izq_a1.place(x=422, y=375)

boton_izq_a2=tk.Button(image=img_azul, height=96,width=98)
boton_izq_a2.place(x=536, y=580)

boton_izq_a3=tk.Button(image=img_azul, height=96,width=98)
boton_izq_a3.place(x=774, y=580)

boton_izq_a4=tk.Button(image=img_azul, height=96,width=98)
boton_izq_a4.place(x=774, y=205)


ventana.mainloop()