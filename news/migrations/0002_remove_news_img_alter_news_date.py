# Generated by Django 5.0 on 2024-01-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='img',
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
