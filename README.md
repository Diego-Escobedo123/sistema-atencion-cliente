# Sistema de Atención al Cliente — Help Desk

Sistema de gestión de tickets de soporte al cliente implementado con una Priority Queue como estructura de datos principal. Los tickets se atienden según su nivel de urgencia, garantizando que los casos más críticos sean resueltos primero.

## Estructura de datos: Priority Queue

La Priority Queue está implementada desde cero usando una **lista enlazada ordenada**. Cada nodo de la lista es un objeto `Ticket` con los atributos `ticket_id`, `client`, `description`, `priority` y `next`.

### Reglas
- Un ticket con mayor prioridad (número menor) es atendido antes que uno con menor prioridad.
- Si dos tickets tienen la misma prioridad, se respeta el orden de llegada (FCFS).

### Complejidad temporal de los métodos

| Método | Complejidad | Descripción |
|---|---|---|
| `insert` | O(n) | Recorre la lista para insertar en la posición correcta |
| `delete` | O(1) | El ticket de mayor prioridad siempre está al inicio |
| `search` | O(n) | Recorre la lista buscando el ticket por su ID |
| `update_priority` | O(n) | Elimina el ticket y lo reinserta con la nueva prioridad |
| `is_empty` | O(1) | Verifica si `start` es `None` |
| `peek` | O(1) | Retorna el primer nodo sin eliminarlo |

## Funcionalidades

1. **Agregar ticket** — registra un nuevo ticket con nombre del cliente, descripción y nivel de prioridad.
2. **Atender siguiente** — atiende el ticket de mayor prioridad y lo mueve al historial.
3. **Ver cola** — muestra todos los tickets pendientes ordenados por prioridad.
4. **Buscar ticket** — busca un ticket por su ID.
5. **Actualizar prioridad** — escala o reduce la prioridad de un ticket existente y lo reubica en la cola.

## Tecnologías

- Python 3
- Flask
- Bootstrap 5

## Estructura del proyecto

```
sistema-atencion-cliente/
├── ticket.py               # Modelo del ticket (nodo de la lista)
├── priority_queue.py       # Implementación de la Priority Queue
├── helpdesk.py             # Lógica del negocio
├── app.py                  # Servidor Flask y rutas
├── tests/
│   └── test_priority_queue.py
├── static/
│   └── js/
│       └── app.js
└── templates/
    └── index.html
```

## Cómo correr el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/Diego-Escobedo123/sistema-atencion-cliente.git
cd sistema-atencion-cliente
```

### 2. Instalar dependencias
```bash
pip install flask
```

### 3. Correr la aplicación
```bash
python app.py
```

### 4. Abrir en el navegador
```
http://127.0.0.1:5000
```

## Correr los tests
```bash
python -m pytest tests/test_priority_queue.py -v
```