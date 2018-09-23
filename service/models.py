import os
from uuid import uuid4

from django.db import models
from django.utils.deconstruct import deconstructible


class ServiceCategory(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = "service_category"

    def __str__(self):
        return self.name


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        uid = uuid4().hex[:20]
        renamed_filename = '{}.{}'.format(uid, ext)
        return os.path.join(self.path, renamed_filename)


class Service(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(null=True, blank=True, default="Không xác định")
    category = models.ForeignKey('service.ServiceCategory',
                                 null=False, blank=False,
                                 related_name="services")
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    image = models.ImageField(upload_to=PathAndRename('image/service'), default='image/hotel/default.jpg',
                              blank=True, null=True)
    star = models.FloatField(default=0)
    description = models.TextField(null=True, blank=True)
    openAt = models.TimeField(default="00:00")
    closeAt = models.TimeField(default="00:00")
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.name
