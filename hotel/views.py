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


class CreateHotel(CreateAPIView):
    serializer_class = CreateHotelSerializer
    queryset = Hotel.objects.all()

