from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Testt
from .serializers import TesttSerializer
from rest_framework import viewsets , generics , permissions , status
from rest_framework.response import Response


# Create your views here.
class ForAdmins(viewsets.ModelViewSet):
    queryset = Testt.objects.all()
    serializer_class = TesttSerializer
    permission_classes = (permissions.IsAuthenticated ,)
    permission_classes = (permissions.IsAdminUser ,)


# GetOne
class GetOne(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = TesttSerializer
    queryset = Testt.objects.all()

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self , request , *args , **kwargs):
        try:
            element = Testt.objects.get(slug=kwargs['slug'])
        except Testt.DoesNotExist:
            return Response({"detail": "Not found."} , status=404)

        # TODO: serialize data
        return Response(str(element) , status=status.HTTP_204_NO_CONTENT)


# GetAll
class GetAll(generics.ListAPIView):
    serializer_class = TesttSerializer

    def get_queryset(self):
        return Testt.objects.all()


# POST
class CreateOne(generics.CreateAPIView):
    queryset = Testt.objects.all()
    serializer_class = TesttSerializer

    def perform_create(self , serializer):
        serializer.save(owner=self.request.user)


# DELETE
class DeleteOne(generics.DestroyAPIView):
    serializer_class = TesttSerializer
    queryset = Testt.objects.all()

    def destroy(self , request , *args , **kwargs):
        try:
            element = Testt.objects.get(slug=kwargs['slug'])
        except Testt.DoesNotExist:
            return Response({"detail": "Not found."} , status=404)

        element.delete()

        return Response(None , status=status.HTTP_204_NO_CONTENT)
