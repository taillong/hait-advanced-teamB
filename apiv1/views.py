from django.shortcuts import get_object_or_404
from rest_framework import status, views, generics
from rest_framework.response import Response

from karaoke.models import Artist, Song
from django.db.models import Q
from .serializers import ArtistSerializer, SongSerializer

from .machine_learning import main


class SongAPIView(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self, request): 
        user_file = self.request.FILES['file']
        artist_list = main(user_file)
        high = self.request.query_params.get('high')
        low = self.request.query_params.get('low')
        return Song.objects.filter(low__gte=low, high__lte=high).filter(Q(artist=artist_list[0]) | Q(artist=artist_list[1]) | Q(artist=artist_list[2])) # 3個出てくることを想定