#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, Canvas

def crea_platos(event, fondo_casilla, pastel_capa1, pastel_capa2, pastel_capa3, pastel_capa_ordenada, pastel_cereza):
    """
    Funcion que recibe el clic del raton y las imagenes de los distintos pasteles a formar.
    Comprueba si el clic ha sido realizado en las zonas activas de la ventana.
    """
    #print(str(event.x) +","+ str(event.y))
    if ((422 <= event.x <= 522) and (212 <= event.y <= 312)) or \
            ((422 <= event.x <= 522) and (586 <= event.y <= 686)) or \
            ((660 <= event.x <= 760) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (382 <= event.y <= 482)) or \
            ((422 <= event.x <= 522) and (383 <= event.y <= 483)) or \
            ((535 <= event.x <= 635) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (586 <= event.y <= 686)) or \
            ((774 <= event.x <= 874) and (212 <= event.y <= 312)):
        #Si el usuario hace clic sobre alguna zona activa, creamos una ventana secundaria que abre esa casilla
        casilla(fondo_casilla, pastel_capa1, pastel_capa2, pastel_capa3, pastel_capa_ordenada, pastel_cereza)

def casilla(fondo_casilla, foto_pastel1,foto_pastel2 ,foto_pastel3 ,foto_pastel3_correcto,foto_pastel_cereza):
    """
    Funcion que recibe la foto de fondo de la zona activa y las fotos de los distintos pasteles a formar,
    creando así la zona activa en la que anteriormente se clicó
    """
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
    """
    Función que recibe el clic izquierdo del raton y las fotos de los distintos pasteles que pueden ser formados.
    Dependiendo de la zona de la zona activa donde se haya clicado se insertará un pastel distinto.
    Se creará un array de imagenes con las imagenes de los distintos pasteles.
    """
    #print(str(event.x) + "," + str(event.y))
    array_pasteles = ['Pasteles/1.png', 'Pasteles/5.png', 'Pasteles/7.png', 'Pasteles/8.png', 'Pasteles/9.png']
    #Zona para pasteles de 1 capa
    if ((0 <= event.x <= 250) and (0 <= event.y <= 166)):
        foto_pastel1.config(file=array_pasteles[0])
        pastel1 = Label(plato, image=foto_pastel1)
        pastel1.place(x=event.x, y=event.y)
    # Zona para pasteles de 2 capas
    elif ((251 <= event.x <= 500) and (0 <= event.y <= 166)):
        foto_pastel2.config(file=array_pasteles[1])
        pastel2 = Label(plato, image=foto_pastel2)
        pastel2.place(x=event.x, y=event.y)
    # Zona para pasteles de 3 capas
    elif ((0 <= event.x <= 250) and (167<= event.y <= 332)):
        foto_pastel3.config(file=array_pasteles[2])
        pastel3 = Label(plato, image=foto_pastel3)
        pastel3.place(x=event.x, y=event.y)
    # Zona para pasteles de 3 capas que siguen la receta
    elif ((251 <= event.x <= 500) and (167 <= event.y <= 332)):
        foto_pastel3_correcto.config(file=array_pasteles[3])
        pastel3_correcto = Label(plato, image=foto_pastel3_correcto)
        pastel3_correcto.place(x=event.x, y=event.y)
    # Zona para pasteles completos, con cereza
    elif ((0 <= event.x <= 500) and (332 <= event.y <= 500)):
        foto_pastel_cereza.config(file=array_pasteles[4])
        pastel_completo = Label(plato, image=foto_pastel_cereza)
        pastel_completo.place(x=event.x, y=event.y)

def cuenta_puntos_plato(contador):
    """
    Funcion que lleva el recuento de puntos de cada zona activa
    """
    pass

def inserta_lineas():
    canvas.create_line(472,0,472,66, width=5)
    canvas.create_line(422, 66, 522, 66, width=5)
    canvas.create_line(422, 32, 522, 32, width=5)
    #canvas.create_line(472, 10, 472, 76, width=5)

# Creamos la ventana principa
ventana = tk.Tk()
ventana.resizable(width=False, height=False)  # para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023")  # titulo de ventana, se muestra en la barra de herramientas
#ventana.geometry("1300x700+30+0")  # dimensiones de la ventana


# Creamos la componente Canvas
canvas=Canvas(ventana,width=1300,height=700)
canvas.pack()

#Mover la ventana 30 pixels a la derecha
ventana.geometry("+30+0")
#canvas.grid(row=0, column=0)

# Establecemos el tablero como fondo de la ventana principal
imgfondo = PhotoImage(file="tablero.png")

canvas.create_image(422,0, anchor=tk.NW, image=imgfondo)

inserta_lineas()

#fondo = Label(ventana, image=imgfondo)
#fondo.place(relwidth=1, relheight=1)

#Creamos photo image de los diferentes tipos de pasteles que contabilizan puntos
pastel_capa1 = PhotoImage()
pastel_capa2 = PhotoImage()
pastel_capa3 = PhotoImage()
pastel_capa_ordenada = PhotoImage()
pastel_cereza= PhotoImage()

# capturamos el clic izquierdo del raton y se lo pasamos a las casillas
#ventana.bind("<Button-1>", lambda event, imgfondo2 = PhotoImage(file="fondo3.png"),
#pastel_capa1=pastel_capa1, pastel_capa2=pastel_capa2, pastel_capa3=pastel_capa3, pastel_capa_ordenada=pastel_capa_ordenada,
#pastel_cereza=pastel_cereza: crea_platos(event, imgfondo2, pastel_capa1, pastel_capa2, pastel_capa3, pastel_capa_ordenada, pastel_cereza))


ventana.mainloop()
