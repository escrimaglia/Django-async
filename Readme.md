# Mixed Django

## Projecto Django que ejecuta funciones Sync y Async

### Servidor Gunicorn

Cuando es necesario ejecutar procesos Asyncs, no es sufuciente Gunicorn (solo soporta operaciones tipo sync, pues es un servidor WSGI), y por ende hay que utilizar un servidor tipo Uvicorn (servidor ASGI). Entonces, en un esenario donde haya que ejecutar tareas Syncs y Asyncs, se debe configurar Django para que use Gunicorn con workers de clase UvicornWorker, o si es posible, para que utilize directamente Uvicorn.

En el caso de usar Gunicorn, este actúa como el servidor maestro que coordina los workers y gestiona el ciclo de vida de los procesos. Ademas, distribuye las solicitudes entrantes a los workers según la configuración (cuantos workers y que clase `worker_class`).

### Uvicorn Worker

Cuando un worker de clase UvicornWorker recibe una solicitud, evalúa si la tarea es síncrona o asíncrona.

- Si la tareas es Sync (def), el worker ejecuta la tarea en un thread pool (un grupo de subprocesos) para evitar bloquear el bucle de eventos principal de asyncio.

- Si la tarea es Async (def async), el worker las ejecuta directamente dentro del bucle de eventos asyncio.

#### gunicorn.conf.py

Este es el archivo de configuración de Gunicorn. Aqui se especifican la cantidad de workers y el tipo de worker.

```
import multiprocessing
bind = "0.0.0.0:8000" #Todas las interfaces responden en el puerto 8000  
workers = multiprocessing.cpu_count() * 2 + 1  
worker_class = "uvicorn.workers.UvicornWorker" #Usa uvicorn para ASGI  
```

#### Ejecutar el servicio a traves de ./startserver.sh

`gunicorn mixedproject.asgi:application -c gunicorn.conf.py`

### Servidor Uvicorn

En el caso de que Django pueda ser utilizado directamente con el servidor HTTP Uvicorn, el servicio se ejecutrá de la siguiente manera:

`uvicorn mixedproject.asgi:appplication --reload`

Ed Scrimaglia
