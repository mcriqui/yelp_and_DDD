from django.contrib import admin

from yelp_info.models import Episode


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('season', 'episode_title', 'restaurant', 'city', 'state', 'business_id', 'rating')

admin.site.register(Episode, EpisodeAdmin)