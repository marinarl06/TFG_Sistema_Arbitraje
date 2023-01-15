def instrucciones():
    '''
    Funcion para explicar donde debe hacer clic el usuario en función de los puntos
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