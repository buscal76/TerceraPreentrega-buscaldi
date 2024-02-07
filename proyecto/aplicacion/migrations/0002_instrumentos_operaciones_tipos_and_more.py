# Generated by Django 5.0.1 on 2024-02-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=6)),
                ('tipo', models.CharField(max_length=6)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('nominales', models.CharField(max_length=50)),
                ('ticker', models.CharField(max_length=6)),
                ('fecha', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
                ('renta', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Profesor',
            new_name='Usuarios',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]