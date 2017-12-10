from django.db import models


class Customer(models.Model):
    user = models.OneToOneField('auth.User')
