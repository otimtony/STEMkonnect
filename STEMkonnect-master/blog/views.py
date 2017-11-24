from django.shortcuts import render, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from taggit.models import Tag

from .models import Event, Place, PostImage, Review
from taggit.models import Tag
from .forms import EventForm, ReviewForm
from django.template import Context, loader
import datetime

from django.template import Context, loader
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


def event_create(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, 'location/events/post_form.html', {'form': form })

def event_list(request, place_slug=None, tag_slug=None):
    tag = None
    place = None
    object_list = Event.published.all()
    places = Place.objects.all()
    tags = Tag.objects.all()

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    if place_slug:
        place = get_object_or_404(Place, slug=place_slug)
        object_list = object_list.filter(place=place)
    
    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
            ).distinct()
    paginator = Paginator(object_list, 6) 
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request, 'location/events/list.html', {'page': page,
                                                   'events': events,
                                                   'tag': tag,
                                                   'tags':tags,
                                                   'places': places,
                                                   'place': place})


def event_detail(request, event_id):
    photos = PostImage.objects.all()
    object_list = Event.published.all()
    event = get_object_or_404(Event, pk=event_id)
    query = request.GET.get("q")

    if query:
        object_list = object_list.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
            ).distinct()

    event_tags_ids = event.tags.values_list('id', flat=True)
    similar_events = Event.published.filter(tags__in=event_tags_ids).exclude(id=event.id)
    similar_events = similar_events.annotate(same_tags=Count('tags')).order_by('-same_tags',
                                                                             '-publish')[:4]
    return render(request, 'location/events/detail.html', {'event': event,
                                                     'similar_events': similar_events, 'photos': photos, 'object_list':object_list})


def event_update(request, year, month, day, event_id):
    instance = get_object_or_404(Event, pk=event_id)
    form = EventForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    event_tags_ids = event.tags.values_list('id', flat=True)
    similar_events = Event.published.filter(tags__in=event_tags_ids).exclude(id=event.id)
    similar_events = similar_events.annotate(same_tags=Count('tags')).order_by('-same_tags',
                                                                             '-publish')[:4]
    return render(request, 'location/events/post_form.html', {'event': event,
                                                     'similar_events': similar_events,
                                                     'form': form,
                                                     'instance': instance})


def about_us(request):
    return render(request , 'location/events/about_us.html', {})


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'location/reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'location/reviews/review_detail.html', {'review': review})


@login_required
def add_review(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = Review()
        review.event = event
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()

        return HttpResponseRedirect(reverse('Location:event_detail', args=(event.id,)))

    return render(request, 'location/events/detail.html', {'event': event, 'form': form})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'location/reviews/user_review_list.html', context)
