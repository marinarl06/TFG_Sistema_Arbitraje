'''
Created on 7 mar 2023

Funciones de acceso a la base de datos para la apliación de arbitraje.

@author: pedrogil
'''
###############################################################################

def partido_actual(cursor, campo):
    cursor.execute("SELECT DISTINCT partido FROM aux_acciones_arbitros WHERE campo = %i" % campo)
    res = cursor.fetchall()
    if len(res) > 1:
        raise RuntimeError("Error base datos: más de un partido en juego")
    if len(res) == 0:
        raise ValueError("No hay ningún partido en juego en el campo %i" % campo)
    return res[0]["partido"]


def vista_arbitro(cursor, campo, lado):
    cursor.execute("SELECT * FROM view_acciones_campo_%c_%i" % (campo, lado))
    vista = cursor.fetchall()
    return vista


def actualizar_accion(cursor, partido, accion, valor):
    cursor.execute("UPDATE acciones SET valor = %i WHERE accion = %i AND partido = %i" % (valor, accion, partido))

