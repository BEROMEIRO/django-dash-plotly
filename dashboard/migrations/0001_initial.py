# Generated by Django 5.2 on 2025-04-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteRegiao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regiao', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VendaCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='VendaMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=10)),
                ('valor', models.FloatField()),
            ],
        ),
    ]
