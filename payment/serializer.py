from rest_framework import serializers
from .models import Order

class GeneratePayLinkSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount = serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = "__all__"