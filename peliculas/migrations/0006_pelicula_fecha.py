# Generated by Django 2.1.5 on 2020-08-14 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0005_auto_20200813_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
