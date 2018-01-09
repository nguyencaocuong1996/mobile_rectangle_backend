from rest_framework import serializers
from hotel.models import Hotel, FavoriteHotel, BookedHotel


class HotelSerializer(serializers.ModelSerializer):

    services = serializers.StringRelatedField(many=True)
    type = serializers.CharField(default="Khách sạn")
    typeId = serializers.IntegerField(default=1)

    class Meta:
        model = Hotel
        exclude = ()


class CreateHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        exclude = ('lat', 'long', )


class AddFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteHotel
        exclude = ()


class BookedHotelSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()

    class Meta:
        model = BookedHotel
        exclude = ()

