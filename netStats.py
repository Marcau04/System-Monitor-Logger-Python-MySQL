import psutil
from datetime import datetime

from sqlConnection import db

def getNetworkStats():
    #Creamos un cursor para ejecutar consultas SQL en la base de datos
    cursor = db.cursor()

    #Utilizamos la funcion de psutil net_io_counters para obtener los bytes enviados y recibidos en un momento determinado
    net_io = psutil.net_io_counters()
    bytes_enviados = net_io.bytes_sent #Bytes enviados
    bytes_recibidos = net_io.bytes_recv #Bytes recibidos

    # Insertar los datos obtenidos (Bytes de entrada y de salida) en la base de datos
    query = """
    INSERT INTO estadisticas_red ( bytes_enviados, bytes_recibidos)
    VALUES (%s, %s)
    """
    cursor.execute(query, ( bytes_enviados, bytes_recibidos))
    
    # Confirmar los cambios en la base de datos
    db.commit()
    cursor.close()
    
    print(str(datetime.now())+" | Estadísticas de red actualizadas.")