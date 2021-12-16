# Generated by Django 3.2.5 on 2021-11-05 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_auto_20210815_2222'),
        ('tabelasbasicas', '0002_rename_nome_tipopagamento_descricao'),
        ('notas_servicos', '0002_auto_20210317_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notaservico',
            name='descricao',
        ),
        migrations.AddField(
            model_name='notaservico',
            name='pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tabelasbasicas.tipopagamento'),
        ),
        migrations.AddField(
            model_name='notaservico',
            name='servicos',
            field=models.ManyToManyField(blank=True, null=True, to='servicos.Servico'),
        ),
        migrations.AlterField(
            model_name='notaservico',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.DeleteModel(
            name='ItemNotaServico',
        ),
    ]
