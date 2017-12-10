from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ()


class UserSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(max_length=15, required=False)
    password = serializers.CharField(max_length=255, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'password']

    def create(self, validated_data):
        with transaction.atomic():
            phone = validated_data.pop('phone')
            password = validated_data.pop('password')

            user = User.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(password)
            user.save()
            Customer.objects.create(user=user, phone=phone)
            return user
