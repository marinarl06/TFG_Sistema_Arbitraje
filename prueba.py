import tkinter as tk
from PIL import Image, ImageTk
import csv
import math

def create_canvas(root,ruta):
    """
    OBJ: Crea el canvas inicial asociado a la ventana (root) con un boton que llama a una función para que cree
    unos radiobutton y nos devuelva los valores seleccionados
    tk,string --> None
    """
    global arbitro, campo
    # Obtiene el tamaño del canvas
    alto_canvas = root.winfo_screenheight()
    ancho_canvas = root.winfo_screenwidth()

    # Crea el canvas
    canvas = tk.Canvas(root, width=ancho_canvas, height=alto_canvas)
    canvas.pack()

    # Creamos los radiobuttons para elegir arbitro y campo
    botones_arbitro_campo(canvas,ancho_canvas)

    # Crear botón para obtener el radiobutton seleccionado
    get_button = tk.Button(canvas, text="Obtener radiobutton seleccionado",
                           command= lambda: get_valores_boton(canvas, ruta, ancho_canvas, alto_canvas))
    canvas.create_window(ancho_canvas/2,250, window=get_button)


def botones_arbitro_campo(canvas,ancho_canvas):
    """
    OBJ: Crea 4 (2 para seleccionar el arbitro y 2 para seleccionar el campo) radiobuttons y los ubica en el canvas principal
    PARAM: canvas -> None
    """
    global arbitro, campo
    # crear Radiobuttons en el canvas
    arbitro1 = tk.Radiobutton(canvas, text="Arbitro 1", variable=arbitro, value="arbitro1")
    arbitro2 = tk.Radiobutton(canvas, text="Arbitro 2", variable=arbitro, value="arbitro2")
    campo1 = tk.Radiobutton(canvas, text="Campo A", variable=campo, value="campoA")
    campo2 = tk.Radiobutton(canvas, text="Campo B", variable=campo, value="campoB")

    # posicionar los Radiobuttons en el canvas
    canvas.create_window(ancho_canvas/2, 50, window=arbitro1)
    canvas.create_window(ancho_canvas/2, 100, window=arbitro2)
    canvas.create_window(ancho_canvas/2, 150, window=campo1)
    canvas.create_window(ancho_canvas/2, 200, window=campo2)


def get_valores_boton(canvas, ruta, ancho_canvas, alto_canvas):
    """
    OBJ: Obtiene los valores que han sido seleccionados por el usuario en los radiobuttons y dependiendo de la selección
    modifica la variable ruta con un valor u otro y si es necesario cambia la rotacion de la imagen.
    Finalmente llama a la función configura_canvas para configura el fondo del canvas con los valores obtenidos segun los radioibuttons seleccionados.
    PARAM: canvas, string, int, int -> None
    """
    global arbitro, campo, rotacion, archivo
    # Obtenemos el valor del radiobutton seleccionado
    if (arbitro.get()=="arbitro1"):
        ruta="arbitro_izq.png"
        archivo='acciones_izq.csv'
    elif (arbitro.get()=="arbitro2"):
        ruta="arbitro_drch.png"
        rotacion=180
        archivo = 'acciones_drch.csv'

    configura_canvas(canvas, ruta, ancho_canvas, alto_canvas)

def configura_canvas(canvas,ruta,ancho_canvas, alto_canvas):
    """
    OBJ: Configura el canvas con la configuración que se establezc.
    Llama una funcion para configurar el fondo del canvas y que la imagen se ajuste a las dimensiones de dicho canvas
    Llama a la funcion para leer los datos del partido que va a disputarse
    PARAM: canvas, string, int, int -> None
    """
    # LLamada a la funcion para que nos redimensione la imagen con las dimensiones del canvas y nos devuelva las dimensiones
    ancho_original, alto_original, nuevo_ancho, nuevo_alto, imagen_fondo = configura_fondo(ruta, ancho_canvas, alto_canvas)

    # Dibuja la imagen de fondo en el canvas
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    canvas.background = imagen_fondo_tk
    canvas.create_image(0, nuevo_alto, anchor="nw", image=imagen_fondo_tk)

    # Llamamos a la función que nos proporciona la info de las acciones de cada partido
    datos_csv(canvas,ancho_original,alto_original,nuevo_ancho,nuevo_alto)

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

def datos_csv(new_canvas, ancho_original, alto_original, nuevo_ancho, nuevo_alto):
    """
    OBJ: Lee los datos de un archivo CSV que se quiera y llama a una funcion que pinta en el canvas toda la informacion
    que extraemos del canvas necesaria.
    PARAM: canvas, int, int,int,int --> None
    """
    global listaAcciones, archivo
    with open(archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        encabezados = next(lector_csv)
        for fila in lector_csv:
            listaAcciones.append(fila)
    inserta_cuadros(new_canvas, listaAcciones, ancho_original, alto_original, nuevo_ancho, nuevo_alto)

def inserta_cuadros(new_canvas, acciones, ancho_original, alto_original, nuevo_ancho, nuevo_alto):
    """
    OBJ: Pintar en el canvas las zonas activas
    PARAM: canvas, array, int, int, int, int --> None
    """
    global rotacion
    for i in range(len(acciones)):
        x1_redimension = (int(acciones[i][7])) * (nuevo_ancho / ancho_original)
        y1_redimension = (int(acciones[i][8])) * (nuevo_alto / alto_original)
        x2_redimension = (int(acciones[i][7]) + int(acciones[i][9])) * (nuevo_ancho / ancho_original)
        y2_redimension = (int(acciones[i][8]) + int(acciones[i][10])) * (nuevo_alto / alto_original)

        if rotacion == 180:
            x1_redimension = nuevo_ancho - x1_redimension
            y1_redimension = (nuevo_alto - y1_redimension) + nuevo_alto
            x2_redimension = nuevo_ancho - x2_redimension
            y2_redimension = (nuevo_alto - y2_redimension) + nuevo_alto

            new_canvas.create_rectangle(x1_redimension + 30, y1_redimension +40 ,
                                    x2_redimension + 30, y2_redimension + 40, width=5)

            if (i >= 25):
                if ('_cesta' in acciones[i][6] or 'estimacion' in acciones[i][6]):
                    new_canvas.create_text(x1_redimension + 120, y1_redimension + 20, text=acciones[i][6], font=("Arial", 20))
                else:
                    new_canvas.create_text(x1_redimension - 50, y1_redimension - 20, text=acciones[i][6], font=("Arial", 20))

        else:
            new_canvas.create_rectangle(x1_redimension, y1_redimension - 40,
                                        x2_redimension, y2_redimension - 40, width=5)

            if (i >= 25):
                if ('_cesta' in acciones[i][6] or 'estimacion' in acciones[i][6]):
                    new_canvas.create_text(x1_redimension - 120, y1_redimension - 20, text=acciones[i][6], font=("Arial", 20))
                else:
                    new_canvas.create_text(x1_redimension + 50, y1_redimension - 60, text=acciones[i][6], font=("Arial", 20))


# Crear ventana principal
root = tk.Tk()

# Inicialización de variables
listaAcciones=[]
ruta_imagen="" #ruta de la imagen que quiero poner de fondo
rotacion=0 #segun el lado en el que arbitre sera necesario rotar la imagen o no
archivo=''
# Variables para crear los radiobutton
arbitro = tk.StringVar(value="EleccionArbitro")
campo = tk.StringVar(value="EleccionCampo")

# Llamada función para crear el canvas con imagen de fondo
create_canvas(root,ruta_imagen)

# Iniciar el bucle principal de la aplicación
root.mainloop()

