# Generated by Django 3.2.5 on 2021-10-23 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CategoriaProd',
                'verbose_name_plural': 'CategoriasProd',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='tienda/productos')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoriaproductos')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
