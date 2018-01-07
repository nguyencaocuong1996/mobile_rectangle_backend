from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCustomer


class ListMyRestaurant(ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (IsCustomer,)

    def get_queryset(self):
        customer = self.request.user.customer
        return Restaurant.objects.filter(owner=customer)


class ListAllRestaurant(ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class ListRestaurant(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class ListFavoriteRestaurant(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        customer = self.request.user.customer
        return Restaurant.objects.filter(favorite_customer_meta__customer=customer)


class ListBookedRestaurant(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookedRestaurantSerializer

    def get_queryset(self):
        customer = self.request.user.customer
        return BookedRestaurant.objects.filter(customer=customer)


class CreateRestaurant(CreateAPIView):
    serializer_class = CreateRestaurantSerializer
    queryset = Restaurant.objects.all()


class AddFavorite(CreateAPIView):
    serializer_class = AddFavoriteSerializer
    queryset = FavoriteRestaurant.objects.all()


class BookRestaurant(CreateAPIView):
    serializer_class = BookedRestaurantSerializer
    queryset = BookedRestaurant.objects.all()
