from rest_framework import status, permissions, generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import UserImage
from .serializers import UserImageSerializer

# Create your views here.


class UserImageViewSetAdmin(viewsets.ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAdminUser,)


class ImageUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserImage.objects.select_related("owner", "owner__user")
    serializer_class = UserImageSerializer

    # def get_queryset(self):
    #     queryset = self.queryset

    #     author = self.request.query_params.get("owner", None)
    #     print("AUTHORRRR")
    #     print(author)

    def create(self, request):
        imagedata = {
            'image': request.data['image'],
            'owner': request.user.profile,
            "tags": {},
            'request': request,
        }

        serializer = self.serializer_class(
            data=imagedata,
            context={"owner": request.user.profile}
        )
        if serializer.is_valid():
            print("SUCCESS")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("ERRORSS")
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAll(generics.ListAPIView):
    serializer_class = UserImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return UserImage.objects.all()
