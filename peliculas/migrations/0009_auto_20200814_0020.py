# Generated by Django 2.1.5 on 2020-08-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0008_auto_20200814_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.TimeField(),
        ),
    ]
