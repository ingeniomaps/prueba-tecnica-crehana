# Prueba Técnica - Crehana

Sistema modular para el control y gestión de tareas, desarrollado como parte de una prueba técnica. El sistema está estructurado en módulos independientes para facilitar su escalabilidad, mantenimiento y despliegue.

---

### Estructura del Proyecto

```
prueba-tecnica-crehana/
├── api/         # Servicio principal (FastAPI)
├── database/    # Definiciones y gestión de la base de datos
├── proxy/       # Controlador de solicitudes externas
└── README.md    # Documentación principal
```

### Descripción de los módulos:

- **`api/`**: Servicio principal desarrollado en Python con FastAPI. Contiene los endpoints y lógica de negocio.
- **`database/`**: Define la estructura de la base de datos y configuraciones relacionadas.
- **`proxy/`**: Se encarga del control y redirección de las solicitudes entrantes hacia los servicios correspondientes.

> Cada módulo incluye su propio `README.md` con instrucciones específicas de uso y despliegue.

---

### Despliegue Rápido

#### Requisitos

- [Docker](https://www.docker.com/) instalado.

#### Pasos para ejecutar

1. Accede al directorio del servicio principal:

   ```bash
   cd api/
   ```

2. Sigue las instrucciones del `README.md` ubicado dentro del directorio `api/` para construir y ejecutar el contenedor.

---

### Servidor de Pruebas

Puedes acceder a la documentación interactiva de la API (generada automáticamente por FastAPI) en el siguiente enlace:

🔗 [https://crehanaprueba.envpops.io/redoc](https://crehanaprueba.envpops.io/redoc)

---

### Licencia

Este proyecto es solo para fines de evaluación técnica y no debe ser utilizado en producción sin ajustes adicionales.
