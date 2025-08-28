from django.urls import path
from . import views
from anime import views_anilist as anime_views_anilist

urlpatterns = [
    path('search/', views_anilist.manga_search_view, name='manga_search'),
]
