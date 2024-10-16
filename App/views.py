from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import ContactForm, RegisterForm, ServiceForm
from django.contrib import messages
from .models import Service, Contact
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
from App.cart import Cart


#desde acá dejando la cagá xd
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse, JsonResponse #pruebas Paypal
from paypal.standard.forms import PayPalPaymentsForm
from paypalrestsdk import Payment
import paypalrestsdk
import logging

# Create your views here.

#Inicio
def home (request):
    return render(request, 'app/home.html') 

#Contacto
def contact (request):
    return render(request, 'app/contact.html')

#Servicios
def services (request):
    service = Service.objects.all()
    return render(request, 'app/services.html', {'services':service})

#Reserva
def reserve (request):
    services = Service.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(services, 5)
        services = paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity':services,
        'paginator':paginator
    }
    return render(request, 'app/reserve.html', data)

#Comprar
def pay (request):
    return render (request, 'app/pay.html')

#Registro
def register(request):
    data = {
        'form':RegisterForm
    }
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Succesful registration!")
            return redirect(to='home')
        else:
            data['form'] = form
    return render(request, 'registration/register.html', data)

#Login
def logIn(request):
    return render(request, 'accounts/login.html')

#Contacto
def contact(request):
    data = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Submitted form")
        else:
            data['form'] = form
    return render(request, 'app/contact.html', data)

#Agregar Servicio
@permission_required('app.add_service')
def add (request):
    data = {
        'form': ServiceForm()
    }
    if request.method == 'POST':
        form = ServiceForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service added succesfully")
        else:
            data['form'] = form
    return render(request, 'app/crud/add.html', data)

#Listar
@permission_required('app.view_service')
@permission_required( 'app.view_contact')
def list(request):
    contacts = Contact.objects.all()
    services = Service.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(services, 5)
        services = paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity':services,
        'entity2':contacts,
        'paginator':paginator
    }
    return render(request, 'app/crud/list.html', data)

#Modificar
@permission_required('app.change_service')
def modify(request, id):
    service = get_object_or_404(Service, id=id)
    data = {
        'form': ServiceForm(instance=service)
    }    
    if request.method == 'POST':
        form = ServiceForm(data=request.POST,instance=service ,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service modified succesfully")
            return redirect(to="list")
        else:
            data['form'] = form
    return render(request, 'app/crud/modify.html', data)

#Eliminar
@permission_required('app.delete_service')
def delete(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    messages.success(request, "Service deleted succesfully")
    return redirect(to="list")


#Carrito
def add_service(request, service_id):
    cart = Cart(request)
    service = Service.objects.get(id=service_id)
    cart.add_service(service)
    return redirect("reserve")

def delete_service(request, service_id):
    cart = Cart(request)
    service = Service.objects.get(id=service_id)
    cart.delete_service(service)
    return redirect("reserve")

def subtract_service(request, service_id):
    cart = Cart(request)
    service = Service.objects.get(id=service_id)
    cart.subtract(service)
    return redirect("reserve")

def clean_cart(request):
    cart = Cart(request)
    cart.clean()
    return redirect("reserve")