from rest_framework import serializers
from apps.profiles.serializers import ProfileSerializer
from .models import Post,Hashtag, Opinion
from .relations import HashtagRelatedField

class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    post = serializers.CharField()
    hashtagList = HashtagRelatedField(many=True, required=False, source='hashtags')

    class Meta:
        model = Post
        fields = (
            'id',
            'post',
            'author',
            'hashtagList',
        )
    
    def create(self, validated_data):
        author = self.context.get('author', None)
        hashtags = validated_data.pop('hashtags', [])
        post = Post.objects.create(author=author, **validated_data)

        for hashtag in hashtags:
            post.hashtags.add(hashtag)

        return post

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = (
            'id',
            'hashtag',
        )

    '''def to_representation(self, obj):
        return obj.hashtag'''

class OpinionSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Opinion
        fields = (
            'id',
            'author',
            'body',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        post = self.context['post']
        author = self.context['author']

        return Opinion.objects.create(
            author=author, post=post, **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()