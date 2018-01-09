from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    cover = models.ImageField(upload_to='image/event', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    startAt = models.DateTimeField(blank=False, null=False)
    joinCount = models.IntegerField(default=0)

    def __str__(self):
        return self.name
