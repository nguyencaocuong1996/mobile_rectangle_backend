from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from customer.models import Customer
from django.db.utils import IntegrityError


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
            email = validated_data.pop('email')
            try:
                user = User.objects.create(
                    username=email,
                    email=email,
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name']
                )
            except IntegrityError:
                raise serializers.ValidationError("Email exists!")
            user.set_password(password)
            user.save()
            Customer.objects.create(user=user, phone=phone)
            return user
