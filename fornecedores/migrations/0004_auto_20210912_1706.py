# Generated by Django 3.2.5 on 2021-09-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0003_auto_20210912_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='endnumero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='estado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='ie',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
