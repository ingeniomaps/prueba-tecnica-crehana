# Proxy de Acceso

Este proyecto proporciona un proxy de acceso configurable para entornos de desarrollo local o producción. Utiliza NGINX como servidor de proxy inverso y permite configurar certificados SSL de forma opcional.

---

### Requisitos

Antes de comenzar, asegúrate de tener:

- Docker

---

### Configuración Inicial

Edita el archivo `.env` con los parámetros deseados. Asegúrate de definir correctamente la variable `NGINX_CONF`, la cual controla el comportamiento de NGINX según el entorno:

| Valor   | Descripción                     |
| ------- | ------------------------------- |
| `nossl` | Para configuración sin HTTPS    |
| `api`   | Configuración del proxy con SSL |

---

### Despliegue Local

Sigue estos pasos para ejecutar:

1. Agrega la siguiente línea a tu archivo `/etc/hosts`:

   ```bash
   127.0.0.1      api.crehana.dev
   ```

2. Ejecuta el instalador:
   ```bash
   bash scripts/installer.sh
   ```

Se configurará con un certificado SSL local para emular el entorno de producción.

---

### Despliegue en Servidor (Producción)

Pasos recomendados para un despliegue seguro con certificado SSL:

1. Establece en `.env`:

   ```env
   NGINX_CONF=nossl
   ```

2. Ejecuta el instalador para configurar NGINX sin SSL:

   ```bash
   bash scripts/installer.sh
   ```

3. Genera el certificado SSL:

   ```bash
   bash scripts/cert.sh
   ```

4. Cambia nuevamente la configuración en `.env`:

   ```env
   NGINX_CONF=api
   ```

5. Reinicia el proxy:
   ```bash
   docker restart $container_name
   ```

---

### Verificación

Una vez desplegado, accede a:

- **Local**: `http://api.crehana.dev`
- **Producción**: DNS configurado

Verifica que los redireccionamientos, encabezados y certificados estén funcionando correctamente según la configuración.

---

### Anotaciones

- Si usas puertos estándar (80 y 443), asegúrate de que ningún otro servicio los esté ocupando.
- El dominio `api.crehana.dev` debe estar apuntando correctamente a tu servidor local o IP pública.

---

### Licencia

Este proyecto es solo para fines de evaluación técnica y no debe ser utilizado en producción sin ajustes adicionales.
