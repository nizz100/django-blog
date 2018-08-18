# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-16 16:20
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='博客标题')),
                ('category', models.CharField(blank=True, max_length=20, verbose_name='博客类型')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('content', DjangoUeditor.models.UEditorField(blank=True, null=True, verbose_name='博文')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-pub_time'],
            },
        ),
    ]
