# Generated by Django 2.2.1 on 2020-01-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
