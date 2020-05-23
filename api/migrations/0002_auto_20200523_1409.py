# Generated by Django 3.0.6 on 2020-05-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=200)),
                ('rua', models.CharField(max_length=300)),
                ('numero', models.IntegerField(default=False)),
                ('apart', models.IntegerField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='quero_doar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(blank=True, max_length=14, verbose_name='tel'),
        ),
        migrations.AddField(
            model_name='user',
            name='endereco',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Endereco'),
            preserve_default=False,
        ),
    ]
