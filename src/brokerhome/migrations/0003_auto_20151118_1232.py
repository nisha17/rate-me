# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('brokerhome', '0002_brokerrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokerrating',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
