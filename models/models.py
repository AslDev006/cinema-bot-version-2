from datetime import timedelta

from django.db import models

class CategoryModels(models.Model):
    name  = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserModels(models.Model):
    user_id = models.BigIntegerField()
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    is_ban = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} {self.user_id}"

class VideoModels(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryModels, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    year = models.DateField()
    language = models.CharField(max_length=255)
    duration = models.DurationField(default=timedelta(minutes=20))
    age_limit = models.CharField(max_length=2, default='00')
    photo_file_id = models.CharField(max_length=255, null=True, blank=True)
    video_file_id = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} {self.category}"

class SavedVideoModels(models.Model):
    user = models.ForeignKey(UserModels, on_delete=models.CASCADE, related_name='saved_videos')
    video_id = models.ForeignKey(VideoModels, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.video_id} for {self.user}"


class InvitedModels(models.Model):
    user = models.CharField(max_length=255)
    invited_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.invited_id} for {self.user}"
