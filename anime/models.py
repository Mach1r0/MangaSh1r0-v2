from django.db import models

class Anime(models.Model): 
    title = models.CharField(max_length=255)
    title_japanese = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='anime/images/', blank=True)
    total_ep = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=[
        ('airing', 'Airing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming')
    ])

    def __str__(self):
        return self.title