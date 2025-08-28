from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=255)
    title_japanese = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='manga', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('publishing', 'Publishing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming') 
    ])

    def __str__(self):
        return self.title