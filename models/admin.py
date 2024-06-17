from django.contrib import admin
from .models import *



admin.site.register([UserModels, VideoModels, SavedVideoModels, InvitedModels, CategoryModels])