import subprocess
from datetime import datetime

from sqlConnection import db


def getED():

    #Creamos un cursor para ejecutar consultas SQL en la base de datos
    cursor = db.cursor()
    # Ejecutar el comando df -h para obtener el espacio disponbile en los sistemas de archivos de la maquina
    ps_output = subprocess.check_output("df -h", shell=True).decode()
    # Contador usado para calcular el espacio disponible total
    total_available = 0
    # Se procesa la salida
    lines = ps_output.splitlines()
    #Procesamos cada linea de salida
    for line in lines[1:]:
        columns=line.split()
        if len(columns) >= 4:
            # De la salida obtenida solo nos interesa el espacio disponible
            available_space = columns[3]
            # Reconvertimos el espacio disponible a GB en funcion de la unidad en la que se encuentre y lo sumamos al contador
            if "B" in available_space:
                total_available += float(available_space.replace("B", "").replace(",", ".")) / 1024 / 1024 / 1024
            elif "K" in available_space:
                total_available += float(available_space.replace("K", "").replace(",", ".")) / 1024 / 1024
            elif "M" in available_space:
                total_available += float(available_space.replace("M", "").replace(",", ".")) / 1024
            elif "G" in available_space:
                total_available += float(available_space.replace("G", "").replace(",", "."))

    # Construir la consulta SQL para insertar los datos
    query = """
    INSERT INTO espacio_disponible (total_available)
    VALUES (%s)
    """
    # Ejecutar la consulta con los datos
    cursor.execute(query, (total_available,))
    # Confirmar los cambios en la base de datos
    db.commit()
    cursor.close()
    print(str(datetime.now())+" | Lista de espacio disponible actualizada.")