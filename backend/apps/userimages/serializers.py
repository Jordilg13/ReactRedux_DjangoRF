from rest_framework import serializers
from .models import UserImage, Tag
from apps.profiles.serializers import ProfileSerializer
from .relations import TagRelatedField
from django.core.files import File
from django.core.files.images import get_image_dimensions
import base64
import os


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag


class UserImageSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)
    tags = TagRelatedField(many=True, required=False)
    base64_image = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    class Meta():
        model = UserImage
        fields = (
            "image",
            "owner",
            "tags",
            "base64_image",
            "size"
            # "createdAt",
            # "updatedAt",
        )

        def validate(self, attrs):
            return attrs

    def create(self, validated_data):
        owner = self.context.get('owner', None)
        tags = validated_data.pop('tags', [])
        image = UserImage.objects.create(owner=owner, **validated_data)
        print(tags)

        for tag in tags:
            image.tags.add(tag)

        return image

    def get_size(self, obj):
        f = obj.image
        image = File(f)
        width, height = get_image_dimensions(obj.image)
        data = {
            "width": width,
            "height": height
        }
        return data

    # Convert the image into a base64 string
    def get_base64_image(self, obj):
        f = obj.image
        image = File(f)
        data = base64.b64encode(image.read())
        return data

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()
