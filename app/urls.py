from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from .views import YoutubeRequestView

urlpatterns = [
    # URL pattern for the UserListView
    url(r'^', YoutubeRequestView, name='youtube_request'),


    ]
