from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import apps.articles.signals

default_app_config = 'apps.articles.ArticlesAppConfig'
