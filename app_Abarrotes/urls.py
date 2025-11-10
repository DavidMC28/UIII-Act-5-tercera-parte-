from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para Empleados
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),
    
    # URLs para Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Ventas
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/actualizar/<int:pk>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/borrar/<int:pk>/', views.borrar_venta, name='borrar_venta'),
]