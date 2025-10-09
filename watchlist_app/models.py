from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

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


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_user",blank = True, null = True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name='review_watchlist')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + "-" + self.watchlist.title
