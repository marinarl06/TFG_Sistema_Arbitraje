#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Canvas
import os

plato1_azul = {'x1': [422, 472, 422, 472, 422], 'x2': [472, 522, 472, 522, 522], 'y1': [0, 0, 32, 32],
                   'y2': [32, 32, 66, 66]}
contador_clics=0
contador_clics_c1=0
contador_clics_c2=0
contador_clics_c3=0
contador_clics_ord=0
contador_clics_cereza=0

def instrucciones():
    '''
    Funcion para explicar donde debe hacer clic el usuario en función de los puntos
    NOTA: No sé si mostrarlas en la parte izquierda de la ventana o crear una ventana principal que muestre las
    instrucciones y al pulsar un boton OK nos muestre ya el tablero
    '''
    canvas.create_text(200, 90, text="Contamos con la siguiente figura en cada plato del tablero:")
    canvas.create_line(100, 110, 200, 110, width=5)  #
    canvas.create_line(100, 130, 200, 130, width=5)  #
    canvas.create_line(100, 150, 200, 150, width=5)  #
    canvas.create_line(100, 170, 200, 170, width=5)
    canvas.create_line(100, 110, 100, 170, width=5)  # VERTICAL
    canvas.create_line(200, 110, 200, 170, width=5)  # VERTICAL
    canvas.create_line(150, 110, 150, 150, width=5)  # VERTICAL



def inserta_lineas():
    '''
    Función que genera las zonas activas
    '''
    #PL1A
    canvas.create_line(472,0,472,66, width=5) #VERTICAL
    canvas.create_line(422, 66, 522, 66, width=5)
    canvas.create_line(422, 32, 522, 32, width=5)

    #PL1V
    canvas.create_line(472, 202, 472, 268, width=5) #VERTICAL
    canvas.create_line(422, 268, 522, 268, width=5)
    canvas.create_line(422, 235, 522, 235, width=5)

    # PL2A
    canvas.create_line(472, 373, 472, 439, width=5)  # VERTICAL
    canvas.create_line(422, 406, 522, 406, width=5)
    canvas.create_line(422, 439, 522, 439, width=5)

    # PL2V
    canvas.create_line(472, 576, 472, 642, width=5)  # VERTICAL
    canvas.create_line(422, 609, 522, 609, width=5)
    canvas.create_line(422, 642, 522, 642, width=5)

    #PL3A
    canvas.create_line(585, 576, 585, 642, width=5)  # VERTICAL
    canvas.create_line(535, 609, 635, 609, width=5)
    canvas.create_line(535, 642, 635, 642, width=5)

    # PL3V
    canvas.create_line(710, 576, 710, 642, width=5)  # VERTICAL
    canvas.create_line(660, 609, 760, 609, width=5)
    canvas.create_line(660, 642, 760, 642, width=5)

    # PL4A
    canvas.create_line(824, 576, 824, 642, width=5)  # VERTICAL
    canvas.create_line(774, 609, 874, 609, width=5)
    canvas.create_line(774, 642, 874, 642, width=5)

    # PL4V
    canvas.create_line(824, 372, 824, 438, width=5)  # VERTICAL
    canvas.create_line(774, 405, 874, 405, width=5)
    canvas.create_line(774, 438, 874, 438, width=5)

    # PL5A
    canvas.create_line(824, 202, 824, 268, width=5)  # VERTICAL
    canvas.create_line(774, 232, 874, 232, width=5)
    canvas.create_line(774, 268, 874, 268, width=5)

    # PL5V
    canvas.create_line(824, 0, 824, 66, width=5)  # VERTICAL
    canvas.create_line(774, 33, 874, 33, width=5)
    canvas.create_line(774, 66, 874, 66, width=5)

def calcula_puntos(event):
    '''
    Funcion que cuenta los puntos parciales realizados
    '''

    global contador_clics_c1
    global contador_clics_c2
    global contador_clics_c3
    global contador_clics_ord
    global contador_clics_cereza

    if(422 <= event.x < 472 and 0 <= event.y <33):
        contador_clics_c1+=1
        if (contador_clics_c1 >= 3):
            contador_clics_c1=3
    elif (472 <= event.x < 522 and 0 <= event.y <33):
        contador_clics_c2+=2
        if (contador_clics_c2 >= 6):
            contador_clics_c2=6
    elif (422 <= event.x < 472 and 33 <= event.y <66):
        contador_clics_c3+=3
        if (contador_clics_c3 >= 9):
            contador_clics_c3=9
    elif (472 <= event.x < 522 and 33 <= event.y <66):
        contador_clics_ord+=7
        if (contador_clics_ord >= 21):
            contador_clics_ord=21
    elif (422 <= event.x < 522 and 66 <= event.y < 100):
        contador_clics_cereza += 3
        if (contador_clics_cereza >= 9):
            contador_clics_cereza=9

    contador_clics = (contador_clics_c1 + contador_clics_c2 + contador_clics_c3 + contador_clics_ord
                      + contador_clics_cereza)
    muestra_puntos(contador_clics)
    datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics)

def muestra_puntos(puntos):
    canvas.itemconfig(texto, text=str(puntos))

def datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics):
    '''
    Funcion que exporta los datos del partido a un txt
    '''

    archivo=open("partido.txt","w")

    archivo.write("Los puntos de este partido han sido:\n")
    archivo.write("Pasteles de 1 capa: "+ str(contador_clics_c1) +"\n" )
    archivo.write("Pasteles de 2 capas: "+ str(contador_clics_c2/2)+ "\n")
    archivo.write("Pasteles de 3 capas: "+ str(contador_clics_c3/3)+"\n")
    archivo.write("Pasteles de 3 capas ordenado: "+ str(contador_clics_ord/7)+"\n")
    archivo.write("Pasteles con cereza: "+ str(contador_clics_cereza/3)+"\n")
    archivo.write("Puntos parciales en el plato 1: "+ str(contador_clics)+ "\n")




# Creamos la ventana principal
ventana = tk.Tk()
ventana.resizable(width=False, height=False)  # para que la ventana no pueda redimensionarse
ventana.title("Eurobot Spain 2023")  # título de ventana, se muestra en la barra

# Creamos la componente Canvas
canvas=Canvas(ventana,width=1300,height=700)
canvas.pack()

imgfondo = PhotoImage(file="tablero.png") #Cargamos la imagen del tablero en la ventana
canvas.create_image(422,0, anchor=tk.NW, image=imgfondo)

ventana.geometry("+20+0")

#ETIQUETAS DE TEXTO
canvas.create_text(350,33, text="Puntuacion parcial")
texto=canvas.create_text(350,50, text=0)

instrucciones()
inserta_lineas()
canvas.bind('<Button-1>', calcula_puntos)

ventana.mainloop()
