from django.conf.urls import url
from . import views
from .feeds import LatestEventsFeed


urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
    url(r'review/$', views.review_list, name='review_list'),
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^event/(?P<event_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^event/(?P<event_id>[0-9]+)/edit/$', views.event_update, name='update'),
    url(r'^create/$', views.event_create),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^(?P<place_slug>[-\w]+)/$', views.event_list, name='event_list_by_place'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.event_list, name='event_list_by_tag'),
    url(r'^feed/$', LatestEventsFeed(), name='event_feed'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    # url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),

]

