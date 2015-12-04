# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerDetails',
            fields=[
                ('broker_id', models.IntegerField(serialize=False, primary_key=True)),
                ('broker_name', models.CharField(max_length=255)),
                ('firm_name', models.CharField(max_length=255, null=True, blank=True)),
                ('website', models.URLField(max_length=1000, null=True, blank=True)),
                ('slug', models.SlugField(help_text=b'A label for url config', max_length=31, null=True, blank=True)),
            ],
            options={
                'db_table': 'broker_details',
                'verbose_name': 'brokers',
            },
        ),
        migrations.CreateModel(
            name='BrokerLocale',
            fields=[
                ('broker_loc_id', models.AutoField(serialize=False, primary_key=True)),
                ('broker_id', models.ForeignKey(related_name='locale_broker', db_column=b'broker_id', to='brokerhome.BrokerDetails')),
            ],
            options={
                'db_table': 'broker_locale',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(serialize=False, primary_key=True)),
                ('city_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text=b'A label for url config', unique=True, max_length=31)),
            ],
            options={
                'ordering': ['city_name'],
                'db_table': 'city',
                'verbose_name': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('locale_id', models.AutoField(serialize=False, primary_key=True)),
                ('locale', models.CharField(max_length=255)),
                ('city_id', models.ForeignKey(related_name='city_locality', db_column=b'city_id', to='brokerhome.City')),
            ],
            options={
                'db_table': 'locality',
                'verbose_name': 'localities',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='brokerlocale',
            name='city_id',
            field=models.ForeignKey(related_name='broker_city', db_column=b'city_id', to='brokerhome.City'),
        ),
        migrations.AddField(
            model_name='brokerlocale',
            name='locale_id',
            field=models.ForeignKey(related_name='broker_locale', db_column=b'locale_id', to='brokerhome.Locality'),
        ),
        migrations.AlterUniqueTogether(
            name='locality',
            unique_together=set([('city_id', 'locale')]),
        ),
        migrations.AlterUniqueTogether(
            name='brokerlocale',
            unique_together=set([('broker_id', 'locale_id')]),
        ),
    ]
