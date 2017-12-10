from django.db import models


class Owner(models.Model):
    user = models.OneToOneField('auth.User', related_name='owner', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=False, null=False)