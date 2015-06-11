from django.db import models


class Episode(models.Model):
    season = models.IntegerField(null=True, blank=True)
    episode_title = models.CharField(null=True, blank=True, max_length=30)
    city = models.CharField(null=True, blank=True, max_length=30)
    state = models.CharField(null=True, blank=True, max_length=30)
    business_id = models.CharField(null=True, blank=True, max_length=100)
    restaurant = models.CharField(null=True, blank=True, max_length=30)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.restaurant

