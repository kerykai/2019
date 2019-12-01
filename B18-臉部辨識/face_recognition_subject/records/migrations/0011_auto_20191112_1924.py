# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-12 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20191019_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='Department',
            field=models.CharField(max_length=150, null=True, verbose_name='系所'),
        ),
        migrations.AlterField(
            model_name='records',
            name='Introduction',
            field=models.TextField(verbose_name='個人介紹'),
        ),
        migrations.AlterField(
            model_name='records',
            name='Picture',
            field=models.ImageField(blank=True, default='', upload_to='', verbose_name='個人圖片'),
        ),
        migrations.AlterField(
            model_name='records',
            name='address',
            field=models.CharField(max_length=50, null=True, verbose_name='住址'),
        ),
        migrations.AlterField(
            model_name='records',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='姓'),
        ),
        migrations.AlterField(
            model_name='records',
            name='grade',
            field=models.CharField(max_length=150, null=True, verbose_name='年級'),
        ),
        migrations.AlterField(
            model_name='records',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='名'),
        ),
        migrations.AlterField(
            model_name='records',
            name='recorded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='資料儲存時間'),
        ),
    ]
