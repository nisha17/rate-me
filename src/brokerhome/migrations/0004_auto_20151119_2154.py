# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerhome', '0003_auto_20151118_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brokerrating',
            old_name='review',
            new_name='revie',
        ),
    ]
