## API_SRE
* API para consumir datos desde una base


# Estructura de carpeta del respositorio:
├── api
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api_requests
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
└── manage.py

# Componentes o apps:
* api_requests: En esta app se encuentra el desarrollo del proyecto.
* views: Contamos con dos views las cuales se encargan de proporcionar los datos al cliente e insertar datos a la base.

# Tecnologias usadas:
* Python - DJango.
* Base de datos SQLite3, esto se puede reemplazar por otro motor de base de datos.
* Pruebas realizadas con Postman en el dasarrollo.
* Docker.

# Modelos creados:
* DataFly: El unico modelo creado. Esto se podria separar a futuro en otras trablas y refereciar los campos.
* Datos: Algunos estan creados en CharField por ej, las fechas. Pero esto se podria pasar a un campo de fecha propiamente.

# Rutas creadas para un cliente.
* /getdata: En esta ruta obtenemos todos los datos de la tabla.
* /putdata: En esta ruta podemos insertar nuevos datos a la tabla de ser necesario.


# Iniciar la API:
1. Ingresar al path: api y levantar django [python manage.py runserver]
2. Ingresar al path: api y levantar con Docker ejecutando /bin/bash installDocker.sh

# Base de datos:
La base de datos se encuentra en el path api bajo el nombre db.sqlite3

## Autor:
[LinkedIn - Ricardo Benitez](https://www.linkedin.com/in/roseabdev/)