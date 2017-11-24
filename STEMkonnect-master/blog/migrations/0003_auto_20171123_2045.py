# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='event',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
