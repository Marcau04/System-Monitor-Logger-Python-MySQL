import subprocess
from datetime import datetime

from sqlConnection import db
                                                                                                                       
def getConnections():
    cursor = db.cursor()

    # Ejecutar el comando ss -tuln para obtener las conexiones activas
    ss_output = subprocess.check_output("ss -tan", shell=True).decode()

    # Procesar la salida
    lines = ss_output.splitlines()

    # Limpiar la tabla de conexiones de red antes de insertar nuevos datos
    cursor.execute("DELETE FROM conexiones_red")

    # Procesar las líneas de la salida
    for line in lines[1:]:
        columns = line.split()

        if len(columns) >= 5:
            state = columns[0]            # Estado de la conexión
            recv_q = columns[1]           # Recv-Q (Número de bytes pendientes en la cola de recepción)
            send_q = columns[2]           # Send-Q (Número de bytes pendientes en la cola de envío)
            local_address = columns[3]    # Dirección local (ej. 0.0.0.0:puerto)
            peer_address = columns[4]     # Dirección del peer (destino)

            # Construir la consulta SQL para insertar los datos
            query = """
            INSERT INTO conexiones_red (estado, recv_q, send_q, direccion_local, direccion_peer)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            # Ejecutar la consulta con los datos
            cursor.execute(query, (state, recv_q, send_q, local_address, peer_address))

    # Insertar el número total de conexiones
    cursor.execute("INSERT INTO numero_conexiones (conexiones) VALUES (%s)", (len(lines) - 1,))

    print(str(datetime.now())+" | conexiones actualizadas.")

    # Confirmar los cambios en la base de datos
    db.commit()
    cursor.close()