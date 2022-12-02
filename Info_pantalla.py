import tkinter as tk

'''
Imprime la información de la pantalla en la que estoy trabajando, para saber 
que dimensiones de ventana establecer en la app
'''
ventana=tk.Tk()

def imprimir_informacion(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")


ventana.update()
imprimir_informacion(ventana)