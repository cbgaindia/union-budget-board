# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-02 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datatable',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='union_budget_board_datatable', serialize=False, to='cms.CMSPlugin')),
                ('url', models.URLField(max_length=300)),
                ('columns', models.CharField(default=b'None', max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
