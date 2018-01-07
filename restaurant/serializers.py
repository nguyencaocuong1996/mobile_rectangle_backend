from rest_framework import serializers
from .models import Restaurant, FavoriteRestaurant, BookedRestaurant


class RestaurantSerializer(serializers.ModelSerializer):

    services = serializers.StringRelatedField(many=True)

    class Meta:
        model = Restaurant
        exclude = ()


class CreateRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        exclude = ('lat', 'long',)


class AddFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurant
        exclude = ()


class BookedRestaurantSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = BookedRestaurant
        exclude = ()
