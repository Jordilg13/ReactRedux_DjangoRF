from rest_framework import serializers
from .models import UserImage, Tag
from apps.profiles.serializers import ProfileSerializer
from .relations import TagRelatedField


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag



class UserImageSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)
    tags = TagRelatedField(many=True, required=False)


    class Meta():
        model = UserImage
        fields = (
            "image",
            "owner",
            "tags",
            # "createdAt",
            # "updatedAt",
        )

        def validate(self, attrs):
            print("ATTRS")
            print(attrs)
            return attrs


    def create(self, validated_data):

        owner = self.context.get('owner', None)

        tags = validated_data.pop('tags', [])
        image = UserImage.objects.create(owner=owner, **validated_data)

        for tag in tags:
            image.tags.add(tag)

        return image

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


