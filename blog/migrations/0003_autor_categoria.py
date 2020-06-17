# Generated by Django 3.0.6 on 2020-06-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_auto_20200616_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres del autor')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos del autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria activada/desactivada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria activada/desactivada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
