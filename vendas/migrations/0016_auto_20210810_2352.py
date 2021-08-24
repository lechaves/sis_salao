# Generated by Django 3.2.5 on 2021-08-10 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0015_negociacaoparcela_datavecimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcelavenda',
            name='valorpago',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='data_criacao',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]