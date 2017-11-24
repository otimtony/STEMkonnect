from haystack import indexes
from .models import Event


class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Event

    def index_queryset(self, using=None):
        return self.get_model().published.all()
