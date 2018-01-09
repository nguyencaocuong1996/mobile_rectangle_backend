from django.db import models
from datetime import datetime
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    image = models.ImageField(upload_to='image/hotel', default='image/hotel/default.jpg', blank=True, null=True)
    star = models.FloatField(default=0)
    price = models.FloatField(default=0)
    discount = models.FloatField
    description = models.TextField(null=True, blank=True)
    services = models.ManyToManyField('hotel.Service', related_name='hotels', blank=True)
    openAt = models.TimeField(default="00:00")
    closeAt = models.TimeField(default="00:00")
    createdAt = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('customer.Customer', related_name='hotels', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FavoriteHotel(models.Model):
    customer = models.ForeignKey('customer.Customer', related_name='favorite_hotel_meta', on_delete=models.CASCADE)
    hotel = models.ForeignKey('hotel.Hotel', related_name='favorite_customer_meta', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.full_name + " - " + self.hotel.name

    class Meta:
        unique_together = (("customer", "hotel"),)


class BookedHotel(models.Model):
    customer = models.ForeignKey('customer.Customer', related_name='booked_hotel_meta', on_delete=models.CASCADE)
    hotel = models.ForeignKey('hotel.Hotel', related_name='booked_customer_meta', on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now_add=True)
    bookedAt = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.customer.full_name + " book " + self.hotel.name + " at " + str(self.bookedAt)
