# Generated by Django 3.0.6 on 2020-05-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200524_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marmita',
            name='hora_solicitacao',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
