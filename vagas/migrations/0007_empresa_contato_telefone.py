# Generated by Django 3.2.12 on 2022-05-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0006_empresa_contato_presencial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='contato_telefone',
            field=models.BooleanField(default=False, verbose_name='Contato por telefone'),
        ),
    ]