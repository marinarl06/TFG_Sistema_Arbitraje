"""import xmltodict

# Abre el archivo XML
with open("xmlprueba.xml", "r") as archivo:
  # Convierte el contenido del archivo a un diccionario
  datos = xmltodict.parse(archivo.read())

# Accede a los datos del diccionario como lo harías con cualquier otro diccionario de Python
print(datos)

acciones=datos["EurobotSpain"]["acciones"]

print(acciones)"""

import xml.etree.ElementTree as ET
tree = ET.parse('xmlprueba.xml')
root = tree.getroot()
listaAcciones=[]

#print(root.tag,root.attrib)"""
for child in root:
    print(child.tag, child.attrib)

    for childs in child:
        if child.tag =='acciones':
            listaAcciones.append(childs)
            print("el tag es " + childs.tag, childs.attrib)
            print(childs.attrib['nombre'])
        elif child.tag =='resultados':
            print("el tag es " + childs.tag, childs.attrib)
            print(childs.attrib['nombre'])

for child in listaAcciones:
    print(child.attrib)
'''
from lxml import etree

xml_file = 'archivo.xml'

# parsear el archivo XML
xml_tree = etree.parse('xmlprueba.xml')

def print_attribs(element, depth=0):
    # imprimir el nombre del elemento y sus atributos
    print(element.tag, element.attrib)
    # iterar sobre los hijos del elemento
    for child in element.getchildren():
        # llamar a la función recursivamente para cada hijo
        print_attribs(child, depth+1)

# llamar la función con el elemento raíz
print_attribs(xml_tree.getroot())

def create_dict(element):
    # crear un diccionario para el elemento actual
    element_dict = {'tag': element.tag, 'attrib': element.attrib}
    element_dict["text"] = element.text
    # crear una lista para almacenar los diccionarios de los hijos
    children_list = []
    # iterar sobre los hijos del elemento
    for child in element.getchildren():
        # llamar a la función recursivamente para cada hijo
        children_list.append(create_dict(child))
    if children_list:
        element_dict['children'] = children_list
    return element_dict

root_dict = create_dict(xml_tree.getroot())
print(root_dict)
'''
