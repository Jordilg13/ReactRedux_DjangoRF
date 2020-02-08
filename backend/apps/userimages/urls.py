from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'images_admin', UserImageViewSetAdmin)  


urlpatterns = [
    path('upload', ImageUploadView.as_view()),
    path('userimages', GetAll.as_view()),
    path("media", Media.as_view()),
    # path("mvimages", UserImageViewSetAdmin.as_view({
    #     "get": "list",
    #     "delete": "destroy",
    # }))

]
