#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, ttk
import random

def crea_casillas(event, imgfondo, imagenes):
    """
    Procedimiento que registra los clics izquierdos del ratón sobre la pantalla
    dependiendo de la zona en la que el usuario clique se crearán unas ventanas secundarias o no.
    :param event: Event
    :param imgfondo: PhotoImage
    :return: None
    """
    # print(str(event.x) +","+ str(event.y))
    if ((422 <= event.x <= 522) and (212 <= event.y <= 312)) or \
            ((422 <= event.x <= 522) and (586 <= event.y <= 686)) or \
            ((660 <= event.x <= 760) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (382 <= event.y <= 482)) or \
            ((422 <= event.x <= 522) and (383 <= event.y <= 483)) or \
            ((535 <= event.x <= 635) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (212 <= event.y <= 312)):

        casilla(imgfondo, imagenes)


def casilla(imgfondo, imagenes):
    c = Toplevel(ventana)
    c.resizable(width=False, height=False)
    c.title("Casilla Verde")
    c.geometry("500x500+422+100")
    fondo = Label(c, image=imgfondo)
    fondo.place(relwidth=1, relheight=1)

    """
     Boton para cerrar la ventana
     cerrar = ttk.Button(verde, text="Cerrar", command=verde.destroy)
     cerrar.place(x=202, y=460)
     verde.focus()  # para que cuando se pulsa el boton salga en primer lugar esta ventana
     verde.grab_set()  # para que no se pueda utilizar la ventana principal
     """

    c.bind("<Button-1>",lambda event, imagenes=imagenes: cuenta_puntos(event,imagenes, c))


def cuenta_puntos(event, imagenes, c):
    print(str(event.x) + "," + str(event.y))
    if ((0 <= event.x <= 250) and (0 <= event.y <= 166)):
        img = PhotoImage(file=imagenes[0])
        f = Label(c, image=img)
        f.place(x=10, y=5)
    elif ((251 <= event.x <= 500) and (0 <= event.y <= 167)):
        print("Pasteles de 2 capas")
    elif ((0 <= event.x <= 250) and (167 <= event.y <= 332)):
        print("Pasteles de 3 capas")
    elif ((251 <= event.x <= 500) and (167 <= event.y <= 332)):
        print("Pastel de 3 capas correcto")
    elif ((0 <= event.x <= 500) and (333 <= event.y <= 500)):
        print("Pastel completo")

# Creamos la ventana principal
ventana = tk.Tk()
ventana.resizable(width=False, height=False)  # para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023")  # titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0")  # dimensiones de la ventana
# ventana.config(width=1300, height=700)

# Establecemos la imagen como fondo
imgfondo = PhotoImage(file="tablero.png")
fondo = Label(ventana, image=imgfondo)
fondo.place(relwidth=1, relheight=1)
#fondo.place(x = 422, y = 0)

#Establecemos la imagen de fondo de las casillas
imgfondo2 = PhotoImage(file="fondo2.png")

#Establecemos el array de imagenes
imagenes=['Imagenes/1.png','Imagenes/2.png','Imagenes/3.png', 'Imagenes/6.png']
num= random.randint(0,3)
imgcasilla = PhotoImage(file=imagenes[num])

# capturamos el click izquierdo del raton y se lo pasamos a las casillas
ventana.bind("<Button-1>", lambda event, imgfondo2 = PhotoImage(file="fondo2.png"), imagenes=imagenes: crea_casillas(event, imgfondo2, imagenes))
ventana.mainloop()
