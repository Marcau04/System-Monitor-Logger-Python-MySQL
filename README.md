# 📊 System-Monitor-Logger: Recolección y Persistencia de Métricas de Rendimiento

Este proyecto implementa un sistema completo de **monitorización de métricas de rendimiento** para un entorno **Linux**. La herramienta está desarrollada en **Python** y utiliza comandos del sistema operativo (`ps`, `vmstat`, `df`, `ping`, `cat /proc/meminfo`) y la librería `psutil` para la recolección de datos en tiempo real.

Toda la información recolectada se procesa y se almacena de forma persistente en una base de datos **MySQL**, permitiendo el análisis histórico del estado del sistema. El diseño utiliza **programación multihilo** para optimizar la recolección de métricas con diferentes frecuencias de actualización.

## 🛠️ Tecnologías Utilizadas

| Tecnología | Rol en el Proyecto |
| :--- | :--- |
| **Python 3** | Lenguaje principal de desarrollo y orquestación. |
| **MySQL** | Base de datos para la persistencia y análisis de todas las métricas. |
| **`psutil`** | Librería para obtener estadísticas de red (bytes y velocidad de transferencia). |
| **`subprocess`** | Ejecución de comandos nativos de Linux (`ps aux`, `vmstat`, `df -h`, `ping`, `cat /proc/meminfo`). |
| **`threading`** | Gestión de concurrencia para la ejecución de tareas con diferentes periodicidades. |
| **`mysql.connector`** | Módulo para la interacción y persistencia de datos en MySQL. |

## 📈 Métricas Recogidas y Almacenadas

El sistema está diseñado para capturar y registrar más de **12 tipos diferentes de métricas** del sistema, almacenadas en tablas dedicadas (ver `script.sql`):

### 💾 Procesos y CPU
* **Lista Detallada de Procesos** (`ps aux`): Usuario, PID, uso de CPU, uso de Memoria RAM/Virtual, Estado, Comando.
* **Número Total de Procesos** en ejecución.
* **Estadísticas de CPU**: Uso instantáneo (%), Frecuencia (MHz).

### 🌐 Red
* **Estadísticas de Red (Bytes)**: Total de bytes enviados y recibidos.
* **Velocidad de Transferencia**: Bytes/segundo enviados y recibidos.
* **Latencia de Red**: Tiempo de respuesta medio a un host externo (e.g., `google.com`) mediante `ping -c 50`.
* **Conexiones de Red**: Estado, Recv-Q, Send-Q, Dirección Local/Peer.
* **Errores de Red**: Errores de entrada/salida y descarte de paquetes.

### 🗃️ Memoria y Disco
* **Información Detallada de Memoria**: Valores de `/proc/meminfo` (MemTotal, SwapTotal, etc.).
* **Histórico de Uso de RAM y SWAP**.
* **Operaciones de E/S (I/O)**: Procesos esperando I/O, bloques de lectura/escritura, porcentaje de CPU esperando I/O (`vmstat`).
* **Espacio en Disco Disponible**: Espacio total disponible calculado a partir de la salida de `df -h`.

## ⚙️ Estructura y Concurrencia

El módulo principal (`main.py`) inicia **tres hilos** de ejecución para gestionar la recolección de forma eficiente:

1.  **`mainThdr`**: Ejecuta las métricas de alta frecuencia (Procesos, CPU, Memoria, I/O, Red Básica). **Frecuencia: Cada 5 segundos.**
2.  **`otherMThdr`**: Ejecuta las métricas más lentas o que requieren un periodo de medición (Latencia de Red, Velocidad de Transferencia). **Frecuencia: Cada 10 segundos.**
3.  **`delThdr`**: Mantenimiento de la base de datos (borrado de datos antiguos). **Frecuencia: Cada 120 segundos (2 minutos) para borrado de datos de hace más de 7 horas.**

## ▶️ Instrucciones de Uso (Configuración)

### 1. Configuración de la Base de Datos

1.  Instalar MySQL en el entorno local.
2.  Crear la base de datos y las tablas ejecutando el script SQL:
    ```bash
    mysql -u usuario -p < script.sql
    *(Nota: Asegúrate de que los credenciales de `sqlConnection.py` coincidan con tu configuración: `usuario`, `foe0004`, `practicas`)*.
    ```
### 2. Dependencias de Python

Instalar las librerías necesarias:
```bash
pip install mysql-connector-python psutil
```

### 3. Ejecución
Ejecutar el script principal para iniciar el servicio de monitorización:

```bash
python main.py
```

## 🧠 Aprendizajes Clave
Este proyecto demuestra experiencia en:

- Programación de Sistemas: Interacción y parsing de la salida de comandos nativos de sistemas operativos (subprocess).

- Concurrencia y Multihilo: Diseño de arquitectura concurrente en Python para gestionar tareas con diferentes temporizaciones (threading).

- Diseño de Bases de Datos (SQL): Diseño de un esquema normalizado para el registro de series temporales (más de 12 tablas).

- Integración de Servicios: Conexión y manipulación de datos entre Python y MySQL.

- Manejo de Librerías de Bajo Nivel: Uso de psutil para obtener estadísticas de sistema de forma programática.
