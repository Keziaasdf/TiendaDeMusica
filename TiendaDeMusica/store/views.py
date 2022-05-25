from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Category, Product, Usuario

def all_products(request):
    products = Product.objects.all()
    return render(request,'store/home.html', {'products': products})

class CreateUser(CreateView):
    model = Usuario
    template_name = "user/register.html"
    fields = [
        'nombre_usuario',
        'apellido_usuario',
        'rut_usuario',
        'correo_usuario',
        'contrasena_usuario',
        'tipo_usuario',
    ]
    success_url = reverse_lazy('store:all_products')
    
    def form_valid(self, form):
        #logica del proceso
        usuario = form.save()
        usuario.save()
        return super(CreateUser, self).form_valid(form)
