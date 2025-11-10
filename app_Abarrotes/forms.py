from django import forms
from .models import Empleado, Cliente, Venta

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ingrese la dirección completa...'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+52 123 456 7890'}),
        }
        labels = {
            'id_empleado': 'Empleado Asignado',
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'productos_vendidos': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Describa los productos vendidos, cantidades y precios...'
            }),
            'total': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }
        labels = {
            'id_empleado': 'Empleado que realizó la venta',
            'id_cliente': 'Cliente',
            'productos_vendidos': 'Descripción de Productos Vendidos',
        }