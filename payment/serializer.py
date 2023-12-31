from rest_framework import serializers
from .models import Order
from user.serailizer import UserSerializer
from courses.serializer import CourseSerializer

class GeneratePayLinkSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount = serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
    user = UserSerializer()
    course = CourseSerializer()
    class Meta:
        model = Order
        fields = ['user',"course","paid","order_id","purchased_at"]

#STRIPE PAYMENT Serializers

import datetime

from rest_framework import serializers

def check_expiry_month(value):
    if not 1 <= int(value) <= 12:
        raise serializers.ValidationError("Invalid expiry month.")

def check_expiry_year(value):
    current_year = datetime.datetime.now().year
    if not int(value) >= current_year:
        raise serializers.ValidationError("Invalid expiry year. Year must be in the future.")

def check_cvc(value):
    if not 3 <= len(value) <= 4:
        raise serializers.ValidationError("Invalid cvc number.")

def check_payment_method(value):
    payment_method = value.lower()
    if payment_method not in ["card"]:
        raise serializers.ValidationError("Invalid payment_method.")

class CardInformationSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=150, required=True)
    expiry_month = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_month],
    )
    expiry_year = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_year],
    )
    cvc = serializers.CharField(
        max_length=4,
        required=True,
        validators=[check_cvc],
    )
    payment_method = serializers.CharField(
        max_length=10,
        required=True,
        validators=[check_payment_method],
    )
