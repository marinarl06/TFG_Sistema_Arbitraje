import pymysql
import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()

ruta_imagen = "/Users/marinaramajolazaro/Documents/Universidad/TFG/TFG_Sistema_Arbitraje/arbitro.png"
imagen_fondo = Image.open(ruta_imagen)

# Obtiene el tamaño del canvas
alto_canvas = root.winfo_screenheight()
ancho_canvas = root.winfo_screenwidth()

#Obtenemos el ancho y el alto de la imagen para usarlo posteriormente
ancho_original=imagen_fondo.width
alto_original= imagen_fondo.height

imagen_fondo_original = Image.open(ruta_imagen)

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

imagen_fondo_redimension = imagen_fondo_original.resize((nuevo_ancho, nuevo_alto))

# Crea el canvas
canvas = tk.Canvas(root, width=ancho_canvas, height=alto_canvas)
canvas.pack()

# Dibuja la imagen de fondo en el canvas
imagen_fondo_canvas = ImageTk.PhotoImage(imagen_fondo_redimension)
canvas.create_image(0, 0, anchor="nw", image=imagen_fondo_canvas)


# Crear un array para almacenar los resultados
array_resultados = []

#--------------------------------------------------------------------------------------------------------#
# Crear la conexión con la base de datos
conexion = pymysql.connect(host='localhost', user='root', password='', database='eurobots_2023_senior')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM view_acciones_campo_A_1")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Recorrer los resultados y agregarlos al array
for resultado in resultados:
    array_resultados.append(list(resultado))
print(array_resultados)

#--------------------------------------------------------------------------------------------------------#

def inserta_cuadros(acciones):
    nombre_archivo = os.path.basename(ruta_imagen)

    # Comprobamos si la palabra buscada está en el nombre del archivo de la imagen
    if '_izq' in os.path.basename(nombre_archivo):
        for i in range(len(acciones)):
            # Para el lado izquierdo
            x1_redimension = int(acciones[i][11]) * (nuevo_ancho / ancho_original)
            y1_redimension = int(acciones[i][12]) * (nuevo_alto / alto_original)-423
            x2_redimension = (int(acciones[i][11]) + int(acciones[i][13])) * (nuevo_ancho / ancho_original)
            y2_redimension = (int(acciones[i][12]) + int(acciones[i][14])) * (nuevo_alto / alto_original)-423

            canvas.create_rectangle(x1_redimension, y1_redimension, x2_redimension, y2_redimension,
                                    width=5)

            """if (i >= 50):
                if ('cesta' in acciones[i][10] or 'estimacion' in acciones[i][10]):
                    canvas.create_text(x1_redimension - 100, y1_redimension + 20, text=acciones[i][10],
                                       font=("Arial", 20))
                else:
                    canvas.create_text(x1_redimension + 50, y1_redimension - 20, text=acciones[i][10],
                                       font=("Arial", 20))"""

    elif '_drch' in os.path.basename(nombre_archivo):
        for i in range(len(acciones)):
            #Para el lado derecho
            x1 = int(acciones[i][11]) * (nuevo_ancho / ancho_original)-28
            y1 = int(acciones[i][12]) * (nuevo_alto / alto_original)-38
            x2 = (int(acciones[i][11]) + int(acciones[i][13])) * (nuevo_ancho / ancho_original)-28
            y2 = (int(acciones[i][12]) + int(acciones[i][14])) * (nuevo_alto / alto_original)-38

            x1_redimension = (nuevo_ancho - x1)
            y1_redimension = (y1 - nuevo_alto)
            x2_redimension = (nuevo_ancho - x2)
            y2_redimension = (y2 - nuevo_alto)

            canvas.create_rectangle(x1_redimension, y1_redimension, x2_redimension, y2_redimension,
                                    width=5)

            """if (i >= 50):
                if ('cesta' in acciones[i][10] or 'estimacion' in acciones[i][10]):
                    canvas.create_text(x1_redimension + 100, y1_redimension + 20, text=acciones[i][10],
                                       font=("Arial", 20))
                else:
                    canvas.create_text(x1_redimension - 70, y1_redimension - 20, text=acciones[i][10],
                                       font=("Arial", 20))"""
    else:
        for i in range(len(acciones)):
            x1_redimension = int(acciones[i][11]) * (nuevo_ancho / ancho_original)
            y1_redimension = int(acciones[i][12]) * (nuevo_alto / alto_original)
            x2_redimension = (int(acciones[i][11])+int(acciones[i][13])) * (nuevo_ancho / ancho_original)
            y2_redimension = (int(acciones[i][12])+int(acciones[i][14])) * (nuevo_alto / alto_original)

            canvas.create_rectangle(x1_redimension, y1_redimension, x2_redimension, y2_redimension,
                                    width=5)

            """if (i >= 50):
                if('cesta' in acciones[i][10] or 'estimacion' in acciones[i][10]):
                    canvas.create_text(x1_redimension-100, y1_redimension+20, text=acciones[i][6], font=("Arial", 20))
                else:
                    canvas.create_text(x1_redimension+50, y1_redimension-20, text=acciones[i][6], font=("Arial", 20))"""

def puntos(event,acciones):
    for i in range(len(acciones)):
        x1 = int(acciones[i][11]) * (nuevo_ancho / ancho_original)
        y1 = int(acciones[i][12]) * (nuevo_alto / alto_original)
        x2 = (int(acciones[i][11]) + int(acciones[i][13])) * (nuevo_ancho / ancho_original)
        y2 = (int(acciones[i][12]) + int(acciones[i][14])) * (nuevo_alto / alto_original)

        if(x1 < event.x < x2) and (y1 - 423 < event.y < y2- 423):
            accion_id=acciones[i][0]
            partido_id=acciones[i][4]
            #valor_dataset=cursor.execute(f'SELECT valor FROM acciones WHERE acciones_ID = {accion_id} AND partido = {partido_id}')
            cursor.execute(f'SELECT valor FROM acciones WHERE acciones_ID = {accion_id} AND partido = {partido_id}')
            valor=cursor.fetchall()
            resultado=valor[0][0]+1
            cursor.execute(f'UPDATE acciones SET valor = {resultado} WHERE acciones_ID = {accion_id} AND partido = {partido_id}')
            print(resultado)

def pintar_lineas(event):
    print(str(event.x) + "," + str(event.y))

root.bind("<Button-1>", lambda event, array_resultados=array_resultados: puntos(event, array_resultados))

inserta_cuadros(array_resultados)

root.mainloop()

# Cerrar el cursor y la conexión de la base de datos
cursor.close()
conexion.close()


