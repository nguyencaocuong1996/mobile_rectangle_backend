from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default="Sự kiện")
    typeId = serializers.IntegerField(default=4)

    class Meta:
        model = Event
        exclude = ()
