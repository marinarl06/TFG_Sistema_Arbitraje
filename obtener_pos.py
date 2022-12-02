from pynput.mouse import Listener

'''
Para obtener la posicion en la que hacemos click y asi poder declarar las zonas activas de la aplicación
'''
def on_move(x, y):
    print("Mouse moved")

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    print("Mouse scrolled")

#Unimos los metodos creados con el listener
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
