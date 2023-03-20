'''
Created on 7 mar 2023

Archivo de test para simular el comportamiento del programa de gestión de
la competición, para poder probar el funcionamiento del programa de recuento
de puntos.

@author: pedrogil
'''

import mariadb
import sys

import base_datos


###############################################################################
# Funciones auxiliares de la base de datos.
# Estas funciones simulan el comportamiento del programa de gestión de la
# competición, para poder crear partidos.

def borrar_partidos_todos(cursor):
    # Eliminamos todos los partidos que tengamos:
    cursor.execute("DELETE FROM partidos")


def anadir_partido(cursor, campo, lado1, lado2):
    cursor.execute(
        "INSERT INTO partidos (campo, lado_1_equipo, lado_2_equipo) VALUES (%i, %i, %i);" % (campo, lado1, lado2))

    connection.commit()
    return cursor.lastrowid



def anadir_partido_fase_final(cursor, campo, fase, lado1, lado2):
    cursor.execute("INSERT INTO partidos (campo, fase, lado_1_equipo, lado_2_equipo) VALUES (%i, %i, %i, %i);" % (
    campo, fase, lado1, lado2))
    return cursor.lastrowid


def partido_en_juego(cursor, partido):
    cursor.execute("UPDATE partidos SET estado = 2 WHERE partidos_ID = %i" % partido)
    connection.commit()


def partido_jugado(cursor, partido):
    cursor.execute("UPDATE partidos SET estado = 3 WHERE partidos_ID = %i" % partido)


def eliminar_partido(cursor, partido):
    cursor.execute("UPDATE partidos SET estado = 4 WHERE partidos_ID = %i" % partido)


def clasificacion(cursor, equipo):
    cursor.execute("SELECT * FROM view_resultados_clasificacion WHERE equipo_id = %i" % equipo)
    clasificacion = cursor.fetchone()
    return clasificacion


###############################################################################


# Base de datos local (cambiar valores por los correctos)
user = "root"
password = ""
host = "localhost"
port = 3306
database = "eurobots_2023"

# Base de datos remota (servidor UAH).
# user="eurobots_arbitro",
# password="arbitro",
# host="xwww6.uah.es",
# port=3306,
# database="eurobots_2023"

try:
    connection = mariadb.connect(
        user=user, password=password, host=host, port=3306, database=database)

except mariadb.Error as e:
    print("Error connecting to MariaDB Platform: %s" % e)
    sys.exit(1)
else:
    print("Base de datos: ", database, "-", host)

cursor = connection.cursor(dictionary=True)

# Eliminamos todos los partidos, para empezar desde cero.
borrar_partidos_todos(cursor)

# Comprobamos que no tenemos ningún partido en juego en ningún campo.
try:
    base_datos.partido_actual(cursor, 1)
except ValueError:
    pass
else:
    raise RuntimeError("Hay un partido en juego.")
try:
    base_datos.partido_actual(cursor, 2)
except ValueError:
    pass
else:
    raise RuntimeError("Hay un partido en juego.")

# Creamos un partido en el campo A:
partido1 = anadir_partido(cursor, 1, 1, 2)
# Creamos un partido en el campo B
partido2 = anadir_partido(cursor, 2, 1, 2)

# Hasta que el partido no esté en juego no debería aparecer ningún partido.
try:
    base_datos.partido_actual(cursor, 1)
except ValueError:
    pass
else:
    raise RuntimeError("Hay un partido en juego.")

# Ponemos el partido en juego, para poder acceder a las acciones del partido.
partido_en_juego(cursor, partido1)
# Comprobamos que el partido en juego se corresponde con el actual
if base_datos.partido_actual(cursor, 1) != partido1:
    raise RuntimeError("Error en la vista de acciones.")

###############################################################################
###############################################################################
###############################################################################
# Descargamos la lista de acciones

acciones = base_datos.vista_arbitro(cursor, "A", 1)
# Comprobamos que tenemos las 32 acciones que corresponden a este lado.
if len(acciones) != 31: #el numero que hay que poner es 32 pero nos falta una accion
    raise RuntimeError("Error: no tenemos las 32 acciones correspondientes")

# Actualizmaos la estimación del equipo del lado 1.
base_datos.actualizar_accion(cursor, partido1, 61, 30)
# Actualizamos una acción, por ejemplo, un pastel de una capa en el plato 1.
base_datos.actualizar_accion(cursor, partido1, 1, 1)

# Guardamos el partido.
partido_jugado(cursor, partido1)
# De tal forma que ahora no habrá ningún partido en la vista del árbitro.
try:
    base_datos.partido_actual(cursor, 1)
except ValueError:
    pass
else:
    raise RuntimeError("Hay un partido en juego.")

# La puntuación de este equipo será:
# 1 pastel de 1 capa -> 1 punto.
# puntos por estimación (30 - 1 ) = 29 -> 0 puntos.
# 1 punto por no penalización.
# Total: 2 puntos.
puntos_equipo1 = clasificacion(cursor, 1)
# Comprobamos que todo está correcto:
if puntos_equipo1['programado'] != 0:
    raise RuntimeError("Clasificación incorrecta")
if puntos_equipo1['en_juego'] != 0:
    raise RuntimeError("Clasificación incorrecta")
if puntos_equipo1['jugado'] != 1:
    raise RuntimeError("Clasificación incorrecta")
if puntos_equipo1['R1'] != 2:
    raise RuntimeError("Clasificación incorrecta")
if puntos_equipo1['puntos'] != 2:
    raise RuntimeError("Clasificación incorrecta")

print(acciones)


print("Fin. Test correcto")