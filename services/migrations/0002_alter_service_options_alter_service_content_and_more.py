# Generated by Django 4.0.2 on 2022-02-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización'),
        ),
    ]
