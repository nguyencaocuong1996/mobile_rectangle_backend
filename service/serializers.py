from rest_framework import serializers

from service.models import Service, ServiceCategory


class ListServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        exclude = ()


class ListCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        exclude = ()
