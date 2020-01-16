from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^tests/(?P<slug>[-\w]+)$', GetOne.as_view()),
    url(r'^tests/' , GetAll.as_view() , name="getall"),
    url(r'^create/$' , CreateOne.as_view()),
    url(r'^delete/(?P<slug>[-\w]+)$', DeleteOne.as_view()),

]
