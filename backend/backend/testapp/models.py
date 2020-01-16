from django.conf import settings
from django.db import models


# Create your models here.
class Testt(models.Model):
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , default=None)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    number = models.IntegerField(default=0)

    def __str__(self):
        return str({
            "slug": self.slug,
            "desc": self.desc
        })
