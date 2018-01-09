from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCustomer


class ListMyHotel(ListAPIView):
    serializer_class = HotelSerializer
    permission_classes = (IsCustomer,)

    def get_queryset(self):
        customer = self.request.user.customer
        return Hotel.objects.filter(owner=customer)


class ListAllHotel(ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class ListHotel(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class ListFavoriteHotel(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HotelSerializer

    def get_queryset(self):
        customer = self.request.user.customer
        return Hotel.objects.filter(favorite_customer_meta__customer=customer)


class ListBookedHotel(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookedHotelSerializer

    def get_queryset(self):
        customer = self.request.user.customer
        return BookedHotel.objects.filter(customer=customer)


class CreateHotel(CreateAPIView):
    serializer_class = CreateHotelSerializer
    queryset = Hotel.objects.all()


class AddFavorite(CreateAPIView):
    serializer_class = AddFavoriteSerializer
    queryset = FavoriteHotel.objects.all()


class BookHotel(CreateAPIView):
    serializer_class = CreateBookedHotelSerializer
    queryset = BookedHotel.objects.all()

