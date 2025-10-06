from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    stream_platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,blank=True,null=True, related_name="watchlist_stream_platform")

    def __str__(self):
        return self.title