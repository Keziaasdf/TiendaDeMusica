# Generated by Django 4.0.4 on 2022-05-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_usuario_id_alter_usuario_code_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut_usuario',
            field=models.CharField(max_length=10),
        ),
    ]
