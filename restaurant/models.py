
from datetime import datetime
from django.db import models
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    image = models.ImageField(upload_to='image/restaurant', default='image/restaurant/default.jpg', blank=True, null=True)
    star = models.FloatField(default=0)
    price = models.FloatField(default=0)
    description = models.TextField(null=True, blank=True)
    services = models.ManyToManyField('restaurant.Service', related_name="restaurants", blank=True)
    openAt = models.TimeField(default="00:00")
    closeAt = models.TimeField(default="00:00")
    createdAt = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('customer.Customer', related_name='restaurants', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FavoriteRestaurant(models.Model):
    customer = models.ForeignKey('customer.Customer', related_name='favorite_restaurant_meta', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurant.Restaurant', related_name='favorite_customer_meta',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.full_name + " - " + self.restaurant.name

    class Meta:
        unique_together = (("customer", "restaurant"),)


class BookedRestaurant(models.Model):
    customer = models.ForeignKey('customer.Customer', related_name='booked_restaurant_meta', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurant.Restaurant', related_name='booked_customer_meta', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    bookedAt = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.customer.full_name + " book " + self.restaurant.name + " at " + str(self.bookedAt)

