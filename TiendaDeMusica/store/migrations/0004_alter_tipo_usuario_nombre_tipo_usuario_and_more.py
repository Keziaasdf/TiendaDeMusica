# Generated by Django 4.0.4 on 2022-05-25 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_tipo_usuario_nombre_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_usuario',
            name='nombre_tipo_usuario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, on_delete=django.db.models.deletion.CASCADE, to='store.tipo_usuario'),
        ),
    ]