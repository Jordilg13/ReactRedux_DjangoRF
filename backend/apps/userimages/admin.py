from django.contrib import admin

# Register your models here.
from .models import UserImage, Tag

admin.site.register(UserImage)
admin.site.register(Tag)
