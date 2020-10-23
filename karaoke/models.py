from django.db import models
from django.utils import timezone

class Artist(models.Model):
    class Meta:
        db_table = 'artist'

    name = models.CharField(verbose_name = 'アーティスト', max_length=30)

    def __str__(self):
        return self.name

class Song(models.Model):
    class Meta:
        db_table = 'song'
        
    title = models.CharField(verbose_name = '曲', max_length=30)
    high = models.IntegerField()
    low = models.IntegerField()
    artist = models.ForeignKey(Artist, verbose_name = 'アーティスト', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
