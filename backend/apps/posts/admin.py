from django.contrib import admin

from .models import Post,Opinion,Hashtag

admin.site.register(Post)

admin.site.register(Opinion)

admin.site.register(Hashtag)