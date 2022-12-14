# Generated by Django 4.1 on 2022-10-25 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='comprador_id',
            new_name='comprador',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='mensaje_id',
            new_name='mensaje',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='vendedor_id',
            new_name='vendedor',
        ),
        migrations.RenameField(
            model_name='producto_apartado',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='producto_apartado',
            old_name='vendedor_id',
            new_name='vendedor',
        ),
        migrations.AlterModelTable(
            name='chat',
            table='Chat',
        ),
        migrations.AlterModelTable(
            name='comprador',
            table='Comprador',
        ),
        migrations.AlterModelTable(
            name='mensaje',
            table='Mensaje',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='Producto',
        ),
        migrations.AlterModelTable(
            name='producto_apartado',
            table='Producto_apartado',
        ),
        migrations.AlterModelTable(
            name='vendedor',
            table='Vendedor',
        ),
    ]
