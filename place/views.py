from rest_framework.generics import ListAPIView
from .serializers import *


class ListAllPlace(ListAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

