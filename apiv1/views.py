from django.shortcuts import get_object_or_404
from rest_framework import status, views, generics
from rest_framework.response import Response

from karaoke.models import Artist, Song
from .serializers import ArtistSerializer, SongSerializer

from .machine_learning import main


class SongAPIView(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self): 
        lowest, highest = main() # ここにファイルが入る
        return Song.objects.filter(low__gte=lowest, high__lte=highest)