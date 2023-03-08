import tkinter as tk
from PIL import Image, ImageTk
import csv

"""def create_canvas(root,ruta):
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    img = tk.PhotoImage(file=ruta)
    canvas.background = img
    canvas.create_image(0, 0, anchor=tk.NW, image=img)"""


def create_canvas(root,ruta):
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
    global arbitro, campo
    # Obtenemos el valor del radiobutton seleccionado
    if (arbitro.get()=="arbitro1"):
        ruta="arbitro_izq.png"
    elif (arbitro.get()=="arbitro2"):
        ruta="arbitro_drch.png"

    new_canvas(canvas, ruta, ancho_canvas, alto_canvas)
    """"# Dibuja la imagen de fondo en el canvas
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    canvas.background=imagen_fondo_tk
    canvas.create_image(0, alto_canvas//2 - 68, anchor="nw", image=imagen_fondo_tk)

    datos_csv(canvas, ancho_canvas, alto_canvas, nuevo_ancho, nuevo_alto)"""

def new_canvas(canvas_previo,ruta,ancho_canvas, alto_canvas):
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
    new_canvas.create_image(0, alto_canvas // 2 - 27, anchor="nw", image=imagen_fondo_tk)

    datos_csv(new_canvas, ancho_original, alto_original, nuevo_ancho, nuevo_alto)

def configura_fondo(ruta, ancho_canvas, alto_canvas):
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
    global listaAcciones
    with open('acciones2.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        encabezados = next(lector_csv)
        for fila in lector_csv:
            listaAcciones.append(fila)
    inserta_cuadros(new_canvas, listaAcciones, ancho_original, alto_original, nuevo_ancho, nuevo_alto)

def inserta_cuadros(new_canvas, acciones, ancho_original, alto_original, nuevo_ancho, nuevo_alto):
    print(ancho_original, alto_original, nuevo_ancho, nuevo_alto)
    for i in range(len(acciones)):
        x1_redimension = (int(acciones[i][7])) * (nuevo_ancho / ancho_original)
        y1_redimension = (int(acciones[i][8])) * (nuevo_alto / alto_original)
        x2_redimension = (int(acciones[i][7]) + int(acciones[i][9])) * (nuevo_ancho / ancho_original)
        y2_redimension = (int(acciones[i][8]) + int(acciones[i][10])) * (nuevo_alto / alto_original)

        new_canvas.create_rectangle(x1_redimension, y1_redimension, x2_redimension, y2_redimension, width=5)

        if (i >= 50):
            if ('cesta' in acciones[i][6] or 'estimacion' in acciones[i][6]):
                new_canvas.create_text(x1_redimension - 100, y1_redimension + 20, text=acciones[i][6], font=("Arial", 20))
            else:
                new_canvas.create_text(x1_redimension + 50, y1_redimension - 20, text=acciones[i][6], font=("Arial", 20))


# crear ventana principal
root = tk.Tk()

#Inicializamos variables
listaAcciones=[]
ruta_imagen="" #ruta de la imagen que quiero poner de fondo
#variables para crear los radiobutton
arbitro = tk.StringVar(value="EleccionArbitro")
campo = tk.StringVar(value="EleccionCampo")

# llamar función para crear el canvas con imagen de fondo
create_canvas(root,ruta_imagen)

# iniciar el bucle principal de la aplicación
root.mainloop()

