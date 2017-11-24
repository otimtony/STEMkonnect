from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Event

@register.simple_tag
def total_events():
    return Event.published.count()


@register.inclusion_tag('location/events/latest_events.html')
def show_latest_events(count=5):
    latest_events = Event.published.order_by('-publish')[:count]
    return {'latest_events': latest_events}


@register.assignment_tag
def get_most_commented_events(count=5):
    return Event.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
