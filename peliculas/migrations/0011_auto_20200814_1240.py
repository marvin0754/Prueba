# Generated by Django 2.1.5 on 2020-08-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0010_auto_20200814_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]