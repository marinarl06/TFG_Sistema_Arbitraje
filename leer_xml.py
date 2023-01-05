import xml.etree.ElementTree as ET

class Archivo:

    def leer_xml(self):
        # Parse the XML file
        tree = ET.parse('temp_2023.xml')
        # Get the root element of the XML document
        root = tree.getroot()
        # Iterate over the child elements of the root element
        for child in root:
            # Print the tag and text for each child element
            print(child.tag, child.text)
            if child.tag == 'element1':
            # Assign the text of the child element to a variable
                variable1 = child.text
            elif child.tag == 'element2':
                # Assign the attribute of the child element to a variable
                variable2 = child.attrib['attribute']
