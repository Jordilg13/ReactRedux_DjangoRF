from rest_framework import serializers

from .models import Hashtag


class HashtagRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Hashtag.objects.all()

    def to_internal_value(self, data):
        hashtag, created = Hashtag.objects.get_or_create(hashtag=data)

        return hashtag

    def to_representation(self, value):
        return value.hashtag