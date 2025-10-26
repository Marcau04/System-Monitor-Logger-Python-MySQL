import subprocess
from datetime import datetime

from sqlConnection import db


def getIOOp():

    #Creamos un cursor para ejecutar consultas SQL en la base de datos
    cursor = db.cursor()
    # Ejecutar el comando vmstat para obtener informacion acerca de las operaciones E/S
    ps_output = subprocess.check_output("vmstat", shell=True).decode()
    # Procesamos la salida
    lines = ps_output.splitlines()

    #Procesamos cada linea de salida
    for line in lines[2:]:
        columns=line.split()
        if len(columns) >= 4:
            ioProcess=columns[1]                    #Numero de procesos en espera de E/S
            read_blocks_fromDisk=int(columns[8])    #Numero de bloques recibidos de dispositivos
            write_blocks_toDisk=int(columns[9])     #Numero de bloques enviados a dispositivos
            cpuTimeWaitingIO=int(columns[15])       #Procentaje de CPU esperando por operaciones E/S

            # Construir la consulta SQL para insertar los datos
            query = """
            INSERT INTO operaciones_IO (ioProcess, read_blocks_fromDisk, write_blocks_toDisk, cpuTimeWaitingIO)
            VALUES (%s, %s, %s, %s)
            """
            # Ejecutar la consulta con los datos
            cursor.execute(query, (ioProcess, read_blocks_fromDisk, write_blocks_toDisk, cpuTimeWaitingIO))
    # Confirmar los cambios en la base de datos
    db.commit()
    cursor.close()
    print(str(datetime.now())+" | Lista de operaciones entrada y salida actualizada.")

            
