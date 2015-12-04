# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerhome', '0004_auto_20151119_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brokerrating',
            old_name='revie',
            new_name='review',
        ),
    ]
