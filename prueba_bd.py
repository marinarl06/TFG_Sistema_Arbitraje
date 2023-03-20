import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk #es necesario instalarlo
import mariadb
import sys
import base_datos

import screeninfo #es necesario instalarlo



#print(f"Tamaño de la pantalla: {width} x {height}")

def create_canvas(root,ruta):
    """
    OBJ: Crea el canvas inicial asociado a la ventana (root) con un boton que llama a una función para que cree
    unos radiobutton y nos devuelva los valores seleccionados
    tk,string --> None
    """
    global arbitro, campo
    # Obtiene el tamaño del canvas

    screen = screeninfo.get_monitors()[0]
    ancho_canvas = screen.width
    alto_canvas = screen.height

    """alto_canvas = root.winfo_screenheight()
    ancho_canvas = root.winfo_screenwidth()"""

    # Crea el canvas
    canvas = tk.Canvas(root, width=ancho_canvas, height=alto_canvas)
    canvas.pack()

    #Creamos los botones para introducir las credenciales de la base de datos
    credenciales_bbdd()

    # Creamos los radiobuttons para elegir arbitro y campo
    botones_arbitro_campo(canvas, ancho_canvas)

    # Crear botón para obtener el radiobutton seleccionado
    get_button = tk.Button(canvas, text="Obtener valores",
                           command= lambda: get_valores_boton(canvas, ruta, ancho_canvas, alto_canvas))
    canvas.create_window(ancho_canvas/2 + 150 ,100, window=get_button)

def credenciales_bbdd():
    global user, password, database
    texto1 = tk.Label(root, text="Introduce usuario base de datos").place(x=50, y=50)
    entry1 = ttk.Entry(textvariable=user, width=15)
    entry1.place(x=300, y=50)

    texto2 = tk.Label(root, text="Introduce contraseña base de datos").place(x=50, y=100)
    entry2 = ttk.Entry(textvariable=password, show="*", width=15)
    entry2.place(x=300, y=100)

    texto3 = tk.Label(root, text="Introduce nombre base de datos").place(x=50, y=150)
    entry3 = ttk.Entry(textvariable=database, width=15)
    entry3.place(x=300, y=150)


    #conectar_bbdd(entry1.get(), entry2.get(), entry3.get())

def botones_arbitro_campo(canvas,ancho_canvas):
    """
    OBJ: Crea 4 (2 para seleccionar el arbitro y 2 para seleccionar el campo) radiobuttons y
    los ubica en el canvas principal
    PARAM: canvas -> None
    """
    global arbitro, campo
    # crear Radiobuttons en el canvas
    arbitro1 = tk.Radiobutton(canvas, text="Arbitro 1", variable=arbitro, value=1)
    arbitro2 = tk.Radiobutton(canvas, text="Arbitro 2", variable=arbitro, value=2)
    campo1 = tk.Radiobutton(canvas, text="Campo A", variable=campo, value="A")
    campo2 = tk.Radiobutton(canvas, text="Campo B", variable=campo, value="B")

    # posicionar los Radiobuttons en el canvas
    canvas.create_window(ancho_canvas / 2, 50, window=arbitro1)
    canvas.create_window(ancho_canvas / 2+100, 50, window=arbitro2)
    canvas.create_window(ancho_canvas / 2+200, 50, window=campo1)
    canvas.create_window(ancho_canvas / 2+300, 50, window=campo2)

def get_valores_boton(canvas, ruta, ancho_canvas, alto_canvas):
    """
    OBJ: Obtiene los valores que han sido seleccionados por el usuario en los radiobuttons y dependiendo de la selección
    modifica la variable ruta con un valor u otro y si es necesario cambia la rotacion de la imagen.
    Finalmente llama a la función configura_canvas para configura el fondo del canvas con los valores obtenidos segun los radioibuttons seleccionados.
    PARAM: canvas, string, int, int -> None
    """
    global arbitro, campo, rotacion
    # Obtenemos el valor del radiobutton seleccionado
    if(arbitro.get()==1):
        ruta="arbitro_izq.png"
    elif (arbitro.get()==2) :
        rotacion = 180
        ruta="arbitro_drch.png"

    configura_canvas(canvas, ruta, ancho_canvas, alto_canvas)

def configura_canvas(canvas,ruta,ancho_canvas, alto_canvas):
    """
    OBJ: Configura el canvas con la configuración que se establezc.
    Llama una funcion para configurar el fondo del canvas y que la imagen se ajuste a las dimensiones de dicho canvas
    Llama a la funcion para leer los datos del partido que va a disputarse
    PARAM: canvas, string, int, int -> None
    """
    global listaAcciones
    # LLamada a la funcion para que nos redimensione la imagen con las dimensiones del canvas y nos devuelva las dimensiones
    ancho_original, alto_original, nuevo_ancho, nuevo_alto, imagen_fondo = configura_fondo(ruta, ancho_canvas, alto_canvas)

    # Dibuja la imagen de fondo en el canvas
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    canvas.background = imagen_fondo_tk
    canvas.create_image(0, nuevo_alto, anchor="nw", image=imagen_fondo_tk)

    # Llamamos a la función que nos proporciona la info de las acciones de cada partido
    listaAcciones=base_datos.vista_arbitro(cursor, campo.get(), arbitro.get())
    inserta_cuadros(canvas, listaAcciones, ancho_original, alto_original, nuevo_ancho, nuevo_alto)

def configura_fondo(ruta, ancho_canvas, alto_canvas):
    """
    OBJ: Configura la imagen que quiero poner como fondo del canvas para que esta se ajuste al canvas correctamente
    y nos devuelve las dimensiones originales de la imagen, las nuevas dimensiones de la imagen, y la imagen.
    PARAM: string, int, int -> int, int, int, int, Image
    """
    # Carga la imagen de fondo
    imagen_fondo_original = Image.open(ruta)

    # Obtenemos el ancho y el alto de la imagen para usarlo posteriormente
    ancho_original = imagen_fondo_original.width
    alto_original = imagen_fondo_original.height

    # Encuentra la relación de aspecto de la imagen y del canvas
    relacion_aspecto_imagen = imagen_fondo_original.width / imagen_fondo_original.height
    relacion_aspecto_canvas = ancho_canvas / alto_canvas

    # Escala la imagen según la relación de aspecto más pequeña
    if relacion_aspecto_imagen > relacion_aspecto_canvas:
        # La imagen es más ancha que el canvas, escala la imagen al ancho del canvas y ajusta la altura
        nuevo_ancho = ancho_canvas
        nuevo_alto = int(nuevo_ancho / relacion_aspecto_imagen)
    else:
        # La imagen es más alta que el canvas, escala la imagen a la altura del canvas y ajusta el ancho
        nuevo_alto = alto_canvas
        nuevo_ancho = int(nuevo_alto * relacion_aspecto_imagen)

    imagen_fondo = imagen_fondo_original.resize((nuevo_ancho, nuevo_alto))

    return ancho_original, alto_original, nuevo_ancho, nuevo_alto, imagen_fondo


def inserta_cuadros(canvas, acciones, ancho_original, alto_original, nuevo_ancho, nuevo_alto):
    """
    OBJ: Pintar en el canvas las zonas activas
    PARAM: canvas, array, int, int, int, int --> None
    """
    global rotacion, entry
    for i in range(len(acciones)):
        x1_redimension = (int(acciones[i]['x_ini'])) * (nuevo_ancho / ancho_original)
        y1_redimension = (int(acciones[i]['y_ini'])) * (nuevo_alto / alto_original)
        x2_redimension = (int(acciones[i]['x_ini']) + int(acciones[i]['x_tam'])) * (nuevo_ancho / ancho_original)
        y2_redimension = (int(acciones[i]['y_ini']) + int(acciones[i]['y_tam'])) * (nuevo_alto / alto_original)

        if rotacion == 180:
            x1_redimension = nuevo_ancho - x1_redimension
            y1_redimension = (nuevo_alto - y1_redimension) + nuevo_alto
            x2_redimension = nuevo_ancho - x2_redimension
            y2_redimension = (nuevo_alto - y2_redimension) + nuevo_alto

            if (i >= 25):
                if (acciones[i]['tipo_accion'] == 2):
                    canvas.create_text(x1_redimension + 20, y1_redimension + 10, text=acciones[i]['nombre'],
                                       font=("Arial", 15))
                    crea_campo_texto(acciones[i]['accion'], acciones[i]['partido'],
                                     x1_redimension + 100, y1_redimension)

                elif (acciones[i]['tipo_accion'] == 3):
                    # Creamos el boton de seleccion
                    checkbox_value = tk.IntVar()
                    checkbox = tk.Checkbutton(canvas, text=acciones[i]['nombre'], variable=checkbox_value,
                                              command=lambda value=checkbox_value, nombre=acciones[i]['accion']:
                                              checkbox_clicked(value, nombre))
                    # Lo posicionamos en la venta
                    checkbox.place(x=x1_redimension, y=y1_redimension)
            else:
                canvas.create_rectangle(x1_redimension + 30, y1_redimension + 40,
                                        x2_redimension + 30, y2_redimension + 40, width=5)

        else:
            if (i >= 25):
                if (acciones[i]['tipo_accion']==2):
                    canvas.create_text(x1_redimension - 130, y1_redimension + 10, text=acciones[i]['nombre'],
                                       font=("Arial", 15))
                    #Llamamos a la función para que nos cree los campos de texto necesarios
                    crea_campo_texto(acciones[i]['accion'], acciones[i]['partido'],
                                     x1_redimension - 30, y1_redimension)

                elif (acciones[i]['tipo_accion']==3):
                    # Creamos el boton de seleccion
                    checkbox_value = tk.IntVar()
                    checkbox = tk.Checkbutton(canvas, text=acciones[i]['nombre'], variable=checkbox_value,
                                             command= lambda value = checkbox_value, accion=acciones[i]['accion'],
                                            partido=acciones[i]['partido']:
                                            checkbox_clicked(value, partido, accion))
                    # Lo posicionamos en la ventana
                    checkbox.place(x=x1_redimension, y=y1_redimension)
            else:
                canvas.create_rectangle(x1_redimension, y1_redimension - 38,
                                        x2_redimension, y2_redimension - 38, width=5)



def actualiza_puntos(event):
    print("hola")

def checkbox_clicked(checkbox_value, partido, accion):
    print(accion, partido, checkbox_value.get())
    base_datos.actualizar_accion(cursor, partido, accion, checkbox_value.get())
    connection.commit()
    return checkbox_value.get()

def crea_campo_texto(accion, partido, x,y):
    nuevo_entry = tk.IntVar()
    entry=ttk.Entry(textvariable=nuevo_entry, width=5)
    entry.place(x=x, y=y)
    entry.bind("<Return>", lambda event, partido=partido, accion=accion, nuevo_entry=nuevo_entry:
    get_valor_campo_texto(event, partido, accion, nuevo_entry))

def get_valor_campo_texto(event, partido, accion, entry):
    value = entry.get()
    base_datos.actualizar_accion(cursor, partido, accion, value)
    print("El valor introducido es:", partido, accion, value)
    #connection.commit()

#-------------------------------------------------CONEXION BASE DE DATOS ----------------------------------------------#
def conectar_bbdd(user, password, database):
    global cursor, connection
    """user = "root"
    password = ""
    host = "localhost"
    database = "eurobots_2023"""
    host = "localhost"
    try:
        connection = mariadb.connect(
        user=user, password=password, host=host, port=3306, database=database)
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform: %s" % e)
        sys.exit(1)
    else:
        print("Base de datos: ", database, "-", host)

    cursor = connection.cursor(dictionary=True)

#---------------------------------------------------- VENTANA PRINCIPAL -----------------------------------------------#

# Crear ventana principal
root = tk.Tk()

# Inicialización de variables
listaAcciones = []
ruta_imagen = None #ruta de la imagen que quiero poner de fondo
rotacion = 0 #segun el lado en el que arbitre sera necesario rotar la imagen o no
cursor=None #cursor de la base de datos
conecction=None #conexion base de datos

# Variables para crear los radiobutton
arbitro = tk.IntVar(value=0)
campo = tk.StringVar(value="E")

user=tk.StringVar(value="")
password=tk.StringVar(value="")
database=tk.StringVar(value="")

# Llamada función para crear el canvas con imagen de fondo
create_canvas(root,ruta_imagen)

# Iniciar el bucle principal de la aplicación
root.mainloop()

