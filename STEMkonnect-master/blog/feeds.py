from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Event


class LatestEventsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New events of STEMKonnect.'

    def items(self):
        return Event.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
