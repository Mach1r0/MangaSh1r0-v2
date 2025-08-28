from django.shortcuts import render
from rest_framework import viewsets 
from .models import Review
from . import ReviewsSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
