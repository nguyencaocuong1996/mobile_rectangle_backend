from rest_framework.generics import ListAPIView
from .serializers import *


class ListAllEvent(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

