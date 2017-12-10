from django.db import models


class Customer(models.Model):
    user = models.OneToOneField('auth.User')
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=254, blank=False, null=False)

