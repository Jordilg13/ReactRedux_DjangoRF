from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    ListPosts,
    DetailsPost,
    HashtagsListAPIView,
    OpinionsListCreateAPIView,
    PostsFeedAPIView
)

urlpatterns = [
    url(r'^posts/?$', ListPosts.as_view()),
    url(r'^posts/(?P<pk>\d+)/$', DetailsPost.as_view()),
    url(r'^hashtags/?$', HashtagsListAPIView.as_view()),

    url(r'^posts/feed/?$', PostsFeedAPIView.as_view()),
    url(r'^posts/(?P<post_pk>\d+)/opinions/?$', OpinionsListCreateAPIView.as_view()),
]