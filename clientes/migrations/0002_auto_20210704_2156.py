# Generated by Django 3.2.5 on 2021-07-04 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='documento',
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_nasc',
            field=models.DateField(blank=True, null=True),
        ),
    ]