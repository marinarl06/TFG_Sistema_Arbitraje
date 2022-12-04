#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, ttk

def crea_platos(event, fondo_casilla, pastel1,pastel2, pastel3, pastel4, pastel5):
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
        casilla(fondo_casilla, pastel1, pastel2, pastel3, pastel4, pastel5)

def casilla(fondo_casilla, foto_pastel1,foto_pastel2 ,foto_pastel3 ,foto_pastel3_correcto,foto_pastel_cereza):
    plato = Toplevel(ventana)
    plato.resizable(width=False, height=False)
    plato.title("Casilla Verde")
    plato.geometry("500x500+430+22")
    fondo = Label(plato, image=fondo_casilla)
    fondo.place(relwidth=1, relheight=1)
    #Registramos los clics que haga el usuario en la casilla para poder hacer el recuento correctamente
    plato.bind("<Button-1>", lambda event,foto_pastel1=foto_pastel1, foto_pastel2=foto_pastel2,
    foto_pastel3=foto_pastel3, foto_pastel3_correcto=foto_pastel3_correcto,
    foto_pastel_cereza=foto_pastel_cereza:
    inserta_pasteles(event, foto_pastel1,foto_pastel2 ,foto_pastel3 ,foto_pastel3_correcto,foto_pastel_cereza, plato))

def inserta_pasteles(event, foto_pastel1,foto_pastel2 ,foto_pastel3 ,foto_pastel3_correcto,foto_pastel_cereza, plato):
    #print(str(event.x) + "," + str(event.y))
    array_pasteles = ['Pasteles/1.png', 'Pasteles/5.png', 'Pasteles/7.png', 'Pasteles/8.png', 'Pasteles/9.png']
    if ((0 <= event.x <= 250) and (0 <= event.y <= 166)):
        foto_pastel1.config(file=array_pasteles[0])
        pastel1 = Label(plato, image=foto_pastel1)
        pastel1.place(x=event.x, y=event.y)

    elif ((251 <= event.x <= 500) and (0 <= event.y <= 166)):
        foto_pastel2.config(file=array_pasteles[1])
        pastel2 = Label(plato, image=foto_pastel2)
        pastel2.place(x=event.x, y=event.y)
    elif ((0 <= event.x <= 250) and (167<= event.y <= 332)):
        foto_pastel3.config(file=array_pasteles[2])
        pastel3 = Label(plato, image=foto_pastel3)
        pastel3.place(x=event.x, y=event.y)
    elif ((251 <= event.x <= 500) and (167 <= event.y <= 332)):
        foto_pastel3_correcto.config(file=array_pasteles[3])
        pastel3_correcto = Label(plato, image=foto_pastel3_correcto)
        pastel3_correcto.place(x=event.x, y=event.y)
    elif ((0 <= event.x <= 500) and (332 <= event.y <= 500)):
        foto_pastel_cereza.config(file=array_pasteles[4])
        pastel_completo = Label(plato, image=foto_pastel_cereza)
        pastel_completo.place(x=event.x, y=event.y)

def cuenta_puntos_plato(contador):
    pass


# Creamos la ventana principal
ventana = tk.Tk()
ventana.resizable(width=False, height=False)  # para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023")  # titulo de ventana, se muestra en la barra de herramientas
ventana.geometry("1300x700+30+0")  # dimensiones de la ventana

# Establecemos el tablero como fondo de la ventana principal
imgfondo = PhotoImage(file="tablero.png")
fondo = Label(ventana, image=imgfondo)
fondo.place(relwidth=1, relheight=1)

#Creamos photo image de los diferentes tipos de pasteles que contabilizan puntos
pastel_capa1 = PhotoImage()
pastel_capa2 = PhotoImage()
pastel_capa3 = PhotoImage()
pastel_capa_ordenada = PhotoImage()
pastel_cereza= PhotoImage()

# capturamos el clic izquierdo del raton y se lo pasamos a las casillas
ventana.bind("<Button-1>", lambda event, imgfondo2 = PhotoImage(file="fondo3.png"),
pastel1=pastel_capa1, pastel2=pastel_capa2, pastel3=pastel_capa3, pastel4=pastel_capa_ordenada,
pastel5=pastel_cereza: crea_platos(event, imgfondo2, pastel1, pastel2, pastel3, pastel4, pastel5))

ventana.mainloop()
