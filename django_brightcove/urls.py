from django.conf.urls import patterns, url

from .views import refresh_item_list

urlpatterns = patterns(
    '',

    url(r'^brightcove-refresh-item-list/(?P<pk>[\w-]+)/$', refresh_item_list, name='brightcove-refresh-item-list'),
)
