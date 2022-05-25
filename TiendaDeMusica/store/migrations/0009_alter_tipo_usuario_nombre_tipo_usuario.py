# Generated by Django 4.0.4 on 2022-05-25 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_tipo_usuario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_usuario',
            name='nombre_tipo_usuario',
            field=models.CharField(choices=[('GERENTE', 'GERENTE'), ('VENDEDOR', 'VENDEDOR'), ('BODEGUERO', 'BODEGUERO'), ('CONTADOR', 'CONTADOR')], max_length=10, verbose_name='Tipo de Usuario'),
        ),
    ]
