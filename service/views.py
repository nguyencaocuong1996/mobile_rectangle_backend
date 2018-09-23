from rest_framework.generics import ListAPIView
from service.models import Service, ServiceCategory
from service.serializers import ListServiceSerializer, ListCategorySerializer


class ListServiceView(ListAPIView):
    serializer_class = ListServiceSerializer
    queryset = Service.objects.all()

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return Service.objects.filter(category_id=category)
        return Service.objects.all()


class ListCategoryView(ListAPIView):
    serializer_class = ListCategorySerializer
    queryset = ServiceCategory.objects.all()

