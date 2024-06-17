from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModels
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModels
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModels
        fields = "__all__"

class InvitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedModels
        fields = "__all__"

class SavedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedVideoModels
        fields = "__all__"


