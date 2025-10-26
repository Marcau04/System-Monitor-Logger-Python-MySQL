import psutil
from datetime import datetime
from sqlConnection import db

# Monitoriza frecuencia (MHz) y uso (%) de la CPU
def updateCpuStats():
    cursor = db.cursor() # Declaracion del cursor de la db

    # Insertar la frecuencia actual y el uso actual en la db
    cursor.execute("INSERT INTO cpu_Stats (uso_cpu, frec_cpu) VALUES (%s, %s)", (psutil.cpu_percent(interval=1), psutil.cpu_freq().current))
    
    db.commit() # Actualizar db
    cursor.close() # Cerrar el cursor

    print(str(datetime.now())+" | Estadisticas de la CPU actualizadas.")