from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated


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

