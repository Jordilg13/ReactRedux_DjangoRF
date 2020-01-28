# from django.conf.urls import include, url

# from rest_framework.routers import DefaultRouter

# from .views import (
#     ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
#     CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
# )

# router = DefaultRouter(trailing_slash=False)
# router.register(r'articles', ArticleViewSet)

# urlpatterns = [
#     url(r'^', include(router.urls)),

#     url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),

#     url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',
#         ArticlesFavoriteAPIView.as_view()),

#     url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$', 
#         CommentsListCreateAPIView.as_view()),

#     url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
#         CommentsDestroyAPIView.as_view()),

#     url(r'^tags/?$', TagListAPIView.as_view()),
# ]

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView,
    ArticleViewSetAdmin, CommentViewSetAdmin, TagViewSetAdmin
)

app_name = 'articles'

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

#Admin
router.register(r'articles_Admin', ArticleViewSetAdmin)  
router.register(r'comments_Admin', CommentViewSetAdmin)   
router.register(r'tags_Admin', TagViewSetAdmin)  

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',ArticlesFavoriteAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$', CommentsListCreateAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',CommentsDestroyAPIView.as_view()),
    url(r'^tags/?$', TagListAPIView.as_view()),
]
