# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('number', models.IntegerField(verbose_name='Numer baterii')),
                ('on', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pojazd')),
            ],
        ),
        migrations.AddField(
            model_name='battery',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batteries', to='vehicle.Vehicle', verbose_name='Pojazd'),
        ),
    ]
