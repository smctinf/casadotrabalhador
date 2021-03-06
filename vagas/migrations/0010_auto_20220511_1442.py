# Generated by Django 3.2.12 on 2022-05-11 17:42

from django.db import migrations, models
import vagas.validations


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0009_vaga_emprego_atribuicoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='observacao',
            field=models.TextField(blank=True, default='', verbose_name='Observações internas'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=11, validators=[vagas.validations.validate_TELEFONE], verbose_name='Whatsapp'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='endereco',
            field=models.CharField(blank=True, max_length=60, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, validators=[vagas.validations.validate_TELEFONE], verbose_name='Telefone'),
        ),
    ]
