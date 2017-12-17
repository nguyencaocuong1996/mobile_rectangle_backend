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


class CreateRestaurant(CreateAPIView):
    serializer_class = CreateRestaurantSerializer
    queryset = Restaurant.objects.all()

