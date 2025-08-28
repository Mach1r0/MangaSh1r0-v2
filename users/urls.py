from django.urls import path
from . import views

urlpatterns = [
    path('login/anilist/', views.login_with_anilist, name='login_with_anilist'),
    path('login/anilist/callback/', views.anilist_callback, name='anilist_callback'),
    path('profile/', views.profile, name='profile'),
]
