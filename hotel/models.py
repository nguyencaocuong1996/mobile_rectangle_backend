from django.db import models


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
    image = models.ImageField(upload_to='image/hotel', blank=True, null=True)
    star = models.FloatField(default=0)
    price = models.FloatField(default=0)
    discount = models.FloatField
    description = models.TextField(null=True, blank=True)
    services = models.ManyToManyField('hotel.Service', related_name='hotels')
    openAt = models.TimeField(auto_now=True)
    closeAt = models.TimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('customer.Customer', related_name='hotels', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
