# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_bookwithchapters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parent'),
        ),
    ]