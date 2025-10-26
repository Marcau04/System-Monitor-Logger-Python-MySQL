import threading
from time import sleep

from listaProcesos import getPsList
from netStats import getNetworkStats
from IOOperation import getIOOp
from cpuStats import updateCpuStats
from memoriaRamYSwap import get_memory_info
from conexiones import getConnections
from erroresRed import getNetworkErrors
from espacioDisco import getED
from latenciaRed import getLN
from velocidadRed import getTransferSpeed
from borrarDatosAntiguos import deleteOld

def main():
    #A traves de un bucle vamos obteniendo los datos necesarios (la información se actualiza cada 5 segundos)
    while True:
        getPsList()  #Obtener el listado de procesos
        getNetworkStats() #Obtener las estadisticas de red (Bytes entrada/salida)
        getIOOp() #Obtener las operaciones de entrada/salida
        updateCpuStats() #Actualizar las estadisticas de CPU (uso y frecuencia de CPU)
        get_memory_info() #Obtener informacion de la memoria RAM y SWAP
        getConnections() #Obtener informacion de las conexiones (Estado, numero de bytes en cola de recepcion/envio...)
        getNetworkErrors()#Obtener errores de red (errores de entrada, de salida, descartes de paquetes...)
        getED() #Obtener el espacio en disco

        sleep(5)

def delete():
    #Vamos borrando los datos de la base de datos con un intervalo de 7 horas
    while True:
        deleteOld() #Borramos datos fuera de rango (de hace mas de 7 horas)
        sleep(120)


def otherMetrics(): 
    # Utilizado para las metricas que tardan demasiado y emplean una temporizacion diferente (latencia pej)
    while True:
        getLN() #Obtener la latencia de red en un instante determinado

        #Obtener la velocidad de transferencia
        transferSpeed = threading.Thread(target = getTransferSpeed)
        transferSpeed.start()

        sleep(10)

if __name__ == "__main__":

    # Creamos tres hilos, cada uno ejecutará una funcion diferente
    mainThdr = threading.Thread(target = main) # Hilo que ejecutara la función main()
    delThdr = threading.Thread(target = delete) # Hilo que ejecutará la función delete()
    otherMThdr = threading.Thread(target = otherMetrics) #Hilo que ejecutara otherMetrics

    #Iniciamos los hilos
    mainThdr.start()
    delThdr.start()
    otherMThdr.start()

    # Esperamos a que cada hilo termine antes de continuar con el codigo principal
    mainThdr.join()
    delThdr.join()
    otherMThdr.join()
    