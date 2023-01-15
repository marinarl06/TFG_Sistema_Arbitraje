#Importacion de librerias necesarias
import tkinter as tk
from tkinter import PhotoImage, Canvas
import xml.etree.ElementTree as ET

#Contadores provisionales para el recuento de puntos para comprobar si funciona la capturacion de clics
contador_clics_c1=0
contador_clics_c2=0
contador_clics_c3=0
contador_clics_ord=0
contador_clics_cereza=0

listaAcciones=[] #lista que almacena las acciones del xml
estiloAcciones=[] #lista que almacena el campo estilo de las acciones del xml
graficos=[] #lista que almacena el campo graficos de las acciones del xml
listaResultados=[] #lista que almacena los resultados del xml
estiloResultado=[] #lista que almacena el campo estilo de los resultados del xml

def read_children(element):
    '''
    Funcion que lee todos los hijos, subhijos..., que tiene un xml de manera recursiva
    '''
    global listaAcciones
    global listaResultados

    for child in element:
        if element.tag == 'acciones' or element.tag=='accion':
            if(child.tag == 'estilo'):
                estiloAcciones.append(child.attrib)
            elif child.tag == 'graficos':
                graficos.append(child.attrib)
            else:
                listaAcciones.append(child.attrib)

        elif element.tag =='resultados' or element.tag=='resultado':
            if (child.tag == 'estilo'):
                estiloResultado.append(child.attrib)
            else:
                listaResultados.append(child.attrib)

        read_children(child)

def leer_xml():
    '''
    Funcion que extrae de un archivo xml los datos que necesitamos para la aplicacion
    '''
    tree = ET.parse('xmlprueba.xml') #leemos el archivo txt
    root = tree.getroot() #obtenemos la raiz de dicho archivo
    read_children(root)


def inserta_lineas(acciones):
    '''
    Función que pinta las zonas activas en el lienzo
    '''
    for i in range(len(acciones)):
        canvas.create_rectangle(acciones[i]['x1'], acciones[i]['y1'], acciones[i]['x2'], acciones[i]['y2'],
                                width=estiloAcciones[i]['ancho'], outline=estiloAcciones[i]['borde'])


def calcula_puntos(event, acciones):
    '''
    Funcion que cuenta los puntos en cada zona activa y los suma para obtener los puntos parciales
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
                if (contador_clics_c1 >= 3):
                    contador_clics_c1 = 3
            elif str(acciones[i]['nombre']).__contains__("2_capas"):
                contador_clics_c2 = +1
                if (contador_clics_c2 >= (int(acciones[i]['max']))):
                    contador_clics_c2= 6
            elif str(acciones[i]['nombre']).__contains__("3_capas"):
                contador_clics_c3 += 3
                if (contador_clics_c3 >= 9):
                    contador_clics_c3 = 9
            elif str(acciones[i]['nombre']).__contains__("orden"):
                contador_clics_ord += 7
                if (contador_clics_ord >= 21):
                    contador_clics_ord = 21
            elif str(acciones[i]['nombre']).__contains__("cereza"):
                contador_clics_cereza += 3
                if (contador_clics_cereza >= 9):
                    contador_clics_cereza = 9

            posicion = (i // 5) #calcula el plato en el que hay que actualizar el marcador cuando hago clic en un plato
            contador_clics=contador_clics_c1+contador_clics_c2+contador_clics_c3+contador_clics_ord+contador_clics_cereza


    #contador_clics = (contador_clics_c1 + contador_clics_c2 + contador_clics_c3 + contador_clics_ord
                     # + contador_clics_cereza)
    muestra_puntos(contador_clics, listaResultados, posicion)
    datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics)

def muestra_puntos(puntos, resultado, posicion):
    '''
    Función encargada de modificar los resultados parciales de cada plato
    '''
    for i in range(len(resultado)):
        canvas.itemconfig(etiquetas[posicion], text=puntos)

def etiqueta_puntos(resultado):
    '''
    Funcion encargado de insertar el titulo del marcador parcial de cada plato
    ej: "Total Plato 1 Azul"
    '''
    for i in range(len(resultado)):
        canvas.create_text((int(resultado[i]["x1"])), (int(resultado[i]["y1"])),
                           text=(str(resultado[i]["nombre"])), font=(estiloResultado[i]["fuente"], (int(estiloResultado[i]["tamano"]))))

def total_puntos():
    '''
    Funcion que calcula el total de puntos de cada equipo
    NOTA: realizar cuando funcione correctamente la funcion que calcula los puntos parciales
    '''
    pass

def datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics):
    '''
    Funcion que exporta los datos del partido a un txt
    NOTA: Poner como nombre del  txt los datos del partido, como nombre equipos y fecha de disputa
    NOTA2: Modificar cuando la funcion calculo funcione correctamente
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
ventana.title("Eurobot Spain 2023")  # título de ventana, se muestra en la barra

# Creamos la componente Canvas
canvas=Canvas(ventana)
canvas.config(width=ventana.winfo_screenwidth(), height=ventana.winfo_screenheight()) #establecemos las dimensiones del canvas acorde a las dimensiones de la pantalla del ordenador
canvas.place(x = ventana.winfo_screenwidth()/2, y = ventana.winfo_screenheight()/2)
canvas.pack()

imgfondo = PhotoImage(file="tablero.png") #Cargamos la imagen del tablero en la ventana
canvas.create_image(422,0,anchor=tk.NW, image=imgfondo) #ubicamos el lienzo en la posicion deseada

#Boton para ver las instrucciones de la aplicación (?)
#boton_intrucciones = tk.Button(ventana, text="Instrucciones", command=instrucciones) #creamos el boton
#boton_intrucciones.pack()

leer_xml()
inserta_lineas(listaAcciones)
etiqueta_puntos(listaResultados)

#Capturamos el clic en las zonas activas
canvas.bind("<Button-1>",lambda event, acciones=listaAcciones: calcula_puntos(event, acciones))


#Array para mostrar la puntuación inicial e ir modificandola
etiquetas=[
canvas.create_text((int(listaResultados[0]["x2"])),(int(listaResultados[0]["y2"])),text=0,
                   font=(estiloResultado[0]["fuente"], (int(estiloResultado[0]["tamano"])))),
canvas.create_text((int(listaResultados[1]["x2"])),(int(listaResultados[1]["y2"])),text=0,
                   font=(estiloResultado[1]["fuente"], (int(estiloResultado[1]["tamano"])))),
canvas.create_text((int(listaResultados[2]["x2"])),(int(listaResultados[2]["y2"])),text=0,
                   font=(estiloResultado[2]["fuente"], (int(estiloResultado[2]["tamano"])))),
canvas.create_text((int(listaResultados[3]["x2"])),(int(listaResultados[3]["y2"])),text=0,
                   font=(estiloResultado[3]["fuente"], (int(estiloResultado[3]["tamano"])))),
canvas.create_text((int(listaResultados[4]["x2"])),(int(listaResultados[4]["y2"])),text=0,
                   font=(estiloResultado[4]["fuente"], (int(estiloResultado[4]["tamano"])))),
canvas.create_text((int(listaResultados[5]["x2"])),(int(listaResultados[5]["y2"])),text=0,
                   font=(estiloResultado[5]["fuente"], (int(estiloResultado[5]["tamano"])))),
canvas.create_text((int(listaResultados[6]["x2"])),(int(listaResultados[6]["y2"])),text=0,
                   font=(estiloResultado[6]["fuente"], (int(estiloResultado[6]["tamano"])))),
canvas.create_text((int(listaResultados[7]["x2"])),(int(listaResultados[7]["y2"])),text=0,
                   font=(estiloResultado[7]["fuente"], (int(estiloResultado[7]["tamano"])))),
canvas.create_text((int(listaResultados[8]["x2"])),(int(listaResultados[8]["y2"])),text=0,
                   font=(estiloResultado[8]["fuente"], (int(estiloResultado[8]["tamano"])))),
canvas.create_text((int(listaResultados[9]["x2"])),(int(listaResultados[9]["y2"])),text=0,
                   font=(estiloResultado[9]["fuente"], (int(estiloResultado[9]["tamano"]))))
]

ventana.mainloop()
