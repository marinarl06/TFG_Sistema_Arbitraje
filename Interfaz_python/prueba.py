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
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # Creamos los radiobuttons para elegir arbitro y campo
    botones_arbitro_campo(canvas)

    # Crear botón para obtener el radiobutton seleccionado
    get_button = tk.Button(canvas, text="Obtener radiobutton seleccionado",
                           command= lambda: get_valores_boton(canvas, ruta, ancho_canvas, alto_canvas))
    canvas.create_window(200,300, window=get_button)

def botones_arbitro_campo(canvas):
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
    canvas.create_window(200, 100, window=arbitro1)
    canvas.create_window(200, 150, window=arbitro2)
    canvas.create_window(200, 200, window=campo1)
    canvas.create_window(200, 250, window=campo2)


def get_valores_boton(canvas, ruta, ancho_canvas, alto_canvas):
    """
    OBJ: Obtiene los valores que han sido seleccionados por el usuario en los radiobuttons y dependiendo de la selección
    modifica la variable ruta con un valor u otro y si es necesario cambia la rotacion de la imagen
    y finalmente llama a la función new_canvas para crear un nuevo canvas
    asociado a la ventana con la configuración establecida segun los radioibuttons seleccionados.
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

    new_canvas(canvas, ruta, ancho_canvas, alto_canvas)

def new_canvas(canvas_previo,ruta,ancho_canvas, alto_canvas):
    """
    OBJ: Crea un nuevo canvas con la configuración que se establezca y elimina el canvas anterior.
    Llama una funcion para configurar el fondo del canvas y que la imagen se ajuste a las dimensiones de dicho canvas
    Llama a la funcion para leer los datos del partido que va a disputarse
    PARAM: canvas, string, int, int -> None
    """
    # Cerramos el canvas anterior
    canvas_previo.destroy()
    # LLamada a la funcion para que nos redimensione la imagen con las dimensiones del canvas y nos devuelva las dimensiones
    ancho_original, alto_original, nuevo_ancho, nuevo_alto, imagen_fondo = configura_fondo(ruta, ancho_canvas, alto_canvas)

    # Creamos el nuevo canvas
    new_canvas = tk.Canvas(root, width=ancho_original, height=alto_original)
    new_canvas.pack()

    # Dibuja la imagen de fondo en el canvas
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    new_canvas.background = imagen_fondo_tk
    new_canvas.create_image(0, nuevo_alto, anchor="nw", image=imagen_fondo_tk)

    # Llamamos a la función que nos proporciona la info de las acciones de cada partido
    datos_csv(new_canvas, ancho_original, alto_original, nuevo_ancho, nuevo_alto)

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
            x1_redimension, y1_redimension = rotacion_pixel(x1_redimension, y1_redimension, nuevo_ancho / 2,
                                                          nuevo_alto, 180)
            x2_redimension, y2_redimension = rotacion_pixel(x2_redimension, y2_redimension, nuevo_ancho / 2,
                                                          nuevo_alto, 180)

            new_canvas.create_rectangle(x1_redimension + 30, y1_redimension + 40 ,
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

def rotacion_pixel(x, y, cx, cy, angulo):
    """
    OBJ: Rota un pixel (x, y) alrededor del centro (cx, cy) por el ángulo dado
    PARAM: int, int, int, int, int --> int, int
    """
    radians = angulo * math.pi / 180.0
    cos = math.cos(radians)
    sin = math.sin(radians)
    nuevo_x = cos * (x - cx) + sin * (y - cy) + cx
    nuevo_y = -sin * (x - cx) + cos * (y - cy) + cy
    return nuevo_x, nuevo_y

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

