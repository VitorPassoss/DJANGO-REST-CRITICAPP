# Generated by Django 4.0 on 2023-05-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_films_description_alter_films_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='description',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='films',
            name='image_url',
            field=models.CharField(max_length=350),
        ),
    ]
