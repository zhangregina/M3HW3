# Generated by Django 4.0 on 2021-12-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_film2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Film',
        ),
    ]
