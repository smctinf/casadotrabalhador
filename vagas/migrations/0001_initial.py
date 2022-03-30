# Generated by Django 3.2.12 on 2022-03-16 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vagas.validations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga_Emprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('quantidadeVagas', models.IntegerField(verbose_name='Quantidade de vagas')),
                ('vaga', models.CharField(max_length=60)),
                ('empresa', models.CharField(max_length=60)),
                ('cnpj', models.CharField(max_length=60, validators=[vagas.validations.validate_CNPJ], verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=60, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=11)),
                ('escolaridade', models.CharField(max_length=60)),
                ('experiencia', models.CharField(choices=[('s', 'Sim'), ('n', 'Não')], max_length=1, verbose_name='Experiência')),
                ('formaDeContato', models.CharField(max_length=60, verbose_name='Forma de contato')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vaga de Emprego',
                'verbose_name_plural': 'Vagas de Emprego',
                'ordering': ['empresa'],
            },
        ),
    ]
