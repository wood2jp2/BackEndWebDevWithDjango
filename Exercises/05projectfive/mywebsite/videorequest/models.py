from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    videoTitle = models.CharField(max_length=40)
    videoDescription = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.videoTitle, self.id)