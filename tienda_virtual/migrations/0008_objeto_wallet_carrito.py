# Generated by Django 4.2.3 on 2023-08-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_virtual', '0007_alter_message_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.CharField(max_length=50)),
                ('precio', models.IntegerField(null=True)),
                ('dueño', models.CharField(max_length=50)),
                ('foto', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='wallet',
            name='carrito',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
