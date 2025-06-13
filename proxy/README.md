# Proxy

Proxy de acceso

Se debe modificar el archivo .env con parámetros deseados

### Despliegue local

1. Agregar `127.0.0.1 api.crehana.dev` a /etch/host
2. Instalar `bash scripts/installer.sh`

### Despliegue en servidor

1. Cambiar a NGINX_CONF=nossl en .env
2. Instalar `bash scripts/installer.sh`
3. Generar certificado `bash scripts/cert.sh`
4. Cambiar a NGINX_CONF=api en .env
5. Reiniciar proxy

##### NGINX_CONF

Posibles valores:

- nossl: Dominios sin ssl
- api: Configuración para servidor
