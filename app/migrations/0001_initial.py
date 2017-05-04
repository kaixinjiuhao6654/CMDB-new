# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cmd_run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('command', models.CharField(max_length=30, verbose_name='\u547d\u4ee4')),
                ('track_mark', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u547d\u4ee4\u7ba1\u7406',
                'verbose_name_plural': '\u547d\u4ee4\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=40, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('remark', models.CharField(max_length=40, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f\u5217\u8868',
                'verbose_name_plural': '\u673a\u623f\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='salt_return',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fun', models.CharField(max_length=50)),
                ('jid', models.CharField(max_length=255)),
                ('result', models.TextField()),
                ('host', models.CharField(max_length=255)),
                ('success', models.CharField(max_length=10)),
                ('full_ret', models.TextField()),
            ],
            options={
                'verbose_name': '\u547d\u4ee4\u8fd4\u56de\u7ed3\u679c',
                'verbose_name_plural': '\u547d\u4ee4\u8fd4\u56de\u7ed3\u679c',
            },
        ),
        migrations.CreateModel(
            name='ServerAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=20, verbose_name='\u5382\u5546')),
                ('productname', models.CharField(max_length=30, verbose_name='\u4ea7\u54c1\u578b\u53f7')),
                ('service_tag', models.CharField(unique=True, max_length=80, verbose_name='\u5e8f\u5217\u53f7')),
                ('cpu_model', models.CharField(max_length=50, verbose_name='CPU\u578b\u53f7')),
                ('cpu_nums', models.PositiveSmallIntegerField(verbose_name='CPU\u7ebf\u7a0b\u6570')),
                ('cpu_groups', models.PositiveSmallIntegerField(verbose_name='CPU\u7269\u7406\u6838\u6570')),
                ('mem', models.CharField(max_length=100, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('disk', models.CharField(max_length=300, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('os', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headImg', models.FileField(upload_to=b'./upload/')),
            ],
            options={
                'verbose_name': '\u6587\u4ef6\u4e0a\u4f20',
                'verbose_name_plural': '\u6587\u4ef6\u4e0a\u4f20',
            },
        ),
    ]
