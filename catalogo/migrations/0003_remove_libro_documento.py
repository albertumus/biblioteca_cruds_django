# Generated by Django 2.2.1 on 2020-01-22 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_libro_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='documento',
        ),
    ]