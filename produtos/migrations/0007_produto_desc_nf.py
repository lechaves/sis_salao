# Generated by Django 3.2.5 on 2021-08-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20210815_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='desc_nf',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]