from rest_framework import serializers
from hotel.models import Hotel


class HotelSerializer(serializers.ModelSerializer):

    services = serializers.StringRelatedField(many=True)

    class Meta:
        model = Hotel
        exclude = ()


class CreateHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        exclude = ('lat', 'long', 'star')
