from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    name = 'apps.posts'
    label = 'posts'
    verbose_name = 'Posts'

default_app_config = 'apps.posts.PostsAppConfig'
