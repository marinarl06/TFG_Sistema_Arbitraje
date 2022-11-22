import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel,ttk

def casillas(event):
    print(str(event.x) +","+ str(event.y))
    if ((event.x >= 422 and event.x <= 522) and (event.y >= 212 and event.y <= 312)) or \
        ((event.x >= 422 and event.x <= 522) and (event.y >= 586 and event.y <= 686)) or \
        ((event.x >= 660 and event.x <= 760) and (event.y >= 586 and event.y <= 686)) or \
        ((event.x >= 774 and event.x <= 874) and (event.y >= 382 and event.y <= 482)) :
        izq_v1 = tk.Toplevel(ventana)
        izq_v1.resizable(width=False, height=False)
        izq_v1.title("Casilla Verde")
        izq_v1.geometry("500x500+422+100")
        #Boton para cerrar la ventana
        cerrar = ttk.Button(izq_v1, text="Cerrar", command=izq_v1.destroy)
        cerrar.place(x=202, y=460)
        izq_v1.focus()  # para que cuando se pulsa el boton salga en primer lugar esta ventana
        izq_v1.grab_set()  # para que no se pueda utilizar la ventana principal

    elif ((event.x >= 422 and event.x <= 522) and (event.y >= 383 and event.y <= 483)) or \
         ((event.x >= 535 and event.x <= 635) and (event.y >= 586 and event.y <= 686))  or \
         ((event.x >= 774 and event.x <= 874) and (event.y >= 586 and event.y <= 686)) or \
         ((event.x >= 774 and event.x <= 874) and (event.y >= 212 and event.y <= 312)):
        izq_a1 = tk.Toplevel(ventana)
        izq_a1.resizable(width=False, height=False)
        izq_a1.title("Casilla Azul")
        izq_a1.geometry("500x500+422+100")
        # Boton para cerrar la ventana
        cerrar = ttk.Button(izq_a1, text="Cerrar", command=izq_a1.destroy)
        cerrar.place(x=202, y=460)
        izq_a1.focus()  # para que cuando se pulsa el boton salga en primer lugar esta ventana
        izq_a1.grab_set()  # para que no se pueda utilizar la ventana principal

ventana=tk.Tk() #creamos la ventana principal
ventana.resizable(width=False, height=False) #para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023") #titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0") #dimensiones de la ventana
#ventana.config(width=1300, height=700)

#Establecemos la imagen como fondo
imgfondo = PhotoImage(file = "tablero.png")
fondo = Label(ventana, image = imgfondo)
fondo.place(relwidth=1, relheight=1)
#fondo.place(x = 422, y = 0)

ventana.bind("<Button-1>", casillas) #capturamos el click izquierdo del raton

ventana.mainloop()
