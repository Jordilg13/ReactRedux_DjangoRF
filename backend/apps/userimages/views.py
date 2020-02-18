from rest_framework import status, permissions, generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import UserImage
from .serializers import UserImageSerializer

# Face recognition
from utils.face_recognition.lib_detect_faces import Faces

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
        # analyze the image to detect faces
        # TODO: change the absolute route 
        # TODO: call the face detection function from here, not from Faces.__init__
        faces = Faces(
            "/drf/utils/face_recognition/pickles/raul_jordi.pickle", 
            request.data['image'],
            "hog"
            )

        imagedata = {
            'image': request.data['image'],
            'owner': request.user.profile,
            "tags": {},
            'request': request,
        }

        # If there are any detected face
        print(faces.detected_faces)
        if len(faces.detected_faces[1]) > 0:
            facess = {}
            # TODO: change the tags system
            for j in faces.detected_faces[0]:
                facess[j] = j
            print(facess)
            imagedata['tags'] = facess

        serializer = self.serializer_class(
            data=imagedata,
            context={
                "owner": request.user.profile,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAll(generics.ListAPIView):
    serializer_class = UserImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return UserImage.objects.all()


class Media(generics.ListAPIView):
    serializer_class = UserImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserImage.objects.select_related("owner", "owner__user")

    def get_queryset(self):
        owner = self.request.user.profile
        return self.queryset.filter(owner__user__username=owner)
