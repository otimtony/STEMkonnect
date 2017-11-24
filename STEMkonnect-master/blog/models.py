from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from taggit.managers import TaggableManager
import datetime
import numpy as np


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Place(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='places/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'place'
        verbose_name_plural = 'places'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Location:event_list_by_place', args=[self.slug])



class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    place = models.ForeignKey(Place, related_name='events')
    location = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='events/%Y/%m/%d', blank=True)
    author = models.ForeignKey(User, related_name='events_posted')
    description = models.TextField()
    publish = models.DateTimeField(null=True, blank=True, default=timezone.now)
    startTime = models.DateTimeField(auto_now_add=False, auto_now=False)
    endTime = models.DateTimeField(auto_now_add=False, auto_now=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # The Dahl-specific manager.

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        index_together = (('id', 'slug'),)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.name
        

    def get_absolute_url(self):
        return reverse('Location:event_detail', args=[self.id])

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
    event = models.ForeignKey(Event)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Event.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
 

def pre_save_event_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_event_receiver, sender=Event)

class PostImage(models.Model):
    file = models.ImageField(upload_to='events/%Y/%m/%d', blank=True)
    event = models.ForeignKey('Event')

