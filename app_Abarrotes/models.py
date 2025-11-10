from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    # Campo para la foto del empleado
    foto = models.ImageField(upload_to='empleados/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    fecha_compra = models.DateField(auto_now_add=True)
    direccion = models.TextField()
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='clientes_atendidos')
    
    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos_vendidos = models.TextField(help_text="Descripción de los productos vendidos")
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='ventas_realizadas')
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='compras_realizadas')
    
    def __str__(self):
        return f"Venta {self.id} - {self.fecha.strftime('%d/%m/%Y')} - ${self.total}"