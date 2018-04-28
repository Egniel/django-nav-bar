# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-27 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_main', models.BooleanField(default=False)),
                ('slug', models.CharField(blank=True, max_length=64, null=True, verbose_name='slug')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('named_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='named URL')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='menu.Menu')),
            ],
            options={
                'verbose_name_plural': 'MenuItems',
                'verbose_name': 'MenuItem',
            },
        ),
    ]