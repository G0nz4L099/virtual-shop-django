# 🛒 Virtual Shop - Proyecto Web con Django

Este proyecto es una **tienda virtual construida con Django + Bootstrap**, que permite a usuarios navegar productos, registrarse, agregar al carrito y realizar compras. También incluye panel de administración para el staff con reportes, dashboard y exportación de datos.

---

## 🚀 Funcionalidades principales

### 👤 Usuarios
- Registro de usuarios con:
  - Nombre de usuario
  - Edad
  - Email
  - Teléfono
- Inicio de sesión y cierre de sesión
- Edición de perfil y cambio de contraseña

### 🛍️ Catálogo de productos
- Vista estilo catálogo con tarjetas modernas
- Estilo oscuro con colores turquesa y fondo personalizado
- Imágenes de productos
- Agregar múltiples productos al carrito

### 🧺 Carrito de compras
- Vista personalizada y dinámica
- Eliminar productos antes de confirmar
- Confirmación de compra con animación (🛒 fadeout)

### 💻 Panel administrativo (solo staff)
- Ver ventas realizadas con opción de "Ver Detalle"
- Ver clientes registrados
- Exportar ventas y clientes a CSV
- Dashboard gráfico con Chart.js:
  - Ventas diarias de los últimos 30 días
  - Total de ingresos
  - Promedio por venta
  - Total de usuarios

### 💬 Reseñas
- Usuarios logueados pueden dejar reseñas desde la página de bienvenida

---

## 🖼️ Estética y diseño

- Basado en Bootstrap 5
- Tema oscuro + turquesa
- Fondos personalizados (`carrito.jpg`, `login.jpg`)
- Dashboard moderno con KPIs y gráfico animado
- Responsive (adaptado a dispositivos móviles)

---

## ⚙️ Tecnologías usadas

- Python 3
- Django 5
- Bootstrap 5
- Chart.js
- SweetAlert / animación CSS
- SQLite (base de datos por defecto)

---

## 📦 Cómo clonar este proyecto

```bash
git clone https://github.com/tu-usuario/virtual-shop-django.git
cd virtual-shop-django
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
