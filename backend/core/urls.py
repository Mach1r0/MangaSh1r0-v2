from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from anime.views import AnimeViewSet
from manga.views import MangaViewSet
from users.views import UserViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'anime', AnimeViewSet)
router.register(r'manga', MangaViewSet)
router.register(r'user', UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('users/', include('users.urls')),
    path('anime/', include('anime.urls')),
    path('manga/', include('manga.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
