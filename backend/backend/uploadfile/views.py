from rest_framework import views , status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .serializers import FileSerializer


# Create your views here.
class FileUploadView(views.APIView):
    parser_class = (FileUploadParser ,)

    def post(self , request , *args , **kwargs):
        file_serializer = FileSerializer(data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
