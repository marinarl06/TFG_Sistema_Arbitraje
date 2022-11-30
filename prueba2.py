import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, ttk

def casillas(event):
    #print(str(event.x) +","+ str(event.y))
    if ((422 <= event.x <= 522) and (212 <= event.y <= 312)) or \
        ((422 <= event.x <= 522) and (586 <= event.y <= 686)) or \
        ((660 <= event.x <= 760) and (586 <= event.y <= 686)) or \
        ((774 <= event.x <= 874) and (382 <= event.y <= 482)) :
        verde = Toplevel(ventana)
        verde.resizable(width=False, height=False)
        verde.title("Casilla Verde")
        verde.geometry("500x500+422+100")
        """"
        # Boton para cerrar la ventana
        cerrar = ttk.Button(verde, text="Cerrar", command=verde.destroy)
        cerrar.place(x=202, y=460)
        verde.focus()  # para que cuando se pulsa el boton salga en primer lugar esta ventana
        verde.grab_set()  # para que no se pueda utilizar la ventana principal
        """
        verde.bind("<Button-1>", cuenta_puntos)

    elif ((422 <= event.x <= 522) and (383 <= event.y <= 483)) or \
         ((535 <= event.x <= 635) and (586 <= event.y <= 686))  or \
         ((774 <= event.x <= 874) and (586 <= event.y <= 686)) or \
         ((774 <= event.x <= 874) and (212 <= event.y <= 312)):
        azul = Toplevel(ventana)
        azul.resizable(width=False, height=False)
        azul.title("Casilla Azul")
        azul.geometry("500x500+422+100")

        """"
        # Boton para cerrar la ventana
        cerrar = ttk.Button(verde, text="Cerrar", command=verde.destroy)
        cerrar.place(x=202, y=460)
        azul.focus()  # para que cuando se pulsa el boton salga en primer lugar esta ventana
        azul.grab_set()  # para que no se pueda utilizar la ventana principal
        """
        azul.bind("<Button-1>", cuenta_puntos)

def cuenta_puntos(event):
    print(str(event.x) +","+ str(event.y))
    if ((0 <= event.x <= 250) and (0 <= event.y <= 166)):
        print("Pasteles de 1 capa")
    elif ((251 <= event.x <= 500) and (0 <= event.y <= 167)):
        print("Pasteles de 2 capas")
    elif ((0 <= event.x <= 250) and (167 <= event.y <= 332)):
        print("Pasteles de 3 capas")
    elif((251 <= event.x <= 500) and (167 <= event.y <= 332)):
        print("Pastel de 3 capas correcto")
    elif ((0 <= event.x <= 500) and (333 <= event.y <= 500)):
        print("Pastel completo")

#Creamos la ventana principal
ventana=tk.Tk()
ventana.resizable(width=False, height=False) #para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023") #titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0") #dimensiones de la ventana
#ventana.config(width=1300, height=700)

#Establecemos la imagen como fondo
imgfondo = PhotoImage(file = "tablero.png")
fondo = Label(ventana, image = imgfondo)
fondo.place(relwidth=1, relheight=1)
#fondo.place(x = 422, y = 0)

ventana.bind("<Button-1>",casillas) #capturamos el click izquierdo del raton

ventana.mainloop()
