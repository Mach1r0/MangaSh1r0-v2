from django.db import models
from users.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey('anime.Anime', on_delete=models.CASCADE)
    manga = models.ForeignKey('manga.Manga', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.anime.title if self.anime else self.manga.title}"