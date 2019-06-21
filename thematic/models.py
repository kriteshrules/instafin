from django.db import models

class Thematic(models.Model):
    image = models.CharField(max_length=100)
    theme_name = models.CharField(max_length=100)
    description = models.TextField()
    trend = models.CharField(max_length=200)
    explore = models.CharField(max_length=200)

    def __str__(self):
        return self.theme_name
