# Generated by Django 5.1.1 on 2024-10-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('degree_title', models.CharField(max_length=150, verbose_name='Descripcion obtenido')),
                ('desccription', models.TextField(verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
            ],
            options={
                'verbose_name': 'formación',
                'verbose_name_plural': 'formaciones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('image', models.ImageField(upload_to='skills', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
            ],
            options={
                'verbose_name': 'conocimiento',
                'verbose_name_plural': 'conocimientos',
                'ordering': ['-created'],
            },
        ),
    ]
