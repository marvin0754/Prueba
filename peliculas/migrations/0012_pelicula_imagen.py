# Generated by Django 2.1.5 on 2020-08-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0011_auto_20200814_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
