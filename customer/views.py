from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class ListCustomer(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CreateCustomer(CreateAPIView):
    serializer_class = UserSerializer
