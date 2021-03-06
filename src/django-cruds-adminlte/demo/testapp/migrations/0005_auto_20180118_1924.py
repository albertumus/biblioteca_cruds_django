# Generated by Django 2.0.1 on 2018-01-18 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20170421_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresses',
            options={'ordering': ('pk',), 'permissions': (('view_addresses', 'Can see available Addresses'),)},
        ),
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ('pk',), 'permissions': (('view_author', 'Can see available Authors'),)},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('pk',), 'permissions': (('view_customer', 'Can see available customers'),)},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('pk',), 'permissions': (('view_invoice', 'Can see available Invoices'),), 'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='line',
            options={'ordering': ('pk',), 'permissions': (('view_line', 'Can see available lines'),), 'verbose_name': 'Line', 'verbose_name_plural': 'Lines'},
        ),
    ]
