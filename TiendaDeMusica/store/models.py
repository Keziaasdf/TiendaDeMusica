from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    instrument_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.instrument_name

class Tipo_usuario(models.Model):
    TIPE_CHOICES = (
        ('GERENTE', 'GERENTE'),
        ('VENDEDOR', 'VENDEDOR'),
        ('BODEGUERO', 'BODEGUERO'),
        ('CONTADOR', 'CONTADOR'),
    )
    
    id_tipo_usuario = models.IntegerField
    nombre_tipo_usuario = models.CharField('Tipo de Usuario', max_length=10, choices=TIPE_CHOICES)
    descripcion_tipo_usuario = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_tipo_usuario
    
    class Meta:
        verbose_name = 'Tipo de Usuario'
        verbose_name_plural = 'Tipos de Usuarios'
        unique_together = ('nombre_tipo_usuario','descripcion_tipo_usuario')
    

class Usuario(models.Model):
    
    code_id_usuario = models.AutoField(primary_key=True)
    rut_usuario = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    correo_usuario = models.EmailField(max_length=50)
    contrasena_usuario = models.CharField(max_length=50)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Todos los usuarios'
        unique_together = ('rut_usuario',)
    
    def __str__(self):
        return self.nombre_usuario + ' ' + str(self.tipo_usuario)
    
