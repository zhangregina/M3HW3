# Generated by Django 4.0 on 2021-12-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_film2', '0002_series_delete_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(upload_to='series/'),
        ),
    ]