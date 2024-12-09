# Mixed Django

## Projecto Django que ejecuta funciones Sync y Async

### Procesos Sync

Para los procesos Syncs, se utliza Gunicorn, pues esta construido para eso.

### Procesos Async

Para los procesos Asyncs, se utiliza Uvicorn. Aunque este puede ejectar tambien procesos syncs, no es eficiente como lo es un servidor especifico como Gunicorn.

Uvicorn ejecuta los procesos Syncs en un hilo separado no bloqueante (Simula un Non-blocking Async), pero segun la documentacion, ejecutar procesos síncronos en Uvicorn introduce un ligero overhead porque cada operación bloqueante se delega a un thread (Non-blocking Async), lo que puede reducir el rendimiento en comparación con un servidor optimizado para WSGI, como Gunicorn en modo síncrono.

### Uvicorn Worker

Finalmente, el servidor que se ejecuta para mapear todos los paths es Gunicorn, y Uvicorn corre como un worker para ejecutar especificamente las peticiones async

#### gunicorn.conf.py

import multiprocessing

bind = "0.0.0.0:8000" #Todas las interfaces responden en el puerto 8000  
workers = multiprocessing.cpu_count() * 2 + 1  
worker_class = "uvicorn.workers.UvicornWorker" #Usa uvicorn para ASGI  

#### Ejecutar el servicio a traves de ./startserver.sh

Ed Scrimaglia
