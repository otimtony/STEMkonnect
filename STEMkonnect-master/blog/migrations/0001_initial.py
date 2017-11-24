# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date=b'publish')),
                ('image', models.ImageField(upload_to=b'events/%Y/%m/%d', blank=True)),
                ('description', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'published', b'Published')])),
                ('author', models.ForeignKey(related_name='events_posted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('location', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'places/%Y/%m/%d', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'events/%Y/%m/%d', blank=True)),
                ('event', models.ForeignKey(to='blog.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(related_name='events', to='blog.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together=set([('id', 'slug')]),
        ),
    ]
