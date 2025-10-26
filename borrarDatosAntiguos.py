from sqlConnection import newConnection

# Borrado de datos anteriores a 7 horas
def deleteOld():
    db = newConnection() # Nueva conexion sql para evitar condiciones de carrera con los otros hilos
    cursor = db.cursor() # Declaracion del cursor
    cursor.execute("SHOW TABLES") # Obtener todas las tablas de la base de datos
    tables = [table[0] for table in cursor.fetchall()] # Insertar los nombres de las tablas de la db en un array de strings

    for table in tables:
        cursor.execute(f"DELETE FROM {table} WHERE time < NOW() - INTERVAL 7 HOUR") # Para cada tabla de la base de datos eliminar los datos anteriores a 7 horas

    print("Datos Antiguo Borrados (+ 7 horas)")
    db.commit() # Actualizar db
    cursor.close() # Cerrar el cursor