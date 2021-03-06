from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=25)
    artist_name=models.CharField(max_length=30)
    album_genre=models.CharField(max_length=10)
    album_cover=models.FileField()

    def _str_(self):
       return self.album_name

    def get_absolute_url(self):
        return reverse('music:index')

class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name=models.CharField(max_length=25)
    song_audio=models.FileField()

    def _str_(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse('music/detail.html')
