from anime.models import Anime 
from rest_framework import serializers 

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
        