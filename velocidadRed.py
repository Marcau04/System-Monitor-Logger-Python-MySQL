import psutil
from datetime import datetime
from sqlConnection import newConnection
from time import sleep

def getTransferSpeed():

    # Se establece la conexión con la base de datos
    db = newConnection()
    #Creamos un cursor para ejecutar consultas SQL en la base de datos
    cursor = db.cursor()

    # Obtener las estadísticas iniciales de la red
    net_io_start = psutil.net_io_counters()

    # Esperar un segundo para obtener la nueva lectura
    sleep(1)

    # Obtener las estadísticas finales de la red
    net_io_end = psutil.net_io_counters()

    # Calcular la diferencia en bytes enviados y recibidos con tal de obtener los bytes por segundo
    bytes_sent_per_sec = net_io_end.bytes_sent - net_io_start.bytes_sent
    bytes_recv_per_sec = net_io_end.bytes_recv - net_io_start.bytes_recv

    fecha = datetime.now()

    # Insertar los datos en la base de datos
    query = """
    INSERT INTO velocidad_transferencia (bytes_enviados_por_segundo, bytes_recibidos_por_segundo)
    VALUES (%s, %s)
    """
    cursor.execute(query, (bytes_sent_per_sec, bytes_recv_per_sec))

    # Confirmar los cambios en la base de datos
    db.commit()
    cursor.close()
    
    print(f"{fecha} | Velocidad de transferencia registrada: {bytes_sent_per_sec} B/s enviados, {bytes_recv_per_sec} B/s recibidos.")