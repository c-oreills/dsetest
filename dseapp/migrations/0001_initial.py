# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-17 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dseapp.Parent'),
        ),
    ]
