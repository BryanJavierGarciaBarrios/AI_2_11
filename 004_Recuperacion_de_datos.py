import csv

# Abrir el archivo CSV
with open('datos.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    # Leer los datos línea por línea
    for fila in lector:
        print(fila)

# Recuperación de datos desde una base de datos SQLite:

import sqlite3

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Ejecutar una consulta SQL para recuperar datos de una tabla
cursor.execute('SELECT * FROM mi_tabla')

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()

#
La recuperación de datos generalmente implica acceder y extraer información de una fuente de datos, como una base de datos, un archivo o un servicio en línea. El código específico para recuperar datos dependerá de la fuente y del tipo de datos que desees recuperar. A continuación, te mostraré ejemplos simples de cómo recuperar datos de algunas fuentes comunes en Python.

Recuperación de datos desde un archivo CSV:

Supongamos que tienes un archivo CSV llamado "datos.csv" y deseas recuperar los datos de él. Puedes utilizar la biblioteca csv de Python para hacerlo:

python
Copy code
import csv

# Abrir el archivo CSV
with open('datos.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    # Leer los datos línea por línea
    for fila in lector:
        print(fila)
Recuperación de datos desde una base de datos SQLite:

Supongamos que tienes una base de datos SQLite y deseas recuperar datos de una tabla en ella. Puedes utilizar la biblioteca sqlite3:

python
Copy code
import sqlite3

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Ejecutar una consulta SQL para recuperar datos de una tabla
cursor.execute('SELECT * FROM mi_tabla')

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
Recuperación de datos desde una API web (por ejemplo, JSON):
