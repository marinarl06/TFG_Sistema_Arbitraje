#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, ttk
import random

def crea_casillas(event, fondo_casilla, pastel):
    # print(str(event.x) +","+ str(event.y))
    if ((422 <= event.x <= 522) and (212 <= event.y <= 312)) or \
            ((422 <= event.x <= 522) and (586 <= event.y <= 686)) or \
            ((660 <= event.x <= 760) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (382 <= event.y <= 482)) or \
            ((422 <= event.x <= 522) and (383 <= event.y <= 483)) or \
            ((535 <= event.x <= 635) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (212 <= event.y <= 312)):
        #Si el usuario hace clic sobre alguna zona activa, creamos una ventana secundaria que abre esa casilla
        casilla(fondo_casilla, pastel)

def casilla(fondo_casilla, pastel):
    plato = Toplevel(ventana)
    plato.resizable(width=False, height=False)
    plato.title("Casilla Verde")
    plato.geometry("700x700+350+0")
    fondo = Label(plato, image=fondo_casilla)
    fondo.place(relwidth=1, relheight=1)
    #Registramos los clics que haga el usuario en la casilla para poder hacer el recuento correctamente
    plato.bind("<Button-1>", lambda event, pastel=pastel: cuenta_puntos(event, pastel, plato))


def cuenta_puntos(event, pastel, plato):
    #print(str(event.x) + "," + str(event.y))
    array_pasteles = ['Pasteles/1.png', 'Pasteles/2.png', 'Pasteles/3.png', 'Pasteles/4.png', 'Pasteles/5.png', 'Pasteles/6.png', 'Pasteles/7.png', 'Pasteles/8.png']
    if ((0 <= event.x <= 350) and (0 <= event.y <= 233)):
        n=random.randint(0,2)
        pastel.config(file=array_pasteles[n])
        p1 = Label(plato, image=pastel)
        p1.place(x=event.x, y=event.y)
    elif ((351 <= event.x <= 700) and (0 <= event.y <= 233)):
        n = random.randint(3, 5)
        pastel.config(file=array_pasteles[n])
        p2 = Label(plato, image=pastel)
        p2.place(x=event.x, y=event.y)
    elif ((0 <= event.x <= 350) and (234<= event.y <= 466)):
        print("Pasteles de 3 capas")
    elif ((351 <= event.x <= 700) and (234 <= event.y <= 466)):
        print("Pastel de 3 capas correcto")
    elif ((0 <= event.x <= 700) and (466 <= event.y <= 700)):
        print("Pastel completo")

# Creamos la ventana principal
ventana = tk.Tk()
ventana.resizable(width=False, height=False)  # para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023")  # titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0")  # dimensiones de la ventana

# Establecemos el tablero como fondo de la ventana principal
imgfondo = PhotoImage(file="tablero.png")
fondo = Label(ventana, image=imgfondo)
fondo.place(relwidth=1, relheight=1)
#fondo.place(x = 422, y = 0)

#Establecemos un array con imagenes de los diferentes pasteles
pastel_casilla = PhotoImage()

# capturamos el clic izquierdo del raton y se lo pasamos a las casillas
ventana.bind("<Button-1>", lambda event, imgfondo2 = PhotoImage(file="fondo3.png"), pastel=pastel_casilla: crea_casillas(event, imgfondo2, pastel))
ventana.mainloop()
