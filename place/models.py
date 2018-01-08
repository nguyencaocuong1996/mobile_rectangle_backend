from django.db import models


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='image/place', blank=True, null=False)
    place = models.ForeignKey('place.Place', related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return 'Place image ' + str(self.id)


class Place(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    cover = models.ImageField(upload_to='image/place', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
