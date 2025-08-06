# 🛒 Virtual Shop - Proyecto Web con Django

**Virtual Shop** es una tienda virtual desarrollada con Django + Bootstrap. Permite a los usuarios navegar productos, registrarse, agregar al carrito y realizar compras. Además, cuenta con un panel administrativo exclusivo para el staff que incluye reportes, dashboard visual y exportación de datos.

---

## 🚀 Funcionalidades principales

### 👤 Gestión de usuarios
- Registro con: nombre, edad, email y teléfono
- Inicio y cierre de sesión
- Edición de perfil y cambio de contraseña
- Visualización del historial de compras
- Imagen de perfil y dirección de envío

### 🛍️ Catálogo de productos
- Vista estilo catálogo con tarjetas modernas
- Estética oscura y profesional con detalles en turquesa
- Búsqueda dinámica de productos por nombre y descripción
- Agregar múltiples productos al carrito

### 🧺 Carrito de compras
- Vista clara y responsiva
- Eliminar productos antes de confirmar
- Validación de stock
- Confirmación de compra que genera una venta

### 💼 Panel administrativo (solo staff)
- Listado de ventas con opción de "Ver Detalle"
- Listado de clientes registrados
- Filtros por fecha y precio en reportes de ventas
- Exportación de ventas y clientes a CSV
- Dashboard interactivo con Chart.js:
  - Ventas diarias (últimos 30 días)
  - Total de ingresos
  - Promedio por venta
  - Total de usuarios registrados

### 💬 Reseñas
- Usuarios autenticados pueden dejar reseñas públicas desde la pantalla de bienvenida

### 🖼️ Estética general
- Tema oscuro + turquesa
- Fondos personalizados (carrito, login, etc.)
- Estilo responsive (apto para dispositivos móviles)

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Django 5
- Bootstrap 5
- Chart.js
- SweetAlert / animación CSS
- SQLite (base de datos por defecto)

---

---

## IMPORTANTE 

1-Abrí el archivo virtualshop/settings.py

2-Cambiá esta línea: DEBUG = True por DEBUG=False 
        ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

3- guardar y ejecutar para ver el manejo de error404 correctamente 


## 📦 Instrucciones para correr el proyecto localmente

```bash
git clone https://github.com/G0nz4L099/virtual-shop-django.git
cd virtual-shop-django
python -m venv venv
venv\Scripts\activate         # En Windows
# source venv/bin/activate   # En Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

