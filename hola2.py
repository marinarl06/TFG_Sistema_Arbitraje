import tkinter as tk
from PIL import Image, ImageTk
import csv
import os

root = tk.Tk()

# Carga la imagen de fondo
ruta_imagen = "/Users/marinaramajolazaro/Documents/Universidad/TFG/TFG_Sistema_Arbitraje/arbitro_izq.png"
imagen_fondo_original = Image.open(ruta_imagen)

#Obtenemos el ancho y el alto de la imagen para usarlo posteriormente
ancho_original=imagen_fondo_original.width
alto_original= imagen_fondo_original.height

# Obtiene el tamaño del canvas
alto_canvas = root.winfo_screenheight()
ancho_canvas = root.winfo_screenwidth()

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

# Crea el canvas
canvas = tk.Canvas(root, width=ancho_canvas, height=alto_canvas)
canvas.pack()

# Dibuja la imagen de fondo en el canvas
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
canvas.create_image(0, 0, anchor="nw", image=imagen_fondo_tk)

def datos_csv():
    global listaAcciones
    with open('acciones2.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        encabezados = next(lector_csv)
        for fila in lector_csv:
            listaAcciones.append(fila)

def inserta_cuadros(acciones):
    print(ancho_original, nuevo_ancho)
    for i in range(len(acciones)):
        x1_redimension = int(acciones[i][7]) * (nuevo_ancho / ancho_original)
        y1_redimension = int(acciones[i][8]) * (nuevo_alto / alto_original)
        x2_redimension = (int(acciones[i][7]) + int(acciones[i][9])) * (nuevo_ancho / ancho_original)
        print(x1_redimension, x2_redimension)
        y2_redimension = (int(acciones[i][8]) + int(acciones[i][10])) * (nuevo_alto / alto_original)

        canvas.create_rectangle(x1_redimension, y1_redimension, x2_redimension, y2_redimension, width=5)

        if (i >= 50):
            if ('cesta' in acciones[i][6] or 'estimacion' in acciones[i][6]):
                canvas.create_text(x1_redimension - 100, y1_redimension + 20, text=acciones[i][6], font=("Arial", 20))
            else:
                canvas.create_text(x1_redimension + 50, y1_redimension - 20, text=acciones[i][6], font=("Arial", 20))


listaAcciones=[]
datos_csv()
inserta_cuadros(listaAcciones)


root.mainloop()


