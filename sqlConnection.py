import mysql.connector

# Datos de conexion a la base de datos MySQL
conexionData = {
    "host": "localhost",
    "user": "usuario",
    "password": "pyData",
    "database": "practicas"
}

# Devuelve una nueva conexion a la base de datos
def newConnection():
    return mysql.connector.connect(**conexionData)

# Conexion a la base de datos utilizada por el hilo principal del programa
db = newConnection()