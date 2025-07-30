from django.shortcuts import render

# Create your views here.

# core/views.py


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, ItemCarrito, Cliente, DetalleVenta, Venta , Reseña , DireccionEnvio
from .forms import RegistroForm, AgregarAlCarritoForm




def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('productos')
    else:
        form = RegistroForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def productos(request):
    productos = Producto.objects.all()
    form = AgregarAlCarritoForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para agregar productos al carrito.')
            return redirect('login')

        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            producto = Producto.objects.get(id=form.cleaned_data['producto_id'])
            cantidad = form.cleaned_data['cantidad']

            if cantidad > producto.stock:
                messages.error(request, 'No hay suficiente stock disponible.')
                return redirect('productos')

            carrito, _ = Carrito.objects.get_or_create(cliente=request.user)

            item = ItemCarrito.objects.filter(carrito=carrito, producto=producto).first()
            if item:
                item.cantidad += cantidad
                item.save()
            else:
                ItemCarrito.objects.create(carrito=carrito, producto=producto, cantidad=cantidad)

            messages.success(request, f'Se agregó "{producto.nombre}" al carrito.')
            return redirect('productos')

    return render(request, 'core/productos.html', {
        'productos': productos,
        'form': form
    })

@login_required
def carrito(request):
    carrito, _ = Carrito.objects.get_or_create(cliente=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)

    if request.method == 'POST':
        if 'eliminar' in request.POST:
            item_id = request.POST.get('item_id')
            ItemCarrito.objects.filter(id=item_id).delete()
            return redirect('carrito')

        elif 'confirmar' in request.POST:
            if not items:
                messages.warning(request, 'No hay productos en el carrito.')
                return redirect('carrito')

            venta = Venta.objects.create(cliente=request.user, total=total)

            for item in items:
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=item.producto,
                    cantidad=item.cantidad
                )
                item.producto.stock -= item.cantidad
                item.producto.save()

            items.delete()  # Vaciar el carrito
            messages.success(request, 'Compra confirmada correctamente.')
            return redirect('productos')

    return render(request, 'core/carrito.html', {
        'items': items,
        'total': total
    })




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import DireccionEnvio
import os

@login_required
def perfil(request):
    user = request.user

    direccion_envio = DireccionEnvio.objects.filter(cliente=user).first()

    if request.method == 'POST':
        # Actualizar datos personales
        user.first_name = request.POST.get('nombre', user.first_name)
        user.last_name = request.POST.get('apellido', user.last_name)
        user.edad = request.POST.get('edad', user.edad)
        user.telefono = request.POST.get('telefono', user.telefono)
        user.email = request.POST.get('email', user.email)

        # Procesar foto si se subió
        nueva_foto = request.FILES.get('foto')
        if nueva_foto:
            # Eliminar imagen anterior si existe
            if user.foto and hasattr(user.foto, 'path') and os.path.isfile(user.foto.path):
                os.remove(user.foto.path)

            user.foto = nueva_foto

        user.save()

        # Dirección de envío
        if not direccion_envio:
            direccion_envio = DireccionEnvio(cliente=user)

        direccion_envio.pais = request.POST.get('pais', direccion_envio.pais)
        direccion_envio.provincia = request.POST.get('provincia', direccion_envio.provincia)
        direccion_envio.ciudad = request.POST.get('ciudad', direccion_envio.ciudad)
        direccion_envio.codigo_postal = request.POST.get('codigo_postal', direccion_envio.codigo_postal)
        direccion_envio.calle = request.POST.get('calle', direccion_envio.calle)
        direccion_envio.numero = request.POST.get('numero', direccion_envio.numero)
        direccion_envio.casa_depto = request.POST.get('casa_depto', direccion_envio.casa_depto)
        direccion_envio.piso = request.POST.get('piso', direccion_envio.piso)
        direccion_envio.save()

        messages.success(request, "Perfil actualizado correctamente.")
        return redirect('perfil')

    ventas = Venta.objects.filter(cliente=user).order_by('-fecha')
    total_gastado = sum(venta.total for venta in ventas)

    return render(request, 'core/perfil.html', {
        'direccion_envio': direccion_envio,
        'ventas': ventas,
        'total_gastado': total_gastado,
    })




from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def clientes_report(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/admin_clientes.html', {'clientes': clientes})

@staff_member_required
def ventas_report(request):
    ventas = Venta.objects.all().order_by('fecha')
    return render(request, 'core/admin_ventas.html', {'ventas': ventas})

@staff_member_required
def detalle_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'core/admin_detalle_venta.html', {
        'venta': venta,
        'detalles': detalles
    })



def bienvenida(request):
    return render(request, 'core/bienvenida.html')





from django.shortcuts import redirect
from .models import Reseña
from django.contrib import messages

@login_required
def guardar_reseña(request):
    if request.method == 'POST':
        contenido = request.POST.get('reseña')
        if contenido:
            Reseña.objects.create(usuario=request.user, contenido=contenido)
            messages.success(request, '¡Gracias por tu reseña!')
        else:
            messages.warning(request, 'La reseña no puede estar vacía.')
    return redirect('inicio')




from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.db.models.functions import TruncDay
from .models import Venta
import json
from datetime import datetime, timedelta 
from django.utils.timezone import now 
from django.utils import timezone


@staff_member_required
def admin_dashboard(request):
    ventas = Venta.objects.filter(fecha__gte=timezone.now() - timedelta(days=30))

    total_ventas = ventas.count()
    total_ingresos = ventas.aggregate(total=Sum('total'))['total'] or 0
    promedio_venta = round(total_ingresos / total_ventas, 2) if total_ventas > 0 else 0


    ventas_por_dia = ventas.annotate(day=TruncDay('fecha')).values('day').annotate(total_dia=Sum('total')).order_by('day')

    labels = [v["day"].strftime("%d-%m") for v in ventas_por_dia]
    datos = [float(v["total_dia"]) for v in ventas_por_dia]

    total_usuarios = Cliente.objects.count()  #  Nuevo KPI

    context = {
        'total_ventas': total_ventas,
        'total_ingresos': total_ingresos,
        'promedio_venta': promedio_venta,
        'labels': json.dumps(labels),
        'datos': json.dumps(datos),
        'total_usuarios': total_usuarios,  #  Pasarlo al template
    }

    return render(request, 'core/admin_dashboard.html', context)


import csv
from django.http import HttpResponse


def exportar_clientes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Edad', 'Teléfono', 'Fecha de Registro'])

    for cliente in Cliente.objects.all():
        writer.writerow([
            cliente.username,
            cliente.email,
            cliente.edad,
            cliente.telefono,
            cliente.fecha_registro.strftime("%Y-%m-%d %H:%M")
        ])

    return response




def exportar_ventas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ventas.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID Venta', 'Cliente', 'Total', 'Fecha'])

    for venta in Venta.objects.all():
        writer.writerow([
            venta.id,
            venta.cliente.username,
            venta.total,
            venta.fecha.strftime("%Y-%m-%d %H:%M")
        ])

    return response
