# core/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('guardar_reseña/', views.guardar_reseña, name='guardar_reseña'),
    path('', views.bienvenida, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('productos', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    #path('confirmar/', views.confirmar_compra, name='confirmar'),
    path('perfil/', views.perfil, name='perfil'),
    path('staf/clientes/', views.clientes_report, name='clientes_report'),
    path('staf/ventas/', views.ventas_report, name='ventas_report'),
    path('staf/venta/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('staff/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('exportar/clientes/', views.exportar_clientes_csv, name='exportar_clientes'),
    path('exportar/ventas/', views.exportar_ventas_csv, name='exportar_ventas')
    


]
