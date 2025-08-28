from django.shortcuts import render
from .models import Manga
from .serializers import MangaSerializer
from rest_framework import viewsets

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
