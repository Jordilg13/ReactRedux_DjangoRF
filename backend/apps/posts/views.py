from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated)
from .models import Post,Hashtag, Opinion
from .serializers import (
    PostSerializer,
    HashtagSerializer,
    OpinionSerializer
)

class ListPosts(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        hashtag = self.request.query_params.get('hashtags', None)
        
        if hashtag is not None:
            queryset = queryset.filter(hashtags__hashtag=hashtag)

        return queryset

    def get(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer_context = {
            'author': request.user.profile,
            'request': request
        }
        serializer_data = request.data.get('post', {})
        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DetailsPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class HashtagsListAPIView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class PostsFeedAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            author__in=self.request.user.profile.follows.all()
        )

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer_context = {'request': request}
        
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )

        return self.get_paginated_response(serializer.data)

class OpinionsListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'post__id'
    lookup_url_kwarg = 'post_pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Opinion.objects.select_related(
        'post', 'post__author', 'post__author__user',
        'author', 'author__user'
    )
    serializer_class = OpinionSerializer

    def filter_queryset(self, queryset):
        # The built-in list function calls `filter_queryset`. Since we only
        # want comments for a specific article, this is a good place to do
        # that filtering.
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        return queryset.filter(**filters)

    def create(self, request, post_pk=None):
        data = request.data.get('opinion', {})
        context = {'author': request.user.profile}

        try:
            context['post'] = Post.objects.get(id=post_pk)
        except Post.DoesNotExist:
            raise NotFound('An post with this slug does not exist.')
            
        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)