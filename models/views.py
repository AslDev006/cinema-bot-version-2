from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.generics import get_object_or_404
from .models import *
from .serializers import *



class UserListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None) -> Response:
        posts = UserModels.objects.all()
        serializer = UsersSerializer(posts, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None) -> Response:
        post = get_object_or_404(UserModels.objects.all(), pk=pk)
        serializer = UsersSerializer(post)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class VideoListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None) -> Response:
        posts = VideoModels.objects.all()
        serializer = VideoSerializer(posts, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class VideoDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None) -> Response:
        post = get_object_or_404(VideoModels.objects.all(), pk=pk)
        serializer = VideoSerializer(post)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)



class CategoryListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None) -> Response:
        posts = CategoryModels.objects.all()
        serializer = CategorySerializer(posts, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None) -> Response:
        post = get_object_or_404(CategoryModels.objects.all(), pk=pk)
        serializer = CategorySerializer(post)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)



class SavedVideoListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None) -> Response:
        posts = SavedVideoModels.objects.all()
        serializer = SavedVideoSerializer(posts, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        serializer = SavedVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class SavedVideoDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None) -> Response:
        post = get_object_or_404(SavedVideoModels.objects.all(), pk=pk)
        serializer = SavedVideoSerializer(post)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class InvitedListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None) -> Response:
        posts = InvitedModels.objects.all()
        serializer = InvitedSerializer(posts, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        serializer = InvitedSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class InvitedDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None) -> Response:
        post = get_object_or_404(InvitedModels.objects.all(), pk=pk)
        serializer = InvitedSerializer(post)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)



class InvitedDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None) -> Response:
        post = get_object_or_404(InvitedModels.objects.all(), pk=pk)
        serializer = InvitedSerializer(post)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)