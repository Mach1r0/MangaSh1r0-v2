from django.urls import path
from . import views
from . import views_anilist

urlpatterns = [
    path('search/', views_anilist.anime_search_view, name='anime_search'),
]
