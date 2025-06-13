# DECISION_LOG.md

## 0002 - 2025-06-12 - Desacoplamiento de servicios

### Contexto

Estructurar el proyecto en servicios separados

### Decisión

Manejar cada servicio por separado:

- `project` → Proyecto principal
- `proxy` → Intermediario de solicitudes
- `database` → Base de datos

### Consecuencias

- Mayor modulación y escalabilidad
- Lógica separada
- Emulación de una arquitectura casi similar a un entorno de producción

---

## 0001 - 2025-06-12 - Estructura hexagonal por módulos (Domain/Application/API)

### Contexto

Se quiere escalar el proyecto y separar responsabilidades.

### Decisión

Estructura por módulos, cada uno con:

- `domain/` → Entidades, interfaces
- `application/` → Casos de uso, servicios
- `api/` → Endpoints

### Consecuencias

- Modularized alta

---
