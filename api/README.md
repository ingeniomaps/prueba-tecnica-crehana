# Asignación de Tareas

Sistema de asignación de tareas a determinados usuarios.

### Configuración de entorno local

Uso recomendado con Docker

#### Validaciones y formateo de código

Si se usa un editor de código, descargar los complementos para

- Python
- Black
- Flake8
- REST client

Ejemplo de configuración para entorno VSCode:

```json
{
  "flake8.enabled": true,

  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

Uso manual

```sh
flake8 .
black .
```

### Despliegue de la aplicación

#### Despliegue sin Docker

- Requerimientos:

  - Python [tutorial](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
  - PostgreSQL [tutorial](https://www.hostinger.com/co/tutoriales/instalar-postgresql-ubuntu)

- Variables de entorno:
  Copiar el .env-template a .env y reemplazar las variables según su configuración

- Ejecutar el proyecto:

  ```sh
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  uvicorn main:app --host 0.0.0.0 --port 8080 --reload
  ```

#### Despliegue con Docker

- Requerimientos:

  - Docker [tutorial](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)

1. Cambiar los permisos de entrypint `chmod +x ./scripts/entrypoint.sh`
2. Instalar `bash ./scripts/installer.sh`
3. Agregar a /etc/hosts `127.0.0.1    api.crehana.dev`
4. Realizar consultas a la url `api.crehana.dev`

- Documentación del api: `https://api.crehana.dev/redoc`

### Testing

### Pruebas con solicitudes reales

Se genera una carpeta http que contiene todas las solicitudes permitidas en el sistema.

Para realizar pruebas solo abrir el archivo y ejecutar la consulta

- Requerimientos:
  - Rest Client
