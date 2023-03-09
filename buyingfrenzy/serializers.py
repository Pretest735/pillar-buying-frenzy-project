from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'restaurant_name', 'cash_balance')
        model = Restaurant

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'dish_name', 'price', 'restaurant')
        model = Menu

class OpenHoursSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'day', 'opening_hour', 'closing_hour', 'restaurant')
        model = OpenHours

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'cash_balance')
        model = User

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'dish_name', 'restaurant', 'transaction_amount', 'transaction_date', 'user')
        model = PurchaseHistory