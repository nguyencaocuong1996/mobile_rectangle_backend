from django.db import models


class Customer(models.Model):
    user = models.OneToOneField('auth.User', related_name='customer', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return self.user.first_name + " " + self.user.last_name


