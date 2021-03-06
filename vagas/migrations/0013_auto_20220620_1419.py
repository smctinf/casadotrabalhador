# Generated by Django 3.2.12 on 2022-06-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0012_alter_empresa_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga_emprego',
            name='carga_horaria',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vaga_emprego',
            name='regime',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vaga_emprego',
            name='salario',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vaga_emprego',
            name='tipo_de_vaga',
            field=models.CharField(choices=[('NML', 'Normal'), ('JAP', 'Jovem aprendiz'), ('PED', 'Pessoa com deficiência')], default='NML', max_length=3),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome do cargo'),
        ),
    ]
