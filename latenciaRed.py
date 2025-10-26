import subprocess
from datetime import datetime
import re

from sqlConnection import newConnection


def getLN():

    # Se establece la conexión con la base de datos
    db = newConnection()
    #Creamos un cursor para ejecutar consultas SQL en la base de datos  
    cursor = db.cursor()

    # Ejecutar el comando ping -c 50 google.com para poder realizar una media realista de los tiempos de respuesta
    ps_output = subprocess.check_output("ping -c 50 google.com", shell=True).decode()

    # Se procesa la salida para unicamente mantener un array con los tiempos de respuesta
    times = re.findall(r'time=(\d+\.\d+)', ps_output)
    # Se castea cada uno de los tiempos anteriormente procesados para mantener un array con los tiempos de tipo float
    times = [float(time) for time in times]

    # Se calcula la media de los tiempos recogidos
    average_times = sum(times) / len(times)
    # Se construye la consulta SQL para insertar los datos
    query = """
    INSERT INTO latency_in_networking (average_times)
    VALUES (%s)
    """
    # Se ejecuta la consulta con los datos
    cursor.execute(query, (average_times,))
    # Se confirman los cambios en la base de datos
    db.commit()
    cursor.close()
    print(str(datetime.now())+" | Latencia en red actualizada.")