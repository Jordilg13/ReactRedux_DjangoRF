from rest_framework import status , permissions , generics
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer

# Create your views here.
class FileUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAdminUser,)

    def post(self , request , *args , **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class GetAll(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticated ,)

    def get_queryset(self):
        return File.objects.all()
