# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-28 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to=b'pictures/')),
                ('email', models.EmailField(max_length=254)),
                ('Area', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
