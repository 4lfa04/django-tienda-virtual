# Generated by Django 4.2.3 on 2023-08-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_virtual', '0010_alter_objeto_dueño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='foto',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
