#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Canvas, Toplevel
import xml.etree.ElementTree as ET

contador_clics=0
contador_clics_c1=0
contador_clics_c2=0
contador_clics_c3=0
contador_clics_ord=0
contador_clics_cereza=0

listaAcciones=[]
listaResultados=[]

def leer_xml():
    global listaAcciones
    tree = ET.parse('xmlprueba.xml')
    root = tree.getroot()
    for child in root:
        #print(child.tag, child.attrib)

        for childs in child:
            if child.tag =='acciones':
                #print(childs.attrib)
                listaAcciones.append(childs.attrib)
            elif child.tag =='resultados':
                listaResultados.append(childs.attrib)

def instrucciones():
    '''
    Funcion para explicar donde debe hacer clic el usuario en función de los puntos
    NOTA: No sé si mostrarlas en la parte izquierda de la ventana o crear una ventana principal que muestre las
    instrucciones y al pulsar un boton OK nos muestre ya el tablero
    '''
    newWindow=Toplevel(ventana)
    newWindow.title("Instrucciones")
    newWindow.geometry("700x500")

    canvas2 = Canvas(newWindow, width=700, height=500)
    canvas2.pack()

    canvas2.create_text(350, 90, text="Contamos con la siguiente figura en cada plato del tablero:")
    canvas2.create_line(300, 110, 400, 110, width=5)  #
    canvas2.create_line(300, 130, 400, 130, width=5)  #
    canvas2.create_line(300, 150, 400, 150, width=5)  #
    canvas2.create_line(300, 170, 400, 170, width=5)
    canvas2.create_line(300, 110, 300, 170, width=5)  # VERTICAL
    canvas2.create_line(400, 110, 400, 170, width=5)  # VERTICAL
    canvas2.create_line(350, 110, 350, 150, width=5)  # VERTICAL
    canvas2.create_text(330, 250, text=" Clica en el primer cuadrado para puntuar pasteles de una capa\n"
                                      "En el segundo para puntuar pasteles de dos capas\n"
                                      "En el tercer cuadrado para puntuar pasteles de 3 capas que no siguen un orden\n"
                                      "En el cuarto para puntuar los de tres capas que siguen un orden\n"
                                      "Y en el utlimos rectangulo para los pasteles que tienen una cereza.\n")

def inserta_lineas(acciones):
    '''
    Función que pinta las zonas activas en el lienzo
    '''

    for i in range(len(acciones)):
        canvas.create_rectangle(acciones[i]["x1"], acciones[i]["y1"], acciones[i]["x2"], acciones[i]["y2"], width=3,
                                outline='black')


def calcula_puntos(event, acciones):
    '''
    Funcion que cuenta los puntos parciales realizados
    '''

    global contador_clics_c1
    global contador_clics_c2
    global contador_clics_c3
    global contador_clics_ord
    global contador_clics_cereza

    for i in range(len(acciones)):
        if (int(acciones[i]['x1']) <= event.x < int(acciones[i]['x2']) and
                int(acciones[i]['y1']) <= event.y < int(acciones[i]['y2'])):
            if str(acciones[i]['nombre']).__contains__("1_capa"):
                contador_clics_c1 += 1
                if (contador_clics_c1 >= (int(acciones[i]['max']))):
                    contador_clics_c1 = 3
            elif str(acciones[i]['nombre']).__contains__("2_capas"):
                contador_clics_c2 += 2
                if (contador_clics_c2 >= (int(acciones[i]['max']))*2):
                    contador_clics_c2 = 6
            elif str(acciones[i]['nombre']).__contains__("3_capas"):
                contador_clics_c3 += 3
                if (contador_clics_c3 >= (int(acciones[i]['max']))*3):
                    contador_clics_c3 = 9
            elif str(acciones[i]['nombre']).__contains__("orden"):
                contador_clics_ord += 7
                if contador_clics_ord >= (int(acciones[i]['max']))*7:
                    contador_clics_ord = 21
            elif str(acciones[i]['nombre']).__contains__("cereza"):
                contador_clics_cereza += 3
                if (contador_clics_cereza >= (int(acciones[i]['max']))*3):
                    contador_clics_cereza = 9

    contador_clics = (contador_clics_c1 + contador_clics_c2 + contador_clics_c3 + contador_clics_ord
                      + contador_clics_cereza)
    muestra_puntos(contador_clics, listaResultados)
    datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics)

def muestra_puntos(puntos, resultado):
    for i in range(len(resultado)):
        texto= canvas.create_text((int(resultado[i]["x2"])), (int(resultado[i]["y2"])), text=puntos)
        canvas.itemconfig(texto, text=puntos)


def modifica_etiqueta_puntos(resultado):
    for i in range(len(resultado)):
        canvas.create_text((int(resultado[i]["x1"])),(int(resultado[i]["y1"])), text=str(resultado[i]["nombre"]))

def datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics):
    '''
    Funcion que exporta los datos del partido a un txt
    NOTA: Poner como nombre del  txt los datos del partido, como nombre equipos y fecha de disputa
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
canvas.create_image(422,0, anchor=tk.NW, image=imgfondo) #ubicamos el lienzo en la posicion deseada

ventana.geometry("+20+0") #ubicacion de la ventana

#Boton para ver las instrucciones de la aplicación (?)
boton_intrucciones = tk.Button(ventana, text="Instrucciones", command=instrucciones) #creamos el boton
boton_intrucciones.pack()

leer_xml()
inserta_lineas(listaAcciones)

canvas.bind("<Button-1>",  lambda event, acciones=listaAcciones: calcula_puntos(event, listaAcciones))


e1=canvas.create_text((int(listaResultados[0]["x2"])),(int(listaResultados[0]["y2"])),text=0)
e2=canvas.create_text((int(listaResultados[1]["x2"])),(int(listaResultados[1]["y2"])),text=0)
e3=canvas.create_text((int(listaResultados[2]["x2"])),(int(listaResultados[2]["y2"])),text=0)
e4=canvas.create_text((int(listaResultados[3]["x2"])),(int(listaResultados[3]["y2"])),text=0)
e5=canvas.create_text((int(listaResultados[4]["x2"])),(int(listaResultados[4]["y2"])),text=0)
e6=canvas.create_text((int(listaResultados[5]["x2"])),(int(listaResultados[5]["y2"])),text=0)
e7=canvas.create_text((int(listaResultados[6]["x2"])),(int(listaResultados[6]["y2"])),text=0)
e8=canvas.create_text((int(listaResultados[7]["x2"])),(int(listaResultados[7]["y2"])),text=0)
e9=canvas.create_text((int(listaResultados[8]["x2"])),(int(listaResultados[8]["y2"])),text=0)
e10=canvas.create_text((int(listaResultados[9]["x2"])),(int(listaResultados[9]["y2"])),text=0)

#print(listaAcciones[1])

ventana.mainloop()
