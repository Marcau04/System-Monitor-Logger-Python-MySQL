import subprocess
from datetime import datetime

from sqlConnection import db


# Función para obtener datos de memoria desde /proc/meminfo
def get_memory_info():
    cursor = db.cursor()
    meminfo_output = subprocess.check_output("cat /proc/meminfo", shell=True).decode()
    lines = meminfo_output.strip().split("\n")

    cursor.execute("DELETE FROM memoria_ram_swap")

    ramMem = 0
    swapMem = 0
    
    for line in lines:
        partes = line.split(":")
        nombre = partes[0].strip()
        valores = partes[1].strip().split()
        valor = valores[0]
        unidad = valores[1] if len(valores) > 1 else "N/A"

        query="""
        INSERT INTO memoria_ram_swap (nombre, valor, unidad)
        VALUES (%s, %s, %s)
        """      
  
        cursor.execute(query, (nombre, valor, unidad))

        if nombre == "MemTotal":
            ramMem = int(valor)
        elif nombre == "MemAvailable":
            ramMem = ramMem - int(valor)
        elif nombre == "SwapTotal":
            swapMem = int(valor)
        elif nombre == "SwapFree":
            swapMem = swapMem - int(valor)


    cursor.execute("INSERT INTO memoria_ram_swap_history (ram, swap) VALUES (%s, %s)", (ramMem, swapMem))
  
    db.commit()
    cursor.close()
    print(str(datetime.now())+" | memoria_ram_swap actualizada.")