from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from .models import Taxi, Order, StatusDriver


class TaxiSerializer(serializers.ModelSerializer):
    # drivers = serializers.ReadOnlyField(source='only_drivers')

    class Meta:
        model = Taxi
        fields = '__all__'
        read_only_fields = ['profile']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class StatusDriverSerializer(serializers.ModelSerializer):
    point = serializers.CharField(write_only=True, max_length=20)

    class Meta:
        model = StatusDriver
        fields = '__all__'
        read_only_fields = ['profile']

