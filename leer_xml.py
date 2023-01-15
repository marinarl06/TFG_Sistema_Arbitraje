import xml.etree.ElementTree as ET

listaAcciones=[] #lista que almacena las acciones del xml
estiloAcciones=[] #lista que almacena el campo estilo de las acciones del xml
graficos=[] #lista que almacena el campo graficos de las acciones del xml
listaResultados=[] #lista que almacena los resultados del xml
estiloResultado=[] #lista que almacena el campo estilo de los resultados del xml

def read_children(element):
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
                print(listaAcciones)

        elif element.tag =='resultados' or element.tag=='resultado':
            if (child.tag == 'estilo'):
                estiloResultado.append(child.attrib)
            else:
                listaResultados.append(child.attrib)

        read_children(child)

def leer_xml():
    """
    Funcion que extrae de un archivo xml los datos que necesitamos para la aplicacion
    """
    tree = ET.parse('xmlprueba.xml') #leemos el archivo txt
    root = tree.getroot() #obtenemos la raiz de dicho archivo
    read_children(root)