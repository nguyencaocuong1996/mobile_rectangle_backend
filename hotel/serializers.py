from rest_framework import serializers
from hotel.models import Hotel


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        exclude = ()


class CreateHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        exclude = ('lat', 'long', 'star')
