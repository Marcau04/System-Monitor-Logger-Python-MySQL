CREATE DATABASE practicas;

USE practicas;

DROP TABLE lista_procesos;
-- Guarda informacion detallada sobre los procesos en ejecucion en el sistema
CREATE TABLE lista_procesos (
    user LONGTEXT,                              -- Usuario que ejecuta el proceso
    pid INT(10) DEFAULT '0',                    -- ID del proceso
    cpu FLOAT(10) DEFAULT '0.0',                -- Carga de CPU empleada por ese proceso
    mem FLOAT(10) DEFAULT '0.0',                -- Memoria empleada por ese proceso
    virtual_memsize INT(100) DEFAULT '0',       -- Tamaño de la memoria virtual de ese proceso
    resident_memsize INT(100) DEFAULT '0',      -- Cantidad de la memoria RAM empleada
    terminal_associated LONGTEXT DEFAULT '?',   -- Terminal asociada al proceso
    p_state LONGTEXT,                           -- Estado del proceso
    p_start_time LONGTEXT,                      -- Fecha y hora de inicio del proceso
    p_time LONGTEXT,                            -- Tiempo de ejecucion del proceso
    command LONGTEXT,                           -- Comando asociado
    `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP() -- Instante de tiempo cuando se realiza la medicion
);

DROP TABLE numero_procesos;
-- Almacena el numero de procesos en un instante determinado de tiempo
CREATE TABLE numero_procesos (
    procesos INT(10) DEFAULT '0',                -- Numero de procesos
    `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP() -- Instante de tiempo cuando se realiza la medicion
);

DROP TABLE estadisticas_red;
--Guardamos informacion sobre los Bytes (enviados y recibidos) en un instante de tiempo
CREATE TABLE estadisticas_red (
    bytes_enviados BIGINT,                          --Bytes enviados
    bytes_recibidos BIGINT,                         --Bytes recibidos
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()      --Instante de tiempo en el que se reciben
);

DROP TABLE operaciones_IO;
CREATE TABLE operaciones_IO (
    ioProcess INT(10),                              --Numero de procesos en espera de E/S
    read_blocks_fromDisk INT(10),                   --Numero de bloques recibidos de dispositivos
    write_blocks_toDisk INT(10),                    --Numero de bloques enviados a dispositivos
    cpuTimeWaitingIO INT(10),                       --Procentaje de CPU esperando por operaciones E/S
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

DROP TABLE cpu_Stats;
-- Guarda informacion relevante acerca del uso de la CPU
CREATE TABLE cpu_Stats (
    uso_cpu REAL,                               -- Uso instantaneo de la CPU (%)
    frec_cpu REAL,                              -- Frecuencia instantanea de la CPU (MHz)
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()  -- Instante de tiempo cuando se realiza la medicion
);

DROP TABLE memoria_ram_swap;
CREATE TABLE memoria_ram_swap (
    nombre VARCHAR(255),                         -- Nombre de la métrica (por ejemplo, MemTotal, SwapTotal, etc.)
    valor LONGTEXT,                                   -- Valor de la métrica (por ejemplo, la cantidad de memoria en KB)
    unidad VARCHAR(50),                           -- Unidad de la métrica (por ejemplo, KB, MB, etc.)
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

DROP TABLE conexiones_red;
CREATE TABLE conexiones_red (
    estado VARCHAR(10),                          -- Estado de la conexión (LISTEN, UNCONN, etc.)
    recv_q INT(10),                                  -- Recv-Q (Número de bytes pendientes en la cola de recepción)
    send_q INT(10),                                  -- Send-Q (Número de bytes pendientes en la cola de envío)
    direccion_local VARCHAR(50),                 -- Dirección local (ej. 127.0.0.1:puerto)
    direccion_peer VARCHAR(50),                   -- Dirección del peer (ej. 0.0.0.0:* o [::]:*)
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

DROP TABLE numero_conexiones;
CREATE TABLE numero_conexiones (
    conexiones INT(10),                               -- Número total de conexiones activas
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

DROP TABLE memoria_ram_swap_history;
-- Cantidad de memoria RAM y SWAP que se emplea en un determinado instante
CREATE TABLE memoria_ram_swap_history (
    ram INT(10),                                -- Cantidad de RAM (KB)
    swap INT(10),                               -- Cantidad de SWAP (KB)
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()  -- Instante de tiempo cuando se realiza la medicion
);

DROP TABLE errores_red;
--Guardamos informacion sobre los errores de red que suceden
CREATE TABLE errores_red (
    errin BIGINT,                                   --Errores de entrada
    errout BIGINT,                                  --Errores de salida
    dropin BIGINT,                                  --Descartes de paquetes de entrada
    dropout BIGINT,                                 --Descartes de paquetes de salida
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()      --Instante de tiempo en el que suceden
);

DROP TABLE espacio_disponible;
CREATE TABLE espacio_disponible (
    total_available FLOAT(20),                      --Espacio disponible total 
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

DROP TABLE latency_in_networking;
CREATE TABLE latency_in_networking (
    average_times FLOAT(10),                        --Tiempo de respuesta medio en milisegundos
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

DROP TABLE velocidad_transferencia;
--Medimos los Bytes/s que transfieren la red
CREATE TABLE velocidad_transferencia (
    bytes_enviados_por_segundo FLOAT,               --B/s de enviados
    bytes_recibidos_por_segundo FLOAT,              --B/s recibidos
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP()      --Instante de tiempo en el que se reciben los B/s
);