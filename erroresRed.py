import psutil
from datetime import datetime
from sqlConnection import db

def getNetworkErrors():
    
    #Creamos un cursor para ejecutar consultas SQL en la base de datos
    cursor = db.cursor()

    # Obtener las estadísticas de la red
    net_io = psutil.net_io_counters()

    # Obtener los errores de entrada y salida, y los paquetes descartados
    errin = net_io.errin #errores de entrada
    errout = net_io.errout #errores de salida
    dropin = net_io.dropin #descartes de paquetes de entrada
    dropout = net_io.dropout #descartes de paquetes de salida

    fecha = datetime.now()

    # Insertar los datos de errores de red en la base de datos
    query = """
    INSERT INTO errores_red (errin, errout, dropin, dropout)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (errin, errout, dropin, dropout))

    # Confirmar los cambios en la base de datos
    db.commit()
    cursor.close()
    
    print(f"{fecha} | Errores de red registrados.")