# Generated by Django 5.1.3 on 2024-11-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0002_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]