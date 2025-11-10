from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Cliente, Venta
from .forms import EmpleadoForm, ClienteForm, VentaForm

def inicio(request):
    return render(request, 'inicio.html')

# ========== VISTAS PARA EMPLEADOS ==========
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/agregar_empleado.html', {'form': form})

def actualizar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/actualizar_empleado.html', {'form': form})

def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ========== VISTAS PARA CLIENTES ==========
def ver_clientes(request):
    clientes = Cliente.objects.all().select_related('id_empleado')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente/agregar_cliente.html', {'form': form})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/actualizar_cliente.html', {'form': form})

def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ========== VISTAS PARA VENTAS ==========
def ver_ventas(request):
    ventas = Venta.objects.all().select_related('id_cliente', 'id_empleado')
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

def agregar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_ventas')
    else:
        form = VentaForm()
    return render(request, 'venta/agregar_venta.html', {'form': form})

def actualizar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ver_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta/actualizar_venta.html', {'form': form})

def borrar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})