from django.db import models

from apps.core.models import TimestampedModel

class Post(TimestampedModel):
    post = models.TextField(max_length=255)

    author = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='posts'
    )

    hashtags = models.ManyToManyField(
        'posts.Hashtag', related_name='posts', blank=True
    )

    def __str__(self):
        return self.post

class Opinion(TimestampedModel):
    body = models.TextField()

    post = models.ForeignKey(
        'posts.Post', related_name='opinions', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'profiles.Profile', related_name='opinions', on_delete=models.CASCADE
    )

class Hashtag(TimestampedModel):
    hashtag = models.CharField(max_length=255)

    def __str__(self):
        return self.hashtag