# Generated by Django 4.0.4 on 2022-05-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_tipo_usuario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_usuario',
            name='nombre_tipo_usuario',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Tipo de usuario'),
        ),
    ]
