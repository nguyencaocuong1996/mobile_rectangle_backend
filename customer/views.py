from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ListCustomer(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CreateCustomer(CreateAPIView):
    serializer_class = UserSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        customer = user.customer
        token, created = Token.objects.get_or_create(user=user)
        response = {
            'id': user.id,
            'token': token.key,
            'name': customer.full_name,
            'email': user.email,
        }
        return Response(response)
