
from django.contrib import admin
from .models import Empleado, Cliente, Venta

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'puesto', 'salario', 'fecha_contratacion']
    list_filter = ['puesto', 'fecha_contratacion']
    search_fields = ['nombre', 'apellido', 'puesto']
    list_per_page = 20

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo', 'fecha_compra', 'id_empleado']
    list_filter = ['fecha_compra', 'id_empleado']
    search_fields = ['nombre', 'telefono', 'correo']
    list_per_page = 20

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'total', 'id_cliente', 'id_empleado']
    list_filter = ['fecha', 'id_empleado']
    search_fields = ['id_cliente__nombre', 'id_empleado__nombre', 'productos_vendidos']
    list_per_page = 20
    date_hierarchy = 'fecha'