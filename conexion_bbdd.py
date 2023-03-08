import pymysql

# Crear la conexión con la base de datos
conexion = pymysql.connect(host='localhost', user='root', password='', database='eurobots_2023_senior')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM view_acciones_campo_A_1")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Crear un array para almacenar los resultados
array_resultados = []

# Recorrer los resultados y agregarlos al array
for resultado in resultados:
    array_resultados.append(list(resultado))

# Imprimir el array de resultados
print(array_resultados[0][11])

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()


