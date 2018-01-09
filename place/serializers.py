from rest_framework import serializers
from .models import *


class PlaceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaceImage
        exclude = ('place',)


class PlaceSerializer(serializers.ModelSerializer):

    images = PlaceImageSerializer(many=True)
    type = serializers.CharField(default="Địa điểm")
    typeId = serializers.IntegerField(default=3)

    class Meta:
        model = Place
        exclude = ()
