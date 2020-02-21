# Generated by Django 3.0.3 on 2020-02-21 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0006_auto_20200220_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='apellidos',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='client',
            name='shipping_way',
            field=models.CharField(choices=[('E', 'Email'), ('F', 'Fisico'), ('L', 'Linea')], default='L', max_length=1, null=True),
        ),
    ]
