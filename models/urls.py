from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<pk>/', UserDetailView.as_view()),
    path('video/', VideoListView.as_view()),
    path('video/<pk>/', VideoDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<pk>/', CategoryDetailView.as_view()),
    path('saved-video/', SavedVideoListView.as_view()),
    path('saved-video/<pk>/', SavedVideoDetailView.as_view()),
    path('invited/', SavedVideoListView.as_view()),
    path('invited/<pk>/', InvitedDetailView.as_view()),
]