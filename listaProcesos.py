import subprocess
from datetime import datetime

from sqlConnection import db

# Obtiene la lista de procesos detallada asi como el numero de procesos en ejecucion en tiempo real
def getPsList():

    cursor = db.cursor()

    ps_output = subprocess.check_output("ps aux", shell=True).decode() # Obtener la lista de procesos a traves del comando ps aux

    lines = ps_output.splitlines() # Separar las lineas de la salida estandar del comando

    cursor.execute("DELETE FROM lista_procesos") # Eliminar los registros antiguos de la tabla

    for line in lines[1:]:
        columns = line.split() # Separar las columnas de cada fila

        if len(columns) >= 11:
            user = columns[0] # Obtener el usuario que ejecuta el proceso
            pid = int(columns[1]) # Obtener el id de proceso
            cpu = float(columns[2]) # Carga de cpu empleada por ese proceso
            mem = float(columns[3]) # Memoria empleada por ese proceso
            virtual_mensize = int(columns[4]) # Tamaño de la memoria virtual de ese proceso
            resident_memsize = int(columns[5]) # Cantidad de la memoria RAM empleada
            terminal_associated = columns[6] # Terminal asociada al proceso
            p_state = columns[7] # Estado del proceso
            p_start_time = columns[8] # Fecha y hora de inicio del proceso
            time = columns[9] # Tiempo de ejecucion del proceso
            command = " ".join(columns[10:]) # Comando asociado

            # Insertar los datos en la tabla SQL
            query = """
            INSERT INTO lista_procesos (user, pid, cpu, mem, virtual_memsize, resident_memsize, terminal_associated, p_state, p_start_time, p_time, command)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(query, (user, pid, cpu, mem, virtual_mensize, resident_memsize, terminal_associated, p_state, p_start_time, time, command))


    cursor.execute("INSERT INTO numero_procesos (procesos) VALUES (%s)", ((len(lines) - 1),)) # Actualizar el numero de procesos en ejecucion 
    db.commit() # Actualizar db
    cursor.close() # Cerrar cursor
    print(str(datetime.now())+" | Lista de procesos actualizada.")

