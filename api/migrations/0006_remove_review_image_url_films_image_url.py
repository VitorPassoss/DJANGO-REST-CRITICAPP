# Generated by Django 4.0 on 2023-04-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_review_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image_url',
        ),
        migrations.AddField(
            model_name='films',
            name='image_url',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
    ]
